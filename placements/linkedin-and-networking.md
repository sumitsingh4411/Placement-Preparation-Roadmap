<div align="center">

# 💼 LinkedIn & Networking

### The unfair advantage nobody in your college is using.

[🏠 Home](../README.md) • [🎯 Placements](../placements/) • [📤 Off-campus](off-campus-strategy.md) • [🐙 GitHub](portfolio-and-github.md)

</div>

---

## Why this matters more than you think

**A referral is roughly 10× more likely to get you an interview than a portal application.** Referrals come from people. People come from networking. Networking, for a tier-3 student with no industry connections, happens on LinkedIn.

Your batchmates treat LinkedIn as a place to post "Excited to share that I have completed a 3-day webinar 🙏". That is the opportunity — the bar is on the floor, and a genuinely well-run profile stands out immediately.

> [!IMPORTANT]
> **Build your network before you need it.** Connecting with 200 engineers in your 3rd year means 200 possible referral sources in your 4th. Connecting with them the week you start applying means you're a stranger asking for a favour.

---

## 🎯 Your profile

### Photo & banner
- [ ] **Clear headshot** — good lighting, plain background, look at the camera, smile. A phone photo is fine
- [ ] **Banner** — a simple tech-themed one, or your tech stack. Not the default grey

### Headline ⭐ (the most-read line on your profile)

```
✅ Final Year CS Student | Full Stack Developer | React, Node.js, PostgreSQL | Open to SDE Roles 2026

✅ SDET Aspirant | Selenium, Java, TestNG, REST Assured | Building automation frameworks

❌ Aspiring Software Engineer | Passionate Learner | Student at XYZ College
❌ Student | Fresher | Looking for opportunities
```

**Formula:** `[Who you are] | [What you do] | [Your stack] | [What you want]`

Include your actual technologies — **recruiters search LinkedIn by keyword.** "Passionate learner" is not a search term. "React" is.

### About section

Write 3–4 short paragraphs, first person, no buzzwords:

```
I'm a final-year CS student who builds full-stack web applications.

Most recently I built ShopNest, an e-commerce platform with real-time order
tracking — React on the front, Node and PostgreSQL behind it, with Redis
caching that cut search latency from 800ms to 120ms. Live at shopnest.vercel.app.

I've solved 500+ DSA problems on LeetCode and I'm most interested in backend
work — caching, queues, and the parts of a system that break under load.

Looking for SDE roles starting mid-2026. Open to conversations about backend
and full-stack engineering.

📧 sumit.singh@gmail.com | 🔗 github.com/sumitsingh
```

**Rules:** specific over generic, include real numbers, name your technologies, end with contact details. **Never** write "I am a hardworking and dedicated individual seeking an opportunity to utilise my skills."

### Featured section ⭐
Pin your **best 3 projects** with live links and thumbnails. This is the first thing people click.

### Experience
Internships, freelance work, significant open-source contributions. Same bullet style as your resume — action verb, what you did, quantified result. → [resume.md](resume.md)

### Projects
Add your top 4–5 with descriptions, tech used, and links.

### Skills
- [ ] Add 20–30 relevant skills *(recruiters filter by these)*
- [ ] Reorder so your top 3 are the ones you actually want to be hired for
- [ ] Ask friends to endorse your top skills

