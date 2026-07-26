#!/usr/bin/env python3
"""
Build the static site in docs/ from the repository's markdown files.

No dependencies. Run:  python3 tools/build_site.py
Output is committed, so GitHub Pages can serve /docs directly.
"""

import datetime
import html
import json
import os
import re
import shutil
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs")
TOOLS = os.path.join(ROOT, "tools")

GH_USER = "YOUR_USERNAME"
REPO_NAME = "placement-preparation-roadmap"
REPO_URL = f"https://github.com/{GH_USER}/{REPO_NAME}"
SITE_URL = f"https://{GH_USER}.github.io/{REPO_NAME}"
SITE_TITLE = "Tier-3 to Top Tech"
SITE_NAME = "Placement Preparation Roadmap"

# Per-page search-optimised title and description. Titles lead with the phrase
# people actually type; descriptions are written to be clicked, not stuffed.
SEO = {
    "README.md": (
        "Placement Preparation Roadmap — 4-Year Guide for Engineering Students (India)",
        "A free, complete placement preparation roadmap for B.Tech and engineering "
        "students in India. Year-by-year plans, 8 career tracks, DSA, aptitude, "
        "resume and off-campus strategy — built for tier-3 colleges."),
    "START-HERE.md": (
        "Where to Start — Placement Preparation for Engineering Students",
        "A 10-minute orientation: pick your year, choose a career track, set up your "
        "tools, and start your placement preparation today."),
    "roadmap/README.md": (
        "4-Year Engineering Roadmap — Year-by-Year Placement Plan",
        "What to do in 1st, 2nd, 3rd and 4th year of B.Tech to get placed. "
        "Semester-by-semester targets for DSA, projects, internships and applications."),
    "roadmap/year-1.md": (
        "1st Year B.Tech Roadmap — What to Learn for Placements",
        "What a first-year engineering student should do: pick one language, start DSA, "
        "learn Git and Linux, and build the base for placements."),
    "roadmap/year-2.md": (
        "2nd Year B.Tech Roadmap — Pick a Track and Build Projects",
        "The make-or-break year. Choose a career track, ship your first deployed "
        "project, reach 300 DSA problems and start CS fundamentals."),
    "roadmap/year-3.md": (
        "3rd Year B.Tech Roadmap — Internships, Projects and Resume",
        "How to land an internship, build portfolio projects, reach 500 DSA problems "
        "and get your resume and LinkedIn ready for placements."),
    "roadmap/year-4.md": (
        "Final Year Placement Preparation — Apply, Interview, Convert",
        "Final-year placement plan: how many applications to send, what to revise, "
        "and how to convert interviews into offers."),
    "roadmap/late-start.md": (
        "Started Late? Placement Preparation Plan for 3rd and 4th Year",
        "Behind on placement preparation? Compressed 4, 8 and 18-month plans for "
        "students starting in 3rd year, final year, or after graduating."),
    "core/dsa.md": (
        "DSA Roadmap for Placements — 30 Patterns and How Many Problems",
        "A complete DSA roadmap for placement preparation: the 30 patterns that cover "
        "90% of interviews, how many problems each company tier needs, and which sheet to follow."),
    "core/aptitude-and-maths.md": (
        "Aptitude Preparation for Placements — 8-Week Plan",
        "Quantitative aptitude, logical reasoning and verbal preparation for TCS, "
        "Infosys, Wipro, Cognizant and Accenture placement tests."),
    "core/cs-fundamentals.md": (
        "CS Fundamentals for Interviews — OS, DBMS, CN and OOP",
        "Operating systems, DBMS, computer networks and OOP prepared the way "
        "interviews ask, with the questions you will actually be asked."),
    "core/system-design.md": (
        "System Design Interview Preparation for Freshers",
        "When to start system design, the interview framework, 15 practice problems "
        "and the numbers worth memorising."),
    "core/git-and-linux.md": (
        "Git and Linux Basics Every Developer Is Expected to Know",
        "The Git commands, branching workflow and Linux fundamentals assumed on day "
        "one of any software job or internship."),
    "placements/company-tiers.md": (
        "Which Companies Hire from Tier-3 Colleges — Service to FAANG",
        "Company tiers explained with real CTC ranges: TCS, Infosys, Zoho, Razorpay, "
        "Amazon and more — what each expects and how long preparation takes."),
    "placements/off-campus-strategy.md": (
        "Off-Campus Placement Guide for Freshers in India",
        "How to get an off-campus job: referrals, cold emails, job portals and hiring "
        "challenges, with the weekly system and realistic conversion numbers."),
    "placements/resume.md": (
        "Fresher Resume for Software Jobs — ATS-Friendly Format",
        "How to write a fresher software engineer resume that beats the ATS, with a "
        "full example, bullet formulas and free templates."),
    "placements/interview-playbook.md": (
        "Technical Interview Preparation — OA to Offer",
        "What each interview round tests, the script that works in DSA rounds, HR "
        "questions with sample answers, and how to handle rejection."),
    "placements/internships.md": (
        "How to Get an Internship as an Engineering Student in India",
        "Where to find internships, when to apply, cold outreach templates, and how "
        "to convert an internship into a pre-placement offer (PPO)."),
    "tracks/README.md": (
        "Which Career Track to Choose — Frontend, Backend, QA, DevOps or Data",
        "Compare 8 software career tracks by entry difficulty, fresher openings and "
        "salary, and pick the one that fits you."),
}

