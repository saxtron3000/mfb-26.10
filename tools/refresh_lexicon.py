#!/usr/bin/env python3
"""Refresh guide traceability fields in the published Bitcoin lexicon.

Each guide reference requires a visible term or appropriate alias linked to the
exact URL in the terms register. --check audits both words and destinations;
--link-patch emits guide link repairs; --patch refreshes the reference tables.
"""

from __future__ import annotations

import argparse
import difflib
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STUDENT_LEXICON = ROOT / "publish/mfb-lx-26.10-sg-index.md"
EDUCATOR_LEXICON = ROOT / "publish/mfb-lx-26.10-eg-index.md"
LEXICON = STUDENT_LEXICON
TERMS = ROOT / "publish/mfb-lx-26.10-terms.md"
STUDENT_GUIDE = ROOT / "publish/mfb-bd-26.10/mfb-bd-sg-26.10.md"
EDUCATOR_GUIDE = ROOT / "publish/mfb-bd-26.10/mfb-bd-eg-26.10.md"

ROW_RE = re.compile(r'^\| (.*?) \| (.*?) \| <a id="([^"]+)"></a>(.*?) \| (.*?) \|$')
EDUCATOR_ROW_RE = re.compile(r'^\| (.*?) \| (.*?) \| \[(.*?)\]\(#([^)]+)\) \| (.*?) \|$')
TERMS_ROW_RE = re.compile(r"^\| (BD-LEX-\d+) \| (.*?) \| ")
LEXICON_LINK_RE = re.compile(
    r"\]\((?:(?:\.\./mfb-lx-26\.10-index\.md|https://programs\.myfirstbitcoin\.org/lexicon/en/)#)?(term-[^)\s]+|BD-LEX-\d+|[a-z0-9]+(?:-[a-z0-9]+)*)\)"
)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\[\]]+)\]\(([^)]+)\)")

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
    "term-central-bank": ["Federal Reserve"],
    "term-satoshi-nakamoto": ["Satoshi"],
    "term-lightning-liquidity": ["liquidity"],
    "term-person-to-person-transaction": ["person-to-person Bitcoin transaction"],
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
    "term-lightning-liquidity": "BD-LEX-132",
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
    "term-liquidity": re.compile(r"\b(?:bank|banks|banking|deposit|deposits|withdrawals|cash)\b", re.I),
    "term-lightning-liquidity": re.compile(r"\b(?:Lightning|channel|channels|routing)\b", re.I),
    "term-difficulty": re.compile(r"\b(?:hash|proof|work|miner|miners|mining|target|adjustment)\b", re.I),
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
            output.append(visible_text(line)[0])
        if "-->" in line:
            in_comment = False
    return output


def visible_text(line: str) -> tuple[str, list[int]]:
    """Visible text plus source offsets, excluding Markdown URLs and markers."""
    hidden = set()
    for match in MARKDOWN_LINK_RE.finditer(line):
        hidden.add(match.start())
        hidden.update(range(match.end(1), match.end()))
    for match in re.finditer(r"<[^>]*>|\*\*|(?<!\w)\*(?!\s)|(?<!\s)\*(?!\w)|`", line):
        hidden.update(range(match.start(), match.end()))
    offsets = [index for index in range(len(line)) if index not in hidden]
    return "".join(line[index] for index in offsets), offsets


def term_matches(entries: list[dict[str, str]], lines: list[str]) -> dict[int, list[tuple[int, int, str]]]:
    """Select non-overlapping, sense-appropriate visible terms on each line."""
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

    found = defaultdict(list)
    for line_number, line in enumerate(searchable_lines(lines), 1):
        candidates = []
        for entry in entries:
            anchor = entry["anchor"]
            context = CONTEXT_RE.get(anchor)
            if context and not context.search(line):
                continue
            for alias, pattern in aliases[anchor]:
                for match in pattern.finditer(line):
                    if anchor == "term-target" and re.match(r"\s+(?:one|a|an|about|every)\b", line[match.end():], re.I):
                        continue
                    if anchor == "term-sat" and match.group() == "Satoshi":
                        continue
                    if anchor == "term-satoshi-nakamoto" and alias == "Satoshi" and match.group() != "Satoshi":
                        continue
                    if anchor == "term-privacy" and PRIVACY_ATTRIBUTIVE.match(line, match.start()):
                        continue
                    candidates.append((match.start(), match.end(), len(match.group()), anchor, alias))

        # Prefer longer listed phrases when terms overlap on the same source text.
        occupied: list[tuple[int, int]] = []
        for start, end, length, anchor, alias in sorted(candidates, key=lambda item: (-item[2], item[0])):
            if any(start < used_end and end > used_start for used_start, used_end in occupied):
                continue
            occupied.append((start, end))
            found[line_number].append((start, end, anchor))
    return found


