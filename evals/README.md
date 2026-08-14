# Evaluations

Three scenarios that check the `erc-review` skill does the thing that makes it worth having:
**reports from the highest failing stage and stops**, rather than producing a flat list of
whatever it noticed. There is no runner — Claude Code has no built-in eval harness, and
these are written to be run by hand or fed to a judge.

Each `*.json` follows the structure in Anthropic's
[skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#build-evaluations-first):
a query, the files it runs against, and the behaviour a pass requires. `expected_behavior`
entries are graded independently; a scenario passes only if all of them hold. `failure_modes`
is an addition of ours, not part of that structure: it names the wrong answers that look
right, which is what a human judge needs and a schema does not carry.

## Running one by hand

```sh
cd evals/fixtures/<scenario>
claude "<the scenario's query>"
```

Then read the transcript against `expected_behavior`. What to watch for, in order of how
often it goes wrong:

1. **Did it stop?** The whole design claim is that findings below an open failure are wasted
   work. A report that names a stage-2 failure *and* lists passive-voice fixes has not
   followed the skill, even if every individual finding is correct.
2. **Does every finding name a cost?** A finding without an evaluation question and a reader
   is a preference. This is the field the skill says is usually missing, so it is the field
   to check.
3. **Did it invent anything?** No fabricated citations, results, or claims about the PI.
   Where a fix needs a fact that is not in the draft, the output must be a question.
4. **Did it edit above stage 8?** Stages 1–7 are reported, never silently rewritten.

## The scenarios

| File | Fixture | Tests |
|---|---|---|
| `01-stops-at-highest-failure.json` | `fixtures/vague-question/` | The stop rule. The draft has a stage-2 failure *and* abundant stage-7/8 bait; a pass reports stage 2 only and defers the rest by name. |
| `02-costs-are-named.json` | `fixtures/parked-in-b2/` | The cost field, and Step-1 sufficiency. Content the Step-1 panel needs sits in B2, where it scores zero; a pass names that reader and that consequence. |
| `03-asks-rather-than-invents.json` | `fixtures/missing-why-now/` | The no-invention rule. The why-now argument needs a fact only the PI has; a pass asks for it instead of drafting a plausible one. |

`fixtures/` are deliberately flawed skeletons, like `example/`. They are not model proposals
and should not be read as templates.
