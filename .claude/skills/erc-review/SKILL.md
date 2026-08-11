---
name: erc-review
description: Review an ERC Starting/Consolidator Grant draft (Part B1/B2) against ERC_writing_guide.md. Works top-down — fundability, then question, then layers, then criteria coverage, then work-plan shape, then prose — and stops at the highest level that is failing. Use when asked to review, critique, improve, or check an ERC proposal draft, or a section of one.
---

# Reviewing an ERC draft

You are reviewing a proposal that a panel will read once, under time pressure, looking for
a reason to stop. Your job is to find the highest-level thing that is wrong and explain what
it costs. The rules live in `ERC_writing_guide.md` in this skill's own repository; cite them
by section number so the author can check you, and read the stage rubrics in its §13.2
before reporting — they carry the cost and suggestion for each check.

**Locating the kit.** The draft is in the working directory; the guide and checker are
wherever this skill was installed from. Resolve them once at the start of a review, in this
order: `./ERC_writing_guide.md`, `../erc-review/`, then
`readlink -f ~/.claude/skills/erc-review` and walk up three levels. Set `ERC` to that
directory and use `$ERC/tools/erc_check.py` throughout.

Two hard constraints. **Never invent** content — no fabricated citations, results, or
claims about the PI's work; when a fix needs knowledge that is not in the draft, the output
is a question, not a drafted sentence. **Never rewrite the argument silently** — see
*Deciding what to do* below.

## Work top-down, and stop

The stages below run from the most expensive mistake to the cheapest. Fixing stage 2
rewrites everything downstream of it, so findings below an open failure are wasted work.

**Report only from the highest stage that has failures.** If stage 2 fails, do not report
stage 6 prose. Add one closing line naming what you deferred and at which stage, so the
author knows the review is not finished rather than clean.

**Budget: at most five findings per report.** More than that is a rewrite the author cannot
review back. If a stage has more, report the five with the largest consequence and say how
many remain.

| # | Stage | Question | Rubric |
|---|---|---|---|
| 0 | Census | What exists at all? | `--census`, below |
| 1 | Fundability | Is this an ERC project rather than an excellent next paper? | guide §1, §13.2 T1 |
| 2 | Problem | Is there a nameable question, with an instability and a cost to *these* readers? | §7.1–7.3 |
| 3 | Layers | Is each passage at its right altitude — vision, aim, objective, work unit, task? | §5, §7.4, §7.5 |
| 4 | Step-1 sufficiency | Can all four Step-1 questions be scored from B1 alone, by a generalist? | §3, §4 |
| 5 | Criteria coverage | Does every evaluation question have an address in the document? | §4, §7.6–7.9 |
| 6 | Work plan | WP objective vs rationale, task shape, moonshots, risk, Gantt | §9 |
| 7 | Argument mechanics | Topic/stress positions, old-before-new, named causality, claim support | §10 |
| 8 | Prose | Fillers, hedges, passive where a human acts, jargon, tics | §10 |
| 9 | Compliance | Pages, placeholders, empty citations, funding table | `erc_check.py` |

Stage 0 is not a report. Run it first and read it as a map:

```
python3 $ERC/tools/erc_check.py --census --pages
```

It prints words per part, which units are still unwritten, how many placeholders remain,
and pages against the limit. Use it to skip stages that cannot be answered yet — a section
that is a `\wzm{}` note has no prose to criticise, and saying so once beats five findings
about absent content. If a part is **at** its page limit, every suggestion you make from
here on must name what it displaces.

Stages 8 and 9 are mechanical. Do not spend reasoning on them:

```
python3 $ERC/tools/erc_check.py --pages        # all findings, triaged BLOCK/SCORE/POLISH
python3 $ERC/tools/erc_check.py --only BLOCK   # just the submission blockers
python3 $ERC/tools/erc_check.py --json         # findings + per-unit structure, parseable
```

Before writing anything, read the `\ercblock`/`\ercscore`/`\ercpolish` comments already in
the draft. Those are open findings from a previous review; do not raise them again, and do
not re-order the author's queue by adding a sixth item on top of five unanswered ones.

## What a finding looks like

Four parts, in this order. The third is what makes a finding actionable rather than
opinionated, and it is the one usually missing.

1. **Where** — `b1.tex:112`, plus a quote short enough to locate the sentence.
2. **What** — the defect in one sentence, naming the rule: *"this is the rationale, not the
   objective (§9.2)"*.
3. **Why it costs** — which evaluation question scores lower, and for which reader. *"A
   Step-1 panel member scoring ground-breaking nature has nothing to point at; they read
   only B1 (§3)."* If you cannot name the reader and the question, the finding is a
   preference — drop it.
4. **What to do** — either a concrete replacement drafted in the author's register, or the
   specific missing content plus where it goes. "Tighten this" is not a suggestion. A
   finding that identifies an absence without saying where it belongs hands the author a
   search problem on top of a writing problem.

When the finding is that a *connection* is missing rather than a sentence being wrong, say
so and stop. That is a hole in the argument, not in the prose, and papering it over with a
transition hides the thing worth fixing. Ask about it instead (§13.2, gap diagnostic).

## Deciding what to do

The split is content versus form, and it follows from who owns the sentence.

**Stages 1–7 — do not edit.** These change what the proposal claims. Report reason and
suggestion, then let the author choose. Offer the three routes explicitly, per finding:

- **draft it** — you write the replacement, the author reviews the diff;
- **mark it** — you insert `\ercscore{9.2}{...}` at the site and move on, leaving a queue;
- **ask it** — the content is in the author's head, not the draft; you ask the question.

Prefer *ask* whenever the fix needs a fact, result, or intention you cannot see. Prefer
*mark* when the author is mid-draft and a diff would collide with what they are writing.

**Stages 8–9 — just fix them,** in the file, and report a count rather than a list. Filler
words, passive constructions with a human agent, placeholders, empty `\citep{}`: these are
safe, reversible, and not the author's voice.

Batch questions. At most three, numbered, each answerable in one sentence, and only the
ones that block the next edit. Everything else goes into the draft as `\ercscore` comments,
which `\listoferccomments` collects into a summary page, so the author answers on their own
schedule.

## Reporting

Drafts and comments go in the `.tex` files. Chat carries the finding list, the reasons, and
the questions — never a pasted rewritten section. Name `file:line` so the author can jump
there. Open with the stage you reached and close with what you deferred:

```
Stage 2 (problem statement) — 3 findings, reported below.
Deferred: stages 3–7 not run; 21 BLOCK / 11 SCORE from the checker, unchanged.
```

A clean stage gets one line, not a paragraph of reassurance. Say which stage passed and
move to the next one in the same report if the budget allows.
