#!/usr/bin/env python3
"""Refresh guide traceability fields in the published Bitcoin lexicon.

The guide columns record links from lines containing a listed term or alias to
the matching section in the Student Guide or Educator Guide.
Run with --check to print an audit or --patch to emit an apply_patch patch.
"""

from __future__ import annotations

import argparse
import difflib
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEXICON = ROOT / "publish/mfb-lx-26.10.md"
TERMS = ROOT / "publish/mfb-lx-26.10-terms.md"
STUDENT_GUIDE = ROOT / "publish/mfb-bd-26.10/mfb-bd-sg-26.10.md"
EDUCATOR_GUIDE = ROOT / "publish/mfb-bd-26.10/mfb-bd-eg-26.10.md"

ROW_RE = re.compile(r'^\| (.*?) \| (.*?) \| <a id="([^"]+)"></a>(.*?) \| (.*?) \|$')
EDUCATOR_ROW_RE = re.compile(r'^\| (.*?) \| (.*?) \| \[(.*?)\]\(#([^)]+)\) \| (.*?) \|$')
TERMS_ROW_RE = re.compile(r"^\| (BD-LEX-\d+) \| (.*?) \| ")
LEXICON_LINK_RE = re.compile(
    r"\]\((?:\.\./mfb-lx-26\.10\.md#)?(term-[^)\s]+|BD-LEX-\d+|[a-z0-9]+(?:-[a-z0-9]+)*)\)"
)

# Aliases that cannot be recovered reliably from display punctuation alone.
EXTRA_ALIASES = {
    "term-barter": ["bartering"],
    "term-cbdc": ["central bank digital currency", "central bank digital currencies"],
    "term-no-kyc": ["non-KYC", "no KYC", "non KYC"],
    "term-proof-of-work": ["proof-of-work"],
    "term-reusable-proof-of-work": ["RPoW"],
    "reusable-proof-of-work": ["RPoW"],
    "term-sat": ["sats", "satoshis"],
    "term-seed-phrase": ["recovery words"],
    "term-transaction-id": ["txids"],
}

# These lexicon labels use a source-term alias or a source definition rather
# than the exact canonical term label in mfb-lx-26.10-terms.md.
LEX_ID_OVERRIDES = {
    "term-sat": "BD-LEX-192",
    "term-inflation": "BD-LEX-119",
    "term-cbdc": "BD-LEX-051",
    "term-transaction-id": "BD-LEX-220",
    "term-kyc": "BD-LEX-125",
    "term-no-kyc": "BD-LEX-158",
}

# Some terms are deliberately nested under a parent entry in the terms file.
# They share the parent's ID rather than receiving a separate ID.
NESTED_TERM_IDS = {
    "basket of goods": "BD-LEX-120",
    "bitcoin privacy": "BD-LEX-179",
    "deposit money": "BD-LEX-012",
    "double-spend problem": "BD-LEX-083",
    "mining": "BD-LEX-182",
    "monetary expansion": "BD-LEX-149",
    "price inflation": "BD-LEX-119",
    "satoshis per byte (sat/b)": "BD-LEX-094",
    "timechain": "BD-LEX-041",
    "trustless": "BD-LEX-222",
    "validating node": "BD-LEX-099",
}

# These common words only count in their curriculum-specific sense.
CONTEXT_RE = {
    "term-capital": re.compile(
        r"(?:\bbank(?:ing)?\b.{0,100}\bcapital\b|\bcapital\b.{0,100}\b(?:rules?|loss|funding|earnings|requirements?)\b)",
        re.I,
    ),
    "term-issuer": re.compile(
        r"\b(?:bitcoin|money|monetary|currency|currencies|asset|assets|stablecoin|cbdc|bank|supply|digital)\b",
        re.I,
    ),
    "term-liquid": re.compile(r"\bLiquid\b"),
    "term-target": re.compile(r"\b(hash|proof|work|difficult|threshold|miner)", re.I),
    "term-verification": re.compile(
        r"\b(?:node|nodes|transaction|transactions|block|blocks|ledger|double spending|proof of work|block explorer)\b",
        re.I,
    ),
}

PRIVACY_ATTRIBUTIVE = re.compile(
    r"\bprivacy(?:\s+(?:and\s+)?(?:risk|risks|boundary|boundaries|trade-off|trade-offs|"
    r"consideration|considerations|practice|practices|tool|tools|feature|features|policy|policies)\b|"
    r"\s*,[^.;:]*\b(?:risks|boundaries|trade-offs)\b)",
    re.I,
)


