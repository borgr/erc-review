#!/usr/bin/env python3
"""Mechanical checks for an ERC B1/B2 draft, keyed to ERC_writing_guide.md.

Every finding cites the guide section that justifies it, so a comment on the
draft can quote a rule instead of an opinion. Findings are triaged:

  BLOCK   compliance or placeholder — the proposal is not submittable as-is
  SCORE   affects how an evaluation question scores
  POLISH  sentence-level; fix in a word pass

Judgment calls (is the vision actually a vision? is this objective a knowledge
claim?) are deliberately NOT here — the erc-review skill does those, and this
script exists so that it never spends attention on what a regex can settle.

Usage:
    python3 tools/erc_check.py                 # check b1.tex and b2.tex
    python3 tools/erc_check.py b2.tex          # one file
    python3 tools/erc_check.py --pages         # also compile and report pages
    python3 tools/erc_check.py --census        # what exists: units, words, pages
    python3 tools/erc_check.py --json          # machine-readable, for the skill
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import zlib
from collections import Counter
from dataclasses import dataclass

KIT = pathlib.Path(__file__).resolve().parent.parent  # where this script lives
DEFAULT_PARTS = ("b1.tex", "b2.tex")

# ERC-2027-StG / CoG: Information for Applicants v11.0, 22.07.2026. See guide §12.
# b1 = cover page + Part I (5) + CV and Track Record (4); b2 = Part II (7).
# References and Funding ID are outside the limits, so a compiled page count that
# includes a bibliography over-reports — treat an overrun as a prompt to check by hand.
PAGE_LIMITS = {"b1": 10, "b2": 7}
ABSTRACT_CHAR_LIMIT = 2000

# --- patterns -------------------------------------------------------------

PLACEHOLDERS = [
    (r"HERE GOES", "unwritten placeholder text"),
    (r"X{4,}", "XXXX placeholder"),
    (r"DD/MM/YYYY|YYYY\s*--\s*YYYY|YYYY\s*--\s*present", "unfilled date template"),
    (r"Name Surname|Faculty/Department, Institution, Country", "unfilled CV template"),
    (r"%\s*EDIT:", "template EDIT marker still present"),
    (r"\\temp\{", r"\temp{} marker"),
    (r"\bTODO\b|\bFIXME\b", "TODO marker"),
]

# "X is poorly understood" — unscoreable challenge statements. Guide §7.3.
VAGUE_CHALLENGE = [
    r"poorly understood",
    r"not (?:yet )?fully understood",
    r"not well understood",
    r"remains? (?:unclear|elusive|poorly|largely unknown|an open question)",
    r"(?:is|are) unclear",
    r"little is known",
    r"has received (?:limited|little) attention",
    r"despite (?:decades|years) of",
    r"has (?:not )?been (?:widely |extensively )?studied",
]

# Guide §10 (word level). Helper verbs and empty intensifiers.
FILLER = [
    r"\bsimply\b",
    r"\bclearly\b",
    r"\btrivially\b",
    r"\beasily\b",
    r"\bleverage[sd]?\b",
    r"\butiliz(?:e|es|ed|ing)\b",
    r"\bvery\b",
    r"\bextremely\b",
    r"\bquite\b",
    r"\bvarious\b",
    r"\bdifferent aspects\b",
]

# Guide §10. Causal chains hidden behind and/then.
CAUSAL_SMELL = [
    (r"\band then\b", '"and then" — name the causal relation'),
    (r"(?<![.!?])\.\s+Then\b", 'sentence opening with "Then"'),
    (r"\band we will\b.*\band we will\b", 'two "and we will" clauses in one sentence'),
]

# [\w-]+ed rather than \w+ed so hyphenated participles are caught too: a compound like
# "will be re-analysed" or "will be cross-validated" is passive in exactly the same way.
PASSIVE_FUTURE = r"\bwill be (?:[\w-]+ed|measured|shown|performed|conducted|investigated|analysed|analyzed)\b"

# Objectives should be knowledge claims, not deliverables. Guide §7.5.
DELIVERABLE_VERBS = r"^\s*(?:OBJ\s*\d|O\d)[.):]?\s*(?:We will )?(?:Build|Implement|Release|Create|Deliver|Produce|Set up)\b"

BODY_NOTE_MAX_WORDS = 6

# --- model ----------------------------------------------------------------


@dataclass
class Finding:
    severity: str
    code: str
    file: str
    line: int
    message: str
    guide: str

    def __str__(self) -> str:
        return f"{self.file}:{self.line}  [{self.code}] {self.message}  (guide §{self.guide})"


SEV_ORDER = {"BLOCK": 0, "SCORE": 1, "POLISH": 2}


def strip_comments(text: str) -> list[tuple[int, str]]:
    """Return (1-indexed line number, comment-free line) pairs."""
    out = []
    for i, raw in enumerate(text.splitlines(), start=1):
        # A % is a comment unless escaped as \%
        stripped = re.sub(r"(?<!\\)%.*$", "", raw)
        out.append((i, stripped))
    return out


def body_lines(lines: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Lines that render as body text: inside document, not pure macro calls."""
    out, in_doc = [], False
    for n, line in lines:
        if r"\begin{document}" in line:
            in_doc = True
            continue
        if r"\end{document}" in line:
            break
        if not in_doc:
            continue
        bare = line.strip()
        if not bare:
            continue
        # Skip lines that are only a macro invocation or environment delimiter.
        if re.fullmatch(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?(\{[^{}]*\})*\s*", bare):
            continue
        out.append((n, bare))
    return out


def sentences(text: str) -> list[str]:
    text = re.sub(r"\\citep?\[[^\]]*\]\{[^}]*\}|\\cite[tp]?\{[^}]*\}", "", text)
    text = re.sub(r"\\\w+\{([^{}]*)\}", r"\1", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text)
    return [p.strip() for p in parts if len(p.strip()) > 20]


# --- checks ---------------------------------------------------------------


def check_file(path: pathlib.Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    name = path.name
    lines = strip_comments(text)
    body = body_lines(lines)
    f: list[Finding] = []

    def add(sev, code, line, msg, guide):
        f.append(Finding(sev, code, name, line, msg, guide))

    # -- BLOCK: instructions still printed -------------------------------
    for n, line in lines:
        if "showinstructions" in line and not line.strip().startswith("%"):
            add("BLOCK", "instructions-on", n,
                "showinstructions is enabled; ERC boilerplate prints in the PDF", "13.3")

    # -- BLOCK: \wzm revealed --------------------------------------------
    for n, line in lines:
        if re.search(r"\\renewcommand\{\\wzm\}\[1\]\{#1\}", line):
            add("BLOCK", "notes-visible", n,
                r"\wzm is set to reveal; private notes will print", "13.3")

    # -- BLOCK: placeholders ---------------------------------------------
    for n, line in lines:
        for pat, desc in PLACEHOLDERS:
            if re.search(pat, line):
                add("BLOCK", "placeholder", n, desc, "13.3")

    # -- BLOCK: empty or missing citations / refs -------------------------
    for n, line in lines:
        for m in re.finditer(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{\s*\}", line):
            add("BLOCK", "empty-cite", n, "empty citation — claim has no support", "7.3")
        for m in re.finditer(r"\\(?:ref|autoref|eqref)\{\s*\}", line):
            add("BLOCK", "empty-ref", n, "empty cross-reference", "13.3")

    # -- BLOCK: empty funding table ---------------------------------------
    if re.search(r"\\begin\{fundingtable\}\s*(?:&\s*)*\\\\\s*\\hline\s*(?:&\s*)*\\\\\s*\\end", text, re.S):
        n = text[: text.index("fundingtable")].count("\n") + 1
        add("BLOCK", "funding-blank", n,
            'funding table is blank — needs entries or "No funding"/"None"', "13.3")

    # -- BLOCK: abstract length -------------------------------------------
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    if m:
        inner = re.sub(r"(?<!\\)%.*", "", m.group(1))
        inner = re.sub(r"\\wzm\{.*?\}", "", inner, flags=re.S)
        inner = re.sub(r"\\\w+\{?|\}", "", inner)
        chars = len(inner.strip())
        n = text[: m.start()].count("\n") + 1
        if chars > ABSTRACT_CHAR_LIMIT:
            add("BLOCK", "abstract-long", n,
                f"abstract is {chars} chars, limit {ABSTRACT_CHAR_LIMIT}", "6")
        elif chars < 400:
            add("SCORE", "abstract-thin", n,
                f"abstract is only {chars} chars of a {ABSTRACT_CHAR_LIMIT}-char budget", "6")

    # -- SCORE: vague challenge statements --------------------------------
    for n, line in body:
        for pat in VAGUE_CHALLENGE:
            m = re.search(pat, line, re.I)
            if m:
                add("SCORE", "vague-challenge", n,
                    f'"{m.group(0)}" — say what specifically is unknown and why', "7.3")

    # -- SCORE: objectives phrased as deliverables ------------------------
    for n, line in body:
        if re.search(DELIVERABLE_VERBS, line):
            add("SCORE", "objective-deliverable", n,
                "objective opens with a build/deliver verb, not a knowledge verb", "7.5")

    # -- SCORE: stray note fragments in body text -------------------------
    for n, line in body:
        if line.startswith("\\") or line.endswith(("{", "}")):
            continue
        # Table rows and line-broken lists are not note fragments, and neither
        # are CV entries, which are legitimately short and unpunctuated.
        if "&" in line or line.endswith("\\\\"):
            continue
        if ":" in line or re.search(r"\b(?:19|20)\d\d\b", line):
            continue
        # A planning note never cites, and a citation command is a single long
        # token that makes a full prose line look like a three-word fragment.
        if re.search(r"\\(?:cite|citep|citet|citealp|citeauthor|autocite)\b", line):
            continue
        words = line.split()
        if len(words) <= BODY_NOTE_MAX_WORDS and not re.search(r"[.!?:]$", line):
            add("SCORE", "stray-note", n,
                f'note fragment renders as body text: "{line[:48]}"', "13.3")

    # -- SCORE: causal chains ---------------------------------------------
    for n, line in body:
        for pat, desc in CAUSAL_SMELL:
            if re.search(pat, line, re.I):
                add("SCORE", "causality", n, desc, "10")

    # -- POLISH: passive future -------------------------------------------
    for n, line in body:
        for m in re.finditer(PASSIVE_FUTURE, line, re.I):
            add("POLISH", "passive", n, f'"{m.group(0)}" — use active voice', "10")

    # -- POLISH: filler ---------------------------------------------------
    for n, line in body:
        for pat in FILLER:
            m = re.search(pat, line, re.I)
            if m:
                add("POLISH", "filler", n, f'filler: "{m.group(0)}"', "10")

    return f


def structure_units(path: pathlib.Path) -> list[dict]:
    """Every heading with its length and any shape flag. Guide §9.3, §9.4."""
    text = path.read_text(encoding="utf-8", errors="replace")
    text = re.sub(r"(?<!\\)%.*", "", text)
    out = []
    units = re.split(r"\\(?:sub)*section\*?\{|\\paragraph\{", text)
    heads = re.findall(r"\\((?:sub)*section)\*?\{([^}]*)\}|\\(paragraph)\{([^}]*)\}", text)
    kinds = [k1 or k2 for k1, _, k2, _ in heads]
    for i, ((kind1, title1, kind2, title2), chunk) in enumerate(zip(heads, units[1:])):
        kind = kind1 or kind2
        title = (title1 or title2).strip()
        chunk = chunk.split("}", 1)[-1] if chunk.startswith(title) else chunk
        sents = sentences(chunk)
        words = len(chunk.split())
        # A chunk running to a *higher*-level heading has absorbed the unit's
        # closing prose, so its length says nothing about the task itself.
        clean_tail = i + 1 < len(kinds) and kinds[i + 1] == "paragraph"
        note = ""
        if words == 0:
            note = "unwritten"
        elif kind == "paragraph":
            is_moonshot = "moonshot" in title.lower()
            if is_moonshot and words > 260:
                note = "moonshot over ~200 words (guide §9.4)"
            elif not is_moonshot and len(sents) < 6:
                note = "task under purpose+approach+contribution length (guide §9.3)"
            elif not is_moonshot and len(sents) > 14 and clean_tail:
                note = "task longer than 4-8 approach sentences implies (guide §9.3)"
        out.append({"file": path.name, "kind": kind, "title": title,
                    "words": words, "sentences": len(sents), "flag": note})
    return out


def structure_report(path: pathlib.Path) -> list[str]:
    return [
        f"  {u['kind']:<12} {u['title'][:52]:<54} {u['words']:>5}w {u['sentences']:>3}s"
        + (f"  <- {u['flag']}" if u["flag"] else "")
        for u in structure_units(path)
    ]


def page_counts(tex: pathlib.Path) -> int | None:
    if not _which("tectonic"):
        return None
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run(
            ["tectonic", "-X", "compile", str(tex), "--outdir", tmp, "--keep-logs"],
            capture_output=True, cwd=tex.parent,
        )
        pdf = pathlib.Path(tmp) / (tex.stem + ".pdf")
        if not pdf.exists():
            return None
        data = pdf.read_bytes()
        total = 0
        for m in re.finditer(rb"stream\r?\n", data):
            s = m.end()
            e = data.find(b"endstream", s)
            try:
                raw = zlib.decompress(data[s:e])
            except Exception:
                continue
            total += len(re.findall(rb"/Type\s*/Page\b(?![s])", raw))
        return total or None


def _which(prog: str) -> bool:
    return subprocess.run(["which", prog], capture_output=True).returncode == 0


def resolve_targets(names: list[str]) -> list[pathlib.Path]:
    """Files to check: those named, else b1.tex/b2.tex beside the draft.

    The draft is wherever you invoke this from, not wherever the script lives —
    the checker is meant to be cloned once and pointed at any proposal.
    """
    if names:
        out = []
        for n in names:
            a = pathlib.Path(n)
            if a.is_dir():
                out += [a / p for p in DEFAULT_PARTS if (a / p).exists()]
            elif a.exists():
                out.append(a)
            else:
                print(f"missing: {a}", file=sys.stderr)
        return out
    for base in (pathlib.Path.cwd(), KIT):
        found = [base / p for p in DEFAULT_PARTS if (base / p).exists()]
        if found:
            return found
    return []


def census(targets: list[pathlib.Path], want_pages: bool) -> dict:
    """What exists, before asking whether it is any good.

    A review that opens with prose findings on a section that is a placeholder
    wastes the author's attention, so the skill reads this first.
    """
    out: dict = {"parts": {}}
    for t in targets:
        units = structure_units(t)
        written = [u for u in units if u["words"] > 0]
        out["parts"][t.name] = {
            "units": len(units),
            "unwritten": [u["title"] for u in units if u["words"] == 0],
            "words": sum(u["words"] for u in units),
            "pages": page_counts(t) if want_pages else None,
            "page_limit": PAGE_LIMITS.get(t.stem),
            "placeholders": sum(
                1 for f in check_file(t) if f.code in ("placeholder", "abstract-thin")
            ),
            "shape_flags": [
                {"title": u["title"], "flag": u["flag"]} for u in written if u["flag"]
            ],
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", default=None)
    ap.add_argument("--pages", action="store_true", help="compile and report page counts")
    ap.add_argument("--only", choices=["BLOCK", "SCORE", "POLISH"])
    ap.add_argument("--census", action="store_true",
                    help="what exists: units, unwritten sections, words, pages")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    targets = resolve_targets(args.files)
    if not targets:
        print("no b1.tex / b2.tex found — run from the draft directory, or name the files",
              file=sys.stderr)
        return 2

    if args.census:
        data = census(targets, args.pages)
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
            return 0
        for name, p in data["parts"].items():
            pg = "" if p["pages"] is None else f", {p['pages']} of {p['page_limit']} pages"
            print(f"{name}: {p['words']} words in {p['units']} units{pg}")
            if p["unwritten"]:
                print(f"  unwritten ({len(p['unwritten'])}): "
                      + "; ".join(p["unwritten"][:8]))
            if p["placeholders"]:
                print(f"  placeholder text in {p['placeholders']} place(s)")
            for s in p["shape_flags"]:
                print(f"  {s['title'][:48]:<50} {s['flag']}")
        return 0

    findings: list[Finding] = []
    for t in targets:
        findings += check_file(t)

    if args.only:
        findings = [f for f in findings if f.severity == args.only]
    findings.sort(key=lambda f: (SEV_ORDER[f.severity], f.file, f.line))

    counts = Counter(f.severity for f in findings)

    if args.json:
        print(json.dumps({
            "findings": [vars(f) for f in findings],
            "structure": [u for t in targets for u in structure_units(t)],
            "counts": dict(counts),
        }, indent=2, ensure_ascii=False))
        return 1 if counts["BLOCK"] else 0

    for sev in ("BLOCK", "SCORE", "POLISH"):
        group = [f for f in findings if f.severity == sev]
        if not group:
            continue
        print(f"\n=== {sev} ({len(group)}) ===")
        for f in group:
            print(" ", f)

    print("\n=== STRUCTURE ===")
    for t in targets:
        print(f" {t.name}")
        for line in structure_report(t):
            print(line)

    if args.pages:
        print("\n=== PAGES ===")
        for t in targets:
            n = page_counts(t)
            limit = PAGE_LIMITS.get(t.stem)
            if n is None:
                print(f"  {t.name}: could not compile")
            else:
                flag = ("" if limit is None or n <= limit
                        else "  <- OVER LIMIT (references excluded from the limit;"
                             " check by hand)")
                print(f"  {t.name}: {n} pages"
                      + (f" of {limit} allowed{flag}" if limit else ""))

    print(f"\n{counts['BLOCK']} block, {counts['SCORE']} score, {counts['POLISH']} polish")
    return 1 if counts["BLOCK"] else 0


if __name__ == "__main__":
    sys.exit(main())
