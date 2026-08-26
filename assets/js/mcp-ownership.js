/*
 * Ownership lookup for /tools/mcp-ownership/.
 *
 * This lives in its own file rather than inline in the page for a hard reason:
 * Chirpy builds with compress_html, which collapses an inline <script> onto a
 * single line. Every // comment then swallows the rest of the file. It shipped
 * that way once — 6,157 of 6,675 bytes were commented out and the page silently
 * did nothing. External assets are not compressed, so comments are safe here.
 *
 * Spec: _plans/2026-08-26-mcp-ownership-lookup-spec.md
 */
(function () {
  var BASE = '/data/mcp/ownership';
  var manifest = null;
  var shardCache = {};

  var form = document.getElementById('mo-form');
  var input = document.getElementById('mo-input');
  var button = document.getElementById('mo-submit');
  var out = document.getElementById('mo-result');
  var meta = document.getElementById('mo-meta');

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // Accepts a GitHub URL, a bare owner/name, or an io.github.* registry name.
  // The registry-name path is a convenience that FAILS BY DESIGN on mismatched
  // entries: when the namespace owner and the repository owner differ — which is
  // what "mismatch" means — the derived key is not the repository. A miss here is
  // reported as a miss, never as an absence from the registry.
  function normalize(raw) {
    var s = String(raw || '').trim();
    if (!s) return null;
    s = s.replace(/^[a-z][a-z0-9+.-]*:\/\//i, '');
    s = s.replace(/^(www\.)?github\.com\//i, '');
    s = s.split(/[?#]/)[0];
    s = s.replace(/\.git$/i, '').replace(/\/+$/, '');
    s = s.replace(/^io\.github\./i, '');
    var parts = s.split('/').filter(Boolean);
    if (parts.length < 2) return null;
    // github.com/owner/name/tree/main → keep the first two segments
    var key = (parts[0] + '/' + parts[1]).toLowerCase();
    return /^[^\s/]+\/[^\s/]+$/.test(key) ? key : null;
  }

  function shardOf(key) {
    var c = key.charAt(0);
    return /[a-z0-9]/.test(c) ? c : '_';
  }

  function getJSON(url) {
    return fetch(url, { cache: 'no-cache' }).then(function (r) {
      if (!r.ok) throw new Error(r.status + ' ' + url);
      return r.json();
    });
  }

  function loadManifest() {
    if (manifest) return Promise.resolve(manifest);
    return getJSON(BASE + '/index.json').then(function (m) { manifest = m; return m; });
  }

  function emptyShard(s) {
    return {
      snapshot_date: (manifest && manifest.snapshot_date) || 'the latest',
      shard: s,
      entries: {}
    };
  }

  // Only shards the manifest lists actually exist. No repository in the registry
  // starts with a non-alphanumeric character, so the "_" shard is never emitted —
  // asking for it must read as a miss, not as a broken index.
  function loadShard(s) {
    if (shardCache[s]) return Promise.resolve(shardCache[s]);
    if (manifest && manifest.shards && !(s in manifest.shards)) {
      return Promise.resolve(emptyShard(s));
    }
    return getJSON(BASE + '/by-repo/' + s + '.json').then(function (d) {
      shardCache[s] = d;
      return d;
    }, function (err) {
      if (/\b404\b/.test(err.message)) return emptyShard(s);
      throw err;
    });
  }

  function namespaceOwner(name) {
    var ns = String(name).split('/')[0];
    if (/^io\.github\./i.test(ns)) {
      return { owner: ns.replace(/^io\.github\./i, ''), kind: 'GitHub namespace' };
    }
    return { owner: ns, kind: 'domain namespace' };
  }

  function renderEntry(rec, date) {
    var name = rec[0], repo = rec[1], status = rec[2], stars = rec[3];
    var ns = namespaceOwner(name);
    var label = (manifest && manifest.labels && manifest.labels[status]) || status;
    var repoOwner = String(repo).split('/')[0];

    var rows =
      '<dt>Registry entry</dt><dd>' + esc(name) + '</dd>' +
      '<dt>Declared repository</dt><dd><a href="https://github.com/' + esc(repo) +
        '" rel="nofollow noopener">' + esc(repo) + '</a></dd>' +
      '<dt>Namespace owner</dt><dd>' + esc(ns.owner) +
        ' <span class="mo-chip">' + esc(ns.kind) + '</span></dd>' +
      '<dt>Repository owner</dt><dd>' + esc(repoOwner) + '</dd>' +
      '<dt>Stars</dt><dd>' +
        (stars === null || stars === undefined
          ? 'not measured — repository unreachable at collection time'
          : Number(stars).toLocaleString('en-US')) +
      '</dd>' +
      '<dt>Snapshot</dt><dd>' + esc(date) + '</dd>';

    var note = '';
    if (status === 'mismatch') {
      note = '<p class="mo-note">This states that two strings differ. It is not a finding of ' +
             'wrongdoing: transferring a repository to an organisation produces the same ' +
             'difference honestly, and so does a copy-paste error. Compare the two owners above ' +
             'and judge the entry on its own.</p>';
    } else if (status === 'unverifiable') {
      note = '<p class="mo-note">The namespace is a domain rather than a GitHub account, so ' +
             'there is no account to compare against. We do not infer ownership from names.</p>';
    }

    return '<div class="mo-card">' +
             '<span class="mo-chip">' + esc(status) + '</span>' +
             '<p class="mo-verdict">' + esc(label) + '</p>' +
             '<dl class="mo-pairs">' + rows + '</dl>' + note +
           '</div>';
  }

  function renderMiss(key, date) {
    var pct = '22.2%';
    if (manifest && manifest.totals && manifest.totals.servers_in_snapshot) {
      pct = (100 * manifest.totals.not_indexed / manifest.totals.servers_in_snapshot).toFixed(1) + '%';
    }
    out.innerHTML =
      '<div class="mo-card">' +
        '<span class="mo-chip">not found</span>' +
        '<p class="mo-verdict">No entry in the ' + esc(date) + ' snapshot declares ' +
          '<code>' + esc(key) + '</code>.</p>' +
        '<p class="mo-note">This does not mean the server is unregistered. ' + esc(pct) +
          ' of the registry declares no repository at all, and those entries cannot appear ' +
          'in a repository index. A registry name will also miss here whenever its namespace ' +
          'owner differs from the repository owner.</p>' +
      '</div>';
  }

  function lookup(rawValue) {
    var key = normalize(rawValue);
    if (!key) {
      out.innerHTML = '<div class="mo-card"><p class="mo-verdict">That does not look like a ' +
        'repository. Try <code>owner/name</code> or a GitHub URL.</p></div>';
      return;
    }

    button.disabled = true;
    out.innerHTML = '<p class="mo-count">Checking ' + esc(key) + '…</p>';

    loadManifest()
      .then(function () { return loadShard(shardOf(key)); })
      .then(function (shard) {
        var hits = shard.entries[key];
        if (!hits || !hits.length) return renderMiss(key, shard.snapshot_date);
        var header = hits.length > 1
          ? '<p class="mo-count">' + hits.length + ' registry entries declare this repository.</p>'
          : '';
        out.innerHTML = header + hits.map(function (r) {
          return renderEntry(r, shard.snapshot_date);
        }).join('');
      })
      .catch(function (err) {
        out.innerHTML = '<div class="mo-card"><p class="mo-verdict">Could not load the ' +
          'ownership index.</p><p class="mo-note">' + esc(err.message) +
          ' — try again, or read the shard directly at <code>' + BASE + '/by-repo/' +
          esc(shardOf(key)) + '.json</code>.</p></div>';
      })
      .then(function () { button.disabled = false; });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    lookup(input.value);
  });

  loadManifest().then(function (m) {
    meta.textContent = 'Snapshot ' + m.snapshot_date + ' — ' +
      m.totals.indexed.toLocaleString('en-US') + ' entries indexed by repository, out of ' +
      m.totals.servers_in_snapshot.toLocaleString('en-US') + ' in the registry. ' +
      'Updated weekly.';
  }).catch(function () {
    meta.textContent = 'Snapshot metadata is temporarily unavailable.';
  });
})();
