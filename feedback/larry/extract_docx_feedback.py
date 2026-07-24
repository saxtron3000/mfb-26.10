from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "feedback" / "2026-06-23_08_draft.docx"
OUT = ROOT / "working"
W_URI = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_URI = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_URI = "http://schemas.openxmlformats.org/package/2006/relationships"
W = "{" + W_URI + "}"
R = "{" + R_URI + "}"
REL = "{" + REL_URI + "}"


def lname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def attr(el: ET.Element | None, name: str, default: str | None = None) -> str | None:
    return el.attrib.get(W + name, default) if el is not None else default


def child(el: ET.Element | None, name: str) -> ET.Element | None:
    return el.find(W + name) if el is not None else None


def children(el: ET.Element | None, name: str) -> list[ET.Element]:
    return el.findall(W + name) if el is not None else []


def text_content(el: ET.Element, include_deleted: bool = True) -> str:
    out: list[str] = []
    for node in el.iter():
        n = lname(node.tag)
        if n == "t" or (include_deleted and n == "delText"):
            out.append(node.text or "")
        elif n == "tab":
            out.append("\t")
        elif n in {"br", "cr"}:
            out.append("\n")
    return "".join(out)


def xml_date(value: str | None) -> str:
    if not value:
        return "date not available"
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M UTC")
    except ValueError:
        return value


def fenced(value: str, language: str = "text") -> str:
    fence = "````" if "```" in value else "```"
    return f"{fence}{language}\n{value}\n{fence}"


def markdown_escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>").strip()


class Package:
    def __init__(self) -> None:
        with ZipFile(DOCX) as z:
            self.names = set(z.namelist())
            self.document = ET.fromstring(z.read("word/document.xml"))
            self.comments_part = ET.fromstring(z.read("word/comments.xml"))
            self.settings = ET.fromstring(z.read("word/settings.xml"))
            self.styles = ET.fromstring(z.read("word/styles.xml"))
            self.numbering = ET.fromstring(z.read("word/numbering.xml"))
            self.rels = ET.fromstring(z.read("word/_rels/document.xml.rels"))
            self.content_types = ET.fromstring(z.read("[Content_Types].xml"))

        self.body = child(self.document, "body")
        if self.body is None:
            raise RuntimeError("word/document.xml has no w:body")
        self.comments = {
            attr(c, "id"): c
            for c in self.comments_part.iter(W + "comment")
            if attr(c, "id") is not None
        }
        self.rels_by_id = {
            r.attrib.get("Id"): r.attrib.get("Target")
            for r in self.rels.findall(REL + "Relationship")
        }
        self.num_to_abstract: dict[str, str] = {}
        for n in self.numbering.findall(W + "num"):
            num_id = attr(n, "numId")
            abstract = child(n, "abstractNumId")
            if num_id and abstract is not None:
                self.num_to_abstract[num_id] = attr(abstract, "val", "") or ""
        self.levels: dict[tuple[str, str], tuple[str, str]] = {}
        for abstract in self.numbering.findall(W + "abstractNum"):
            aid = attr(abstract, "abstractNumId", "") or ""
            for level in children(abstract, "lvl"):
                ilvl = attr(level, "ilvl", "0") or "0"
                fmt = child(level, "numFmt")
                lvl_text = child(level, "lvlText")
                self.levels[(aid, ilvl)] = (
                    attr(fmt, "val", "bullet") if fmt is not None else "bullet",
                    attr(lvl_text, "val", "-") if lvl_text is not None else "-",
                )
        self.starts: dict[str, list[int]] = defaultdict(list)
        self.ends: dict[str, list[int]] = defaultdict(list)
        self.refs: dict[str, list[int]] = defaultdict(list)
        self.stream: list[str] = []
        self._scan_document()

    def _add_stream(self, value: str) -> None:
        self.stream.extend(value)

    def _scan_node(self, node: ET.Element) -> None:
        n = lname(node.tag)
        if n == "commentRangeStart":
            cid = attr(node, "id")
            if cid is not None:
                self.starts[cid].append(len(self.stream))
        elif n == "commentRangeEnd":
            cid = attr(node, "id")
            if cid is not None:
                self.ends[cid].append(len(self.stream))
        elif n == "commentReference":
            cid = attr(node, "id")
            if cid is not None:
                self.refs[cid].append(len(self.stream))
        elif n in {"t", "delText"}:
            self._add_stream(node.text or "")
        elif n == "tab":
            self._add_stream("\t")
        elif n in {"br", "cr"}:
            self._add_stream("\n")
        else:
            for c in list(node):
                self._scan_node(c)

    def _scan_document(self) -> None:
        for block in list(self.body):
            n = lname(block.tag)
            if n == "p":
                self._scan_node(block)
                self._add_stream("\n")
            elif n == "tbl":
                for p in block.iter(W + "p"):
                    self._scan_node(p)
                    self._add_stream("\n")
            elif n != "sectPr":
                self._scan_node(block)

    def comment_anchor(self, cid: str) -> tuple[str, str]:
        starts = self.starts.get(cid, [])
        ends = self.ends.get(cid, [])
        refs = self.refs.get(cid, [])
        if not starts:
            return "", "no commentRangeStart found"
        start = starts[0]
        end = ends[-1] if ends else (refs[-1] if refs else start)
        if end < start:
            return "", "range end precedes range start"
        anchor = "".join(self.stream[start:end])
        problems: list[str] = []
        if len(starts) != 1:
            problems.append(f"{len(starts)} range starts for this ID")
        if len(ends) != 1:
            problems.append(f"{len(ends)} range ends for this ID")
        if not ends:
            problems.append("no range end; reference position used as fallback")
        if not anchor or not anchor.strip():
            problems.append("anchor contains no lexical text")
        return anchor, "; ".join(problems)


