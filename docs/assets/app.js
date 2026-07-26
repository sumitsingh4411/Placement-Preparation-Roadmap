/* Tier-3 to Top Tech — site behaviour. No dependencies except Mermaid (docs pages only). */
(function () {
  "use strict";

  var base = window.T3_BASE || "";
  var root = document.documentElement;
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ───────────────────────────────────────────────────────── theme ── */
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = root.dataset.theme === "light" ? "dark" : "light";
      root.dataset.theme = next;
      try { localStorage.setItem("t3-theme", next); } catch (e) {}
      if (window.__t3RedrawDiagrams) window.__t3RedrawDiagrams();
    });
  }

  /* ──────────────────────────────────────────────── mobile sidebar ── */
  var navBtn = document.querySelector(".nav-toggle");
  function closeNav() {
    document.body.classList.remove("nav-open");
    if (navBtn) navBtn.setAttribute("aria-expanded", "false");
  }
  if (navBtn) {
    navBtn.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      navBtn.setAttribute("aria-expanded", String(open));
    });
  }
  document.querySelectorAll("[data-close-nav]").forEach(function (el) {
    el.addEventListener("click", closeNav);
  });
  document.querySelectorAll(".sidebar a").forEach(function (a) {
    a.addEventListener("click", closeNav);
  });

  /* ────────────────────────────────────────────────── copy buttons ── */
  document.querySelectorAll(".code-block .copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var code = btn.parentElement.querySelector("code");
      if (!code) return;
      navigator.clipboard.writeText(code.textContent).then(function () {
        btn.textContent = "Copied";
        btn.classList.add("done");
        setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("done"); }, 1600);
      });
    });
  });

  /* ─────────────────────────────────── read progress + TOC scrollspy ── */
  var bar = document.querySelector(".read-progress i");
  var article = document.querySelector(".prose");
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  var heads = tocLinks.map(function (a) {
    return document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
  });

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      if (bar && article) {
        var top = article.offsetTop;
        var span = article.offsetHeight - window.innerHeight + 160;
        var pct = span > 0 ? (window.scrollY - top + 160) / span : 1;
        bar.style.width = Math.max(0, Math.min(1, pct)) * 100 + "%";
      }
      if (tocLinks.length) {
        var active = 0;
        for (var i = 0; i < heads.length; i++) {
          if (heads[i] && heads[i].getBoundingClientRect().top < 140) active = i;
        }
        tocLinks.forEach(function (a, i) { a.classList.toggle("active", i === active); });
      }
    });
  }
  if (bar || tocLinks.length) {
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ───────────────────────────────────────────────────────── search ── */
  var modal = document.querySelector(".search-modal");
  if (modal) {
    var input = modal.querySelector("input");
    var results = modal.querySelector(".search-results");
    var docs = null, sel = 0, loading = false;

    function load() {
      if (docs || loading) return Promise.resolve();
      loading = true;
      return fetch(base + "assets/search.json")
        .then(function (r) { return r.json(); })
        .then(function (d) { docs = d; loading = false; })
        .catch(function () { loading = false; docs = []; });
    }

    function open() {
      modal.hidden = false;
      document.body.style.overflow = "hidden";
      load().then(function () { input.focus(); input.select(); });
    }
    function close() {
      modal.hidden = true;
      document.body.style.overflow = "";
    }

    document.querySelectorAll("[data-search-open]").forEach(function (b) {
      b.addEventListener("click", open);
    });
    modal.querySelector("[data-search-close]").addEventListener("click", close);

    document.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") { e.preventDefault(); modal.hidden ? open() : close(); }
      else if (e.key === "/" && modal.hidden && !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)) {
        e.preventDefault(); open();
      }
      else if (e.key === "Escape" && !modal.hidden) close();
    });

    function score(doc, terms) {
      var t = doc.t.toLowerCase(), h = doc.h.join(" ").toLowerCase(), b = doc.b.toLowerCase();
      var s = 0;
      for (var i = 0; i < terms.length; i++) {
        var q = terms[i];
        if (!q) continue;
        if (t.indexOf(q) === 0) s += 60;
        else if (t.indexOf(q) > -1) s += 40;
        if (doc.l.toLowerCase().indexOf(q) > -1) s += 25;
        if (h.indexOf(q) > -1) s += 14;
        var c = b.split(q).length - 1;
        if (c) s += Math.min(c, 6) * 3;
        if (!s) return 0;
      }
      return s;
    }

    function snippet(doc, term) {
      var b = doc.b, i = b.toLowerCase().indexOf(term);
      if (i < 0) return b.slice(0, 150);
      var start = Math.max(0, i - 55);
      var txt = (start ? "…" : "") + b.slice(start, i + 110);
      return txt.replace(new RegExp("(" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"),
                         "<mark>$1</mark>");
    }

    function esc(s) { return s.replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

    function render(q) {
      if (!docs) return;
      var terms = q.toLowerCase().trim().split(/\s+/).filter(Boolean);
      if (!terms.length) {
        results.innerHTML = '<p class="sr-empty">Try “year 2”, “DSA”, “Zoho”, “resume”, “off-campus”…</p>';
        return;
      }
      var hits = docs.map(function (d) { return { d: d, s: score(d, terms) }; })
                     .filter(function (x) { return x.s > 0; })
                     .sort(function (a, b) { return b.s - a.s; })
                     .slice(0, 8);
      if (!hits.length) {
        results.innerHTML = '<p class="sr-empty">Nothing found for “' + esc(q) + '”</p>';
        return;
      }
      sel = 0;
      results.innerHTML = hits.map(function (x, i) {
        var crumb = x.d.u.indexOf("/") > -1 ? x.d.u.split("/")[0].replace(/-/g, " ") : "guide";
        return '<a class="sr-item' + (i === 0 ? " sel" : "") + '" href="' + base + x.d.u + '">' +
               '<p class="sr-crumb">' + esc(crumb) + "</p>" +
               '<p class="sr-title">' + esc(x.d.t) + "</p>" +
               '<p class="sr-snip">' + snippet(x.d, terms[0]) + "</p></a>";
      }).join("");
    }

    input.addEventListener("input", function () { render(input.value); });
    input.addEventListener("keydown", function (e) {
      var items = results.querySelectorAll(".sr-item");
      if (!items.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        items[sel].classList.remove("sel");
        sel = (sel + (e.key === "ArrowDown" ? 1 : items.length - 1)) % items.length;
        items[sel].classList.add("sel");
        items[sel].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        e.preventDefault();
        window.location.href = items[sel].getAttribute("href");
      }
    });
  }

  /* ══════════════════════════════════════════ landing: 208-week rail ══ */
  var rail = document.getElementById("rail");
  if (rail) {
    var WEEKS = 208;
    var frag = document.createDocumentFragment();
    for (var w = 0; w < WEEKS; w++) {
      var cell = document.createElement("i");
      // Stagger via transition-delay, not animation-delay: the bars are visible
      // from first paint, and the wave only plays when a year is selected.
      if (!reduced) cell.style.transitionDelay = (w * 2.2) + "ms";
      frag.appendChild(cell);
    }
    rail.appendChild(frag);
    var cells = rail.children;

    var YEARS = [
      { spent: 0,   label: "You have all 208 weeks left. This is the best position anyone reading this can be in.",
        goal: "Learn one language properly and solve 150 problems." },
      { spent: 52,  label: "156 weeks left. This is the make-or-break year — most students who succeed got serious here.",
        goal: "Pick one track, ship one deployed project, reach 300 problems." },
      { spent: 104, label: "104 weeks left. Applications open <b>this year</b>, not next. Internship season starts in July.",
        goal: "Land an internship, build 2 strong projects, reach 500 problems." },
      { spent: 156, label: "52 weeks left. Stop learning new things — start converting what you know.",
        goal: "Apply to 25+ roles a week and convert interviews." },
      { spent: 208, label: "Graduated with nothing done? Companies hire year-round. You now have full-time hours — that's an advantage.",
        goal: "Run a focused 5-month sprint, then apply everywhere." }
    ];

    var readout = document.getElementById("rail-readout");
    var counter = document.getElementById("rail-count");
    var goalOut = document.getElementById("rail-goal");
    var cta = document.getElementById("rail-cta");
    var buttons = Array.prototype.slice.call(document.querySelectorAll(".year-btn"));

    function paint(idx) {
      var y = YEARS[idx];
      var left = WEEKS - y.spent;
      for (var i = 0; i < WEEKS; i++) {
        var c = cells[i];
        c.className = i < y.spent ? "dim" : "on";
      }
      // milestone markers at the end of each academic year still ahead
      [51, 103, 155, 207].forEach(function (m) {
        if (m >= y.spent) cells[m].className = "mark";
      });
      if (counter) counter.firstChild.nodeValue = String(left);
      if (readout) readout.innerHTML = y.label;
      if (goalOut) goalOut.textContent = y.goal;
      if (cta) {
        cta.href = base + (idx === 4 ? "roadmap/late-start.html" : "roadmap/year-" + (idx + 1) + ".html");
        cta.querySelector("span").textContent =
          idx === 4 ? "Open the catch-up plan" : "Open the Year " + (idx + 1) + " plan";
      }
      buttons.forEach(function (b, i) { b.setAttribute("aria-pressed", String(i === idx)); });
    }

    buttons.forEach(function (b, i) {
      b.addEventListener("click", function () { paint(i); });
    });
    paint(0);
  }


  /* ────────────────────────────────────────────────── diagrams ── */
  /* Mermaid and svg-pan-zoom are vendored into assets/vendor rather than
     pulled from a CDN, so diagrams work offline and cannot be broken by a
     third party being slow or blocked.

     Every diagram renders into a fixed-height viewport and is then handed to
     svg-pan-zoom. That is the whole point of using the library: the box owns
     its own size, so a tall or wide graph can never overflow it, be sliced,
     or force the page to grow. Panning and zooming replace scrolling. */
  var wraps = document.querySelectorAll(".mermaid-wrap");
  if (wraps.length) {
    /* Match on *= not $=: the src carries a ?v= cache-busting hash, so it
       does not end in "app.js". Getting this wrong 404s the bundles. */
    var appSrc = document.querySelector('script[src*="app.js"]');
    var vendor = appSrc ? appSrc.src.replace(/app\.js.*$/, "vendor/") : "assets/vendor/";

    var load = function (file) {
      return new Promise(function (res, rej) {
        var el = document.createElement("script");
        el.src = vendor + file;
        el.onload = res;
        el.onerror = rej;
        document.head.appendChild(el);
      });
    };

    var theme = function () {
      var dark = document.documentElement.dataset.theme !== "light";
      return {
        startOnLoad: false,
        theme: "base",
        fontFamily: "Instrument Sans, sans-serif",
        flowchart: { curve: "basis", nodeSpacing: 44, rankSpacing: 58, padding: 14, useMaxWidth: false },
        themeVariables: {
          background: "transparent",
          primaryColor: dark ? "#161F3A" : "#E7EDFA",
          primaryTextColor: dark ? "#E9EDF8" : "#131A2E",
          primaryBorderColor: dark ? "#2A3757" : "#C6D2EC",
          lineColor: dark ? "#55628A" : "#8C9AC0",
          secondaryColor: dark ? "#141C34" : "#EAEFFA",
          tertiaryColor: dark ? "#0F1528" : "#F2F5FC",
          edgeLabelBackground: dark ? "#0F1528" : "#F2F5FC",
          fontSize: "14px"
        }
      };
    };

    var panners = [];
    var draw = function () {
      panners.forEach(function (p) { try { p.destroy(); } catch (e) {} });
      panners = [];
      var nodes = document.querySelectorAll(".mermaid");
      nodes.forEach(function (n, i) {
        n.removeAttribute("data-processed");
        n.textContent = window.__t3src[i];
      });
      window.mermaid.initialize(theme());
      /* run() resolves once every diagram is in the DOM. Attaching there is
         reliable; postRenderCallback is not. */
      window.mermaid.run({ nodes: nodes }).then(function () {
        document.querySelectorAll(".mermaid svg").forEach(function (svg) {
          svg.removeAttribute("width");
          svg.removeAttribute("height");
          svg.style.width = "100%";
          svg.style.height = "100%";
          var p = window.svgPanZoom(svg, {
            zoomEnabled: true,
            controlIconsEnabled: true,
            fit: true,
            center: true,
            minZoom: 0.4,
            maxZoom: 12,
            contain: false,
            dblClickZoomEnabled: true,
            mouseWheelZoomEnabled: false
          });
          requestAnimationFrame(function () {
            p.resize(); p.fit(); p.center();
          });
          panners.push(p);
        });
      });
    };

    /* Mermaid sizes each node by measuring its label, so it must not run
       before the webfont is ready or the viewBox comes out too narrow and
       pan/zoom then clips to it. Raced against a timeout so a slow font can
       delay the diagram but never prevent it. */
    var fontsReady = new Promise(function (res) {
      setTimeout(res, 2000);
      if (!document.fonts) return res();
      document.fonts.load('500 14px "Instrument Sans"')
        .then(function () { return document.fonts.ready; })
        .then(res, res);
    });

    Promise.all([load("mermaid.min.js"), load("svg-pan-zoom.min.js")])
      .then(function () { return fontsReady; })
      .then(draw)
      .catch(function () {
        /* If the bundles ever fail, show the source rather than an empty box. */
        wraps.forEach(function (w) { w.classList.add("mermaid-failed"); });
      });

    window.__t3RedrawDiagrams = draw;
  }
})();
