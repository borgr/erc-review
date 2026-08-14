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
- **Secondary source:** the seminar recording, and follow-up notes on work-package and
  task-level structure.
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
extra reviews from remote Step-1 experts. Up to 44 proposals per panel are retained for
Step 2. Scores are A-invited, A-not-invited, B or C; only A-invited proceeds, and the
rest are rejected with an evaluation report.

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

Recommended sections and page budget. The five pages are not divided by the call, so this
allocation is editorial: the *Covered in* column is where each band's rules live, and the
bracket on each of those subsection headings is its share of the band, so the nine brackets
sum to five pages. Treat a bracket as an opening bid rather than a rule — what matters is
that a section running to twice its bracket has taken the pages from somewhere, and that you
can say from where.

| Band | Pages | Covered in |
|---|---|---|
| Introduction / project rationale + vision | 1 – 1.5 | [§7.1](#71-introduction--project-rationale--page), [§7.2](#72-limitations-versus-barriers-a-rule-for-71-not-a-section-of-its-own), [§7.3](#73-state-the-challenge-in-falsifiable-terms-24-sentences-inside-71), [§7.4](#74-vision-versus-overarching-aim--page) |
| Objectives + state of the art | 1.5 – 2 | [§7.5](#75-objectives--page), [§7.6](#76-state-of-the-art-1-page) |
| Research approach / strategy | 1.5 – 2 | [§7.7](#77-research-strategy-12-pages) |
| Why now, why me + impact | 0.5 – 1 | [§7.8](#78-why-now-why-me--page), [§7.9](#79-impact--page) |

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

### 7.6 State of the art (¾–1 page)

- **Expose the field's current limitations** — this is an argument, not a survey.
- **Tie each part to an objective.** The reader should be able to map SoA sub-area → objective.
- **Divide into 3–4 sub-areas.** More becomes a literature review.
- **Highlight your own contributions** within it — this is where PI fit gets established
  implicitly.
- **State your plan to surpass it.** The section ends with what you will do that the
  state of the art cannot.

### 7.7 Research strategy (1½–2 pages)

The scientific approach for testing your core hypotheses and addressing the main
research questions. Three things to make explicit: the **logic of the conceptual steps**
and the rationale linking them; the **integration of disciplines**; and the **main
innovation** in the approach.

This is layer 2½ — enough about how to make the approach believable, not so much that
you have written B2 twice.

### 7.8 Why now, why me (¼–½ page)

- **Timeliness** — why this question is answerable now and was not five years ago (a new
  method, a new dataset, a new theoretical result, your own preliminary finding).
- **Preliminary results**, if you have them. Their function here is to establish
  timeliness, not to prove the project works. The strongest form is a preliminary
  finding that *raises* the project's questions: "our data show A, which prompts two
  questions: does B? and can we C?" — the result creates the project rather than
  pre-empting it.
- **PI expertise** — why you.

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
  consequence but is not the criterion.

The move that works: name the breakthroughs, then say what fields they seed and *why the
findings generalise* beyond your system. "These findings have implications likely
generalisable to … because …" — the *because* is what separates impact from wishful
thinking.

## 8. Part B1 — CV and track record (4 pages)

Same single PDF as the synopsis. The template can be modified if needed. Four pages, and
the outputs and peer-recognition blocks are worth more than half of them:

| Block | Pages |
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

**Research achievements — opening paragraph.** Write a narrative, not a list. Four
elements: your background, what drives your research, a description of your research
focus, and a showcase of your main expertise. This paragraph is where a generalist panel
member forms their model of you.

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

**Peer recognition.** Grants, awards, prizes, honours; invited talks, presentations,
keynotes; scientific evaluation and editorial reviewing; leadership roles.

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

Page budget for the seven pages — editorial in the same way as [§7](#7-part-i-of-the-scientific-proposal-5-pages-in-b1)'s, and the brackets on the
subsection headings are these numbers:

| Section | Pages | Covered in |
|---|---|---|
| Compressed recap: intro, vision, objectives, state of the art | ½ – 1 | this section |
| Project design, with the objectives-to-work-units figure | ¾ | [§9.1](#91-project-design--page-figure-included) |
| Work plan — every work package, task and moonshot | 4½ | [§9.2](#92-work-packages-objective-versus-rationale-4-pages-for-the-whole-work-plan), [§9.3](#93-tasks--page-each-inside-the-work-plan-budget), [§9.4](#94-moonshot-tasks--page-150200-words) |
| Gantt chart | ¼ | [§9.1](#91-project-design--page-figure-included) |
| Risk analysis and concluding remarks | ½ | [§9.5](#95-risk-assessment--page-with-the-gantt-chart-alongside) |

The work plan is four fifths of what is left after the recap, which is the allocation to
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
- **Unjustified budgets are cut, not queried.** The panel assesses the estimate; the
  reduction happens without a conversation.

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
generalists reading only B1, is a strategic decision rather than an administrative one. The
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

**Four things changed recently enough that older advice is actively wrong.**

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
