<div align="center">

# 🧾 Resume That Gets Interviews

### 6 seconds of human attention, or an ATS that never shows it to a human at all.

[🏠 Home](../README.md) • [🎯 Placements](../placements/) • [🐙 GitHub](portfolio-and-github.md) • [📤 Off-campus](off-campus-strategy.md)

</div>

---

## The two gatekeepers

**1. The ATS (Applicant Tracking System)** — software that parses your resume into text and matches keywords. If it can't parse your file, a human never sees it.

**2. A recruiter, for 6–8 seconds** — they scan for role fit, tech stack, projects, and any reason to move you forward.

Your resume has one job: **get you an interview.** Nothing else. It doesn't need to tell your life story or look like a designer's portfolio.

---

## The non-negotiable rules

<div align="center">

| Rule | Why |
|---|---|
| **One page.** Always. | You have 0–1 years experience. Two pages signals padding. |
| **PDF only** | Word files break formatting. Name it `Sumit_Singh_Resume.pdf` |
| **Single column** ⭐ | Two-column layouts scramble in most ATS parsers |
| **No tables, text boxes, images, icons or charts** ⭐ | ATS parsers frequently drop their contents entirely |
| **No photo** | Not standard in Indian tech; wastes space |
| **Standard fonts** | Calibri, Arial, Helvetica, Garamond, Times. 10–11pt |
| **Standard section headings** | "Experience", "Education", "Projects", "Skills" — not "My Journey" |
| **Reverse chronological** | Most recent first, always |
| **No personal details** | No age, marital status, father's name, full address, or "Declaration" |

</div>

> [!WARNING]
> **Do not use fancy Canva templates with sidebars, icons and progress bars.** They look impressive to you and parse as gibberish to an ATS. The "skill level: React ▓▓▓▓░" bars are especially bad — they convey nothing and often break parsing.

---

## The structure

```
┌─────────────────────────────────────────────────────┐
│  SUMIT SINGH                                        │
│  sumit.singh@gmail.com · +91-XXXXXXXXXX             │
│  linkedin.com/in/sumitsingh · github.com/sumitsingh │
│  Portfolio: sumitsingh.dev                          │
├─────────────────────────────────────────────────────┤
│  EDUCATION                          (2-3 lines)     │
├─────────────────────────────────────────────────────┤
│  SKILLS                             (4-5 lines)     │
├─────────────────────────────────────────────────────┤
│  EXPERIENCE / INTERNSHIPS           (if any)        │
├─────────────────────────────────────────────────────┤
│  PROJECTS  ⭐ YOUR BIGGEST SECTION  (2-3 projects)  │
├─────────────────────────────────────────────────────┤
│  ACHIEVEMENTS                       (2-4 lines)     │
└─────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **As a tier-3 student, PROJECTS is your most important section — put it above Experience if you have no internship.** Your college name won't sell you. Your work will.

---

## Section by section

### Header

```
SUMIT SINGH
sumit.singh@gmail.com | +91-98765-43210
linkedin.com/in/sumitsingh | github.com/sumitsingh | sumitsingh.dev
```

- ✅ Professional email — `firstname.lastname@gmail.com`
- ✅ **Hyperlink** your LinkedIn, GitHub and portfolio (recruiters click)
- ❌ No full postal address — city is enough, and only if relevant
- ❌ No photo, no "Curriculum Vitae" title, no declaration

### Education

```
B.Tech, Computer Science Engineering                              2022 – 2026
XYZ Institute of Technology, Lucknow                              CGPA: 8.2/10
```

- Add CGPA **only if it's 7.0+**. If it's lower, omit it — don't lie, just leave it out
- Relevant coursework only if you have space to fill
- Class 10/12 marks: omit unless a specific company asks for them

### Skills

Group them. Don't rate yourself. **Only list what you can be interviewed on.**

```
Languages:     Java, JavaScript, Python, SQL
Frontend:      React, Redux, HTML5, CSS3, Tailwind CSS
Backend:       Node.js, Express, Spring Boot, REST APIs
Databases:     PostgreSQL, MongoDB, Redis
Tools:         Git, Docker, Postman, AWS (EC2, S3), Linux
```

> [!WARNING]
> **Everything on this list is fair game in the interview.** Listing "Kubernetes" because you watched one video will end badly. Cut anything you can't defend for 5 minutes.

### Projects ⭐ (your most important section)

**Format for each — 3–4 bullets:**

```
E-Commerce Platform | React, Node.js, PostgreSQL, Redis, Stripe
Live: shopnest.vercel.app | Code: github.com/sumit/shopnest

