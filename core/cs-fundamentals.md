<div align="center">

# 🖥️ CS Fundamentals

### OS · DBMS · Computer Networks · OOP — asked in literally every technical interview.

[🏠 Home](../README.md) • [📚 Core skills](../core/) • [🧮 DSA](dsa.md) • [🏗️ System Design](system-design.md)

![Time](https://img.shields.io/badge/Time%20needed-3--4%20months-7c3aed?style=flat-square)
![When](https://img.shields.io/badge/Best%20time-Year%202--3-2563eb?style=flat-square)
![Weight](https://img.shields.io/badge/Interview%20weight-High-dc2626?style=flat-square)

</div>

---

## The good news

**Your college already teaches these subjects.** OS, DBMS, CN and OOP are all in your syllabus. The problem is your college teaches them for *exams* — definitions, diagrams, 15-mark answers — and interviews test them differently.

**Interview style:** "What's the difference between a process and a thread, and when would you use each?"
**Exam style:** "Explain the five states of a process with a neat diagram."

Same knowledge, different framing. Study once, for interviews, and your exams get easier as a side effect.

> [!TIP]
> **Align this with your semester.** If DBMS is your current subject, do the interview prep for DBMS now. You'll ace the exam *and* the interview from one effort. This is the single most efficient thing a tier-3 student can do with their syllabus.

---

## 💾 Operating Systems

<details open>
<summary><b>Topics to cover</b></summary>

<br>

**Processes & Threads** ⭐
- [ ] Process vs thread — memory, creation cost, communication
- [ ] Process states and lifecycle
- [ ] PCB (Process Control Block), context switching
- [ ] Multithreading, concurrency vs parallelism
- [ ] User-level vs kernel-level threads

**CPU Scheduling** ⭐
- [ ] FCFS, SJF, SRTF, Round Robin, Priority scheduling
- [ ] Preemptive vs non-preemptive
- [ ] Calculating turnaround time, waiting time, response time
- [ ] Starvation and aging

**Synchronisation** ⭐
- [ ] Race conditions, critical section problem
- [ ] Mutex vs semaphore *(classic question)*
- [ ] Binary vs counting semaphores
- [ ] Producer-consumer, readers-writers, dining philosophers
- [ ] Deadlock — the **four necessary conditions**, prevention, avoidance (Banker's algorithm), detection, recovery

**Memory Management** ⭐
- [ ] Paging, segmentation
- [ ] **Virtual memory**, demand paging
- [ ] **Page faults**, page replacement algorithms — FIFO, LRU, Optimal
- [ ] Thrashing, Belady's anomaly
- [ ] Internal vs external fragmentation
- [ ] TLB (Translation Lookaside Buffer)

**Other**
- [ ] File systems, inodes, directory structure
- [ ] I/O management, interrupts, DMA
- [ ] System calls, kernel vs user mode

</details>

<details>
<summary><b>❓ OS questions you WILL be asked</b></summary>

<br>

1. **Process vs thread?** *(Almost guaranteed. Cover memory space, creation cost, communication, crash isolation.)*
2. What is a deadlock? What are the four conditions? How do you prevent one?
3. Mutex vs semaphore — when do you use each?
4. What is virtual memory and why do we need it?
5. Explain paging vs segmentation.
6. What is thrashing and how do you fix it?
7. What is a context switch and why is it expensive?
8. Explain LRU page replacement. Implement it. *(This is also a LeetCode problem — LRU Cache. Know both.)*
9. What is a race condition? Give an example and fix it.
10. Concurrency vs parallelism?
11. What happens when you run a program? *(Compilation → loading → process creation → execution)*
12. What is a zombie process? An orphan process?

</details>

---

## 🗄️ DBMS & SQL

<details open>
<summary><b>Topics to cover</b></summary>

<br>

**Design** ⭐
- [ ] ER diagrams, entities, relationships, cardinality
- [ ] Keys — primary, foreign, candidate, super, composite, unique
- [ ] **Normalisation** ⭐ — 1NF, 2NF, 3NF, BCNF; functional dependencies
- [ ] **Denormalisation** — when and why you'd deliberately break normal form
- [ ] Schema design for a real scenario *(commonly asked as a live exercise)*

**Transactions** ⭐
- [ ] **ACID properties** ⭐ — with a concrete example for each
- [ ] Transaction states
- [ ] **Concurrency control** — locks, two-phase locking, timestamp ordering
- [ ] **Isolation levels** — read uncommitted, read committed, repeatable read, serializable
- [ ] Anomalies — dirty read, non-repeatable read, phantom read
- [ ] Deadlock in databases

**Performance** ⭐
- [ ] **Indexing** ⭐ — B-trees, clustered vs non-clustered, when indexes hurt
- [ ] Query optimisation, `EXPLAIN` plans
- [ ] The **N+1 query problem**
- [ ] Sharding, partitioning, replication

**SQL** ⭐⭐ *(most practically tested)*
- [ ] `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] **Joins** — inner, left, right, full, self, cross
- [ ] `GROUP BY`, `HAVING`, aggregate functions
- [ ] Subqueries, correlated subqueries
- [ ] **CTEs** (`WITH` clause)
- [ ] **Window functions** ⭐ — `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `PARTITION BY`
- [ ] `UNION` vs `UNION ALL`
- [ ] `CASE WHEN`
- [ ] DDL vs DML vs DCL vs TCL

**NoSQL**
- [ ] Document, key-value, column-family, graph databases
- [ ] SQL vs NoSQL — when to choose which
- [ ] **CAP theorem** ⭐
- [ ] Eventual consistency
- [ ] MongoDB basics, aggregation pipeline

</details>

<details>
<summary><b>❓ DBMS questions you WILL be asked</b></summary>

<br>

**Theory**
1. Explain normalisation up to 3NF with an example. When would you denormalise?
2. Explain ACID with a bank-transfer example.
3. What is an index? Why does adding one slow down `INSERT`?
4. Clustered vs non-clustered index?
5. `DELETE` vs `TRUNCATE` vs `DROP`?
6. What is a dirty read? Which isolation level prevents it?
7. SQL vs NoSQL — when would you pick each?
8. Explain the CAP theorem.
9. What is a foreign key and what does `ON DELETE CASCADE` do?
10. `WHERE` vs `HAVING`?

**Live SQL (practise writing these)**
11. Find the **2nd highest salary** *(the classic — know 3 ways: `LIMIT/OFFSET`, subquery, `DENSE_RANK`)*
12. Find the highest-paid employee **per department**
13. Find duplicate rows in a table
14. Find employees who earn more than their manager
15. Calculate a **running total** / cumulative sum
16. Find users active for 3 consecutive days
17. Find departments with more than 5 employees
18. Delete duplicates keeping one row

**Practise:** [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) — do all 50. [DataLemur](https://datalemur.com/) for harder ones.

</details>

---

## 🌐 Computer Networks

<details open>
<summary><b>Topics to cover</b></summary>

<br>

**Models & layers** ⭐
- [ ] **OSI model** — 7 layers, what each does
- [ ] **TCP/IP model** — 4/5 layers, and how it maps to OSI
- [ ] Encapsulation, headers

**Transport** ⭐
- [ ] **TCP vs UDP** ⭐ — reliability, ordering, speed, use cases
- [ ] **TCP 3-way handshake** ⭐ (SYN, SYN-ACK, ACK) and 4-way termination
- [ ] Flow control, congestion control, sliding window
- [ ] Ports, sockets

**Application** ⭐
- [ ] **HTTP vs HTTPS** ⭐, HTTP methods, **status codes** ⭐
- [ ] HTTP/1.1 vs HTTP/2 vs HTTP/3
- [ ] **DNS** ⭐ — resolution process, record types (A, AAAA, CNAME, MX), caching
- [ ] **TLS/SSL handshake**, certificates, symmetric vs asymmetric encryption
- [ ] Cookies, sessions, CORS
- [ ] WebSockets vs HTTP polling
- [ ] REST vs GraphQL vs gRPC
- [ ] FTP, SMTP, SSH, DHCP

**Network layer**
- [ ] IP addressing — IPv4, IPv6, subnetting, CIDR
- [ ] Public vs private IP, **NAT**
- [ ] Routing, ARP
- [ ] Switches vs routers vs hubs
- [ ] Firewalls, VPN
- [ ] Load balancing, CDN

</details>

<details>
<summary><b>❓ CN questions you WILL be asked</b></summary>

<br>

1. **What happens when you type google.com and press enter?** ⭐⭐
   *(The single most-asked systems question in tech interviews. Full chain: browser cache → OS cache → DNS resolution → TCP handshake → TLS handshake → HTTP request → server processing → response → rendering. Practise saying this in 3 minutes.)*
2. **TCP vs UDP** — differences and when to use each? *(Video streaming and gaming use UDP; file transfer and web use TCP)*
3. Explain the TCP 3-way handshake. Why three and not two?
4. HTTP vs HTTPS — what does TLS actually add?
5. Explain the OSI model layer by layer.
6. What are HTTP status codes 200, 301, 400, 401, 403, 404, 500, 502, 503?
7. How does DNS resolution work?
8. What is CORS and why does the browser enforce it?
9. GET vs POST? Which is idempotent?
10. What is a load balancer and what algorithms can it use?
11. Symmetric vs asymmetric encryption?
12. What is NAT and why do we need it?
13. WebSockets vs HTTP — when do you need WebSockets?

</details>

---

## 🧱 OOP & Design Principles

<details open>
<summary><b>Topics to cover</b></summary>

<br>

**The four pillars** ⭐
- [ ] **Encapsulation** — data hiding, access modifiers
- [ ] **Abstraction** — interfaces, abstract classes
- [ ] **Inheritance** — types, the diamond problem
- [ ] **Polymorphism** ⭐ — compile-time (overloading) vs runtime (overriding)

**Core concepts**
- [ ] Classes vs objects, constructors, destructors
- [ ] `static` — variables, methods, blocks
- [ ] `this` / `super`
- [ ] **Abstract class vs interface** ⭐ *(guaranteed question)*
- [ ] Method overloading vs overriding ⭐
- [ ] Composition vs inheritance *(and why "favour composition")*
- [ ] Access modifiers
- [ ] `final` / `const` / sealed
- [ ] Shallow vs deep copy
- [ ] Exception handling hierarchy
- [ ] Garbage collection, memory model (heap vs stack)

**SOLID principles** ⭐
- [ ] **S** — Single Responsibility
- [ ] **O** — Open/Closed
- [ ] **L** — Liskov Substitution
- [ ] **I** — Interface Segregation
- [ ] **D** — Dependency Inversion

**Design patterns** *(know these five well; recognise the rest)*
- [ ] **Singleton** ⭐ — and how to make it thread-safe
- [ ] **Factory / Abstract Factory** ⭐
- [ ] **Builder** ⭐
- [ ] **Observer** ⭐
- [ ] **Strategy** ⭐
- [ ] Adapter, Decorator, Facade, Proxy, Command

</details>

<details>
<summary><b>❓ OOP questions you WILL be asked</b></summary>

<br>

1. **Abstract class vs interface** — when do you use each? ⭐
2. Explain the four pillars with real examples from your own project.
3. Overloading vs overriding?
4. Can you override a static method? *(No — explain why)*
5. What is the diamond problem and how does your language solve it?
6. Explain SOLID with an example of violating and then fixing one principle.
7. Why is "favour composition over inheritance" good advice?
8. Implement a thread-safe Singleton.
9. What is dependency injection and why does it help testing?
10. Design a parking lot / BookMyShow / Splitwise system. *(Low-level design — see [tracks/backend.md](../tracks/backend.md))*

**The best answers use examples from your own projects**, not textbook Animal/Dog/Cat examples. Prepare one real example per pillar from code you actually wrote.

</details>

---

## 📅 A 12-week study plan (45 min/day)

<div align="center">

| Weeks | Subject | Output |
|:---:|---|---|
| **1–3** | **DBMS + SQL** *(start here — most practically useful)* | 50 SQL queries written by hand |
| **4–6** | **Operating Systems** | Notes + all questions above answered out loud |
| **7–9** | **Computer Networks** | Can explain "what happens when you type a URL" fluently |
| **10–12** | **OOP + SOLID + design patterns** | Refactored one of your projects using SOLID |

</div>

**Every subject, same method:**
1. Watch/read the topic (30 min)
2. **Write your own one-page summary** — don't copy, compress
3. Answer the interview questions **out loud, without notes**
4. Revise all four subjects for 15 min every Sunday

> [!IMPORTANT]
> **Speaking the answers out loud is the entire point.** You can recognise every one of these concepts and still freeze in an interview because you've never formed the sentences. Record yourself once — it's uncomfortable and extremely effective.

---

## 📚 Free resources

<div align="center">

| Subject | Resource |
|---|---|
| **OS** | [Gate Smashers (YouTube)](https://www.youtube.com/@GateSmashers) ⭐ *(best free Indian CS explanations)* · [Neso Academy](https://www.youtube.com/@nesoacademy) |
| **OS (deep)** | [OSTEP — free textbook](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| **DBMS** | [Gate Smashers DBMS](https://www.youtube.com/@GateSmashers) · [CMU Database Course](https://www.youtube.com/@CMUDatabaseGroup) |
| **SQL practice** ⭐ | [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) · [SQLZoo](https://sqlzoo.net/) · [DataLemur](https://datalemur.com/) |
| **Networks** | [Gate Smashers CN](https://www.youtube.com/@GateSmashers) · [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/) |
| **Networks (practical)** | [High Performance Browser Networking (free)](https://hpbn.co/) |
| **OOP** | [Refactoring Guru](https://refactoring.guru/) ⭐ *(design patterns explained brilliantly, free)* |
| **SOLID** | [SOLID principles — Refactoring Guru](https://refactoring.guru/design-patterns) |
| **All-in-one revision** | [InterviewBit CS core subjects](https://www.interviewbit.com/technical-interview-questions/) · [GeeksforGeeks](https://www.geeksforgeeks.org/) |
| **Last-minute revision** | Search "OS/DBMS/CN interview questions GeeksforGeeks" — good for the night before |

</div>

---

## ⚠️ Mistakes

| Mistake | Fix |
|---|---|
| **Studying for exams instead of interviews** | Same topics, different framing. Focus on "when would you use X". |
| **Memorising definitions** | Interviewers ask follow-ups. Understand the *why*. |
| **Skipping SQL practice** | SQL is written live in interviews. Theory alone fails. Write 50 queries. |
| **Ignoring CN** | It's the most-skipped subject and it's asked constantly. |
| **Not connecting theory to your projects** | "I used indexing in my project because queries were slow" is a far stronger answer than a definition. |
| **Cramming all four in the last month** | Spread it across year 3 alongside your semester subjects. |
| **Never practising out loud** | Recognition ≠ articulation. Speak the answers. |

---

<div align="center">

### Your syllabus already contains this. Just study it the way interviews ask it.

[🏠 Home](../README.md) • [📚 Core](../core/) • [🧮 DSA](dsa.md) • [🏗️ System Design](system-design.md) • [🎤 Interview Playbook](../placements/interview-playbook.md)

</div>