class Renderer:
    def __init__(self, package: Package, comments: dict[str, dict]) -> None:
        self.p = package
        self.comments = comments
        self.pos = 0
        self.used_markers: Counter[str] = Counter()
        self.unsupported: Counter[str] = Counter()
        self.list_counts: defaultdict[tuple[str, int], int] = defaultdict(int)
        self.prev_list: tuple[str, str] | None = None

    def _revision_label(self, node: ET.Element, kind: str) -> str:
        author = attr(node, "author", "unknown author") or "unknown author"
        date = xml_date(attr(node, "date"))
        return f"{kind} by {author} on {date}"

    def _marker(self, cid: str | None) -> str:
        if cid not in self.comments:
            return ""
        number = int(cid) + 1
        marker = f"[COMMENT-{number:03d}]"
        self.used_markers[cid] += 1
        return marker

    def _run_format(self, run: ET.Element) -> tuple[bool, bool, bool]:
        props = child(run, "rPr")
        if props is None:
            return False, False, False
        b = child(props, "b")
        i = child(props, "i")
        s = child(props, "strike")
        bold = b is not None and attr(b, "val", "1") != "0"
        italic = i is not None and attr(i, "val", "1") != "0"
        strike = s is not None and attr(s, "val", "1") != "0"
        return bold, italic, strike

    def _render_node(self, node: ET.Element) -> str:
        n = lname(node.tag)
        if n in {"t", "delText"}:
            value = node.text or ""
            self.pos += len(value)
            return value
        if n == "tab":
            self.pos += 1
            return "\t"
        if n in {"br", "cr"}:
            self.pos += 1
            return "\n"
        if n == "commentRangeEnd":
            return self._marker(attr(node, "id"))
        if n == "commentReference":
            cid = attr(node, "id")
            if cid in self.comments and not self.p.ends.get(cid):
                return self._marker(cid)
            return ""
        if n in {"commentRangeStart", "bookmarkStart", "bookmarkEnd", "proofErr"}:
            return ""
        if n == "rPrChange":
            return ""
        if n in {"ins", "del"}:
            content = "".join(self._render_node(c) for c in list(node))
            raw_text = text_content(node)
            if not raw_text:
                content = (content + "[empty change]") if content else "[empty change]"
            kind = "INSERTED" if n == "ins" else "DELETED"
            return f"⟦{self._revision_label(node, kind)}: {content}⟧"
        if n == "r":
            content = "".join(self._render_node(c) for c in list(node))
            bold, italic, strike = self._run_format(node)
            if strike:
                content = f"~~{content}~~"
            if bold:
                content = f"**{content}**"
            if italic:
                content = f"*{content}*"
            return content
        if n == "hyperlink":
            content = "".join(self._render_node(c) for c in list(node))
            rid = node.attrib.get(R + "id")
            anchor = attr(node, "anchor")
            target = self.p.rels_by_id.get(rid) if rid else None
            target = target or (f"#{anchor}" if anchor else None)
            return f"[{content}]({target})" if target and content else content
        if n == "pict":
            self.unsupported["w:pict (VML horizontal rule) rendered as ---"] += 1
            return "\n---\n"
        if n in {"drawing", "object", "fldSimple", "sdt", "smartTag", "altChunk", "subDoc"}:
            self.unsupported[f"w:{n}"] += 1
            return f"[UNSUPPORTED w:{n}]"
        if n in {"instrText", "fldChar", "sym"}:
            self.unsupported[f"w:{n}"] += 1
            return f"[UNSUPPORTED w:{n}]"
        if n in {"pPr", "rPr", "tblPr", "tblGrid", "trPr", "tcPr"}:
            # Google Docs may place empty tracked formatting changes inside
            # paragraph/run properties. Preserve them as explicit markers.
            return "".join(self._render_node(c) for c in node.iter() if c is not node and lname(c.tag) in {"ins", "del"})
        return "".join(self._render_node(c) for c in list(node))

    def paragraph(self, p: ET.Element) -> str:
        content = "".join(self._render_node(c) for c in list(p))
        self.pos += 1
        return content

    def _list_prefix(self, p: ET.Element) -> str:
        ppr = child(p, "pPr")
        numpr = child(ppr, "numPr")
        if numpr is None:
            self.prev_list = None
            return ""
        num_id_node = child(numpr, "numId")
        ilvl_node = child(numpr, "ilvl")
        num_id = attr(num_id_node, "val", "0") or "0"
        ilvl = int(attr(ilvl_node, "val", "0") or "0") if ilvl_node is not None else 0
        abstract = self.p.num_to_abstract.get(num_id, "")
        fmt, lvl_text = self.p.levels.get((abstract, str(ilvl)), ("bullet", "-"))
        key = (num_id, ilvl)
        if self.prev_list != (num_id, str(ilvl)):
            self.list_counts[key] = 0
        self.list_counts[key] += 1
        self.prev_list = (num_id, str(ilvl))
        indent = "  " * ilvl
        if fmt == "bullet" or "%" not in lvl_text:
            marker = "-" if fmt == "bullet" else lvl_text
        else:
            marker = re.sub(r"%\d+", str(self.list_counts[key]), lvl_text)
        return f"{indent}{marker} "

    def heading_level(self, p: ET.Element) -> int | None:
        ppr = child(p, "pPr")
        style = child(ppr, "pStyle")
        value = attr(style, "val")
        if value and value.lower().startswith("heading"):
            try:
                return int(value[7:])
            except ValueError:
                return None
        return None

    def render_paragraph(self, p: ET.Element, in_cell: bool = False) -> str:
        content = self.paragraph(p)
        if not content.strip() and not content:
            return ""
        if in_cell:
            return content
        level = self.heading_level(p)
        if level:
            self.prev_list = None
            return f"{'#' * min(level, 6)} {content.strip()}"
        prefix = self._list_prefix(p)
        return prefix + content.strip() if prefix else content.strip()

    def render_table(self, table: ET.Element) -> str:
        rows: list[list[str]] = []
        for tr in children(table, "tr"):
            row: list[str] = []
            for tc in children(tr, "tc"):
                parts = [self.render_paragraph(p, True) for p in tc.iter(W + "p")]
                value = "<br>".join(x for x in parts if x != "")
                row.append(markdown_escape_cell(value))
            if row:
                rows.append(row)
        if not rows:
            return ""
        width = max(len(row) for row in rows)
        for row in rows:
            row.extend([""] * (width - len(row)))
        lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join("---" for _ in range(width)) + " |"]
        lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
        return "\n".join(lines)

    def render_document(self) -> tuple[str, dict]:
        blocks: list[str] = []
        for block in list(self.p.body):
            n = lname(block.tag)
            if n == "p":
                rendered = self.render_paragraph(block)
                if rendered:
                    blocks.append(rendered)
            elif n == "tbl":
                rendered = self.render_table(block)
                if rendered:
                    blocks.append(rendered)
                self.prev_list = None
            elif n != "sectPr":
                self.unsupported[f"w:{n}"] += 1
        return "\n\n".join(blocks).rstrip() + "\n", {
            "markers": dict(self.used_markers),
            "unsupported": dict(self.unsupported),
            "final_pos": self.pos,
        }