• Built a full-stack marketplace with JWT authentication, role-based access
  control, and Stripe payment integration, serving 200+ registered users
• Reduced product-listing API response time from 800ms to 120ms by adding
  Redis caching and composite database indexes
• Implemented an admin dashboard with real-time order tracking via WebSockets,
  handling 50+ concurrent connections
• Deployed on AWS EC2 with Docker and a GitHub Actions CI/CD pipeline
```

**What makes those bullets work:**

| Element | Example |
|---|---|
| **Action verb first** | Built, Implemented, Reduced, Designed, Optimised, Automated |
| **What you did** | "added Redis caching and composite indexes" |
| **Quantified impact** ⭐ | "800ms → 120ms", "200+ users", "50+ concurrent connections" |
| **Tech named specifically** | Not "used a database" — "PostgreSQL with composite indexes" |

<details>
<summary><b>📊 How to quantify when you have "no numbers"</b></summary>

<br>

Students think they have nothing to measure. You do:

| Instead of | Write |
|---|---|
| "Made the app faster" | "Reduced page load from 4.2s to 1.1s using code splitting and lazy loading" |
| "Built a REST API" | "Built a REST API with 24 endpoints, documented with Swagger" |
| "Used a database" | "Designed a normalised PostgreSQL schema across 12 tables with foreign key constraints" |
| "Added authentication" | "Implemented JWT auth with refresh tokens and bcrypt hashing, supporting 3 user roles" |
| "Handled a lot of data" | "Processed 50,000+ records with pagination and server-side filtering" |
| "Wrote tests" | "Achieved 78% test coverage with 45 unit and integration tests (Jest)" |
| "Deployed it" | "Deployed via Docker on AWS EC2 with automated CI/CD, 99% uptime over 3 months" |

**Sources for real numbers:** Lighthouse scores, API response times (Postman shows them), database row counts, number of endpoints, test coverage, GitHub stars, actual user count, Play Store downloads, lines of code processed.

**Never invent numbers.** If asked "how did you measure that 800ms?", you must have an answer. Use real ones — you have more than you think.

</details>

### Experience / Internships

Same bullet format. Focus on **what you shipped**, not what you were "responsible for".

```
Software Development Intern | TechCorp Solutions, Remote          Jun – Aug 2025

• Developed 6 REST API endpoints in Spring Boot for the vendor onboarding
  module, used by 3 internal teams
• Fixed 23 production bugs, reducing customer-reported issues in the module by 40%
• Wrote 35 unit tests with JUnit, raising module coverage from 45% to 72%
```

**No internship?** Use freelance work, open-source contributions, or significant college projects. Label them honestly — "Freelance Web Developer" is a legitimate entry if you built a site for a local business.

### Achievements

Only what's verifiable and relevant:

```
• Solved 500+ DSA problems on LeetCode (Top 8% globally, rating 1750+)
• 1st place, XYZ National Hackathon 2025 (240 teams)
• Contributed 4 merged PRs to [open-source project] (2.3k GitHub stars)
• AWS Certified Cloud Practitioner (2025)
```

❌ Skip: school-level prizes, "participated in" anything, non-technical certificates of attendance, sports awards *(unless national level)*

---

## ✅ Full example (fresher, no internship)

```
─────────────────────────────────────────────────────────────────────────
SUMIT SINGH
sumit.singh@gmail.com | +91-98765-43210
linkedin.com/in/sumitsingh | github.com/sumitsingh | sumitsingh.dev
─────────────────────────────────────────────────────────────────────────

EDUCATION
B.Tech, Computer Science Engineering                          2022 – 2026
XYZ Institute of Technology, Lucknow                          CGPA: 8.2/10

SKILLS
Languages:   Java, JavaScript, Python, SQL
Frontend:    React, Redux Toolkit, HTML5, CSS3, Tailwind CSS
Backend:     Node.js, Express, Spring Boot, REST APIs, JWT
Databases:   PostgreSQL, MongoDB, Redis
Tools:       Git, Docker, AWS (EC2, S3), Postman, Linux, GitHub Actions

PROJECTS

ShopNest — E-Commerce Platform | React, Node.js, PostgreSQL, Redis, Stripe
Live: shopnest.vercel.app | Code: github.com/sumitsingh/shopnest
• Built a full-stack marketplace with JWT authentication, role-based access
  for buyers/sellers/admins, and Stripe payments; 200+ registered users
• Reduced product-search API latency from 800ms to 120ms via Redis caching
  and composite PostgreSQL indexes
• Implemented real-time order tracking with Socket.io supporting 50+
  concurrent connections
• Containerised with Docker and deployed to AWS EC2 with GitHub Actions CI/CD