### Settings
- [ ] Turn on **"Open to Work"** *(choose recruiters-only if you'd rather not display the badge)*
- [ ] Set a **custom URL** — `linkedin.com/in/sumitsingh` not `linkedin.com/in/sumit-singh-8a4f92b1c`
- [ ] Turn on **creator mode** if you plan to post regularly

---

## 🤝 Building the network

### Who to connect with (in priority order)

<div align="center">

| Priority | Who | Why |
|:---:|---|---|
| 🥇 | **Alumni from your college** ⭐ | Highest response rate by far. Shared context, genuine goodwill |
| 🥈 | **Engineers with 1–4 years experience** | More responsive than senior people, often get referral bonuses |
| 🥉 | **People from your city or home state** | Shared context helps |
| 4 | **Recruiters** at your target companies | They're literally paid to find candidates |
| 5 | **People who post about hiring** | They're actively looking |
| 6 | **Students ahead of you who got placed** | They know your college's specific situation |

</div>

**How to find alumni:** LinkedIn → search your college → "Alumni" tab → filter by "where they work" and "what they do".

### Connection requests

**Always send a note.** Blank requests from strangers get ignored.

> Hi [Name], I'm a 3rd-year CS student at [College] — saw you graduated from there too. I'm working on backend development and would love to follow your work. Thanks!

> Hi [Name], I've been following [Company]'s engineering blog, especially the post on [topic]. I'm a CS student working in a similar space — would love to connect.

**Then wait.** Do not ask for a referral in the first message. Connect first, engage a little, ask later. → [off-campus-strategy.md](off-campus-strategy.md#-channel-1--referrals-do-this-the-most)

---

## 📝 Posting (the compounding advantage)

**Posting consistently generates inbound recruiter messages.** Almost no student does this, which is exactly why it works.

### What to post

| ✅ Post this | ❌ Not this |
|---|---|
| A project you shipped, with a live link and what you learned | "Excited to share I completed a 3-day webinar 🙏" |
| A technical problem you solved and how | Generic motivational quotes |
| What you learned from a rejection | "Humbled and blessed" certificate photos |
| A comparison you researched (e.g. two caching strategies) | Reposting other people's content with no comment |
| Your DSA milestone with a specific insight | "Looking for opportunities, please help 🙏" |
| A useful resource you actually used | Chain-post engagement bait |

### A post format that works

```
I spent 3 days debugging why my API got slower as data grew.

The endpoint took 120ms with 1,000 products and 4 seconds with 50,000.

Turned out I had an N+1 query problem — for every product I was making a
separate query to fetch its category. 50,000 products meant 50,001 queries.

The fix was one line: a JOIN instead of a loop.

Response time went from 4s back to 140ms.

Two things I took from it:
→ Always check the actual queries your ORM generates
→ Test with realistic data volumes, not 10 seed rows

Code: github.com/sumitsingh/shopnest

#backend #postgresql #webdevelopment
```

**Why it works:** specific problem, real numbers, an actual lesson, proof, no self-congratulation.

**Cadence:** 1–2 posts a week is plenty. Consistency beats volume.

### Engaging

Commenting thoughtfully on other people's posts is **more effective than posting** when you're starting out — it puts you in front of their network.

- Add something substantive, not "Great post! 👏"
- Comment on posts from engineers at your target companies
- 10 minutes a day is enough

---

## 🌐 Beyond LinkedIn

<div align="center">

| Platform | Why it's worth your time |
|---|---|
| **Twitter/X** ⭐ | Many Indian startups post openings only here. Devs are very accessible. Underused by students |
| **[r/developersIndia](https://www.reddit.com/r/developersIndia/)** ⭐ | Honest Indian-context advice, resume reviews, salary data, referral threads |
| **Discord servers** | Framework communities (React, Node), Indian dev communities, DSA groups |
| **GitHub** | Contributing to a project puts you in front of its maintainers → [portfolio-and-github.md](portfolio-and-github.md) |
| **Hackathons** ([Devfolio](https://devfolio.co/), [MLH](https://mlh.io/)) | Meet people who build. Winning teams get recruiter attention |
| **Local meetups** ([Meetup.com](https://www.meetup.com/), tech conferences) | Rare in tier-3 cities, but powerful if available. Many have free student tickets |
| **[Peerlist](https://peerlist.io/)** | Indian professional network for developers, growing fast |

</div>

---

## 💬 Warming up before you ask

Cold-asking for a referral works, but a *warm* ask works much better. Over 2–3 weeks:

1. **Connect** with a note
2. **Engage** — comment thoughtfully on 2–3 of their posts
3. **Share something relevant** — "Saw your post on X, I ran into the same thing building Y, here's what I found"
4. **Then ask** — for advice first, referral second

**Asking for advice is a better opener than asking for a referral:**

> Hi [Name], I'm a final-year student targeting backend roles. I've built [project] and solved 500+ DSA problems. Given your experience at [Company], is there anything you'd suggest I focus on to be a strong candidate for teams like yours?

People love giving advice. Many will follow up with "actually, send me your resume — I'll refer you." That conversion happens far more often than you'd expect.

---

## ⚠️ Networking mistakes

| Mistake | Fix |
|---|---|
| **Blank connection requests** | Always add a note. It doubles acceptance rates. |
| **Asking for a referral in the first message** | Connect, engage, then ask. |
| **"Please refer me sir, I need job urgently"** | Be specific and professional. Show what you built first. |
| **Following up 5 times** | Once, after a week. Then move on. |
| **Only networking when you need something** | Build it in your 3rd year, before you need it. |
| **Posting certificate photos** | Post work, problems and lessons instead. |
| **Copy-pasted mass DMs** | Personalise at least one line. It's obvious when you don't. |
| **Never posting at all** | 1–2 posts a week generates inbound opportunities. |
| **Ignoring recruiters who message you** | Always reply, even to decline politely. Keep the relationship. |
| **Being negative in public** | Recruiters read your feed. Complaining about companies is visible. |

---

## ✅ Your weekly networking routine

<div align="center">

| Task | Time | Frequency |
|---|:---:|:---:|
| Send 15 connection requests with notes | 30 min | Weekly |
| Comment meaningfully on 10 posts | 20 min | Weekly |
| Write 1 post about what you built or learned | 20 min | Weekly |
| Send 15 referral requests *(final year)* | 45 min | Weekly |
| Reply to every message you receive | 10 min | Daily |

</div>

**Compounding effect:** 15 connections a week = ~750 a year. Even at a 10% response rate on referral asks, that's 75 possible referrals during your placement season. Your batchmates will have zero.

---

<div align="center">

### Your batch has 200 people. Your network can have 2,000. Build it in year 3, use it in year 4.

[🏠 Home](../README.md) • [📤 Off-campus](off-campus-strategy.md) • [🧾 Resume](resume.md) • [🐙 GitHub](portfolio-and-github.md) • [🎯 Internships](internships.md)

</div>