# Real questions with real answers → eligible for Google's FAQ rich results.
FAQ = {
    "guides/tier-3-college-placement.md": [
        ("Can you get a good job from a tier-3 college?",
         "Yes. Online assessments and coding interviews do not show your college name, "
         "so skill is the filter. Most tier-3 students who reach product companies do it "
         "off-campus, and many reach top companies by switching jobs after 18–24 months."),
        ("How much DSA is needed for placement from a tier-3 college?",
         "Around 150–200 problems for service companies, 300–400 for mid product "
         "companies and startups, and 450–550 for strong product companies."),
        ("When should a tier-3 student start placement preparation?",
         "Second year is ideal, because internship applications open in the third year. "
         "Starting in third year still works; starting in the final semester limits you "
         "mostly to service companies."),
    ],
    "guides/software-engineer-roadmap-india.md": [
        ("What is the roadmap to become a software engineer in India?",
         "Learn one programming language well, build DSA alongside it, pick a single "
         "track such as full stack or backend, ship two deployed projects, learn CS "
         "fundamentals, then apply widely off-campus."),
        ("How long does it take to become job-ready?",
         "About 6 months of consistent daily work for service companies, 12–18 months "
         "for product companies and startups, and roughly 24 months for strong product companies."),
    ],
    "guides/btech-placement-preparation.md": [
        ("How to prepare for placement in B.Tech?",
         "Work on four things in parallel: DSA daily, one career track with real "
         "projects, CS fundamentals, and aptitude if you are targeting service "
         "companies. Then apply off-campus at volume from third year."),
        ("Which subjects are important for placement?",
         "Data structures and algorithms, operating systems, DBMS with SQL, computer "
         "networks and object-oriented programming."),
    ],
    "guides/dsa-roadmap-for-placement.md": [
        ("How many DSA questions are enough for placement?",
         "150–200 for service companies, 300–400 for mid product companies, 450–550 "
         "for strong product companies, and 600+ for FAANG-level roles."),
        ("Which DSA sheet is best for placement preparation?",
         "Striver's A2Z sheet if you have eight months or more, or NeetCode 150 if you "
         "have less time. Pick one and finish it rather than collecting sheets."),
        ("Which language is best for DSA?",
         "C++, Java or Python all work. C++ is strongest for contests, Java has the most "
         "openings in Indian mass hiring, and Python is the quickest to start with. "
         "Pick one and stay with it for a year."),
    ],
    "guides/off-campus-placement-guide.md": [
        ("How do freshers get off-campus jobs?",
         "Mostly through referrals, direct applications on company career pages, "
         "curated portals such as Instahyre and Wellfound, cold emails to startups, "
         "and hiring challenges. Referrals convert best by a wide margin."),
        ("How many applications does it take to get a job?",
         "Roughly 300 applications produce about 40 responses, 12 interviews and 2–3 "
         "offers. That ratio is normal, not a sign of failure."),
    ],
}