DevConnect — Developer Community Platform | React, Spring Boot, MySQL
Live: devconnect.up.railway.app | Code: github.com/sumitsingh/devconnect
• Designed a normalised MySQL schema across 14 tables supporting posts,
  threaded comments, follows and notifications
• Built 28 REST endpoints documented with Swagger; secured with Spring
  Security and role-based authorisation
• Added full-text search over 10,000+ seeded posts with sub-200ms response times

TaskFlow — Kanban Project Manager | React, Node.js, MongoDB, Socket.io
Code: github.com/sumitsingh/taskflow
• Built drag-and-drop boards with optimistic UI updates and real-time
  multi-user sync via WebSockets
• Wrote 45 unit and integration tests with Jest, reaching 78% coverage

ACHIEVEMENTS
• Solved 500+ DSA problems on LeetCode — LeetCode rating 1750+ (Top 10%)
• Winner, CodeSprint 2025 National Hackathon (180 participating teams)
• 4 merged pull requests to [OSS project], a 2.3k-star open-source library
─────────────────────────────────────────────────────────────────────────
```

---

## 🤖 Beating the ATS

- [ ] **Mirror keywords from the job description.** If the JD says "RESTful APIs", write "RESTful APIs" — not just "REST"
- [ ] Use standard section headings
- [ ] Single column, no tables, no text boxes, no headers/footers
- [ ] Spell out and abbreviate: "Amazon Web Services (AWS)"
- [ ] Save as PDF with selectable text *(not an exported image)*
- [ ] **Test it:** paste your PDF into a plain text editor. If the order is scrambled or content is missing, the ATS sees the same mess
- [ ] Free checks: [Resume Worded](https://resumeworded.com/) · [Jobscan](https://www.jobscan.co/)

> [!TIP]
> **Tailor per application — it takes 5 minutes.** Keep one master resume, then for each application swap the skills order and adjust 2–3 project bullets to echo the JD's language. This measurably improves your callback rate.

---

## 🛠️ Tools

<div align="center">

| Tool | Notes |
|---|---|
| **[Overleaf + Jake's Resume](https://www.overleaf.com/latex/templates/jakes-resume/syzfjbzwjncs)** ⭐ | LaTeX, ATS-safe, the standard in tech. **Best choice** |
| **[FlowCV](https://flowcv.com/)** ⭐ | Free, ATS-friendly, no watermark |
| **[Resumake](https://resumake.io/)** | Free, simple, open source |
| **Google Docs** | Use a plain single-column template. Export as PDF |
| ❌ Canva | Beautiful and ATS-hostile. Avoid for tech applications |

</div>

---

## 🔍 Getting it reviewed

- **[r/developersIndia](https://www.reddit.com/r/developersIndia/)** — resume review threads, honest Indian-context feedback
- **[r/EngineeringResumes](https://www.reddit.com/r/EngineeringResumes/)** — very thorough, read their wiki first
- **[Resume Worded](https://resumeworded.com/)** — instant automated scoring
- **LinkedIn** — ask an engineer you've connected with
- **Seniors who got placed** — they know what worked for your specific college

**Ask specifically:** "Would you interview this person for a [role] position? What's the weakest part?" — that gets far better feedback than "please review".

---

## ⚠️ Resume mistakes

| Mistake | Fix |
|---|---|
| **Two pages as a fresher** | Cut to one. Ruthlessly. |
| **Fancy template with sidebars** | ATS-safe single column. Boring parses better. |
| **"Responsible for..." bullets** | Start with an action verb + quantify the result. |
| **No live links** | Deploy your projects. Link them. This is the #1 thing recruiters click. |
| **Listing every technology you've touched** | 5–6 you can defend. Everything listed is interview material. |
| **Objective/summary section** | Wasted space for a fresher. Cut it and add a project bullet. |
| **Skill rating bars** | Meaningless and ATS-hostile. Remove them. |
| **Same resume for every company** | Tailor keywords per JD. 5 minutes, big impact. |
| **Typos** | Instant credibility loss. Run Grammarly. Have someone else read it. |
| **Photo, DOB, father's name, declaration** | Not standard in tech. Remove all of it. |
| **Lying about skills** | You will be caught in the first technical round. Always. |

---

<div align="center">

### Your resume's only job is getting you in the room. Optimise for that, nothing else.

[🏠 Home](../README.md) • [🐙 GitHub profile](portfolio-and-github.md) • [💼 LinkedIn](linkedin-and-networking.md) • [📋 Template](../templates/resume-template.md) • [📤 Off-campus](off-campus-strategy.md)

</div>
