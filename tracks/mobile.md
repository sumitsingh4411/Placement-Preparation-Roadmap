<div align="center">

# 📱 Mobile Developer

### You ship apps people carry in their pocket. Smaller market, but you can publish real products alone.

[🏠 Home](../README.md) • [💼 All tracks](README.md) • [🎨 Frontend](frontend.md) • [🧩 Full Stack](full-stack.md)

![Difficulty](https://img.shields.io/badge/Entry-Medium-eab308?style=flat-square)
![Openings](https://img.shields.io/badge/Fresher%20openings-Medium-eab308?style=flat-square)
![CTC](https://img.shields.io/badge/Fresher%20CTC-%E2%82%B94--20%20LPA-2563eb?style=flat-square)
![Time](https://img.shields.io/badge/Time%20to%20job--ready-10--14%20months-7c3aed?style=flat-square)

</div>

---

## Is this you?

✅ **Pick mobile if:** you want to build things friends and family can actually install and use · you like polished UI and smooth interactions · you want a portfolio piece with real downloads

❌ **Skip it if:** you want maximum job options *(web has more openings)* · you don't have an Android device or decent laptop *(emulators are heavy)*

**Best part:** the most tangible portfolio in tech. **A published Play Store app with real users is one of the strongest things a tier-3 student can put on a resume** — it's public, verifiable, and almost nobody in your batch has one.

**Hardest part:** a smaller job market than web, and iOS development requires a Mac (₹60k+), which prices out most students.

---

## Pick your platform

<div align="center">

| Platform | Language | Job market in India | Cost to start |
|---|---|:---:|---|
| **Android (Native)** ⭐ | Kotlin | 🟢 Good | Free — any laptop + Android phone |
| **Flutter** ⭐ | Dart | 🟢 Good, growing fast | Free — builds for Android + iOS |
| **React Native** | JavaScript | 🟡 Decent | Free — great if you already know React |
| **iOS (Native)** | Swift | 🔴 Small in India | **Needs a Mac** — usually not viable for students |

</div>

> [!TIP]
> **Two safe picks:**
> - **Kotlin + Android** if you want the most native Android job openings in India and deep platform knowledge.
> - **Flutter** if you want one codebase for both platforms and the fastest path to a shipped app. Startups love it.
>
> **Already know React?** React Native gets you productive in weeks — but it's the weakest of the three for pure mobile job openings.

---

## Path A — Android with Kotlin

### Phase 1 — Kotlin (1.5 months)
- [ ] Syntax, `val`/`var`, null safety (`?`, `?:`, `!!`)
- [ ] Functions, lambdas, higher-order functions, extension functions
- [ ] OOP — classes, data classes, sealed classes, objects, interfaces
- [ ] Collections and their operations (`map`, `filter`, `groupBy`)
- [ ] **Coroutines** ⭐ — suspend functions, scopes, dispatchers, Flow *(essential; async is everywhere in Android)*

### Phase 2 — Android fundamentals (2 months)
- [ ] Android Studio, Gradle, project structure
- [ ] **Activity and Fragment lifecycles** ⭐ *(the #1 interview topic)*
- [ ] Layouts — XML and ConstraintLayout
- [ ] **Jetpack Compose** ⭐ — the modern standard; learn this, not just XML
- [ ] RecyclerView / LazyColumn, adapters
- [ ] Intents, navigation, passing data
- [ ] Permissions (runtime permissions)
- [ ] `SharedPreferences` / DataStore
- [ ] Resources, themes, dark mode, localisation

### Phase 3 — Architecture & data (2 months)
- [ ] **MVVM architecture** ⭐ *(asked in every Android interview)*
- [ ] ViewModel, LiveData / StateFlow
- [ ] **Room** — local database
- [ ] **Retrofit** — REST API calls
- [ ] **Hilt / Dagger** — dependency injection
- [ ] Repository pattern
- [ ] WorkManager — background tasks
- [ ] Navigation Component
- [ ] Error handling and offline-first design

### Phase 4 — Production (2 months)
- [ ] **Firebase** — Auth, Firestore, Cloud Messaging (push notifications), Analytics, Crashlytics
- [ ] Image loading — Coil / Glide
- [ ] Testing — JUnit, Espresso, Mockito
- [ ] ProGuard / R8, app size optimisation
- [ ] Performance — memory leaks, ANRs, profiling
- [ ] **Publishing to the Play Store** *(₹2,000 one-time developer fee — worth it)*
- [ ] App signing, release builds, versioning
- [ ] CI/CD — GitHub Actions for Android builds

---

## Path B — Flutter

### Phase 1 — Dart (1 month)
- [ ] Syntax, variables, null safety, functions
- [ ] OOP — classes, inheritance, mixins, abstract classes
- [ ] Collections, generics
- [ ] **Async** — Future, Stream, `async`/`await`

### Phase 2 — Flutter basics (2 months)
- [ ] Widget tree, StatelessWidget vs StatefulWidget
- [ ] Layout widgets — Row, Column, Stack, Container, Expanded, Flex
- [ ] `setState` and the widget lifecycle
- [ ] ListView, GridView, ListView.builder
- [ ] Navigation and routing
- [ ] Forms and validation
- [ ] Theming, dark mode, responsive layouts
- [ ] Animations — implicit and explicit

### Phase 3 — State management & data (2 months)
- [ ] **State management** — pick ONE: **Riverpod** ⭐ (modern), Provider (common), or BLoC (enterprise)
- [ ] HTTP / Dio for API calls
- [ ] JSON serialisation
- [ ] Local storage — SharedPreferences, Hive, SQFlite
- [ ] Clean architecture — data / domain / presentation layers
- [ ] Dependency injection (get_it)
- [ ] Error handling and loading states

### Phase 4 — Production (2 months)
- [ ] **Firebase** — Auth, Firestore, FCM, Analytics, Crashlytics
- [ ] Push notifications
- [ ] Platform channels (calling native code)
- [ ] Testing — unit, widget, integration
- [ ] Performance profiling
- [ ] **Publish to Play Store**
- [ ] CI/CD — Codemagic or GitHub Actions

---

## 💡 Projects that get you hired

<div align="center">

| Level | Project | What it proves |
|:---:|---|---|
| 🟢 | **Weather app** with an API | Networking, state, UI |
| 🟢 | **Notes app** with a local database | Persistence, CRUD |
| 🟡 | **Expense tracker** — charts, categories, local DB, export | Real utility, data viz |
| 🟡 | **Fitness / habit tracker** — notifications, streaks, charts | Background work, engagement |
| 🟠 | **Chat app** — Firebase auth, real-time messages, images, push notifications | Real-time + backend integration |
| 🟠 | **E-commerce app** — catalogue, cart, payments, order history | Complete product |
| 🔥 | **Published app with real users** | Beats everything else on this list |

</div>

> [!IMPORTANT]
> **Publish at least one app to the Play Store.** The ₹2,000 developer fee is the highest-ROI spend of your degree. "Published app with 500+ downloads" on a resume gets interviews on its own — recruiters can install it in 30 seconds and see your work. Almost nobody in your batch will have this.
>
> Add to your README: Play Store link, screenshots, a demo GIF, download count, and the architecture you used.

---

## 🎤 Interview breakdown

<div align="center">

| Round | What's tested |
|---|---|
| **DSA** | Arrays, strings, hashmaps, trees — Easy/Medium |
| **Language** | Kotlin coroutines & null safety / Dart async & widgets |
| **Platform fundamentals** ⭐ | Lifecycles, memory management, rendering |
| **Architecture** ⭐ | MVVM / Clean architecture, state management, why you chose it |
| **App optimisation** | Performance, memory leaks, app size, battery |
| **Project deep-dive** | Your published app — every decision |
| **UI round** | Build a screen live from a design |

</div>

<details>
<summary><b>❓ Mobile questions you WILL be asked</b></summary>

<br>

**Android**
1. Explain the Activity lifecycle. What happens on rotation?
2. Why does a ViewModel survive configuration changes?
3. Activity vs Fragment — when do you use each?
4. What are coroutines? Dispatchers.IO vs Dispatchers.Main?
5. Explain MVVM. Why not MVC?
6. How do you avoid memory leaks in Android?
7. LiveData vs StateFlow?
8. How does RecyclerView recycle views, and why does that matter?
9. What is an ANR and how do you prevent one?
10. How do you handle offline mode?

**Flutter**
11. StatelessWidget vs StatefulWidget?
12. Explain the Flutter widget tree, element tree and render tree.
13. What state management do you use and why?
14. How does Flutter achieve 60fps?
15. `const` constructors — why do they improve performance?
16. Hot reload vs hot restart?

**General**
17. How do you reduce app size?
18. How do you secure API keys in a mobile app? *(Never hardcode them)*
19. How do you handle different screen sizes?
20. How would you debug a crash reported only by users?

</details>

---

## 🏢 Who hires mobile developers

| Level | Companies | CTC |
|---|---|---|
| 🟢 Service | TCS, Infosys, Wipro, Accenture, Capgemini, Mindtree | ₹3.5–7 LPA |
| 🔵 Mid product & agencies | Nagarro, Thoughtworks, app agencies, funded startups | ₹6–14 LPA |
| 🟣 Strong product | Swiggy, Zomato, PhonePe, Groww, CRED, Meesho, Dream11, Jupiter, Slice | ₹15–30 LPA |
| 🔴 Top tier | Google, Microsoft, Uber, Flipkart, Amazon | ₹25–50 LPA |

> [!TIP]
> **Consumer apps are India's strongest mobile market.** Fintech (PhonePe, CRED, Groww, Jupiter), food delivery (Swiggy, Zomato), gaming (Dream11, MPL) and e-commerce (Meesho, Flipkart) all have large mobile teams and hire aggressively.

📖 **[placements/company-tiers.md](../placements/company-tiers.md)**

---

## 📚 Free resources

<div align="center">

| Topic | Resource |
|---|---|
| Android (official) | [developer.android.com/courses](https://developer.android.com/courses) ⭐ *(genuinely excellent and free)* |
| Kotlin | [kotlinlang.org/docs](https://kotlinlang.org/docs/home.html) · [Kotlin Koans](https://play.kotlinlang.org/koans) |
| Jetpack Compose | [Compose pathway](https://developer.android.com/courses/pathways/compose) |
| Android (YouTube) | [Philipp Lackner](https://www.youtube.com/@PhilippLackner) ⭐ · [CodingWithMitch](https://www.youtube.com/@codingwithmitch) |
| Flutter (official) | [docs.flutter.dev](https://docs.flutter.dev/) · [Flutter codelabs](https://docs.flutter.dev/codelabs) |
| Flutter (YouTube) | [Flutter official channel](https://www.youtube.com/@flutterdev) · [Reso Coder](https://www.youtube.com/@ResoCoder) |
| Dart | [dart.dev/guides](https://dart.dev/guides) |
| React Native | [reactnative.dev/docs](https://reactnative.dev/docs/getting-started) · [Expo docs](https://docs.expo.dev/) |
| Firebase | [firebase.google.com/docs](https://firebase.google.com/docs) |
| UI inspiration | [Mobbin](https://mobbin.com/) *(real app screens)* · [Dribbble](https://dribbble.com/) |

</div>

---

## ⚠️ Mobile-specific mistakes

| Mistake | Fix |
|---|---|
| **Never publishing an app** | ₹2,000 and a weekend. It's your single biggest differentiator. |
| **Ignoring architecture** | MVVM/Clean is asked in every interview. `setState` everywhere won't survive scrutiny. |
| **Only XML, no Compose** | Compose is the standard now. Learn it. |
| **Skipping lifecycles** | The most-asked Android topic. Know it cold. |
| **No offline handling** | Real apps handle bad networks. Show that you thought about it. |
| **Hardcoding API keys** | A security red flag reviewers spot immediately. |
| **Ugly UI** | Mobile is judged on polish. Copy good designs from Mobbin. |
| **Learning both Android and Flutter at once** | Pick one for 12 months. The second takes weeks later. |

---

<div align="center">

### Ship one app to the Play Store. It's the most verifiable proof a student can have.

[🏠 Home](../README.md) • [💼 Tracks](README.md) • [💡 Projects](../projects/README.md) • [📚 DSA](../core/dsa.md)

</div>