# Sidebar structure: (group label, [(source md path, nav label)])
NAV = [
    ("Start here", [
        ("README.md", "Home"),
        ("START-HERE.md", "Start Here"),
    ]),
    ("The 4-year roadmap", [
        ("roadmap/README.md", "Overview"),
        ("roadmap/year-1.md", "Year 1 — Build the base"),
        ("roadmap/year-2.md", "Year 2 — Go deep"),
        ("roadmap/year-3.md", "Year 3 — Get proof"),
        ("roadmap/year-4.md", "Year 4 — Convert"),
        ("roadmap/late-start.md", "Started late?"),
    ]),
    ("Career tracks", [
        ("tracks/README.md", "Choose a track"),
        ("tracks/frontend.md", "Frontend"),
        ("tracks/backend.md", "Backend"),
        ("tracks/full-stack.md", "Full Stack"),
        ("tracks/qa-sdet.md", "QA / SDET"),
        ("tracks/devops-cloud.md", "DevOps / Cloud"),
        ("tracks/data-ai-ml.md", "Data / AI / ML"),
        ("tracks/mobile.md", "Mobile"),
        ("tracks/non-coding-tech-roles.md", "Non-coding tech"),
    ]),
    ("Core skills", [
        ("core/dsa.md", "DSA"),
        ("core/aptitude-and-maths.md", "Aptitude & Maths"),
        ("core/cs-fundamentals.md", "CS Fundamentals"),
        ("core/system-design.md", "System Design"),
        ("core/git-and-linux.md", "Git & Linux"),
    ]),
    ("Getting hired", [
        ("placements/company-tiers.md", "Company tiers"),
        ("placements/off-campus-strategy.md", "Off-campus strategy"),
        ("placements/resume.md", "Resume"),
        ("placements/portfolio-and-github.md", "GitHub & portfolio"),
        ("placements/linkedin-and-networking.md", "LinkedIn & networking"),
        ("placements/internships.md", "Internships"),
        ("placements/interview-playbook.md", "Interview playbook"),
    ]),
    ("Build & practice", [
        ("projects/README.md", "Project ideas"),
        ("resources/free-resources.md", "Free resources"),
        ("resources/practice-platforms.md", "Practice platforms"),
    ]),
    ("Templates", [
        ("templates/90-day-plan.md", "90-day plan"),
        ("templates/weekly-tracker.md", "Weekly tracker"),
        ("templates/resume-template.md", "Resume template"),
    ]),
    ("Popular guides", [
        ("guides/tier-3-college-placement.md", "Tier-3 college placement"),
        ("guides/btech-placement-preparation.md", "B.Tech placement prep"),
        ("guides/software-engineer-roadmap-india.md", "SDE roadmap (India)"),
        ("guides/dsa-roadmap-for-placement.md", "DSA roadmap"),
        ("guides/off-campus-placement-guide.md", "Off-campus placement"),
    ]),
    ("Repo", [
        ("CONTRIBUTING.md", "Contributing"),
    ]),
]

SEO_GUIDES = {
    "guides/tier-3-college-placement.md": (
        "How to Get Placed from a Tier-3 College — Complete Guide",
        "Can you get a good job from a tier-3 college? Yes. Here's how much DSA you "
        "need, which companies hire, and the year-by-year plan that actually works."),
    "guides/btech-placement-preparation.md": (
        "B.Tech Placement Preparation — Complete Guide for Engineering Students",
        "How to prepare for placement in B.Tech: what to study, which subjects matter, "
        "when to start, and how placement rounds actually work."),
    "guides/software-engineer-roadmap-india.md": (
        "Software Engineer Roadmap India — College to First Job",
        "The complete roadmap to become a software engineer in India: language, DSA, "
        "career track, projects, CS fundamentals and how long each stage takes."),
    "guides/dsa-roadmap-for-placement.md": (
        "DSA Roadmap for Placement — How Many Problems Are Enough?",
        "How many DSA questions you need for placement, which sheet to follow, the "
        "order to learn topics in, and the method that makes them stick."),
    "guides/off-campus-placement-guide.md": (
        "Off-Campus Placement Guide for Freshers — How to Get Hired",
        "How freshers get off-campus jobs in India: referrals, cold emails, portals "
        "and hiring challenges, with a weekly system and realistic numbers."),
}
SEO.update(SEO_GUIDES)