def student_occurrences(entries: list[dict[str, str]], lines: list[str]) -> dict[str, list[int]]:
    found = defaultdict(list)
    for line_number, matches in term_matches(entries, lines).items():
        for anchor in sorted({anchor for _, _, anchor in matches}):
            found[anchor].append(line_number)
    return found


def term_register() -> dict[str, dict[str, str]]:
    records = {}
    for line in source_lines(TERMS):
        columns = [column.strip() for column in line.split("|")]
        if len(columns) == 7 and re.fullmatch(r"BD-LEX-\d+", columns[1]):
            records[columns[1]] = {"term": columns[2], "slug": columns[4], "url": columns[5]}
    return records


def published_entries() -> list[dict[str, str]]:
    entries = {}
    for line in source_lines(LEXICON):
        match = ROW_RE.match(line)
        if match:
            _, lex_id, anchor, term, definition = match.groups()
            entries.setdefault(anchor, {"anchor": anchor, "term": term, "definition": definition})
    values = list(entries.values())
    ids = lex_ids(values)
    for entry in values:
        entry["lex_id"] = ids[entry["anchor"]]
    return values


def link_guides() -> dict[Path, str]:
    """Emit guide changes without changing visible prose or line numbering."""
    entries = published_entries()
    register = term_register()
    by_anchor = {entry["anchor"]: entry for entry in entries}
    destination_ids = {entry["anchor"]: entry["lex_id"] for entry in entries}
    destination_ids.update({lex_id: lex_id for lex_id in register})
    destination_ids.update({record["slug"]: lex_id for lex_id, record in register.items()})
    output = {}
    for path in (STUDENT_GUIDE, EDUCATOR_GUIDE):
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines()
        matches = term_matches(entries, lines)
        changed = []
        for number, line in enumerate(lines, 1):
            edits = []
            existing = list(MARKDOWN_LINK_RE.finditer(line))
            _, offsets = visible_text(line)
            for link in existing:
                target = link.group(2)
                key = target.removeprefix("../mfb-lx-26.10-sg-index.md#").removeprefix("../mfb-lx-26.10-eg-index.md#").removeprefix(
                    "https://programs.myfirstbitcoin.org/lexicon/en/#"
                )
                if key in destination_ids:
                    candidates = [(start, end, anchor) for start, end, anchor in matches[number]
                                  if link.start(1) <= offsets[start] and offsets[end - 1] < link.end(1)]
                    lex_id = destination_ids[key]
                    if candidates:
                        anchor = max(candidates, key=lambda item: item[1] - item[0])[2]
                        lex_id = by_anchor[anchor]["lex_id"]
                    edits.append((link.start(2), link.end(2), register[lex_id]["url"]))
            if path == STUDENT_GUIDE:
                for start, end, anchor in matches[number]:
                    raw_start, raw_end = offsets[start], offsets[end - 1] + 1
                    overlaps = [link for link in existing if raw_start < link.end() and raw_end > link.start()]
                    if overlaps:
                        if not all(link.group(2) in {record["url"] for record in register.values()}
                                   and raw_start <= link.start(1) and link.end(1) <= raw_end for link in overlaps):
                            continue
                        raw_start = min(raw_start, *(link.start() for link in overlaps))
                        raw_end = max(raw_end, *(link.end() for link in overlaps))
                        label = visible_text(line)[0][start:end]
                        edits = [edit for edit in edits if not (raw_start <= edit[0] and edit[1] <= raw_end)]
                    else:
                        label = line[raw_start:raw_end]
                    url = register[by_anchor[anchor]["lex_id"]]["url"]
                    edits.append((raw_start, raw_end, f"[{label}]({url})"))
            for start, end, replacement in sorted(edits, reverse=True):
                line = line[:start] + replacement + line[end:]
            changed.append(line)
        output[path] = "\n".join(changed) + ("\n" if original.endswith("\n") else "")
    return output


def linked_occurrences(entries: list[dict[str, str]], lines: list[str]) -> dict[str, list[int]]:
    """Only record a term when its visible label links to its registered URL."""
    register = term_register()
    by_anchor = {entry["anchor"]: entry for entry in entries}
    found = defaultdict(list)
    for number, matches in term_matches(entries, lines).items():
        line = lines[number - 1]
        _, offsets = visible_text(line)
        links = list(MARKDOWN_LINK_RE.finditer(line))
        accepted = set()
        for start, end, anchor in matches:
            url = register[by_anchor[anchor]["lex_id"]]["url"]
            if any(link.start(1) <= offsets[start] and offsets[end - 1] < link.end(1)
                   and link.group(2) == url for link in links):
                accepted.add(anchor)
        for anchor in sorted(accepted):
            found[anchor].append(number)
    return found