def strip_markdown(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("**", "").replace("*", "").replace("`", "")
    value = value.replace("“", "").replace("”", "").replace('"', "")
    return re.sub(r"\s+", " ", value).strip()


def normalized_term(value: str) -> str:
    return re.sub(r"\s+", " ", strip_markdown(value)).casefold()


def lex_ids(entries: list[dict[str, str]]) -> dict[str, str]:
    """Map each published lexicon anchor to its authoritative BD-LEX-ID."""
    terms_by_name = {}
    for line in source_lines(TERMS):
        match = TERMS_ROW_RE.match(line)
        if match:
            lex_id, term = match.groups()
            terms_by_name[normalized_term(term)] = lex_id

    ids = {}
    for entry in entries:
        anchor = entry["anchor"]
        nested_id = NESTED_TERM_IDS.get(normalized_term(entry["term"]))
        if nested_id:
            ids[anchor] = nested_id
            continue
        if anchor in LEX_ID_OVERRIDES:
            ids[anchor] = LEX_ID_OVERRIDES[anchor]
            continue
        matches = {
            terms_by_name[normalized_term(alias)]
            for alias in singular_aliases(entry["term"], anchor)
            if normalized_term(alias) in terms_by_name
        }
        if len(matches) != 1:
            raise ValueError(f"Could not determine one LEX-ID for {anchor}: {sorted(matches)}")
        ids[anchor] = matches.pop()
    return ids


def lex_slugs() -> dict[str, str]:
    """Map each published lexicon slug to its authoritative BD-LEX-ID."""
    slugs = {}
    for line in source_lines(TERMS):
        columns = [column.strip() for column in line.split("|")]
        if len(columns) >= 6 and re.fullmatch(r"BD-LEX-\d+", columns[1]):
            slugs[columns[4]] = columns[1]
    return slugs


def singular_aliases(term_cell: str, anchor: str) -> list[str]:
    plain = strip_markdown(term_cell)
    candidates = [plain]

    # Slash-separated display aliases.
    candidates.extend(part.strip() for part in re.split(r"\s+/\s+", plain))

    # Parenthetical abbreviations or alternate names, plus the base phrase.
    for candidate in list(candidates):
        for inner in re.findall(r"\(([^)]+)\)", candidate):
            if ";" not in inner and len(inner.split()) <= 5:
                candidates.append(inner.strip())
        candidates.append(re.sub(r"\s*\([^)]*\)", "", candidate).strip())

    # Explicitly formatted aliases, such as *txid* or **non-KYC**.
    candidates.extend(re.findall(r"\*{1,2}([^*]+?)\*{1,2}", term_cell))
    candidates.extend(EXTRA_ALIASES.get(anchor, []))

    cleaned = []
    for candidate in candidates:
        candidate = strip_markdown(candidate)
        candidate = re.sub(r"^(?:preferred;\s*also called|also called)\s+", "", candidate, flags=re.I)
        candidate = re.sub(r"\s+(?:preferred;\s*also called|also called)\s+.*$", "", candidate, flags=re.I)
        candidate = candidate.strip(" :;,.-")
        if candidate and candidate.lower() not in {item.lower() for item in cleaned}:
            cleaned.append(candidate)
    return cleaned


def pluralize(alias: str) -> list[str]:
    if len(alias) < 3 or re.fullmatch(r"[A-Z0-9]+", alias):
        return []
    words = alias.split()
    last = words[-1]
    if last.lower().endswith(("s", "x", "z", "ch", "sh")):
        plural = last + "es"
    elif last.lower().endswith("y") and len(last) > 1 and last[-2].lower() not in "aeiou":
        plural = last[:-1] + "ies"
    else:
        plural = last + "s"
    return [" ".join(words[:-1] + [plural])]


def alias_pattern(alias: str) -> re.Pattern[str]:
    escaped = re.escape(alias)
    escaped = escaped.replace(r"\-", r"[\s\-‐‑‒–—]+")
    escaped = escaped.replace(r"\ ", r"[\s\-‐‑‒–—]+")
    return re.compile(rf"(?<![\w-]){escaped}(?![\w-])", re.I)


def source_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def searchable_lines(lines: list[str]) -> list[str]:
    output = []
    in_comment = False
    for line in lines:
        if "<!--" in line:
            in_comment = True
        if in_comment:
            output.append("")
        else:
            # Retain Markdown link labels but remove destinations, where anchor
            # names and filenames could create false term matches.
            output.append(re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", line))
        if "-->" in line:
            in_comment = False
    return output


def student_occurrences(entries: list[dict[str, str]], lines: list[str]) -> dict[str, list[int]]:
    aliases: dict[str, list[tuple[str, re.Pattern[str]]]] = {}
    for entry in entries:
        values = singular_aliases(entry["term"], entry["anchor"])
        for value in list(values):
            values.extend(pluralize(value))
        deduped = []
        seen = set()
        for value in values:
            key = value.casefold()
            if key not in seen:
                seen.add(key)
                deduped.append((value, alias_pattern(value)))
        aliases[entry["anchor"]] = deduped

    found: dict[str, list[int]] = defaultdict(list)
    for line_number, line in enumerate(searchable_lines(lines), 1):
        candidates = []
        for entry in entries:
            anchor = entry["anchor"]
            context = CONTEXT_RE.get(anchor)
            if context and not context.search(line):
                continue
            for alias, pattern in aliases[anchor]:
                for match in pattern.finditer(line):
                    if anchor == "term-privacy" and PRIVACY_ATTRIBUTIVE.match(line, match.start()):
                        continue
                    candidates.append((match.start(), match.end(), len(match.group()), anchor, alias))

        # Prefer longer listed phrases when terms overlap on the same source text.
        occupied: list[tuple[int, int]] = []
        accepted: set[str] = set()
        for start, end, length, anchor, alias in sorted(candidates, key=lambda item: (-item[2], item[0])):
            if any(start < used_end and end > used_start for used_start, used_end in occupied):
                continue
            occupied.append((start, end))
            accepted.add(anchor)
        for anchor in accepted:
            found[anchor].append(line_number)
    return found


def github_slug(heading: str, used: dict[str, int]) -> str:
    heading = re.sub(r"^#{1,6}\s+", "", heading)
    heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
    heading = heading.replace("`", "").replace("*", "").replace("_", "")
    heading = heading.lower()
    # GitHub removes punctuation before replacing each whitespace character.
    heading = "".join(char for char in heading if char.isalnum() or char in "- \t")
    base = re.sub(r"\s", "-", heading.strip())
    occurrence = used[base]
    used[base] += 1
    return base if occurrence == 0 else f"{base}-{occurrence}"


def educator_links(
    lines: list[str], link_target_to_anchor: dict[str, str]
) -> tuple[dict[str, list[int]], dict[int, str]]:
    links: dict[str, list[int]] = defaultdict(list)
    section_at_line: dict[int, str] = {}
    used: dict[str, int] = defaultdict(int)
    current_section = ""
    for line_number, line in enumerate(lines, 1):
        if re.match(r"^#{1,6}\s+", line):
            current_section = github_slug(line, used)
        section_at_line[line_number] = current_section
        for link_target in LEXICON_LINK_RE.findall(line):
            anchor = link_target_to_anchor.get(link_target)
            if anchor:
                links[anchor].append(line_number)
    return links, section_at_line


def section_anchors(lines: list[str]) -> dict[int, str]:
    """Return the containing GitHub-style heading anchor for every source line."""
    section_at_line: dict[int, str] = {}
    used: dict[str, int] = defaultdict(int)
    current_section = ""
    for line_number, line in enumerate(lines, 1):
        if re.match(r"^#{1,6}\s+", line):
            current_section = github_slug(line, used)
        section_at_line[line_number] = current_section
    return section_at_line


def format_student_rows(
    lines: list[int], section_at_line: dict[int, str], old_values: list[str]
) -> list[str]:
    if lines:
        return [
            f"[{line}](mfb-bd-26.10/mfb-bd-sg-26.10.md#{section_at_line[line]})"
            for line in dict.fromkeys(lines)
        ]
    if any(value.startswith("**Outdated:") for value in old_values):
        return ["**Outdated:** no match in current Student Guide"]
    return ["Not present"]


def format_educator_rows(
    lines: list[int], section_at_line: dict[int, str], old_values: list[str]
) -> list[str]:
    if lines:
        return [
            f"[{line}](mfb-bd-26.10/mfb-bd-eg-26.10.md#{section_at_line[line]})"
            for line in dict.fromkeys(lines)
        ]
    return []


def line_reference_number(value: str) -> int:
    """Extract a source-line number from a Markdown traceability link."""
    match = re.match(r"\[(\d+)\]", value)
    if not match:
        return float("inf")
    return int(match.group(1))


def rebuild() -> tuple[str, dict[str, object]]:
    lexicon_text = LEXICON.read_text(encoding="utf-8")
    lexicon_lines = lexicon_text.splitlines()
    student_header = "| Student Guide line(s) | LEX-ID | Word or phrase | Beginner definition |"
    educator_header = "| Educator Guide Guide Line | LEX-ID | Word or phrase | Beginner definition |"
    student_header_index = lexicon_lines.index(student_header)
    educator_header_index = lexicon_lines.index(educator_header)
    entries_by_anchor = {}
    educator_values: dict[str, list[str]] = defaultdict(list)
    student_order = []
    educator_order = []
    for line_number, line in enumerate(lexicon_lines, 1):
        match = ROW_RE.match(line)
        if match:
            student, lex_id, anchor, term, definition = match.groups()
            if anchor not in entries_by_anchor:
                entries_by_anchor[anchor] = {
                    "line_number": line_number,
                    "anchor": anchor,
                    "term": term,
                    "lex_id": lex_id,
                    "definition": definition,
                    "student_values": [],
                }
                student_order.append(anchor)
            entries_by_anchor[anchor]["student_values"].append(student)
        educator_match = EDUCATOR_ROW_RE.match(line)
        if educator_match:
            educator, lex_id, term, anchor, definition = educator_match.groups()
            if anchor not in entries_by_anchor:
                entries_by_anchor[anchor] = {
                    "line_number": line_number,
                    "anchor": anchor,
                    "term": term,
                    "lex_id": lex_id,
                    "definition": definition,
                    "student_values": [],
                }
            if anchor not in educator_order:
                educator_order.append(anchor)
            educator_values[anchor].append(educator)

    ordered_anchors = student_order + [
        anchor for anchor in educator_order if anchor not in entries_by_anchor or anchor not in student_order
    ]
    entries = [entries_by_anchor[anchor] for anchor in ordered_anchors]
    authoritative_lex_ids = lex_ids(entries)
    for entry in entries:
        entry["lex_id"] = authoritative_lex_ids[entry["anchor"]]
    student_lines = source_lines(STUDENT_GUIDE)
    educator_lines = source_lines(EDUCATOR_GUIDE)
    student_found = student_occurrences(entries, student_lines)
    student_section_at_line = section_anchors(student_lines)
    lex_id_to_anchor = {entry["lex_id"]: entry["anchor"] for entry in entries}
    link_target_to_anchor = {entry["anchor"]: entry["anchor"] for entry in entries}
    link_target_to_anchor.update(lex_id_to_anchor)
    link_target_to_anchor.update(
        {
            slug: lex_id_to_anchor[lex_id]
            for slug, lex_id in lex_slugs().items()
            if lex_id in lex_id_to_anchor
        }
    )
    educator_found, section_at_line = educator_links(educator_lines, link_target_to_anchor)

    outdated_student = []
    outdated_educator = []
    newly_present_student = []
    student_rows_to_sort: list[tuple[int, str]] = []
    educator_rows_to_sort: list[tuple[int, str]] = []
    tagged_lex_ids: set[str] = set()
    for entry in entries:
        lex_id_tag = ""
        if entry["lex_id"] not in tagged_lex_ids:
            lex_id_tag = f'<a id="{entry["lex_id"]}"></a>'
            tagged_lex_ids.add(entry["lex_id"])
        student_rows = format_student_rows(
            student_found[entry["anchor"]], student_section_at_line, entry["student_values"]
        )
        educator_rows = format_educator_rows(
            educator_found[entry["anchor"]], section_at_line, educator_values[entry["anchor"]]
        )
        for student in student_rows:
            student_rows_to_sort.append(
                (
                    line_reference_number(student),
                    f'| {student} | {lex_id_tag}{entry["lex_id"]} | '
                    f'<a id="{entry["anchor"]}"></a>{entry["term"]} | {entry["definition"]} |',
                )
            )
            lex_id_tag = ""
        for educator in educator_rows:
            educator_rows_to_sort.append(
                (
                    line_reference_number(educator),
                    f'| {educator} | {lex_id_tag}{entry["lex_id"]} | '
                    f'[{entry["term"]}](#{entry["anchor"]}) | {entry["definition"]} |',
                )
            )
            lex_id_tag = ""
        if student_rows and student_rows[0].startswith("**Outdated:"):
            outdated_student.append(entry["anchor"])
        if not entry["student_values"] and student_found[entry["anchor"]]:
            newly_present_student.append(entry["anchor"])
        if educator_rows and educator_rows[0].startswith("**Outdated:"):
            outdated_educator.append(entry["anchor"])

    student_table = [student_header, "| --- | --- | --- | --- |"] + [
        row for _, row in sorted(student_rows_to_sort)
    ]
    educator_table = [educator_header, "| --- | --- | --- | --- |"] + [
        row for _, row in sorted(educator_rows_to_sort)
    ]

    student_end = student_header_index + 2
    while student_end < len(lexicon_lines) and ROW_RE.match(lexicon_lines[student_end]):
        student_end += 1
    educator_end = educator_header_index + 2
    while educator_end < len(lexicon_lines) and EDUCATOR_ROW_RE.match(lexicon_lines[educator_end]):
        educator_end += 1
    rebuilt_lines = (
        lexicon_lines[:student_header_index]
        + student_table
        + lexicon_lines[student_end:educator_header_index]
        + educator_table
        + lexicon_lines[educator_end:]
    )

    dashboard_values = {
        "Lexicon entries": len(entries),
        "Student Guide (SG) references": sum(len(LEXICON_LINK_RE.findall(line)) for line in student_lines),
        "Student Guide term entries found": sum(bool(student_found[entry["anchor"]]) for entry in entries),
        "Outdated Student Guide traces": len(outdated_student),
        "Educator Guide (EG) references": sum(len(items) for items in educator_found.values()),
        "Educator Guide linked entries": sum(bool(educator_found[entry["anchor"]]) for entry in entries),
        "Outdated Educator Guide traces": len(outdated_educator),
    }
    for line_number, line in enumerate(rebuilt_lines):
        match = re.match(r"^\| (.*?) \| ([0-9]+) \|$", line)
        if match and match.group(1) in dashboard_values:
            rebuilt_lines[line_number] = f"| {match.group(1)} | {dashboard_values[match.group(1)]} |"

    rebuilt = "\n".join(rebuilt_lines) + ("\n" if lexicon_text.endswith("\n") else "")
    report = {
        "entries": len(entries),
        "changed_rows": 0 if rebuilt == lexicon_text else 1,
        "student_entries_found": sum(bool(student_found[entry["anchor"]]) for entry in entries),
        "student_direct_links": sum(len(LEXICON_LINK_RE.findall(line)) for line in student_lines),
        "educator_entries_linked": sum(bool(educator_found[entry["anchor"]]) for entry in entries),
        "educator_direct_links": sum(len(items) for items in educator_found.values()),
        "outdated_student": outdated_student,
        "outdated_educator": outdated_educator,
        "newly_present_student": newly_present_student,
    }
    return rebuilt, report


def emit_patch(content: str) -> None:
    relative = LEXICON.relative_to(ROOT)
    current = LEXICON.read_text(encoding="utf-8")
    diff = list(
        difflib.unified_diff(
            current.splitlines(keepends=True),
            content.splitlines(keepends=True),
            fromfile=str(relative),
            tofile=str(relative),
        )
    )
    print("*** Begin Patch")
    print(f"*** Update File: {relative}")
    for line in diff[2:]:
        print("@@\n" if line.startswith("@@ ") else line, end="")
    print("*** End Patch")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch", action="store_true", help="emit an apply_patch patch")
    parser.add_argument("--check", action="store_true", help="print the refresh audit")
    parser.add_argument("--diff", action="store_true", help="print the proposed unified diff")
    args = parser.parse_args()
    rebuilt, report = rebuild()
    if args.patch:
        emit_patch(rebuilt)
        return
    if args.diff:
        current = LEXICON.read_text(encoding="utf-8")
        print(
            "".join(
                difflib.unified_diff(
                    current.splitlines(keepends=True),
                    rebuilt.splitlines(keepends=True),
                    fromfile=str(LEXICON.relative_to(ROOT)),
                    tofile=str(LEXICON.relative_to(ROOT)),
                )
            ),
            end="",
        )
        return
    print(f"Entries: {report['entries']}")
    print(f"Rows that would change: {report['changed_rows']}")
    print(f"Student entries found: {report['student_entries_found']}")
    print(f"Student direct links: {report['student_direct_links']}")
    print(f"Educator entries linked: {report['educator_entries_linked']}")
    print(f"Educator direct links: {report['educator_direct_links']}")
    print("Outdated Student entries: " + ", ".join(report["outdated_student"]))
    print("Outdated Educator entries: " + ", ".join(report["outdated_educator"]))
    print("Newly present Student entries: " + ", ".join(report["newly_present_student"]))


if __name__ == "__main__":
    main()