# Directories that are linked as `dir/` but have no README.md — build an index for them.
SECTIONS = {
    "core": ("Core skills",
             "The five things every track needs underneath it. None of these are optional.",
             "Core skills"),
    "placements": ("Getting hired",
                   "Who to target, what to send them, and how to convert the interview once you're in the room.",
                   "Getting hired"),
    "resources": ("Resources",
                  "Everything you need is free. These are the pages that prove it.",
                  "Build & practice"),
    "guides": ("Popular guides",
               "The questions students search for most, answered in full and linked "
               "into the detailed roadmaps.",
               "Popular guides"),
    "templates": ("Templates",
                  "Copy these into your fork and fill them in. Planning is 15 minutes a week, not a hobby.",
                  "Templates"),
}

ALERTS = {
    "NOTE":      ("note", "Note"),
    "TIP":       ("tip", "Tip"),
    "IMPORTANT": ("important", "Important"),
    "WARNING":   ("warning", "Warning"),
    "CAUTION":   ("caution", "Caution"),
}

RAW_HTML_RE = re.compile(r"^\s*</?(div|details|summary|br|img|p|span|kbd|sup|sub)\b", re.I)


# ─────────────────────────────────────────────────────────── helpers ──

def slugify(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = "".join(c for c in text if not unicodedata.category(c).startswith("So"))
    text = text.replace("&amp;", "and").replace("&", "and")
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_]+", "-", text) or "section"


def md_to_html_path(src):
    """core/dsa.md -> core/dsa.html ;  roadmap/README.md -> roadmap/index.html"""
    if src == "README.md":
        return "index.html"
    d, f = os.path.split(src)
    f = "index.html" if f == "README.md" else f[:-3] + ".html"
    return os.path.join(d, f) if d else f


def rel(from_page, to_page):
    """Relative URL between two output paths."""
    base = os.path.dirname(from_page) or "."
    return os.path.relpath(to_page, base).replace(os.sep, "/")


def rewrite_link(href, page_dir):
    """Rewrite an in-repo markdown link to its built HTML equivalent."""
    if re.match(r"^(https?:|mailto:|#|//)", href):
        return href
    anchor = ""
    if "#" in href:
        href, anchor = href.split("#", 1)
        anchor = "#" + anchor
    if not href:
        return anchor
    target = os.path.normpath(os.path.join(page_dir, href))
    if href.endswith("/") or (not os.path.splitext(href)[1]):
        # directory link -> that directory's index page
        cand = os.path.join(target, "README.md")
        out = md_to_html_path(os.path.relpath(cand, ".")) if os.path.exists(
            os.path.join(ROOT, cand)) else os.path.join(target, "index.html")
    elif href.endswith(".md"):
        out = md_to_html_path(os.path.relpath(target, "."))
    else:
        return href + anchor
    out = os.path.normpath(out).replace(os.sep, "/")
    return rel(md_to_html_path(os.path.join(page_dir, "x.md")), out) + anchor


# ─────────────────────────────────────────────────────── inline pass ──

def inline(text, page_dir):
    out, i, n = [], 0, len(text)
    while i < n:
        ch = text[i]

        # inline code — protected from everything else
        if ch == "`":
            m = re.match(r"(`+)(.+?)\1", text[i:], re.S)
            if m:
                out.append("<code>%s</code>" % html.escape(m.group(2)))
                i += m.end()
                continue

        # raw html tag passthrough
        if ch == "<":
            m = re.match(r"</?[A-Za-z][^<>]*>", text[i:])
            if m:
                out.append(m.group(0))
                i += m.end()
                continue

        # image
        if ch == "!" and i + 1 < n and text[i + 1] == "[":
            m = re.match(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text[i:])
            if m:
                alt, src = m.group(1), m.group(2)
                cls = "badge" if "img.shields.io" in src else "md-img"
                out.append('<img class="%s" src="%s" alt="%s" loading="lazy">'
                           % (cls, html.escape(src, True), html.escape(alt, True)))
                i += m.end()
                continue

        # link
        if ch == "[":
            m = re.match(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^()\s]+(?:\([^)]*\))?)\)", text[i:])
            if m:
                label, href = m.group(1), m.group(2)
                url = rewrite_link(href, page_dir)
                ext = ' target="_blank" rel="noopener"' if re.match(r"^https?:", url) else ""
                out.append('<a href="%s"%s>%s</a>' % (html.escape(url, True), ext,
                                                      inline(label, page_dir)))
                i += m.end()
                continue

        for pat, tag in ((r"\*\*\*(.+?)\*\*\*", "strong-em"), (r"\*\*(.+?)\*\*", "strong"),
                         (r"~~(.+?)~~", "del"), (r"(?<!\*)\*(?!\*)([^*]+?)\*(?!\*)", "em")):
            m = re.match(pat, text[i:], re.S)
            if m:
                inner = inline(m.group(1), page_dir)
                out.append("<strong><em>%s</em></strong>" % inner if tag == "strong-em"
                           else "<%s>%s</%s>" % (tag, inner, tag))
                i += m.end()
                break
        else:
            out.append(html.escape(ch) if ch in "&<>" else ch)
            i += 1
            continue
    return "".join(out)


