# Writing an ERC Starting / Consolidator Grant

A working reference for the **ERC-2027-StG and ERC-2027-CoG calls**, distilled from the
Weizmann ERC preparatory seminar, the *Information for Applicants* (v11.0) and the *Work
Programme 2027*. Organised so you can read it once for the argument and then work
[§13](#13-review-protocol) against a live draft.

[§13](#13-review-protocol) is a rubric, not a checklist: it runs top-down, from *is this an ERC project* to
*is this word doing work*, and stops at the highest level that is failing. Two tools in
this repository execute it — [`SKILL.md`](../SKILL.md), a Claude Code skill that drives the
judgment stages, and
[`tools/erc_check.py`](../tools/erc_check.py), which settles everything a regex can settle so
that neither a human nor an agent spends attention there. Neither is required: the guide
stands alone if you would rather work the ladder by hand.

## Contents

Sections are cited by number throughout the review protocol, the checker's output and the
`ercreview.sty` margin macros, so the numbers are stable: `\ercscore{9.2}{…}` always means
§9.2 of this file.

| § | | Covers |
|---|---|---|
| | [Provenance and permissions](#provenance-and-permissions) | sources, what is excluded and why |
| 1 | [What an ERC project is — and is not](#1-what-an-erc-project-is--and-is-not) | the six ingredients, the six shapes that get rejected |
| 2 | [Call mechanics](#2-call-mechanics) | eligibility windows, amounts, dates, and every component with its page or character limit |
| 3 | [Who reads what, and when](#3-who-reads-what-and-when) | Step 1 vs Step 2 readers; why B1 must stand alone |
| 4 | [The evaluation questions](#4-the-evaluation-questions) | the scored questions verbatim · [what each is asking](#what-each-question-is-actually-asking) · [the PI criteria](#the-pi-criteria-and-where-stg-and-cog-diverge) |
| 5 | [The four layers](#5-the-four-layers) | challenge/vision/aim · objectives · work units · tasks |
| 6 | [Part B1 — cover page and abstract](#6-part-b1--cover-page-and-abstract) | acronym, the 2,000-character abstract and its administrative job |
| 7 | [Part I of the Scientific Proposal](#7-part-i-of-the-scientific-proposal-5-pages-in-b1) | [7.1 rationale](#71-introduction--project-rationale--page) · [7.2 limitations vs barriers](#72-limitations-versus-barriers-a-rule-for-71-not-a-section-of-its-own) · [7.3 falsifiable challenge](#73-state-the-challenge-in-falsifiable-terms-24-sentences-inside-71) · [7.4 vision vs aim](#74-vision-versus-overarching-aim--page) · [7.5 objectives](#75-objectives--page) · [7.6 state of the art](#76-state-of-the-art-1-page) · [7.7 strategy](#77-research-strategy-12-pages) · [7.8 why now, why me](#78-why-now-why-me--page) · [7.9 impact](#79-impact--page) |
| 8 | [Part B1 — CV and track record](#8-part-b1--cv-and-track-record-4-pages) | the four-page template and how to divide it, the ten outputs, what each entry must carry |
| 9 | [Part II of the Scientific Proposal](#9-part-ii-of-the-scientific-proposal-7-pages--b2) | how the seven pages divide · [9.1 project design](#91-project-design--page-figure-included) · [9.2 WP objective vs rationale](#92-work-packages-objective-versus-rationale-4-pages-for-the-whole-work-plan) · [9.3 tasks](#93-tasks--page-each-inside-the-work-plan-budget) · [9.4 moonshots](#94-moonshot-tasks--page-150200-words) · [9.5 risk](#95-risk-assessment--page-with-the-gantt-chart-alongside) |
| 10 | [Sentence-level rules](#10-sentence-level-rules-for-the-implementation-sections) | named causality, active voice where a human acts |
| 11 | [Budget, resources and panel choice](#11-budget-resources-and-panel-choice) | [11.1 the budget table's five cost categories](#111-the-budget-table) · [11.2 the 8,000-character Resources box](#112-the-resources-text-box) · [11.3 additional funding](#113-additional-funding) · [11.4 panel, keywords, excluded reviewers](#114-panel-keywords-and-who-will-not-review-you) |
| 12 | [What this was checked against](#12-what-this-was-checked-against) | versions, dates, and the four things older advice gets wrong |
| 13 | [Review protocol](#13-review-protocol) | [13.1 the stage ladder](#131-the-stage-ladder) · [13.2 stage rubrics](#132-stage-rubrics) · [13.3 what the checker settles](#133-what-the-checker-settles--stages-8-and-9) · [13.4 scoping a review](#134-scoping-a-review) · [13.5 leaving a finding in the draft](#135-leaving-a-finding-in-the-draft) |

Reading [§13](#13-review-protocol) alone is enough to run a review; it cites the sections above by number when a
finding needs the underlying rule.

## Provenance and permissions

- **Primary source:** "Call Analysis & Proposal Best Practices", ERC-2026-StG/CoG,
  Weizmann Institute of Science, 21 July 2025 — Stewe Bekk (bekkresearchsupport.com)
  and Malte Beringer (sciencepoint.eu). © 2025 by the authors. The deck itself is not
  redistributed here.
- **Secondary source:** the seminar recordings — the 2026-call session above and the same
  presenters' session for the **ERC-2027-StG/CoG** calls, held before the 2027 StG call
  opened — plus follow-up notes on work-package and task-level structure. The 2027 session is
  where the practitioner figures in [§2](#2-call-mechanics) and [§3](#3-who-reads-what-and-when)
  (declared time commitment, readers per proposal) come from, and its recordings and notes are
  not redistributable either. Where a session and the *Information for Applicants* disagree,
  the document wins and the disagreement is flagged in place — see the budget note in
  [§11.1](#111-the-budget-table).
- **Tertiary source:** the official ERC instruction blocks carried in the community B1/B2
  LaTeX template, which reproduce the text of the official forms.
- **Deliberately excluded:** the deck's worked examples drawn from active ERC projects
  (objectives, vision, preliminary data, impact, CV pages). Those carry an explicit
  "do not distribute beyond the seminar" restriction. What follows extracts the
  *rules*; where an illustration helps, the illustration is written fresh.
- **Checked against the primary sources.** Every limit, date and evaluation question here
  was verified on 11 August 2026 against the *Information for Applicants to the Starting
  and Consolidator Grant 2027 Calls* (v11.0, 22 July 2026) and the *ERC Work Programme
  2027* (20 July 2026) — see [§12](#12-what-this-was-checked-against), which also lists
  what changed recently enough that older advice is wrong. Those two documents, for **your**
  call, are the authority; this file is a reading of them.

---

## 1. What an ERC project is — and is not

Six things the panel is looking for:

| Ingredient | What it means |
|---|---|
| Important scientific question | Not a topic. A question whose answer the field is waiting for. |
| Unique, visionary approach | Yours, not the field's default next step. |
| Step-change | There is a recognisable *before* and *after* the project. |
| Viability | Ambitious, but not a "crazy idea" — the approach has to be executable. |
| Knowledge-driven | You are seeking understanding, not delivering a product. |
| Scientific impact | Impact on knowledge, not on markets. |

Six shapes that get rejected:

- **Incremental research** — reads as the natural continuation of your last project.
- **Unclear scientific motivation** — the reader cannot name the trigger for the project.
- **Observational research** — data collection and description without a driving question.
- **Pure technology development** — building a tool rather than answering a question with one.
- **A collaborative project** — ERC single-PI grants fund *your* programme; consortium-shaped work reads as the wrong call.
- **Not aligned with the PI profile** — the proposal could have been written by someone else, and better.

The first and last are the ones that quietly sink otherwise strong applications: a
continuation of your own prior work fails "step-change", and a leap into a field where
you have no record fails "PI fit". You have to be the obvious person to do something
that is not the obvious next thing.

## 2. Call mechanics

Figures below are Work Programme 2027 (calls ERC-2027-StG and ERC-2027-CoG). **The
eligibility windows widened in WP 2027** — if you are working from advice written for
WP 2026 or earlier, that is the first number to re-check.

|  | Starting Grant | Consolidator Grant |
|---|---|---|
| Eligibility: PhD defence date | > 0 and ≤ 10 years before 1 Jan 2027 → 1 Jan 2017 – 31 Dec 2026 | > 5 and ≤ 15 years before 1 Jan 2027 → 1 Jan 2012 – 31 Dec 2021 |
| Maximum grant | € 1.5 M | € 2.0 M |
| Additional funding | up to € 1 M, or € 2 M if based outside the EU/AC at the call deadline — must be justified in the proposal | same |
| Minimum time commitment | ≥ 50 % | ≥ 40 % |
| Working time in a Member State or Associated Country | ≥ 50 % | ≥ 50 % |
| Project length | up to 5 years (60 months) | up to 5 years (60 months) |
| Once per career | one StG, ever | one CoG, ever |

The reference date is the **defence** of your first PhD, not the award. Extensions
(maternity 18 months per child, paternity, long-term illness, national service) need
documentary evidence and are the reason to talk to your grants office early rather than
late.

Deadlines shift each work programme: **ERC-2027-StG opened 22 July 2026 and closes
14 October 2026; ERC-2027-CoG opens 24 September 2026 and closes 12 January 2027.**

The **minimum** time commitments above are floors, not targets. Practitioners who see many
funded applications report that competitive proposals typically declare **80–90 % for a
Starting Grant and 60–70 % for a Consolidator**, and that a figure at or just above the
floor reads as a PI who is not really going to run the project. The number is also
load-bearing arithmetic rather than a gesture: it caps the PI's own personnel cost in the
budget table ([§11.1](#111-the-budget-table)) and it is printed next to the figures for the
Step-2 reviewers ([§3](#3-who-reads-what-and-when)).

**Submission restrictions — check these before you write anything.** Separate from
eligibility, and the part of the rules most likely to have moved since the last time you
or your mentor applied. For WP 2027:

- One proposal to an ERC main grant call **under evaluation** at any time, and only **one
  eligible proposal** to any call published under WP 2027. Apply to two and only the first
  eligible one is evaluated.
- You may **hold** only one ERC main grant at a time, and a new project may only start
  once the previous one has ended. If you currently hold a main frontier grant you may not
  apply **unless that project ends less than two years after the call deadline** — the
  rule that decides, years in advance, which call a current grantee can aim at.
- Selected for funding and preparing a grant agreement under WP 2025 or WP 2026 → you may
  not apply under WP 2027.
- Held a StG → no StG. Held a CoG → no CoG. Serving on an ERC panel for WP 2027, or having
  served for WP 2025 → no application for that same grant type (panels alternate years so
  that members can apply in the off years).
- **Outcome-based bars, which are the ones people are surprised by.** A **B or C at Step 1**
  in the 2026 StG/CoG call bars you from every 2027 call — StG, CoG, AdG, Plus and Synergy.
  A **C at Step 1** in 2025 also bars you from 2027. So a C costs two calls and a B costs
  one, and "we will just resubmit next year" is not available after either. A or B at Step 2,
  and A-not-invited at Step 1, carry **no restriction**. A rejection on the grounds of a
  breach of research integrity bars everything.
- Inadmissible, ineligible and withdrawn proposals do not count against any of these.

Two consequences worth internalising. First, **the penalties have been tightening across
work programmes**, so read the outcome table in the *Information for Applicants* for your
own call rather than carrying forward what applied to a colleague two years ago
([§12](#12-what-this-was-checked-against)). Second, because a weak submission can cost a
year or two of eligibility rather than a few months, submitting a not-quite-ready proposal
"for the feedback" is a much more expensive move than it used to be — which is part of why
the timeliness argument ([§7.8](#78-why-now-why-me--page)) has to justify *this* call and
not merely this decade.

**What you submit.** The call names four components, and the two names for each one —
what the ERC calls it, and which form it lives in — are worth keeping straight, because
the evaluation is split along these lines and not along the file boundaries:

| Component | Lives in | Limit |
|---|---|---|
| Cover page (title, acronym, PI, host, duration, abstract) | Part B1, before Part I | ½ page abstract; the cover page itself is outside the 5-page limit |
| **Part I of the Scientific Proposal** | Part B1, after the cover page | 5 pages |
| **Curriculum Vitae and Track Record** | Part B1, one single template | 4 pages |
| **Part II of the Scientific Proposal** | Part B2 | 7 pages |
| Funding ID (current grants and pending applications) | Part B2, after Part II | outside the page limit |
| Abstract | Part A, *General Information* — the cover page copies it verbatim | 2,000 characters incl. spaces |
| **Budget table** | Part A, *Budget* — five cost categories ([§11.1](#111-the-budget-table)) | whole euros; capped at the grant maximum plus any additional funding |
| **Resources** description | Part A, *Budget*, text box under the table ([§11.2](#112-the-resources-text-box)) | 8,000 characters incl. spaces ≈ 1–2 pages |
| **Time commitment** | Part A, *Other questions* | a percentage, ≥ the minimum in the eligibility table above |

Only Part I, the CV and Part II are page-limited; everything else in the table is capped in
characters, which is the harder constraint to plan for because no editor shows it to you.

B1 (cover page + Part I + CV/Track Record, so up to 10 pages) uploads as **one single
PDF**, never split. B2 carries Part II plus the Funding ID table of current and submitted
grants. References and Funding ID sit outside every page limit; nothing else does, and the
limits are applied strictly — reviewers are instructed not to read past them. Supporting
documents: host institution support letter, PhD certificate, ethics/security
documentation, eligibility extension evidence.

## 3. Who reads what, and when

This is the single most consequential fact about the format.

**Step 1 — remote evaluation, then panel meeting.** Panel members read Part I and the
CV/Track Record and *have no access to the other parts*. They are generalist scientists,
serve for up to four rounds, and handle 10–15 proposals each; the panel may commission
extra reviews from remote Step-1 experts, who may be members of other panels. Up to 44
proposals per panel are retained for Step 2. Scores are A-invited, A-not-invited, B or C;
only A-invited proceeds, and the rest are rejected with an evaluation report.

In practice each B1 is assigned to about **three** panel members as named readers, and at
Step 2 roughly **four to eight** Remote Reviewers are recruited per proposal — they may be
non-European, they review a single proposal, and they never attend the meeting, so their
contribution is written and unrebutted. The ERC does not publish either figure, so treat
them as the shape of the audience rather than as a rule: a handful of generalists decide
Step 1, and the technical depth of B2 is aimed at a genuinely small number of experts.

Panel allocation is yours to propose, not yours to control: a proposal may be **reallocated
to a different panel** where the required expertise sits elsewhere, with the agreement of
both panel chairs, and you are told at the latest with the evaluation result
([§11.4](#114-panel-keywords-and-who-will-not-review-you)).

**Step 2 — remote evaluation, then panel meeting with interview.** Panel members plus
**Remote Reviewers** — topic experts who review a single proposal, deliver written
reviews and do not attend the meeting. They read Part I, Part II, the CV and the Part A
budget and resources. The interview is about 30 minutes, PI remote and panel in the room:
a presentation on the project outline, then questions — and the ERC warns explicitly that
the questions may cover the detailed budget table. Parts I and II are read *together* at
this step, so Part II must not repeat Part I.

Two consequences:

1. **B1 must be self-sufficient.** Everything the Step-1 criteria touch has to be *in
   B1*, because nothing else reaches that reader. A brilliant B2 cannot rescue a B1 that
   fails to make the question sound important.
2. **B1 is written for a smart non-specialist; B2 is written for your subfield.** The
   same sentence cannot serve both. B1 spends its budget on why the question matters and
   why the approach could work at all. B2 spends its budget on how, in technical detail,
   and on convincing an expert the plan survives contact with reality.

## 4. The evaluation questions

Scientific excellence is assessed at two levels — **the research project**
(ground-breaking nature, ambition) and **the principal investigator** (intellectual
capacity, creativity).

The wording below is Work Programme 2027, §1.6.5. **At Step 1 the project has exactly two
questions.** Feasibility is not one of them — it was removed from Step 1 as of WP 2026 —
so at Step 1 an approach has to read as *scientifically convincing*, which is a different
and lower bar than *feasible*, and the place to prove feasibility is Part II.

**Step 1 and 2 — project (the ground-breaking nature and ambition of the Research Project):**

- To what extent does the research address important scientific questions?
- To what extent are the project's objectives ambitious, will the project advance the frontier of knowledge and is the proposed approach scientifically convincing?

**Step 2 only — implementation:**

- To what extent are the research methodology and working arrangements appropriate to achieve the goals of the project?
- To what extent are the timescales and resources adequate and properly justified?

**Steps 1 and 2 — PI (intellectual capacity and creativity):**

- To what extent has the PI demonstrated the ability to conduct ground-breaking research?
- To what extent does the PI provide evidence of creative and original thinking?
- To what extent does the PI have the required scientific expertise and capacity to successfully execute the project?

### What each question is actually asking

**"Important scientific questions"** decomposes into four things you must supply: the
overall topic, its motivation and relevance, the *scientific unknown*, and the
limitations and barriers that keep it unknown.

**"Ambitious objectives / frontier of knowledge"** decomposes into ambition and
originality, breadth and interdisciplinarity, and the verbs of knowledge production —
*uncover, identify, assess, test whether*. Objectives phrased as deliverables ("build
X", "release Y") score badly here; objectives phrased as knowledge claims score well.
The third clause, **"scientifically convincing"**, is the only purchase Step 1 has on
method, and it is satisfied by an approach whose *logic* a generalist can follow — why
this route reaches this objective — not by protocols, sample sizes or contingency plans.

**"Methodology and working arrangements"** means implementation and feasibility: which
methods, technologies and models, and *why those*; inter- and multidisciplinarity; and
your ability to draw conclusions from what the methods will produce.

**"Timescales and resources"** means a plausible, coherent work plan with resources
matched to the activities — and, in the current wording, *properly justified*.

### The PI criteria, and where StG and CoG diverge

Both calls look at the same four blocks, with different weight:

- **Ground-breaking research** — quality of achievements (citations, venues), the PI
  positioned as a reference point in the field, a track record of exceptional results.
  *Emphasised for StG.*
- **Ability and leadership** — stepping stones towards independence, main and senior
  authorships, evidence of research independence, experience managing teams.
  *Emphasised for CoG.*
- **Peer recognition and trust** — international funding, awards, grants and
  collaborations, commissions of trust (peer review, editorial boards); international
  visibility through invited talks and conference organisation.
- **Creativity and originality** — evidence of original research, new concepts and
  methodologies, new research directions you opened in the past.

"Legacy" has been dropped from the official questions but still belongs under other
contributions to the research community.

## 5. The four layers

The organising device for the whole application. Every element of both parts sits at one
of four levels of abstraction, and confusing two adjacent levels is the most common
structural failure.

```
Layer 1   Challenge · Vision · Aim · Impact        the why, and the after
Layer 2   Specific objectives                      3–5 knowledge claims
Layer 3   Work units / work packages               how the objectives are attacked
Layer 4   Tasks                                    what you actually do
```

B1 lives mostly in layers 1 and 2 and gestures at 3. B2 lives mostly in layers 3 and 4
and re-states 1 and 2 compactly. If a B1 paragraph is describing a task, it is in the
wrong document; if a B2 work package never connects to an objective, the mapping is broken.

## 6. Part B1 — cover page and abstract

The cover page carries the title, acronym, PI, host institution and duration, and — if you
are asking for more than one review panel — the additional panel and the reason it is needed
([§11.4](#114-panel-keywords-and-who-will-not-review-you)). It sits outside Part I's five pages. Two things deserve real effort:

**The acronym.** It is the handle the panel uses for your project through two steps of
evaluation. Pick something pronounceable that encodes the idea.

**The abstract** — half a page on the cover page, a verbatim copy-paste of the Part A
summary (2,000 characters including spaces in the submission form), plain text, no
formulae. It has an administrative job beyond first impressions: it is what the ERC shows
to prospective reviewers when allocating your proposal, so it partly determines *who
reviews you*, and it is published if you are funded. Cover five elements in order:
context, challenge, vision, objectives, impact. No confidential information. If the
proposal is not in English, an English translation of the abstract is mandatory.

## 7. Part I of the Scientific Proposal (5 pages, in B1)

The call states the job in three parts: (1) lay out the current state of knowledge,
(2) explain the scientific question and the objectives of the project, (3) present the
overall approach or research strategy. It must convince the panel that the proposal
presents "an original and creative idea addressing an important question", and say what
the project will *change, open or challenge* in the field.

**The template provides no section headings.** That is a trap and an opportunity: you
choose the structure, and a reader who cannot find the answer to an evaluation question
concludes it is absent. Use the criteria as your headings, or as visible threads.

Recommended sections and page budget. **Only the five pages are a limit; every allocation
below is a recommendation.** The call does not divide the five pages, so this split is
editorial: the *Covered in* column is where each band's rules live, and the bracket on each
of those subsection headings recommends its share of the band, so the nine brackets sum to
five pages. Treat a bracket as an opening bid — what matters is that a section running to
twice its recommendation has taken the pages from somewhere, and that you can say from
where.

| Band | Recommended pages | Covered in |
|---|---|---|
| Introduction / project rationale + vision | 1 – 1.5 | [§7.1](#71-introduction--project-rationale--page), [§7.2](#72-limitations-versus-barriers-a-rule-for-71-not-a-section-of-its-own), [§7.3](#73-state-the-challenge-in-falsifiable-terms-24-sentences-inside-71), [§7.4](#74-vision-versus-overarching-aim--page) |
| Objectives + state of the art | 1.5 – 2 | [§7.5](#75-objectives--page), [§7.6](#76-state-of-the-art-1-page) |
| Research approach / strategy | 1.5 – 2 | [§7.7](#77-research-strategy-12-pages) |
| Why now, why me + impact | 0.5 – 1 | [§7.8](#78-why-now-why-me--page), [§7.9](#79-impact--page) |

Two things about this table. It is **tighter on the state of the art than the source
advice is**: practitioners commonly suggest 1½–2 pages for the state of the art and the same
again for the approach, which only fits inside five pages at the very bottom of both ranges
once the introduction, objectives, timeliness and impact have been paid for. The brackets
above are one way of making the arithmetic close; if you want a longer state of the art, the
pages have to come from a named other band and not from the margin. The invariant that
survives either split is the ordering: **the research approach should be at least as long as
the state of the art**, because the balance between the two is itself an argument about
whether the proposal is more interested in what has been done or in what you will do.

References do not count against the limit; the cover page does not either. Formatting is
mandatory and checked: A4, Times New Roman / Arial or similar, **font size ≥ 11**, single
line spacing, side margins 2 cm and bottom margin 1.5 cm. Every page must carry a header
with the PI's last name, the acronym, and which part it belongs to. Compliance here is not
cosmetic: reviewers are instructed to read only what fits inside the limits *provided the
font instructions are respected*, so shrinking the type to fit is a way of having the
squeezed-in material discarded rather than read.

### 7.1 Introduction / project rationale (½–¾ page)

Four moves: set the stage, state the core inquiry (the major research question, key
challenge, or knowledge gap), give the current limitations of the field, and establish
significance.

The failure mode is turning this into a literature review. The introduction exists to
make the reader feel the gap, not to demonstrate that you have read everything.

### 7.2 Limitations versus barriers (a rule for §7.1, not a section of its own)

A distinction worth internalising, because proposals routinely supply one and omit the
other.

- **Limitations — what is not known.** Fundamental gaps in theory or understanding,
  open research questions, unexplained observations or phenomena.
- **Barriers — why it is not known.** Methodological gaps (no validated approach or
  protocol), technical obstacles (equipment, tools, resources, computational limits).

Limitations alone read as "nobody got around to it", which invites the reviewer to
wonder why your project is needed now. Barriers are what make the gap *hard*, and
therefore what make solving it ground-breaking rather than overdue.

### 7.3 State the challenge in falsifiable terms (2–4 sentences, inside §7.1)

The single highest-yield sentence-level fix in the deck. Vague challenge statements are
unscoreable; specific ones carry their own significance.

| Weak | Improved |
|---|---|
| "Despite decades of investigation, we do not fully understand process XYZ." | "We do not know how process XYZ is initiated, maintained and resolved." |
| "The regulation of Y is poorly understood." | "Y's stress-induced regulation is unclear, in part because expression studies lack temporal resolution." |
| "Current tools have limitations in analysing complex data." | "Existing assembly algorithms cannot resolve repetitive regions above 1 kb from short-read data, because …" |

The pattern: replace *"X is poorly understood"* with **what specifically is not known**,
plus **the reason it is not known**. "Poorly understood", "not fully understood",
"remains unclear" and "has received limited attention" are all signals that the sentence
has not been written yet.

### 7.4 Vision versus overarching aim (¼ page)

Also routinely collapsed into one thing, and the collapse costs you either ambition or
credibility.

|  | Vision | Aim |
|---|---|---|
| Time horizon | Long-term, beyond the project | The project duration, 3–5 years |
| Focus | Broader relevance, paradigm shift | The concrete goal of *this* project |
| Language | Inspirational, strategic | Precise, research-focused |
| Function | Sets ambition and context | Defines scope and intent |

The vision answers *what could this research lead to* and *how will it transform the
current state of the art*. The aim answers *what will exist at month 60*. It must be
clear, specific, plausible within the project, and aligned with the vision it descends
from. Write the vision, then write the aim, then check the aim is a genuine down-payment
on the vision rather than a restatement of it.

The vision section should also carry: your idea for addressing the challenge, the core
novelty and targeted breakthrough, the overarching aim and the innovative approach, and
how the work paves the way for future inquiry.

### 7.5 Objectives (½–¾ page)

- **3–5 interlinked objectives.** Fewer reads as thin; more reads as a work programme
  rather than a project.
- **Coherent with the vision** — each one visibly serves it.
- **Tangible and verifiable** — a reader can say whether you achieved it.
- **"What" over "how".** Objectives are knowledge claims, not methods. The methods
  belong in the research approach and in B2.
- **Purpose-driven** — each objective exists because the previous one leaves something
  open, and the set covers the aim.
- **Interlinked, not independent.** Five unrelated objectives read as five small
  projects. Say what depends on what.

Use knowledge verbs: *develop the theory required to describe…*, *explore the limits
of…*, *determine whether…*, *demonstrate the ability of…*, *characterise…*. Avoid
*implement*, *build*, *release*, *apply*.

**"To understand" and "to study" are the two verbs to strike.** They are not wrong, they
are open-ended — nothing about them can be checked at month 60, which is exactly the
property an objective must not have. *To quantify*, *to identify*, *to reveal the mechanism
by which*, *to determine whether* all name a state of knowledge that either exists at the
end or does not. Watch also for the substitution of the **output for the objective**: "a
public database of X" is a deliverable, and the objective it serves is whatever the
database lets anyone conclude.

**Format each objective as a bold standalone claim, then two or three sentences.** The bold
sentence is what a panel member will read on the second pass and quote in the panel meeting,
so it has to survive being extracted; the sentences that follow give the approach in
outline and the connection to the neighbouring objectives. Cross-referencing them explicitly
— "yielding the atomic-scale models relevant to the states addressed in O1 and O3" — is
what stops a numbered list from reading as separable projects.

**Order them so the risk rises.** If one objective is markedly more speculative than the
rest, put it last and let the earlier ones stand on their own. A high-risk objective placed
first forces the reader to ask what remains of the project if it fails, and every later page
is read under that doubt; the same objective placed last reads as upside, and is the natural
place for the one genuinely field-defining result you would like to claim. It is also fine
for the project to be complete without it — say so.

### 7.6 State of the art (¾–1 page)

- **Expose the field's current limitations** — this is an argument, not a survey.
- **Tie each part to an objective.** The reader should be able to map SoA sub-area → objective.
- **Divide into 3–4 sub-areas**, each under its own visible heading. More becomes a
  literature review.
- **Highlight your own contributions** within it — this is where PI fit gets established
  implicitly. But *only* within it: a state of the art that cites mainly your own group
  reads as unfair to the field, and the panel member most likely to notice is the one whose
  work is missing. It has to be a summary your peers would sign.
- **State your plan to surpass it.** One forward-looking sentence at the end of *each*
  sub-area, not only at the end of the section, so that each barrier is answered where it
  is raised.

Inside each sub-area the reliable order is: current understanding and best available
approach → its specific limitation → the technical, experimental or analytical barrier that
has held the field there → one sentence on how the project moves past it. Written that way
the section is an argument with four beats repeated three or four times, which is much
easier for a generalist to follow than a continuous prose review of the field.

### 7.7 Research strategy (1½–2 pages)

The scientific approach for testing your core hypotheses and addressing the main
research questions. Three things to make explicit: the **logic of the conceptual steps**
and the rationale linking them; the **integration of disciplines**; and the **main
innovation** in the approach.

This is layer 2½ — enough about how to make the approach believable, not so much that
you have written B2 twice.

**How to build it.** Open with a global overview: the main conceptual steps, how they follow
from the vision, and how the project unfolds over time — "unfolds" in the sense of *first
this, which makes that answerable*, never a schedule. Then take it down one level into the
major components, which will usually be the objectives but may instead be conceptual steps or
lines of inquiry where the mapping is not one-to-one. For each component say which systems,
datasets, models or theory it draws on, which question it addresses, and how it connects to
the others. Two things must be explicit by the end: **how the parts work together** —
experimental, computational and theoretical strands included — and **why this particular
structure is the right fit for these questions**. Without the second, the section reads as a
list of activities rather than a strategy, which is the single most common way this section
fails.

**What belongs in B2 instead.** Protocols and step-by-step technique, timelines and Gantt
charts, task breakdowns, personnel assignments, risk tables and contingency plans. The moment
you are writing any of those you have crossed from strategy into implementation. The one
licence to go deeper is necessity: add technical detail only where the conceptual approach is
unintelligible without it, and expect that threshold to sit differently in different panels.

Note that the research strategy is a *recent* element — it arrived with WP 2026, and the
ERC's own expectations for it are still settling, which is a reason to make the section's
logic legible rather than to optimise it against precedent.

### 7.8 Why now, why me (¼–½ page)

- **Timeliness** — why this question is answerable now and was not five years ago (a new
  method, a new dataset, a new theoretical result, your own preliminary finding).
- **Preliminary results**, if you have them. Their function here is to establish
  timeliness, not to prove the project works. The strongest form is a preliminary
  finding that *raises* the project's questions: "our data show A, which prompts two
  questions: does B? and can we C?" — the result creates the project rather than
  pre-empting it.
- **PI expertise** — why you. Two or three sentences, even though the CV covers it at
  length: experience, expertise, and why you specifically are placed to do this now.

**The balance on preliminary data is where most applicants get it wrong, in both
directions.** Too much and the project reads as incremental — the hard part looks done, and
what remains looks like execution. None at all, behind a bold claim, reads as wishful
thinking. Include what you have, and be explicit about what it does *not* yet settle: these
data show that A and B connect, and they opened the question of C, *which we cannot answer
with them*. That sentence is simultaneously your evidence and your justification for needing
the grant. Note also that anything you cite which is publicly available — a new instrument, a
released dataset, a published method — is available to your competitors too, and therefore
argues that the field is ready rather than that you are; only your own unpublished results do
both.

**Do not comment directly on feasibility.** Feasibility is something the reader must
conclude, and asserting it invites doubt. Demonstrate it through the specificity of the
approach and the relevance of your record. This is now doubly true: "is the outlined
scientific approach feasible?" was **removed from the Step-1 question list** as of WP 2026
([§12](#12-what-this-was-checked-against)), so a Part I that argues feasibility is
answering a question nobody at Step 1 is asking, at the cost of the ambition they *are*
scoring.

### 7.9 Impact (¼–½ page)

- **A positive conclusion** — the section is also the document's ending, so it carries
  stress position for the whole of B1.
- **Post-project prospects** and research continuity: which new avenues does success open?
- **Scientific impact is the primary focus.** Societal or economic impact is welcome as a
  consequence but is not the criterion — it is not evaluated at all, so it earns its space
  only as a second- or third-order argument after the scientific case is made.
- **Layer the claims rather than spreading them.** Name the uptake that matters to *this*
  panel first and in detail, then the wider fields as potential extensions. Impact asserted
  in every direction at once dilutes: the reader loses track of which consequence you
  actually believe in, which is the opposite of the intended effect.

The move that works: name the breakthroughs, then say what fields they seed and *why the
findings generalise* beyond your system. "These findings have implications likely
generalisable to … because …" — the *because* is what separates impact from wishful
thinking.

## 8. Part B1 — CV and track record (4 pages)

Same single PDF as the synopsis. The template can be modified if needed. Four pages is the
limit; the division below is a recommendation, and it gives the outputs and peer-recognition
blocks more than half of the space:

| Block | Recommended pages |
|---|---|
| Personal details, education, positions | ¾ |
| Research achievements — opening paragraph | ¼ – ½ |
| Ten major research outputs | 1½ |
| Peer recognition | ¾ |
| Career breaks and life events | a few lines, or nothing |
| Other contributions to the research community | ¼ – ½ |

**Personal details.** Personalise: photo, up-to-date web page, ORCID.

**Education and key qualifications.** Add honours — *cum laude*, top-percentile rankings,
prizes attached to degrees. The call asks specifically for the **names of your PhD
supervisor(s) and postdoctoral mentor(s)**; a CV that omits them is missing required
content, and the panel reads the lineage as context for your career stage.

**Current and previous positions.** Stress leadership and tenure status; list dual
affiliations.

**Mix prose with structure.** A CV that is only bullet points tells the panel nothing about
a person; one that is only prose is exhausting to read at proposal fourteen of fifteen. The
version that works opens with a short personal paragraph and then drops into structured
lists for education and positions.

**Research achievements — opening paragraph.** Write a narrative, not a list. Four
elements: your background, what drives your research, a description of your research
focus, and a showcase of your main expertise. This paragraph is where a generalist panel
member forms their model of you. Two or three paragraphs is the working shape: the first
looking back at contributions, recognition and leadership; the second on your present focus
and active lines of inquiry; the third connecting both to *this* project and closing on a
direct statement of expertise. Ending it with the claim in your own words — "this expertise
places me to lead this project" — is better than leaving the panel to assemble the inference
from a list twenty lines later.

**First person or third, but never both.** Either is permitted. First person reads better and
is the recommendation; what costs you is mixing them, which happens by default when a
narrative paragraph is written fresh and the older list entries are pasted in.

**Ten major research outputs.**

- Weight recent contributions.
- Not only papers: books and chapters, patents, **datasets, software, algorithms** all
  count, and for computational fields the non-paper artefacts are often the stronger
  evidence of field-level influence.
- For each one, explain **its significance, your role in it, and its relevance to your
  capacity to run this project**. A bare citation does none of that work.
- **Report them exactly as published:** every author, in the published order, with joint
  authorship marked where it applies — co-first author, co-corresponding. This is an
  explicit instruction in the call, not a courtesy. Trimming an author list to fit the page,
  or promoting yourself to first author of an alphabetical list, is the kind of discrepancy a
  panel member checks and cannot unsee.
- **Group them by area of expertise, not chronologically.** Two or three labelled groups
  reinforce a scientific identity and make relevance to the project visible at a glance;
  a reverse-chronological run of ten items makes the reader do that work themselves.
  Recency still matters, but it is a weighting rule for *what you select*, not an ordering
  rule for how you present it.
- **Tie three or four of them to a specific objective or work package** — a marginal symbol
  is enough — and no more. That is the link the evaluators are looking for. Tying all ten
  produces the opposite impression: that the proposed project is work you have largely
  already done.
- **Citations and other indicators are fine; journal impact factors are not.** The ERC
  assesses outputs on their own merits, in line with the DORA-style commitments now standard
  across European funders, so a venue's impact factor is at best ignored and at worst reads
  as not knowing the current rules. Selectivity figures for competitive things you *won* are
  a different matter and do count — see peer recognition below.
- **Preprints are allowed**, provided they are freely available from a preprint server and
  properly referenced with a link. So is unpublished work, but it needs a stated reason for
  being in the list: not "this is coming", but "this establishes my command of method X,
  which WP2 depends on".

**Peer recognition.** Grants, awards, prizes, honours; invited talks, presentations,
keynotes; scientific evaluation and editorial reviewing; leadership roles.

Open the list with one framing sentence saying what the items below are meant to show,
rather than dropping straight into entries — a small addition that turns a dump into an
argument. Order most recent first, and where an item's weight is not self-evident to a
generalist, annotate it in a clause: a success rate ("13 % success rate"), the size of the
field, the fact that a talk was the plenary. This is also the place for recognition you had
to **give up**: a fellowship declined because you accepted another, or a grant reduced
because you moved country, is evidence of having won it. One parenthetical line does it —
"awarded €X, retained €Y on relocation", "declined in favour of the position at Y" — and
omitting it silently loses you credit you earned.

**Career breaks, diverse career paths and major life events.** Explain breaks or
non-linear paths; you may discuss the effect of long-term illness or pandemic
restrictions on productivity. Factual, brief, no apology.

**Other contributions to the research community.** Patents and tech transfer, other
notable achievements, outreach, open science, diversity work, legacy. Community
infrastructure — benchmarks, shared tasks, large open collaborations — belongs here and
is genuinely scoreable evidence of the "reference point in the field" criterion.

## 9. Part II of the Scientific Proposal (7 pages, = B2)

**Audience:** panel members *and* Remote Reviewers, who are topic experts.
**Function:** in the call's own words, "a detailed explanation of the project
implementation, including research methodology, work plan, risk assessment, and mitigating
measures and any further necessary background not included in Part I". Parts I and II are
reviewed together, so Part II may compress what Part I established and **must not repeat
it** — but it must not contradict it either, and it cannot assume the reader has Part I
memorised.

Order of sections:

1. Introduction, vision, objectives, state of the art — **compressed recap**, only as
   much as an expert reader needs to follow the plan and any background B1 had no room for.
2. **Project design** — the overview.
3. **Work plan** — one block per work package, including feasibility arguments.
4. **Gantt chart.**
5. **Risk analysis** and concluding remarks.

Page budget for the seven pages — a recommendation, editorial in the same way as
[§7](#7-part-i-of-the-scientific-proposal-5-pages-in-b1)'s, and the brackets on the
subsection headings are these numbers:

| Section | Recommended pages | Covered in |
|---|---|---|
| Compressed recap: intro, vision, objectives, state of the art | ½ – 1 | this section |
| Project design, with the objectives-to-work-units figure | ¾ | [§9.1](#91-project-design--page-figure-included) |
| Work plan — every work package, task and moonshot | 4½ | [§9.2](#92-work-packages-objective-versus-rationale-4-pages-for-the-whole-work-plan), [§9.3](#93-tasks--page-each-inside-the-work-plan-budget), [§9.4](#94-moonshot-tasks--page-150200-words) |
| Gantt chart | ¼ | [§9.1](#91-project-design--page-figure-included) |
| Risk analysis and concluding remarks | ½ | [§9.5](#95-risk-assessment--page-with-the-gantt-chart-alongside) |

The work plan is four fifths of what is left after the recap, which is the recommendation to
defend if something has to give. Advice written for the old 14-page Part II implies a much
larger recap and state of the art; if that is what you are working from, see
[§12](#12-what-this-was-checked-against) before dividing anything.

**Do not** reproduce the budget table in Part II — [§11.1](#111-the-budget-table) has the rule about what Part II may
and may not say about resources. References and the Funding ID appendix do not count towards
the page limit, and must not be uploaded separately.

### 9.1 Project design (¾ page, figure included)

An overview before the detail:

- The **number and function** of the work units.
- **Emphasis on the innovative aspects** — say which part is the new thing.
- **How the units interconnect**, and how each relates to the objectives.

A figure earns its space here: a diagram mapping objectives to work units, with the
dependencies between units drawn. It answers "is this a project or a list of projects?"
in one glance, which is exactly the question a generalist panel member is asking.

### 9.2 Work packages: objective versus rationale (4½ pages for the whole work plan)

The distinction the seminar spends real time on, and the most common muddle in draft
work packages.

**Objective — what will be achieved.** The concrete outcome. What knowledge, method,
dataset, model or result exists when the work package is done, and how it contributes to
the project objectives. Short, specific, outcome-oriented. Usually one sentence.

**Rationale — why the work package is needed.** The scientific justification: which gap,
uncertainty, bottleneck or dependency it addresses, why this is the right approach, and
why it matters for the project's goals. Typically 2–5 sentences, plus background and
preliminary data where relevant.

The classic error is writing the objective *as* a rationale:

> ✗ "To address the lack of robust biomarkers…"  ← that is why the WP exists
>
> ✓ "To identify and validate robust biomarkers for disease progression."

Structure per work package:

```
WP objective          what will be achieved                  1 sentence
WP rationale          why it is needed, background, prelim    2–5 sentences
  Task 1 · Task 2 · Task 3
WP expected outcomes  what the field has that it lacked now   1 paragraph
```

Plus, across the work plan: choice of methodology **and evidence of flexibility** (name
key intermediate goals and decision points), development of novel methodology,
interdisciplinary aspects, and explicit arguments in favour of feasibility.

### 9.3 Tasks (½ page each, inside the work-plan budget)

A task should read as a compact scientific story, not a to-do item. Four moves — as
prose, **not** as four sub-headings:

1. **Purpose** (1–2 sentences) — the scientific question this task answers. A mini-objective.
2. **Scientific approach** (4–8 sentences) — how you will answer it: the controlled
   experiments, the interventions, the analyses. High-level enough to stay readable.
3. **Expected scientific contribution** (1–3 sentences) — not "deliver a dataset" but
   "the first taxonomy of X", "principles that will guide the methods in WP2".
4. **Link to the next task** (optional, one sentence) — what these findings motivate.

**Do not recurse.** Giving every task its own objective / rationale / sub-tasks /
outcomes block produces a nested structure that repeats itself and burns pages. The work
package's objective and rationale apply to all its tasks; each task then just needs
*question → approach → contribution*.

Three details inside the approach sentences do disproportionate work, and all three are
cheap:

- **Name who does it.** A task attached to a named postdoc, student profile or collaborator
  is a task with a resource behind it, and it silently connects the work plan to the budget.
- **Include the check.** One clause saying how you will know the step worked — benchmarking
  against known values, a validation on held-out or spiked samples, a control condition —
  tells the reviewer *why* the step is there and not merely that it happens.
- **Say what you do if it does not work**, in one clause, where the risk is specific to this
  task: "if separation proves insufficient we will instead …". Task-level fallbacks are not a
  substitute for the risk section; they are what stop the reviewer from writing the objection
  down in the first place.

### 9.4 Moonshot tasks (¼ page, 150–200 words)

For the one task in a work package that is deliberately far more ambitious and far less
likely than the rest. Treat it differently in *emphasis and rhetoric*, not as a different
kind of object.

Structure — five moves rather than the usual three:

1. **The question or opportunity.** "The preceding tasks establish X. This raises a more
   ambitious question: can Y?"
2. **Why it is plausible.** Motivated by a finding or principle from the core tasks, but
   requiring a step beyond the work package's normal scope.
3. **The approach.** Not a complete solution — a critical prediction or proof of
   principle first, with success motivating the larger investigation.
4. **What success means, and what failure means.** A positive result does A; **a negative
   result still teaches B**. A moonshot with an informative negative outcome is a
   different and much better object than a gamble.
5. **Risk and boundedness.** Name the specific uncertainty, give the decision point or
   bounded strategy, and state that the work package's main objectives remain achievable
   through the core tasks.

Three rules of tone:

- **Do not apologise for the risk.** Not "this task is less likely to succeed" but "this
  is deliberately high-risk because …", immediately followed by why the risk is
  scientifically worth taking. The difference between "we don't know whether this will
  work" and "the fundamental question is unresolved, and answering it would establish
  whether the theory has predictive power beyond the phenomena it was derived from" is
  the difference between an optional experiment and high-risk/high-gain science.
- **Make the core complete without it.** State that the remaining tasks constitute a
  coherent project on their own. The moonshot raises the ceiling; it must not lower the floor.
- **Transfer understanding, not methods.** "If the *principles* uncovered above prove
  sufficiently robust" is much stronger than "if some of the above *methods* prove
  promising" — the second sounds like taking whatever happened to work and trying it
  elsewhere.

**Length:** shorter than a core task. If core tasks run half a page, a moonshot gets a
quarter page, sometimes 150–200 words. But not one line — "we will also explore X" reads
as an unfocused afterthought. It needs enough room to establish the risk/reward logic.

Distinguish a moonshot from a merely *exploratory* task. A task asking "what phenomena
are we currently missing?" is exploratory but integral — part of the core scientific
programme and deserving normal length. A moonshot follows from the work package but goes
substantially beyond its central objective, and would, if it worked, produce a broader
theory than the work package promised.

### 9.5 Risk assessment (½ page, with the Gantt chart alongside)

- A **risk strategy**, not a table of platitudes.
- **Describe and classify** the relevant risks.
- **Mitigations and contingencies** for each.
- **Why do you need to take the risk?** The question that turns a risk section from
  defensive into ambitious. Every work package needs a stated risk and a fallback that
  still yields a result.

**Technical risks go in a table** — risk, probability, impact, contingency — and it is worth
adding the expected outcome of plan B beside that of plan A, because the comparison is what
shows why plan A is the one you are backing rather than an arbitrary first choice. Keep the
table short and specific: a risk register listing every way research can disappoint reads as
padding, and the point is a few well-chosen high-risk elements, deliberately taken.

**Conceptual risks belong outside the table.** If the risk is that the central hypothesis
does not hold, that is not a probability-times-impact cell — it is a paragraph, and what it
has to answer is what the project still establishes if the hypothesis fails. A negative
result that settles a live question is a result; a project that only works if you were right
is a gamble.

**Do not end B2 on risk.** Close with concluding remarks — a short paragraph restating the
ambition, why it matters, how the project moves the field, why the plan is deliverable, and
what success opens up. This is the last thing a Step-2 reviewer reads before scoring, and the
stress position should hold the case for funding rather than the list of things that could go
wrong.

## 10. Sentence-level rules for the implementation sections

**Make cause and effect explicit.** Especially in work package and task descriptions.
Replace every "and" and "then" that is doing causal work with a connective that names the
causality.

> Weaker: "We will design an experiment and collect data. Then we will create a
> reference library and develop an interactive database."
>
> Better: "We will design an experiment *in order to* collect data. *Based on this data*
> we will create a reference library, *which in turn allows us to* develop an interactive
> database."

The point is not elegance. A chain of "and…then…and" gives the reviewer no way to tell
whether the plan has a logic or is a list, and a list is what an incremental project
looks like.

**Active voice where a human is the agent.** "Correlation between X and Y will be
measured" → "We will measure the correlation between X and Y." Passive is fine where the
subject is not the result of human agency: "the hypothesis will be rejected if there is
no indication of …".

## 11. Budget, resources and panel choice

**All of it lives in Part A**, in the online form's *Budget* section: the table, and a
Resources text box under it. Part II may explain resources where the methodology or work
plan makes it natural, and the call explicitly permits that, but the *detailed and
exhaustive* breakdown must be in Part A, Part II **cannot deviate** from it, and no budget
information may live anywhere else — an annex will not be accepted. Where the table and the
prose disagree, **the table prevails**.

Both the table and the Resources text reach the Step-2 panel and the Remote Reviewers, as a
generated *Proposal Budget Report* that also prints your declared time commitment beside the
figures ([§3](#3-who-reads-what-and-when)). Nobody at Step 1 sees any of it. Expect interview questions on the table
itself. Talk to your institution's grant support staff — this is the one section where local
expertise beats general advice.

### 11.1 The budget table

The ERC funds up to **100 % of total eligible costs** for the full project duration: direct
costs, plus a flat-rate 25 % for indirect costs. Whole euros only, no thousands, no
percentages. Five cost categories, and the substructure inside C is what the form actually
asks for:

| | Category | Contains | Indirect costs |
|---|---|---|---|
| **A** | Direct personnel | PI · senior staff · postdocs · students · other personnel | yes |
| **B** | Subcontracting | — | **no** |
| **C1** | Purchase — travel | travel and subsistence | yes |
| **C2** | Purchase — equipment | equipment, including major equipment | yes |
| **C3** | Purchase — other goods, works and services | consumables (incl. fieldwork and animal costs) · publications, including Open Access fees, and dissemination · other additional direct costs | yes |
| **D** | Internally invoiced goods and services | host-institution internal charges | **no** |
| **E** | Indirect costs | computed, not entered: **E = 25 % × (A + C1 + C2 + C3)** | — |

Total eligible costs are A + B + C + D + E. B and D carry no overhead because those charges
already include it.

Four things about the table that cost people grants rather than points:

- **`Total eligible costs` is calculated for you; `Requested EU contribution` is not.** You
  type it, and it does not update when you change a category. Re-check it last, after every
  other edit. If the two differ on purpose, say in the Resources text what the difference is
  funded from.
- **The PI's personnel cost cannot exceed the time commitment** you declare in *Other
  questions* (≥ 50 % StG, ≥ 40 % CoG). These are two separate sections of the form and the
  form does not reconcile them for you.
- **Equipment is a depreciation cost by default.** Full capitalised cost is possible by
  exception, and only for items **listed and justified in the proposal** — so the decision
  has to be made while you are still writing, not at grant preparation.
- **Unjustified budgets are cut, not queried.** The call's own words: "The evaluation panels
  assess the estimated costs carefully; unjustified budgets will be reduced." The reduction
  happens without a conversation. You will hear the opposite claim in practitioner
  circles — that panels no longer trim, they take the request or leave it — and for the 2027
  call it is contradicted by the *Information for Applicants*, which still carries that
  sentence in the Resources instructions. Write to the document.

Two eligible categories that applicants routinely leave out: **care costs** directly caused
by the project — childcare during fieldwork, conferences, visits to large facilities — where
the host's rules allow them, and, for a PI relocating to the EU or an Associated Country, the
PI's **one-way ticket** (family tickets and relocation costs are not eligible).

### 11.2 The Resources text box

8,000 characters including spaces — one to two pages of text — under the table, and
**silently truncated** at the limit, so check the length in the form and not in your editor.
Six things it has to do, in the call's own order:

1. **Every cost category, described and justified**, as accurately as you can estimate.
2. **The size and nature of the team**, with key members and their roles. A member hosted by
   another institution needs the scientific added value spelled out against the extra cost.
3. **Any additional funding**, item by item ([§11.3](#113-additional-funding)).
4. **A short technical description of each piece of requested equipment** — what it is, why
   you need it, and how much of the project you will use it for.
5. **A realistic Open Access estimate.** Eligible only for fully open-access venues and only
   if incurred during the project: article and book processing charges, page and colour
   charges.
6. **Existing resources that need no EU funding** — infrastructure and equipment the host
   provides, and any third-party in-kind contributions.

Personnel, equipment and dissemination are where the panel's attention goes, and each needs a
profile and a responsibility rather than a headcount. Equipment justification is read hardest
where you already hold other funding.

### 11.3 Additional funding

Above the grant ceiling ([§2](#2-call-mechanics)) you may request up to **€1 M**, or **€2 M**
if you are relocating to the EU or an Associated Country to take up the grant. It goes in
the same table, in whichever cost categories the money is actually needed for, and must be
fully justified in the Resources text. It is a separate cost category in the Model Grant
Agreement, it may itself attract the 25 % overhead depending on the category, and it is **not
reduced pro rata** for a shorter project. After award, the breakdown can be changed only
within the objectives the additional funding was granted for — which makes those objectives
worth writing precisely.

### 11.4 Panel, keywords, and who will not review you

You choose the primary panel and, if the proposal is genuinely cross-disciplinary, a
secondary one; up to four ERC keywords from the call's own list, each covering a research
area. This choice determines who reads you in Step 1 — which, given that Step 1 is decided by
generalists reading only B1, is a strategic decision rather than an administrative one.

There are **28 panels: PE1–PE11** in physical sciences and engineering, **LS1–LS9** in life
sciences, **SH1–SH8** in social sciences and humanities, each with its own budget share, so
the panel you pick is also the pool you compete in. The keyword limit of four is a maximum
and not a target: **naming one or two keywords that genuinely describe the proposal steers
allocation more reliably than four**, because a spread of keywords across sub-areas invites
allocation to whichever of them the panel is least equipped for. Allocation can also be
changed without you — the panel may hand a proposal to another panel where the expertise
sits, with both chairs' agreement ([§3](#3-who-reads-what-and-when)) — which is one more
reason to make the primary choice unambiguous. The
ERC publishes past panel membership at
[erc.europa.eu/apply-grant/panel-members](https://erc.europa.eu/apply-grant/panel-members); work
backwards from the composition of a panel to whether your B1 will land with it. A
cross-panel proposal must also *explain on the cover page why* it needs more than one panel.

You may also name **up to three reviewers to be excluded** from your evaluation, in Part A's
*Other questions*. The request is only considered if the details are complete and correct —
first and last name, institution, town, country, web page — so an approximate entry is the
same as no entry.

---

## 12. What this was checked against

Every number and quotation above was verified on **11 August 2026** against two primary
sources, both of which govern the ERC-2027-StG and ERC-2027-CoG calls. The budget, resources
and CV material — [§2](#2-call-mechanics)'s component table, [§8](#8-part-b1--cv-and-track-record-4-pages), and [§11.1](#111-the-budget-table)–[11.4](#114-panel-keywords-and-who-will-not-review-you) — was checked again on
**14 August 2026** against the same *Information for Applicants*, §2.3 and Annexes 4.6
and 4.7 (the Proposal Budget Report), which is where the cost categories, the 25 % indirect
formula and the character limits are stated:

| Source | Version | Settles |
|---|---|---|
| [*Information for Applicants to the Starting and Consolidator Grant 2027 Calls*](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/guidance/information-for-applicants_he-erc-stg-cog_en.pdf) | 11.0, 22 July 2026 | component names, page limits, layout, what each step sees, interview, budget rules |
| [*ERC Work Programme 2027*](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2027/wp_horizon-erc-2027_en.pdf) | C(2026) 4907, 20 July 2026 | evaluation elements verbatim (§1.6.5), eligibility windows, grant amounts, call dates |

The Information for Applicants for **your own** call is the authority, not this file. It is
reissued every July and its version history names the call it serves, so check that the
version you are holding says 2027 (or later) and not 2026.

The **submission restrictions** in [§2](#2-call-mechanics), the panel structure and keyword
rules in [§11.4](#114-panel-keywords-and-who-will-not-review-you), and the budget-reduction
sentence in [§11.1](#111-the-budget-table) were checked on **14 August 2026** against the
same *Information for Applicants* — §1.2 and the outcome table for the restrictions, Annex 4.1
for the panels, Section C of the budget instructions for the reduction.

**Five things changed recently enough that older advice is actively wrong.**

*Part II is 7 pages, not 14.* The cut landed with WP 2026. If your LaTeX template still
prints "14 pages" in its instruction block, it predates the change. A Part II written to
the old limit is not half-full — it is over, and every addition from here displaces
something.

*Feasibility left Step 1.* Also WP 2026. The Step-1 project element now has two questions,
neither of which asks whether the approach is feasible; the surviving clause asks whether
it is *scientifically convincing*. A Part I that spends a page defending feasibility is
spending it on a question no Step-1 reader is answering — and inviting a conservative
verdict on ambition, which is what that reader *is* scoring.

*Novel methodology is no longer a scoring clause.* The Step-2 methodology question used to
ask whether the work would "involve developing novel methodology"; it now asks only whether
the methodology and working arrangements are appropriate. Novel method still helps — it is
evidence of ambition and of creative thinking — but it no longer has its own address.

*The eligibility windows widened in WP 2027*, from 2–7 and 7–12 years post-PhD to 0–10 and
5–15 ([§2](#2-call-mechanics)). Anyone told they were too early or too late for a Starting Grant under the old
rule should recheck.

*The resubmission penalties have been tightening, and they are the rule most often quoted from
memory.* Under WP 2027 a B or C at Step 1 in the 2026 call bars every 2027 call, and a C at
Step 1 reaches back two years ([§2](#2-call-mechanics)) — so a weak submission now costs
eligibility, not just time. The direction of travel is towards longer bars as application
volumes rise, which means the outcome table has to be read in the *Information for Applicants*
for the call you are actually submitting to; the version in a colleague's notes from two years
ago is the wrong one, whichever way it errs.

*Also new in WP 2027, and not covered by this guide:* the **[ERC Plus Grant](https://erc.europa.eu/apply-grant/erc-plus-grant)** (€7 M, 48–84
months, open to all career stages, roughly 30 awarded per year across all fields against
about 1,000 StG/CoG/AdG), which adds its own evaluation question — whether the project
addresses aims unreachable with a regular ERC grant. Everything here is written for StG and
CoG.

---

## 13. Review protocol

This section is a rubric worked from the top down, not a checklist worked through. It is
what the `erc-review` skill ([`SKILL.md`](../SKILL.md)) executes, and a human
reviewer can run the same ladder by hand.

The ordering principle: fixing an early stage rewrites everything downstream, so findings
below an open failure are wasted work. A draft whose scientific question is not nameable
does not benefit from twenty notes on passive voice — it benefits from one note about the
question, and silence about the rest until that is settled.

Three shared conventions make findings comparable across reviews:

| Severity | Meaning | Consequence if left |
|---|---|---|
| **BLOCK** | Compliance breach or unwritten placeholder | Not submittable as-is |
| **SCORE** | Weakens the answer to a named evaluation question | Costs points in Step 1 or 2 |
| **POLISH** | Sentence-level | Costs goodwill, not points |

The same three words label the checker's output ([§13.3](#133-what-the-checker-settles--stages-8-and-9)) and the comment macros ([§13.5](#135-leaving-a-finding-in-the-draft)).

The evaluation questions are referred to below by the shorthands **Q1** important questions,
**Q2** ambitious objectives / frontier, **Q3** methodology and working arrangements, **Q4**
timescales and resources, **Q5** PI ground-breaking research, **Q6** PI creative and
original thinking, **Q7** PI expertise and capacity ([§4](#4-the-evaluation-questions)). Q1, Q2 and Q5–Q7 are scored in
Step 1 from Part I and the CV alone; Q3 and Q4 only in Step 2 ([§3](#3-who-reads-what-and-when)). Naming the question is
what separates a finding from a preference.

And one standing rule: anything you cannot point to a location for is missing, not implicit.
"It's implied by the objectives" is how proposals lose the criterion they thought they had
covered.

### 13.1 The stage ladder

| # | Stage | The question the stage asks | Reported as |
|---|---|---|---|
| 0 | **Census** | What exists at all? | not reported — a map |
| 1 | **Fundability** | Is this an ERC project, or an excellent next paper? | BLOCK on the framing |
| 2 | **Problem** | Is there a nameable question, with an instability and a cost? | SCORE on Q1 |
| 3 | **Layers** | Is each passage at its right altitude? | SCORE on Q1/Q2 |
| 4 | **Step-1 sufficiency** | Can Q1, Q2, Q5–Q7 be scored from B1 alone? | SCORE on all five |
| 5 | **Criteria coverage** | Does every question have an address in the document? | SCORE, per question |
| 6 | **Work plan** | Are work units and tasks correctly typed and bounded? | SCORE on Q3/Q4 |
| 7 | **Argument mechanics** | Do the sentences carry the argument's joints? | SCORE or POLISH |
| 8 | **Prose** | Fillers, hedges, voice, jargon, tics | POLISH, machine-checked |
| 9 | **Compliance** | Pages, placeholders, citations, funding table | BLOCK, machine-checked |

Stage 0 first, always: `erc_check.py --census --pages` ([§13.3](#133-what-the-checker-settles--stages-8-and-9)). It reports words per
part, which units are still unwritten, how many placeholders remain, and pages against the
limit — enough to know which stages are answerable. A part sitting **at** its page limit
changes every later stage, because from then on a suggestion must name what it displaces.

### 13.2 Stage rubrics

Each item gives a **test** (what to look at, and what makes it pass), the **cost** if it
fails (which question, and for which reader), and what to **suggest**. The cost column is
what makes a finding arguable on the merits instead of on taste.

#### Stage 1 — Fundability

- **The PI may actually submit this.** *Test:* PhD defence date inside the window, no prior
  grant of the same type, no outcome-based bar from the last two calls, and any current ERC
  project ending within two years of the deadline ([§2](#2-call-mechanics)). *Cost:* the
  whole application — these are checked administratively before any reviewer reads a word,
  and a bar means the proposal is not evaluated at all. *Suggest:* settle it with the grants
  office in the first conversation, not the last; if a bar applies, the question becomes
  which call to target and the draft is not wasted.
- **A step change exists.** *Test:* read the vision and objectives against the PI's last
  three papers; passes when the project is not their natural continuation and the
  before/after state of the field is stateable in one sentence. *Cost:* Q2 — the panel's
  single most-weighted judgement; an incremental extension scores mid-range and mid-range
  does not fund. *Suggest:* name what becomes possible after the grant that is impossible
  now; if the answer is "more of the same, better", the project needs a different aim, not
  a different paragraph.
- **The scope fits one PI and five years.** *Test:* count the objectives and the methods
  each needs; passes when a team of the proposed size could plausibly do all of it.
  *Cost:* Q4 in Step 2, but also Q2 in Step 1 — over-scoping reads as not understanding
  the work. *Suggest:* cut an objective rather than thinning all of them.
- **It is a research project, not a programme, a platform, or a service.** *Test:* passes
  when the deliverables are knowledge claims and any artefact exists to produce them.
  *Cost:* Q1 and Q2 — infrastructure proposals are the classic ERC rejection. *Suggest:*
  demote the artefact to a task and promote the claim it enables.

#### Stage 2 — Problem

- **The question is nameable.** *Test:* B1 page 1; passes when a non-specialist can write
  the scientific question in one sentence after one read, unprompted. *Cost:* Q1 directly;
  a Step-1 panel member who cannot state your question cannot argue for you in the panel
  meeting. *Suggest:* move the question into the first paragraph and cut whatever currently
  occupies it — usually background or a widening generalisation.
- **The opening is a problem, not a topic.** *Test:* passes when the first paragraph
  contains both an instability (something the field believes that does not hold, or two
  results that cannot both be right) and a cost to *these* readers. *Cost:* Q1. *Suggest:*
  find the "but" the draft is hiding behind an "and". Prefer naming an error or an
  inconsistency over naming a gap: a gap invites "so fill a different one".
- **Limitations and barriers are both present and distinguishable.** *Test:* B1 intro and
  state of the art; passes when one sentence says *what* is unknown and a different
  sentence says *why* it has stayed unknown ([§7.2](#72-limitations-versus-barriers-a-rule-for-71-not-a-section-of-its-own)). *Cost:* Q1 — the "limitations and
  barriers" component is scored explicitly. *Suggest:* if only limitations exist, ask what
  blocked prior attempts; that answer is usually also the why-now ([§7.8](#78-why-now-why-me--page)).
- **The challenge is falsifiable.** *Test:* passes when no challenge statement rests on
  "poorly understood", "remains unclear", "little is known" ([§7.3](#73-state-the-challenge-in-falsifiable-terms-24-sentences-inside-71), machine-checked).
  *Cost:* Q1. *Suggest:* replace with the specific claim that would have to be wrong.

#### Stage 3 — Layers

- **Vision and aim are separate.** *Test:* passes when the vision outlives the grant, the
  aim completes inside 60 months, and neither paraphrases the other ([§7.4](#74-vision-versus-overarching-aim--page)). *Cost:* Q2 —
  a vision-shaped aim reads as unachievable, an aim-shaped vision as unambitious; both lose
  the same point. *Suggest:* keep both sentences and label them.
- **3–5 objectives, each a knowledge claim.** *Test:* passes when each opens with a verb of
  knowledge production — uncover, identify, assess, test whether — is verifiable, and the
  dependencies between them are stated ([§7.5](#75-objectives--page)). *Cost:* Q2, where deliverable-phrased
  objectives are explicitly marked down. *Suggest:* convert "build X" into the claim that
  building X lets you test.
- **No B1 paragraph is describing a task, no B2 work package floats free of an objective.**
  *Test:* [§5](#5-the-four-layers)'s four layers; passes when every passage sits at one level. *Cost:* Q2 in B1
  (detail read as timidity), Q3 in B2 (a work package with no objective has no purpose).
  *Suggest:* move it rather than rewrite it — misplaced material is usually good material.

#### Stage 4 — Step-1 sufficiency

- **B1 stands alone.** *Test:* close B2 entirely; passes when Q1, Q2 and Q5–Q7 can all be
  scored from B1 ([§3](#3-who-reads-what-and-when)). *Cost:* all five, silently — the Step-1 panel never sees B2, so
  content parked there scores zero at the only stage that eliminates. *Suggest:* name what
  must be lifted into B1 and what it displaces from the five pages.
- **Written for a generalist.** *Test:* passes when every term not universal *outside* the
  subfield is defined or gone. *Cost:* Q1 and Q2 — panel members are the applicant's field
  only by accident. *Suggest:* define at first use in a clause, not a sentence.
- **Headings answer the evaluation questions.** *Test:* the table of contents; passes when
  a reviewer scoring question N finds the section without searching. *Cost:* every question,
  by attrition. *Suggest:* make the heading answer rather than ask.

#### Stage 5 — Criteria coverage

Take one question at a time and find its address. The recurring failures:

- **Timeliness is argued, not asserted.** *Test:* the why-now section; passes when a
  specific thing changed — a method, a dataset, a result, a preliminary finding of the PI's.
  "The field is ready" does not count ([§7.8](#78-why-now-why-me--page)). *Cost:* Q2. *Suggest:* the barrier from stage
  2, plus what removed it.
- **PI fit is shown, not claimed.** *Test:* CV opening plus the ten outputs; passes when a
  reader concludes you are the obvious person without the document saying so ([§8](#8-part-b1--cv-and-track-record-4-pages)). *Cost:*
  Q5–Q7. *Suggest:* replace the claim with the evidence that produced it; for CoG,
  weight independence and leadership, for StG, exceptional results ([§4](#4-the-evaluation-questions)).
- **Impact says why the findings generalise.** *Test:* passes when there is a *because*,
  not a list of adjacent fields ([§7.9](#79-impact--page)). *Cost:* Q1's relevance component. *Suggest:* name
  the mechanism of transfer — a principle, not a method.
- **Feasibility is demonstrated, never asserted.** *Test:* search for "feasible"; passes
  when there are no hits and the specificity of the approach does the work. *Cost:* in
  WP2026+ feasibility left Step 1 entirely ([§12](#12-what-this-was-checked-against)), so asserting it in B1 spends space on an
  unscored claim. *Suggest:* delete the assertion; move the evidence to B2 §b.
- **Ten outputs each carry significance, PI role, and project relevance.** *Test:* passes
  when no entry is a bare citation and non-paper artefacts are claimed explicitly ([§8](#8-part-b1--cv-and-track-record-4-pages)).
  *Cost:* Q5–Q7. *Suggest:* one clause per output, in that order.

#### Stage 6 — Work plan

- **Every WP has a one-sentence objective that is an outcome, and a 2–5 sentence rationale
  that is a need.** *Test:* the WP opening; passes when the objective names what will exist
  and the rationale names why the WP is required ([§9.2](#92-work-packages-objective-versus-rationale-4-pages-for-the-whole-work-plan)). *Cost:* Q3 — the external expert
  reads the work plan for whether conclusions can be drawn. *Suggest:* they are usually both
  present and both labelled "objective"; relabel one.
- **Objectives map visibly to work packages.** *Test:* B2 project design; passes when a
  figure shows the mapping and the dependencies ([§9.1](#91-project-design--page-figure-included)). *Cost:* Q3, Q4. *Suggest:* a table
  is enough if a figure will not fit.
- **Every task reads purpose → approach → contribution, as prose.** *Test:* each
  `\paragraph`; passes when no task carries its own objective/rationale/sub-task scaffolding
  and the length matches 1–2 + 4–8 + 1–3 sentences ([§9.3](#93-tasks--page-each-inside-the-work-plan-budget), length machine-flagged). *Cost:*
  Q3. *Suggest:* the missing element is nearly always the expected contribution.
- **Each moonshot is bounded and informative either way.** *Test:* passes when it names the
  specific uncertainty, says what a negative result teaches, and states that the WP's
  objectives survive without it ([§9.4](#94-moonshot-tasks--page-150200-words)). *Cost:* Q2 if absent, Q3 if unbounded. *Suggest:*
  add the sentence that says the other tasks form a complete project alone — and do not
  apologise for the risk.
- **Risk analysis answers *why take this risk*.** *Test:* passes when each risk has a
  classification, a contingency, and a fallback that still yields a result ([§9.5](#95-risk-assessment--page-with-the-gantt-chart-alongside)). *Cost:*
  Q3, Q4. *Suggest:* a fallback that yields nothing is a reason to cut the task.
- **Gantt shows decision points.** *Test:* passes when go/no-go moments are visible, not
  just durations. *Cost:* Q4. *Suggest:* mark them on the existing chart.
- **B2 does not contradict B1.** *Test:* compare aim and objectives in both; passes when
  wording matches or the difference is deliberate. *Cost:* Q3 — the Step-2 expert reads
  both and a drift reads as one of them being stale. *Suggest:* B1 wins; B2 follows.

#### Stage 7 — Argument mechanics

- **Old information before new.** *Test:* read the first six words of each sentence in a
  section; passes when each stands on something already established. *Cost:* Q1/Q2 by
  attrition — a reader re-reading is a reader deciding. *Suggest:* when a sentence has
  nothing to stand on and you cannot repair it without inventing a connection or cutting,
  you have found a hole in the *argument*: report it as a question, not a transition.
- **The stress position carries the payload.** *Test:* sentence endings; passes when the
  emphasis the substance deserves lands where the structure creates emphasis. *Cost:*
  POLISH unless it is a claim sentence, then SCORE. *Suggest:* a colon before the payload,
  or "not X, but Y".
- **Causal chains are named.** *Test:* every "and", "then", "thereby"; passes when the
  causal relation is in the verb (machine-flagged for the common cases, [§10](#10-sentence-level-rules-for-the-implementation-sections)). *Cost:* Q3 —
  an implied chain is a chain the expert can dispute. *Suggest:* name the relation.
- **Every claim is cited, shown, or softened** — including those inside subordinate clauses
  ("widely believed", "frequently dismissed"). *Cost:* the cheapest thing for a reviewer to
  attack. *Suggest:* soften or cut; do not invent a citation.

### 13.3 What the checker settles — stages 8 and 9

Do not spend reasoning on these. The script settles them, cites the guide section, and
triages by severity.

Run it from the directory holding your `b1.tex` and `b2.tex`; it finds them there, so the
kit can be cloned once and pointed at any proposal (`ERC=path/to/erc-review`):

```
python3 $ERC/tools/erc_check.py --census --pages   # stage 0: what exists
python3 $ERC/tools/erc_check.py --pages            # everything, with page counts
python3 $ERC/tools/erc_check.py --only BLOCK       # just the submission blockers
python3 $ERC/tools/erc_check.py --json             # findings + structure, parseable
python3 $ERC/tools/erc_check.py b2.tex             # one file, or a directory
```

Each finding prints `file:line [code] message (guide §)`.

| Code | Catches | Rule |
|---|---|---|
| `instructions-on` | `showinstructions` still enabled | [§7](#7-part-i-of-the-scientific-proposal-5-pages-in-b1) |
| `notes-visible` | `\wzm` set to reveal private notes | — |
| `placeholder` | `HERE GOES`, `XXXX`, `DD/MM/YYYY`, `Name Surname`, `EDIT:`, `\temp{}`, `TODO` | — |
| `empty-cite` / `empty-ref` | `\citep{}`, `\ref{}` — a claim with no support | [§7.3](#73-state-the-challenge-in-falsifiable-terms-24-sentences-inside-71) |
| `funding-blank` | Funding ID table with no entries and no "No funding" | [§2](#2-call-mechanics) |
| `abstract-long` / `abstract-thin` | abstract outside the 2,000-character budget | [§6](#6-part-b1--cover-page-and-abstract) |
| `vague-challenge` | "poorly understood", "remains unclear", "little is known", … | [§7.3](#73-state-the-challenge-in-falsifiable-terms-24-sentences-inside-71) |
| `objective-deliverable` | objective opening with build/implement/release | [§7.5](#75-objectives--page) |
| `stray-note` | drafting fragments that render as body text | — |
| `causality` | "and then", sentences opening "Then", stacked "and we will" | [§10](#10-sentence-level-rules-for-the-implementation-sections) |
| `passive` | `will be …ed` where a human is the agent | [§10](#10-sentence-level-rules-for-the-implementation-sections) |
| `filler` | simply, clearly, easily, leverage, utilize, very, various | [§10](#10-sentence-level-rules-for-the-implementation-sections) |

It also prints a **structure report** — every section, subsection and task with word and
sentence counts, flagging tasks shorter than purpose+approach+contribution needs and
moonshots over ~200 words ([§9.3](#93-tasks--page-each-inside-the-work-plan-budget), [§9.4](#94-moonshot-tasks--page-150200-words)) — and, with `--pages`, page counts against the limits.

The two compliance items no script can check: B1 must be one combined PDF with sections,
references and appendix never uploaded separately ([§2](#2-call-mechanics)), and B2 must contain no budget table
or resources section anywhere ([§11.1](#111-the-budget-table)).

### 13.4 Scoping a review

A full ladder is for a complete draft. Mid-draft, name a scope and one stage:

| Invocation | Scope | Stage |
|---|---|---|
| `erc-review` | both parts | ladder from 0, stop at first failing stage |
| `erc-review b1.tex` | B1 only | 0–5 |
| `erc-review step-1` | B1 alone, B2 closed | 4 |
| `erc-review wp2` | one work package | 6 |
| `erc-review skim` | headings and first sentences only | 2–4, cheaply |
| `erc-review cut 5` | the part that is over | 9, reporting what was sacrificed |

The **skim** scope is worth its own mention: read only headings and first sentences. If the
argument does not survive that, the openings are wrong or the order is, and no amount of
body-text editing will fix it.

### 13.5 Leaving a finding in the draft

Chat is for the finding list and the questions; the draft is for anything that must survive
the conversation. The macros in [`ercreview.sty`](ercreview.sty) take a guide section
plus the comment:

```latex
\ercblock{13.3}{funding table still blank}
\ercscore{9.2}{this is the rationale, not the objective -- the objective is missing}
\ercpolish{10}{"and then" hides the causal step}
```

They render as margin notes coloured by severity (through `todonotes` where it is loaded,
otherwise `\marginpar`), and `\listoferccomments` prints a summary page so the author works
the queue without re-reading the draft. `\ercreviewfalse` before `\begin{document}` drops
all of them for the submission build.

Four conventions, in order of how much trouble ignoring them causes:

1. **Put the severity in the macro, not the prose.** Then a disagreement is about the
   severity, which is arguable, rather than about tone.
2. **Say where the missing thing goes.** A comment that only identifies an absence hands
   the author a search problem on top of a writing problem.
3. **Read the existing comments before adding any.** They are an open queue; a sixth item
   on top of five unanswered ones is not a review, it is noise.
4. **When the fix needs a fact you do not have, ask — do not draft.** Plausible filler in a
   grant proposal is worse than a visible hole, because the hole gets fixed.