def audit_references() -> list[str]:
    entries = published_entries()
    ids = {entry["anchor"]: entry["lex_id"] for entry in entries}
    sources = {"sg": source_lines(STUDENT_GUIDE), "eg": source_lines(EDUCATOR_GUIDE)}
    linked = {key: linked_occurrences(entries, lines) for key, lines in sources.items()}
    sections = {key: section_anchors(lines) for key, lines in sources.items()}
    errors = []
    reference_re = re.compile(r"\[(\d+)\]\(mfb-bd-26\.10/mfb-bd-(sg|eg)-26\.10\.md#([^)]*)\)")
    for number, line in enumerate(source_lines(LEXICON), 1):
        row = ROW_RE.match(line) or EDUCATOR_ROW_RE.match(line)
        if not row:
            continue
        anchor = row.group(3) if ROW_RE.match(line) else row.group(4)
        recorded_id = re.search(r"BD-LEX-\d+", row.group(2))
        if not recorded_id or recorded_id.group() != ids[anchor]:
            errors.append(f"Lexicon:{number}: incorrect LEX-ID for {anchor}")
        reference = reference_re.search(row.group(1))
        if not reference:
            continue
        source_number, guide, section = reference.groups()
        source_number = int(source_number)
        if source_number not in linked[guide][anchor]:
            errors.append(f"Lexicon:{number}: {guide}:{source_number}: {anchor} lacks a matching term linked to its registered URL")
        if sections[guide].get(source_number) != section:
            errors.append(f"Lexicon:{number}: incorrect section anchor")
    for entry in entries:
        anchor = entry["anchor"]
        if not linked["sg"][anchor] and not linked["eg"][anchor]:
            errors.append(f"{anchor}: no verified reference in either guide")
    return errors


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
    lines: list[str], link_target_to_anchor: dict[str, str], entries: list[dict[str, str]] | None = None
) -> tuple[dict[str, list[int]], dict[int, str]]:
    links: dict[str, list[int]] = defaultdict(list)
    section_at_line: dict[int, str] = {}
    used: dict[str, int] = defaultdict(int)
    current_section = ""
    for line_number, line in enumerate(lines, 1):
        if re.match(r"^#{1,6}\s+", line):
            current_section = github_slug(line, used)
        section_at_line[line_number] = current_section
        for link in MARKDOWN_LINK_RE.finditer(line):
            target_match = LEXICON_LINK_RE.search(link.group())
            if not target_match:
                continue
            link_target = target_match.group(1)
            anchor = link_target_to_anchor.get(link_target)
            if anchor and entries:
                # Shared IDs (e.g. mining/proof of work) must follow the label.
                lex_id = next(entry["lex_id"] for entry in entries if entry["anchor"] == anchor)
                matching_entries = [entry for entry in entries if entry["lex_id"] == lex_id]
                label_matches = term_matches(matching_entries, [link.group(1)])[1]
                if not label_matches:
                    continue
                anchor = max(label_matches, key=lambda item: item[1] - item[0])[2]
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