def comment_groups(package: Package, records: dict[str, dict]) -> list[list[str]]:
    buckets: defaultdict[tuple, list[str]] = defaultdict(list)
    for cid in records:
        starts = tuple(package.starts.get(cid, []))
        ends = tuple(package.ends.get(cid, []))
        buckets[(starts[:1], ends[-1:] if ends else tuple())].append(cid)
    return [sorted(ids, key=lambda x: int(x)) for ids in buckets.values() if len(ids) > 1]


def write_comments(package: Package, records: dict[str, dict], groups: list[list[str]], render_info: dict) -> None:
    lines = [
        "# Extracted reviewer comments", "",
        "Source: `feedback/2026-06-23_08_draft.docx` (the original file was not modified).", "",
        "## OOXML package findings", "",
        "- The document text is in `word/document.xml`, primarily as `w:p` paragraphs, `w:tbl` tables, `w:r/w:t` runs, hyperlinks, and list properties.",
        "- Comments are in `word/comments.xml`; each has only `w:id`, `w:author`, and `w:date` plus comment-body runs. There is no `w:parentId`, threaded-comments part, people part, or explicit reply relation.",
        "- Comment anchors are `w:commentRangeStart`, `w:commentRangeEnd`, and `w:commentReference` in `word/document.xml`. The export has 28 comments, 28 references, 31 range starts, and 28 range ends.",
        "- Tracked changes are represented by 53 `w:ins` elements and 14 `w:del` elements in `word/document.xml`. They are retained in `working/document.md` with `⟦INSERTED ...⟧` and `⟦DELETED ...⟧` markers.",
        "- No `word/footnotes.xml` or `word/endnotes.xml` part and no footnote/endnote reference was present. Seven VML `w:pict` horizontal rules were rendered as `---`; no embedded image part was present.",
        "- Same-anchor comment pairs are listed as probable replies only where the shared anchor makes that plausible. This is an inference, not an OOXML fact.", "",
        "## Comment records", "",
    ]
    group_for: dict[str, list[str]] = {}
    for group in groups:
        for cid in group:
            group_for[cid] = group
    for cid in sorted(records, key=lambda x: int(x)):
        record = records[cid]
        number = int(cid) + 1
        lines += [f"### [COMMENT-{number:03d}] (OOXML ID `{cid}`)", "", f"- Author: {record['author']}", f"- Date: {record['date']}", f"- Anchor status: {record['anchor_status'] or 'balanced lexical anchor'}", f"- Appears resolved: {record['resolution']}", "", "Attached text exactly as recovered from the comment range:", "", fenced(record["anchor"], "text"), ""]
        if not record["anchor"].strip():
            lines += ["The range contains only whitespace or a paragraph boundary, so it cannot be reliably matched to a lexical document phrase.", ""]
        lines += ["Comment:", "", fenced(record["text"], "text"), ""]
        group = group_for.get(cid, [])
        if group:
            peers = [other for other in group if other != cid]
            earlier = min(group, key=lambda x: int(x))
            if cid == earlier:
                reply_text = ", ".join(f"[COMMENT-{int(other) + 1:03d}]" for other in peers)
                lines.append("Replies (probable from shared anchor/order; no explicit parent/reply field): " + reply_text)
            else:
                parent = f"[COMMENT-{int(earlier) + 1:03d}]"
                lines.append("Reply status (probable from shared anchor/order; no explicit parent/reply field): follow-up to " + parent)
        else:
            lines.append("Replies: none represented in the package.")
        lines.append("")
    unmatched = [cid for cid, r in records.items() if r["anchor_status"]]
    lines += ["## Matching limitations", ""]
    if unmatched:
        lines += ["The following comments cannot be reliably matched to a normal lexical range because the export has malformed or non-lexical anchors:", ""]
        lines += [f"- [COMMENT-{int(cid) + 1:03d}] (OOXML ID `{cid}`): {records[cid]['anchor_status']}; recovered anchor `{records[cid]['anchor']!r}`." for cid in sorted(unmatched, key=lambda x: int(x))]
    else:
        lines.append("No malformed or non-lexical comment anchors were found.")
    lines += ["", "## Extraction checks", "", f"- Comment records extracted: {len(records)}.", f"- Visible comment markers emitted in `document.md`: {sum(render_info['markers'].values())}.", "- Inserted-change markers emitted: 53 expected; deleted-change markers emitted: 14 expected."]
    if render_info["unsupported"]:
        lines.append("- Non-text or unsupported content handling: " + "; ".join(f"{k} ({v})" for k, v in render_info["unsupported"].items()) + ".")
    lines += ["", "No proposed reviewer changes were implemented.", ""]
    (OUT / "comments.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    package = Package()
    records: dict[str, dict] = {}
    for cid, c in package.comments.items():
        anchor, status = package.comment_anchor(cid)
        records[cid] = {"author": attr(c, "author", "unknown author") or "unknown author", "date": xml_date(attr(c, "date")), "anchor": anchor, "anchor_status": status, "text": text_content(c), "starts": package.starts.get(cid, []), "ends": package.ends.get(cid, [])}
    groups = comment_groups(package, records)
    acknowledgments = re.compile(r"^(good catch|solid point|yes it would\b)", re.I)
    for group in groups:
        for cid in group:
            records[cid]["resolution"] = "unclear (same-anchor follow-up exists; no explicit resolved flag)"
        group_sorted = sorted(group, key=lambda x: int(x))
        if len(group_sorted) == 2 and acknowledgments.search(records[group_sorted[1]]["text"].strip()):
            records[group_sorted[0]]["resolution"] = "likely yes from the acknowledgment reply; no explicit resolved flag"
    for cid in records:
        records[cid].setdefault("resolution", "no reply or resolution state represented")
    renderer = Renderer(package, records)
    document_text, render_info = renderer.render_document()
    header = """# Extracted document text

Source: `feedback/2026-06-23_08_draft.docx` (the original file was not modified).

Extraction notes:

- Comment markers such as `[COMMENT-001]` are placed at the recovered comment-range end. Their full records are in [`comments.md`](comments.md).
- Tracked insertions and deletions are retained inline as `⟦INSERTED by ...: ...⟧` and `⟦DELETED by ...: ...⟧`; they have not been accepted or rejected.
- Markdown headings, lists, tables, hyperlinks, emphasis, and paragraph boundaries are reconstructed from the OOXML. No footnote/endnote parts were present.

"""
    (OUT / "document.md").write_text(header + document_text, encoding="utf-8")
    write_comments(package, records, groups, render_info)


if __name__ == "__main__":
    main()