# ──────────────────────────────────────────────────────── block pass ──

def render(md, page_dir):
    lines = md.split("\n")
    html_out, toc = [], []
    i, n = 0, len(lines)

    def close_lists(stack):
        while stack:
            html_out.append("</%s>" % stack.pop())

    list_stack = []

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # ── code fence (supports 3+ backticks, nested) ──
        fence = re.match(r"^(`{3,})\s*([\w-]*)\s*$", stripped)
        if fence:
            close_lists(list_stack)
            marker, lang = fence.group(1), fence.group(2).lower()
            body, i = [], i + 1
            while i < n and not re.match(r"^`{%d,}\s*$" % len(marker), lines[i].strip()):
                body.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(body)
            if lang == "mermaid":
                html_out.append('<div class="mermaid-wrap"><pre class="mermaid">%s</pre></div>'
                                % html.escape(code))
            else:
                html_out.append(
                    '<div class="code-block" data-lang="%s"><button class="copy" '
                    'aria-label="Copy code">Copy</button><pre><code>%s</code></pre></div>'
                    % (html.escape(lang or "text", True), html.escape(code)))
            continue

        # ── blank ──
        if not stripped:
            close_lists(list_stack)
            i += 1
            continue

        # ── GitHub alert ──
        alert = re.match(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", stripped)
        if alert:
            close_lists(list_stack)
            kind, label = ALERTS[alert.group(1)]
            body, i = [], i + 1
            while i < n and lines[i].strip().startswith(">"):
                body.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = render("\n".join(body), page_dir)[0]
            html_out.append('<div class="alert alert-%s"><p class="alert-label">%s</p>%s</div>'
                            % (kind, label, inner))
            continue

        # ── blockquote ──
        if stripped.startswith(">"):
            close_lists(list_stack)
            body = []
            while i < n and lines[i].strip().startswith(">"):
                body.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            html_out.append("<blockquote>%s</blockquote>" % render("\n".join(body), page_dir)[0])
            continue

        # ── table ──
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            close_lists(list_stack)

            def cells(row):
                return [c.strip() for c in row.strip().strip("|").split("|")]

            head = cells(lines[i])
            aligns = []
            for spec in cells(lines[i + 1]):
                aligns.append("center" if spec.startswith(":") and spec.endswith(":")
                              else "right" if spec.endswith(":") else "left")
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            t = ['<div class="table-wrap"><table><thead><tr>']
            for k, h in enumerate(head):
                t.append('<th style="text-align:%s">%s</th>'
                         % (aligns[k] if k < len(aligns) else "left", inline(h, page_dir)))
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>")
                for k, c in enumerate(r):
                    t.append('<td style="text-align:%s">%s</td>'
                             % (aligns[k] if k < len(aligns) else "left", inline(c, page_dir)))
                t.append("</tr>")
            t.append("</tbody></table></div>")
            html_out.append("".join(t))
            continue

        # ── heading ──
        head = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if head:
            close_lists(list_stack)
            level, text = len(head.group(1)), head.group(2).strip()
            sid = slugify(text)
            rendered = inline(text, page_dir)
            # Skip h3s in the centered page header (the tagline) — they sit before
            # the first h2 and would otherwise dominate the table of contents.
            if level == 2 or (level == 3 and any(t["level"] == 2 for t in toc)):
                toc.append({"level": level, "id": sid,
                            "text": re.sub(r"<[^>]+>", "", rendered).strip()})
            anchor = ('<a class="hanchor" href="#%s" aria-label="Link to this section">#</a>' % sid
                      if level > 1 else "")
            html_out.append('<h%d id="%s">%s%s</h%d>' % (level, sid, rendered, anchor, level))
            i += 1
            continue

        # ── hr ──
        if re.match(r"^(---+|\*\*\*+|___+)$", stripped):
            close_lists(list_stack)
            html_out.append("<hr>")
            i += 1
            continue

        # ── list item ──
        li = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", line)
        if li:
            indent = len(li.group(1))
            ordered = li.group(2).endswith(".")
            content = li.group(3)
            depth = indent // 2
            tag = "ol" if ordered else "ul"

            while len(list_stack) > depth + 1:
                html_out.append("</%s>" % list_stack.pop())
            if len(list_stack) == depth + 1 and list_stack[-1] != tag:
                html_out.append("</%s>" % list_stack.pop())
            if len(list_stack) < depth + 1:
                cls = ""
                if not ordered and re.match(r"^\[[ xX]\]\s", content):
                    cls = ' class="task-list"'
                html_out.append("<%s%s>" % (tag, cls))
                list_stack.append(tag)

            task = re.match(r"^\[([ xX])\]\s+(.*)$", content)
            if task:
                checked = " checked" if task.group(1).lower() == "x" else ""
                html_out.append(
                    '<li class="task"><input type="checkbox" disabled%s><span>%s</span></li>'
                    % (checked, inline(task.group(2), page_dir)))
            else:
                html_out.append("<li>%s</li>" % inline(content, page_dir))
            i += 1
            continue

        # ── raw html block line ──
        if RAW_HTML_RE.match(line):
            close_lists(list_stack)
            html_out.append(line)
            i += 1
            continue

        # ── paragraph ──
        close_lists(list_stack)
        para = []
        while i < n and lines[i].strip() and not re.match(
                r"^(\s*)([-*+]|\d+\.)\s+|^#{1,6}\s|^>|^\||^`{3,}|^(---+|\*\*\*+)$", lines[i]) \
                and not RAW_HTML_RE.match(lines[i]):
            para.append(lines[i].strip())
            i += 1
        if para:
            html_out.append("<p>%s</p>" % inline(" ".join(para), page_dir))
        else:
            html_out.append(line)
            i += 1

    close_lists(list_stack)
    return "\n".join(html_out), toc


# ────────────────────────────────────────────────────────── shell ──

def sidebar_html(current):
    parts = []
    for group, items in NAV:
        parts.append('<div class="nav-group"><p class="nav-label">%s</p><ul>' % html.escape(group))
        for src, label in items:
            page = md_to_html_path(src)
            active = ' class="active" aria-current="page"' if page == current else ""
            parts.append('<li><a href="%s"%s>%s</a></li>'
                         % (rel(current, page), active, html.escape(label)))
        parts.append("</ul></div>")
    return "".join(parts)


FLAT = [(md_to_html_path(s), l) for _, items in NAV for s, l in items]


def canonical_for(page):
    return SITE_URL + ("/" if page == "index.html" else "/" + page)


def structured_data(page, title, description, src_md):
    """JSON-LD: breadcrumbs everywhere, WebSite on the landing page, Article on
    docs, and FAQPage where we have genuine question/answer pairs."""
    org = {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL}
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL}]
    section = os.path.dirname(page)
    if section:
        crumbs.append({"@type": "ListItem", "position": 2,
                       "name": section.replace("-", " ").title(),
                       "item": f"{SITE_URL}/{section}/"})
    if page != "index.html":
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1,
                       "name": title.split(" — ")[0], "item": canonical_for(page)})

    graph = [{"@type": "BreadcrumbList", "itemListElement": crumbs}]

    if page == "index.html":
        graph.append({
            "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL,
            "description": description, "inLanguage": "en-IN", "publisher": org,
            "alternateName": ["Tier-3 College to FAANG Roadmap",
                              "Software Engineer Roadmap India",
                              "B.Tech Placement Roadmap"],
        })
    else:
        graph.append({
            "@type": "Article", "headline": title[:110], "description": description,
            "url": canonical_for(page), "inLanguage": "en-IN",
            "author": org, "publisher": org,
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical_for(page)},
        })

    if src_md in FAQ:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in FAQ[src_md]],
        })

    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))


