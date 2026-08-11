# erc-review

A reviewing kit for ERC Starting and Consolidator Grant proposals: a guide to what the
panel is actually scoring, a review protocol that works top-down and stops at the highest
level that is failing, and two tools that execute it — one for a person, one for an agent.

It exists because reviewing a grant draft usually goes wrong in the same way. You open the
file, start at page 1, and fix sentences. Four hours later the prose is better and the
proposal still is not fundable, because the problem was that the scientific question was
never nameable and no amount of sentence work reaches that.

## What is here

| | |
|---|---|
| [`ERC_writing_guide.md`](ERC_writing_guide.md) | The rules. §1–12 are what the call and the panel want; §13 is the review protocol. |
| [`.claude/skills/erc-review/SKILL.md`](.claude/skills/erc-review/SKILL.md) | A [Claude Code](https://claude.com/claude-code) skill that runs the judgment stages of §13 against a draft. |
| [`tools/erc_check.py`](tools/erc_check.py) | Settles everything a regex can settle, so neither you nor an agent spends attention there. No dependencies. |
| [`ercreview.sty`](ercreview.sty) | Margin-note macros for leaving findings in the draft, keyed to guide sections. |
| [`example/`](example/) | A deliberately flawed skeleton, so the checker has something to find. |

## The protocol

Ten stages, most expensive mistake first:

```
0  census          what exists at all?
1  fundability     an ERC project, or an excellent next paper?
2  problem         a nameable question, with an instability and a cost?
3  layers          is each passage at its right altitude?
4  step-1          can B1 alone be scored? (the Step-1 panel never sees B2)
5  criteria        does every evaluation question have an address?
6  work plan       are work units and tasks correctly typed and bounded?
7  mechanics       do the sentences carry the argument's joints?
8  prose           fillers, hedges, voice, jargon
9  compliance      pages, placeholders, citations, funding table
```

Fixing an early stage rewrites everything downstream of it, so **report only from the
highest stage that has failures** and say what you deferred. Stages 8 and 9 are mechanical;
`erc_check.py` does them. Stages 1–7 are judgment, and each rubric item in guide §13.2
carries three fields — a *test*, the *cost* if it fails (which evaluation question, and for
which reader), and what to *suggest*. The cost field is the point: a finding that cannot
name the question it costs you is a preference, and should be dropped.

## Using the checker

No dependencies beyond Python 3.9+. Run it from the directory holding your `b1.tex` and
`b2.tex`; page counting additionally needs [`tectonic`](https://tectonic-typesetting.github.io)
or any engine you point it at.

```
git clone https://github.com/borgr/erc-review.git
ERC=$(pwd)/erc-review

cd path/to/your/proposal
python3 $ERC/tools/erc_check.py --census --pages   # stage 0: what exists
python3 $ERC/tools/erc_check.py --pages            # everything, with page counts
python3 $ERC/tools/erc_check.py --only BLOCK       # just the submission blockers
python3 $ERC/tools/erc_check.py --json             # for an agent to parse
```

Findings print as `file:line [code] message (guide §)` and are triaged **BLOCK** (not
submittable), **SCORE** (costs points on a named evaluation question), **POLISH** (costs
goodwill). It also reports every section and task with word and sentence counts, flagging
tasks too short to carry purpose–approach–contribution and moonshots over ~200 words.

Try it on the example first:

```
python3 tools/erc_check.py example/
```

## Using the skill

Install it where Claude Code looks for skills, then ask for a review from your draft
directory:

```
ln -s "$ERC/.claude/skills/erc-review" ~/.claude/skills/erc-review
```

The skill reports at most five findings at a time, each as *where* → *what* → *why it
costs* → *what to do*, and offers three routes per finding: draft the replacement, mark it
in the file with `\ercscore{§}{...}`, or ask you the question — the last whenever the fix
needs a fact that is not in the draft. It edits stages 8–9 directly and reports a count;
it never silently rewrites an argument.

## Leaving findings in the draft

```latex
\usepackage{ercreview}          % after todonotes, if you use it
...
\ercblock{13.3}{funding table still blank}
\ercscore{9.2}{this is the rationale, not the objective -- the objective is missing}
\ercpolish{10}{"and then" hides the causal step}
...
\listoferccomments               % summary page of every open finding
```

`\usepackage[off]{ercreview}` drops all of them for the submission build.

## Caveats

**Verify the numbers against your own call.** Everything here was checked on 11 August 2026
against the *Information for Applicants to the Starting and Consolidator Grant 2027 Calls*
(v11.0) and the *ERC Work Programme 2027*, and guide §12 records that plus the four things
that changed recently enough that older advice is actively wrong — Part II went from 14
pages to 7, feasibility left the Step-1 assessment, novel methodology stopped being a
scoring clause, and the eligibility windows widened to 0–10 and 5–15 years post-PhD. The ERC
reissues both documents each July. The authority is the pair for **your** call, not this
repository.

**This is one reading of one seminar plus the official forms.** Guide §13's ordering claim —
that fixing framing before prose is strictly better — is an editorial position, not an ERC
policy. Corrections and disagreements are welcome as issues.

**No worked examples from real proposals.** The seminar deck this draws on contains
examples from active ERC projects under an explicit no-redistribution restriction. Those
are excluded; every illustration here is written fresh. See the guide's Provenance section
for the sources and their terms.

## Licence

Code (`tools/`, `ercreview.sty`, `example/`): MIT. Prose (`ERC_writing_guide.md`,
`SKILL.md`, this README): CC BY 4.0. See [LICENSE](LICENSE).