def _replace_dashboard(text: str, values: dict[str, int]) -> str:
    lines = []
    for line in text.splitlines():
        match = re.match(r"^\| (.*?) \| [0-9]+ \|$", line)
        if match and match.group(1) in values:
            line = f"| {match.group(1)} | {values[match.group(1)]} |"
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def rebuild() -> tuple[dict[Path, str], dict[str, object]]:
    """Rebuild the separate Student Guide and Educator Guide lexicon tables."""
    entries = published_entries()
    register = term_register()
    student_lines = source_lines(STUDENT_GUIDE)
    educator_lines = source_lines(EDUCATOR_GUIDE)
    student_found = linked_occurrences(entries, student_lines)
    educator_found = linked_occurrences(entries, educator_lines)
    student_sections = section_anchors(student_lines)
    educator_sections = section_anchors(educator_lines)
    ids = lex_ids(entries)

    student_rows = [
        "| Student Guide line(s) | LEX-ID | Word or phrase | Beginner definition |",
        "| --- | --- | --- | --- |",
    ]
    tagged_ids: set[str] = set()
    rows_to_sort: list[tuple[int, str]] = []
    for entry in entries:
        lex_id = ids[entry["anchor"]]
        id_markup = "" if lex_id in tagged_ids else f'<a id="{lex_id}"></a>'
        tagged_ids.add(lex_id)
        for reference in format_student_rows(student_found[entry["anchor"]], student_sections, []):
            rows_to_sort.append(
                (line_reference_number(reference),
                 f'| {reference} | {id_markup}{lex_id} | <a id="{entry["anchor"]}"></a>{entry["term"]} | {entry["definition"]} |')
            )
            id_markup = ""
    student_rows.extend(row for _, row in sorted(rows_to_sort))

    educator_rows = [
        "| Educator Guide Guide Line | LEX-ID | Word or phrase | Beginner definition |",
        "| --- | --- | --- | --- |",
    ]
    tagged_ids.clear()
    tagged_anchors: set[str] = set()
    rows_to_sort = []
    for entry in entries:
        lex_id = ids[entry["anchor"]]
        references = format_educator_rows(educator_found[entry["anchor"]], educator_sections, [])
        if not references:
            continue
        id_markup = "" if lex_id in tagged_ids else f'<a id="{lex_id}"></a>'
        tagged_ids.add(lex_id)
        for reference in references:
            term_markup = "" if entry["anchor"] in tagged_anchors else f'<a id="{entry["anchor"]}"></a>'
            tagged_anchors.add(entry["anchor"])
            rows_to_sort.append(
                (line_reference_number(reference),
                 f'| {reference} | {id_markup}{lex_id} | {term_markup}{entry["term"]} | {entry["definition"]} |')
            )
            id_markup = ""
    educator_rows.extend(row for _, row in sorted(rows_to_sort))

    student_current = STUDENT_LEXICON.read_text(encoding="utf-8")
    student_lines_current = student_current.splitlines()
    student_header = "| Student Guide line(s) | LEX-ID | Word or phrase | Beginner definition |"
    student_start = student_lines_current.index(student_header)
    student_end = student_start + 2
    while student_end < len(student_lines_current) and ROW_RE.match(student_lines_current[student_end]):
        student_end += 1
    student_text = "\n".join(
        student_lines_current[:student_start] + student_rows + student_lines_current[student_end:]
    ) + ("\n" if student_current.endswith("\n") else "")

    educator_current = EDUCATOR_LEXICON.read_text(encoding="utf-8")
    educator_lines_current = educator_current.splitlines()
    educator_header = "| Educator Guide Guide Line | LEX-ID | Word or phrase | Beginner definition |"
    educator_start = educator_lines_current.index(educator_header)
    educator_end = educator_start + 2
    while educator_end < len(educator_lines_current) and re.match(r"^\| ", educator_lines_current[educator_end]):
        educator_end += 1
    educator_text = "\n".join(
        educator_lines_current[:educator_start] + educator_rows + educator_lines_current[educator_end:]
    ) + ("\n" if educator_current.endswith("\n") else "")

    urls = {record["url"] for record in register.values()}
    student_direct = sum(link.group(2) in urls for line in student_lines for link in MARKDOWN_LINK_RE.finditer(line))
    educator_direct = sum(link.group(2) in urls for line in educator_lines for link in MARKDOWN_LINK_RE.finditer(line))
    student_text = _replace_dashboard(student_text, {
        "Lexicon entries": len(entries),
        "Student Guide (SG) references": student_direct,
        "Student Guide term entries found": sum(bool(student_found[entry["anchor"]]) for entry in entries),
        "Outdated Student Guide traces": 0,
    })
    educator_text = _replace_dashboard(educator_text, {
        "Educator Guide (EG) references": educator_direct,
        "Educator Guide linked entries": sum(bool(educator_found[entry["anchor"]]) for entry in entries),
        "Outdated Educator Guide traces": 0,
    })
    outputs = {STUDENT_LEXICON: student_text, EDUCATOR_LEXICON: educator_text}
    report = {
        "entries": len(entries),
        "changed_rows": sum(outputs[path] != path.read_text(encoding="utf-8") for path in outputs),
        "student_entries_found": sum(bool(student_found[entry["anchor"]]) for entry in entries),
        "student_direct_links": student_direct,
        "educator_entries_linked": sum(bool(educator_found[entry["anchor"]]) for entry in entries),
        "educator_direct_links": educator_direct,
        "outdated_student": [],
        "outdated_educator": [],
        "newly_present_student": [],
    }
    return outputs, report


def emit_patch(content: str, path: Path = LEXICON) -> None:
    relative = path.relative_to(ROOT)
    current = path.read_text(encoding="utf-8")
    if current == content:
        return
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
    parser.add_argument("--link-patch", action="store_true", help="emit canonical URL links for guide terms")
    args = parser.parse_args()
    if args.link_patch:
        for path, content in link_guides().items():
            emit_patch(content, path)
        return
    rebuilt, report = rebuild()
    if args.patch:
        for path, content in rebuilt.items():
            emit_patch(content, path)
        return
    if args.diff:
        for path, content in rebuilt.items():
            current = path.read_text(encoding="utf-8")
            print(
                "".join(
                    difflib.unified_diff(
                        current.splitlines(keepends=True),
                        content.splitlines(keepends=True),
                        fromfile=str(path.relative_to(ROOT)),
                        tofile=str(path.relative_to(ROOT)),
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
    errors = audit_references()
    print(f"Invalid source references: {len(errors)}")
    for error in errors:
        print(error)
    if args.check and (errors or report["changed_rows"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