def shell(*, page, title, description, body, toc, landing=False):
    depth = rel(page, "index.html")
    assets = os.path.dirname(depth) + "/" if os.path.dirname(depth) else ""
    idx = next((k for k, (p, _) in enumerate(FLAT) if p == page), None)

    pager = ""
    if idx is not None and not landing:
        prev_l = ('<a class="pager-link prev" href="%s"><span>Previous</span><strong>%s</strong></a>'
                  % (rel(page, FLAT[idx - 1][0]), html.escape(FLAT[idx - 1][1]))) if idx > 0 else "<div></div>"
        next_l = ('<a class="pager-link next" href="%s"><span>Next</span><strong>%s</strong></a>'
                  % (rel(page, FLAT[idx + 1][0]), html.escape(FLAT[idx + 1][1]))) if idx < len(FLAT) - 1 else "<div></div>"
        pager = '<nav class="pager">%s%s</nav>' % (prev_l, next_l)

    toc_html = ""
    if toc and not landing:
        items = "".join('<li class="lvl%d"><a href="#%s">%s</a></li>'
                        % (t["level"], t["id"], html.escape(t["text"])) for t in toc)
        toc_html = '<aside class="toc"><p class="toc-label">On this page</p><ul>%s</ul></aside>' % items

    src_md = next((s for _, items in NAV for s, _ in items if md_to_html_path(s) == page), None)
    edit = ('<a class="edit-link" href="%s/blob/main/%s" target="_blank" rel="noopener">Edit on GitHub</a>'
            % (REPO_URL, src_md)) if src_md else ""

    canonical = canonical_for(page)
    og_type = "website" if landing else "article"
    jsonld = structured_data(page, title, description, src_md)

    main = (('<main id="main" class="landing">%s</main>' % body) if landing else
            '<main id="main" class="content"><article class="prose">%s</article>%s%s</main>'
            % (body, edit, pager))

    return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0B1020">
<meta property="og:site_name" content="{html.escape(SITE_NAME)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_IN">
<meta property="og:type" content="{og_type}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(description)}">
<script type="application/ld+json">{jsonld}</script>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='22' fill='%230B1020'/><text y='72' x='50' text-anchor='middle' font-size='58' font-family='monospace' font-weight='700' fill='%23FF6B3D'>T3</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}assets/style.css">
<script>try{{var t=localStorage.getItem('t3-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
</head>
<body class="{'is-landing' if landing else 'is-doc'}">
<a class="skip" href="#main">Skip to content</a>
<div class="read-progress" aria-hidden="true"><i></i></div>

<header class="topbar">
  <button class="icon-btn nav-toggle" aria-label="Open navigation" aria-expanded="false">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
  </button>
  <a class="brand" href="{depth}">
    <span class="brand-mark">T3</span>
    <span class="brand-text">Tier-3 <em>to</em> Top Tech</span>
  </a>
  <button class="search-trigger" data-search-open>
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
    <span>Search</span><kbd>⌘K</kbd>
  </button>
  <div class="topbar-actions">
    <button class="icon-btn theme-toggle" aria-label="Switch theme">
      <svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>
      <svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z"/></svg>
    </button>
    <a class="icon-btn" href="{REPO_URL}" target="_blank" rel="noopener" aria-label="View on GitHub">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.53 2.34 1.09 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.02a9.5 9.5 0 0 1 5 0c1.91-1.29 2.75-1.02 2.75-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.69-4.57 4.94.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>
    </a>
  </div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <nav aria-label="Documentation">{'' if landing else sidebar_html(page)}</nav>
  </aside>
  <div class="scrim" data-close-nav></div>
  {main}
  {'' if landing else toc_html}
</div>

<div class="search-modal" hidden>
  <div class="search-backdrop" data-search-close></div>
  <div class="search-panel" role="dialog" aria-modal="true" aria-label="Search">
    <div class="search-field">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input type="search" placeholder="Search roadmaps, tracks, companies…" aria-label="Search" autocomplete="off">
      <kbd>Esc</kbd>
    </div>
    <div class="search-results" role="listbox"></div>
  </div>
</div>

<footer class="site-footer">
  <div class="foot-inner">
    <p class="foot-brand">Tier-3 <em>to</em> Top Tech</p>
    <p class="foot-note">Free forever, MIT licensed. Your college is a starting point, not a ceiling.</p>
    <p class="foot-links">
      <a href="{REPO_URL}" target="_blank" rel="noopener">GitHub</a>
      <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">Contribute</a>
      <a href="{rel(page, 'START-HERE.html')}">Start here</a>
    </p>
  </div>
</footer>

<script>window.T3_BASE="{assets}";</script>
<script src="{assets}assets/app.js" defer></script>
</body>
</html>"""


# ────────────────────────────────────────────────────────── build ──

def first_paragraph(md):
    for line in md.split("\n"):
        s = line.strip()
        if s and not s.startswith(("#", "<", ">", "-", "|", "!", "[", "*", "=")):
            return re.sub(r"[*`\[\]]|\(.*?\)", "", s)[:180]
    return "A free 4-year career roadmap for students in tier-3 engineering colleges."


def page_title(md, fallback):
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        t = "".join(c for c in t if not unicodedata.category(c).startswith("So")).strip()
        return t or fallback
    return fallback


def main():
    if os.path.isdir(OUT):
        for name in os.listdir(OUT):
            if name != "CNAME":
                p = os.path.join(OUT, name)
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

    for asset in ("style.css", "app.js"):
        shutil.copy(os.path.join(TOOLS, "assets", asset), os.path.join(OUT, "assets", asset))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    index = []
    built = 0

    for _, items in NAV:
        for src, label in items:
            md = open(os.path.join(ROOT, src), encoding="utf-8").read()
            page = md_to_html_path(src)
            page_dir = os.path.dirname(src)
            seo_title, seo_desc = SEO.get(src, (None, None))
            title = seo_title or f"{page_title(md, label)} · {SITE_TITLE}"
            desc = seo_desc or first_paragraph(md)

            if src == "README.md":
                body = open(os.path.join(TOOLS, "landing.html"), encoding="utf-8").read()
                out_html = shell(page=page, title=title, description=desc,
                                 body=body, toc=[], landing=True)
            else:
                body, toc = render(md, page_dir)
                out_html = shell(page=page, title=title, description=desc,
                                 body=body, toc=toc)
                index.append({
                    "t": title, "l": label, "u": page,
                    "h": [x["text"] for x in toc][:24],
                    "b": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))[:1400],
                })

            dest = os.path.join(OUT, page)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "w", encoding="utf-8").write(out_html)
            built += 1

    # ── section index pages for directories linked as `dir/` ──
    for folder, (heading, blurb, nav_group) in SECTIONS.items():
        page = folder + "/index.html"
        items = next((its for grp, its in NAV if grp == nav_group), [])
        items = [(s, l) for s, l in items if s.startswith(folder + "/")]

        cards = []
        for src, label in items:
            md = open(os.path.join(ROOT, src), encoding="utf-8").read()
            m = re.search(r"^###\s+(.+)$", md, re.M)
            tag = re.sub(r"[*_`]", "", m.group(1)).strip() if m else first_paragraph(md)
            cards.append(
                '<a class="track" href="%s"><div class="track-top"><h3>%s</h3></div><p>%s</p></a>'
                % (rel(page, md_to_html_path(src)), html.escape(label), html.escape(tag)))

        body = (
            '<h1>%s</h1><p class="section-blurb">%s</p><div class="track-grid">%s</div>'
            % (html.escape(heading), html.escape(blurb), "".join(cards)))

        out_html = shell(page=page, title=f"{heading} · {SITE_TITLE}",
                         description=blurb, body=body, toc=[])
        dest = os.path.join(OUT, page)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(out_html)
        built += 1

    json.dump(index, open(os.path.join(OUT, "assets", "search.json"), "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))

    # ── sitemap.xml ──
    today = datetime.date.today().isoformat()
    pages = sorted({md_to_html_path(s) for _, items in NAV for s, _ in items} |
                   {f + "/index.html" for f in SECTIONS})
    urls = []
    for p in pages:
        # Landing page first, guides and roadmaps next: priority reflects how much
        # of the site's value each page carries, not wishful thinking.
        if p == "index.html":
            pri, freq = "1.0", "weekly"
        elif p.startswith(("guides/", "roadmap/")):
            pri, freq = "0.9", "monthly"
        elif p.endswith("index.html"):
            pri, freq = "0.6", "monthly"
        else:
            pri, freq = "0.8", "monthly"
        urls.append(f"  <url>\n    <loc>{canonical_for(p)}</loc>\n"
                    f"    <lastmod>{today}</lastmod>\n"
                    f"    <changefreq>{freq}</changefreq>\n"
                    f"    <priority>{pri}</priority>\n  </url>")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "\n".join(urls) + "\n</urlset>\n")

    # ── robots.txt ──
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"Built {built} pages -> docs/")
    print(f"sitemap.xml: {len(urls)} URLs")
    print(f"Search index: {len(index)} documents")


if __name__ == "__main__":
    main()
