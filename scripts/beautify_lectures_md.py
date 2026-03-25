#!/usr/bin/env python3
"""
Beautify MkDocs lecture markdown for readability.

Conservative rules:
- Reflow bullets inside "## Slide-by-slide digestion" into paragraphs.
- Convert bullet pseudo-code blocks (procedure/begin/for/end/return/equations) into fenced code blocks.
- Convert a small set of common math fragments into MathJax-friendly LaTeX.

This script is intentionally conservative to avoid semantic drift.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


LECTURES_DIR = Path("Lectures/docs")
TOPIC_FOLDERS = [
    LECTURES_DIR / "01_Foundations",
    LECTURES_DIR / "02_Geometric_Search",
    LECTURES_DIR / "03_Convex_Hulls",
    LECTURES_DIR / "04_Proximity",
]


def _count_fences(text: str) -> int:
    return text.count("```")


def looks_like_pseudocode_line(s: str) -> bool:
    s = s.strip()
    if not s:
        return False

    # Strong signals for *real* pseudo/algorithm blocks.
    if "procedure " in s:
        return True
    if s in {"begin", "end", "endfor", "endif", "endwhile"}:
        return True
    if s.startswith("return "):
        return True
    if s.startswith("else ") or s == "else":
        return True

    # Modular arithmetic appears in pseudo-code (e.g., parity counting).
    if " mod " in s or s.endswith(" mod"):
        return True

    # Inline pseudocode annotations.
    if "/*" in s:
        return True

    return False


def looks_like_pseudocode_continuation_line(s: str) -> bool:
    """
    Lines that are very likely part of a pseudocode block.

    This is used only after we already detected a strong pseudocode start
    (e.g., "procedure", "begin", "return"), so we can be more permissive.
    """
    s = s.strip()
    if not s:
        return False
    if looks_like_pseudocode_line(s):
        return True
    if s == "for":
        return True
    if s.startswith("for "):
        return True
    if s.startswith("edge "):
        return True
    if " mod " in s or s.endswith(" mod"):
        return True
    # Assignment-like continuation.
    if re.search(r"\b[a-zA-Z_][a-zA-Z0-9_]*\s*=", s):
        return True
    return False


def join_reflow_lines(lines: List[str]) -> str:
    """
    Join reflowed slide bullet fragments into a readable paragraph.

    We use spaces, and keep any punctuation the source already has.
    """
    parts = [ln.strip() for ln in lines if ln.strip()]
    if not parts:
        return ""
    # Avoid double spaces and keep original punctuation.
    return " ".join(parts)


def rewrite_math(text: str) -> str:
    # Avoid double-wrapping if the file already contains MathJax wrappers.
    def wrap(expr: str) -> str:
        return r"\(" + expr + r"\)"

    # 0<=α<=1 style.
    text = re.sub(
        r"0\s*<=\s*α\s*<=\s*1",
        lambda m: wrap(r"0 \le \alpha \le 1"),
        text,
    )

    # p(α) = p0 + α(p1 - p0) into LaTeX.
    text = re.sub(
        r"p\(α\)\s*=\s*p0\s*\+\s*α\(p1\s*-\s*p0\)",
        lambda m: wrap(r"p(\alpha)=p_0+\alpha(p_1-p_0)"),
        text,
    )

    # Parametric segment restriction sometimes written as "0 <= α <= 1"
    text = re.sub(
        r"0\s*<=\s*α\s*<=\s*1",
        lambda m: wrap(r"0 \le \alpha \le 1"),
        text,
    )

    # distance(pi,pj) = sqrt((xi - xj)2 + (yi - yj)2).
    # Input is often exactly as in the slides.
    dist_expr = r"d(p_i,p_j)=\sqrt{(x_i-x_j)^2+(y_i-y_j)^2}"
    text = re.sub(
        r"distance\(pi,pj\)\s*=\s*sqrt\(\(xi\s*-\s*xj\)2\s*\+\s*\(yi\s*-\s*yj\)2\)",
        lambda m: wrap(dist_expr),
        text,
    )

    # distance(pi,pj) variant without extra spaces inside sqrt arguments.
    # (Kept as a separate regex in case spacing differs.)
    text = re.sub(
        r"distance\(pi,pj\)\s*=\s*sqrt\(\(xi\s*-\s*xj\)2\s*\+\s*\(yi\s*-\s*yj\)2\)",
        lambda m: wrap(dist_expr),
        text,
    )

    # O(dN2) -> O(d N^2) (render as plain text; still readable).
    text = text.replace("O(dN2)", "O(d N^2)")
    text = text.replace("O(dN^2)", "O(d N^2)")

    return text


@dataclass
class SlideBlock:
    header: str
    bullet_lines: List[str]


def transform_slide_by_slide(section_lines: List[str]) -> List[str]:
    """
    Transform a "Slide-by-slide digestion" section.

    Assumes input does not include the leading "## Slide-by-slide digestion" header.
    """
    out: List[str] = []

    i = 0
    n = len(section_lines)
    slide_heading_re = re.compile(r"^###\s+p\.\s*\d+\s*-\s*.*$")

    while i < n:
        line = section_lines[i]
        if not line.startswith("### "):
            # Preserve any stray lines verbatim.
            out.append(line)
            i += 1
            continue

        if not slide_heading_re.match(line.strip()):
            out.append(line)
            i += 1
            continue

        # Collect this slide block until next "### p." or end.
        header = line
        i += 1
        block: List[str] = []
        while i < n:
            if section_lines[i].startswith("### ") and slide_heading_re.match(section_lines[i].strip()):
                break
            block.append(section_lines[i])
            i += 1

        bullet_lines: List[str] = []
        other_lines: List[str] = []
        for b in block:
            stripped = b.strip()
            if stripped.startswith("- "):
                bullet_lines.append(stripped[2:].rstrip())
            else:
                other_lines.append(b)

        # If there are no bullet lines, keep verbatim.
        if not bullet_lines:
            out.append(header)
            out.extend(other_lines)
            continue

        # Split into reflow paragraphs and potential pseudocode fences.
        # Find first pseudocode line.
        code_start = None
        for idx, bl in enumerate(bullet_lines):
            if looks_like_pseudocode_line(bl):
                code_start = idx
                break
        if code_start is None:
            # Preserve bullet formatting for readability.
            out.append(header)
            for bl in bullet_lines:
                out.append(f"- {bl}")
            out.append("")
            continue

        # Choose code_end:
        # - include the whole slide's algorithm-ish block
        # - stop before an explicit "Analysis" marker (when present)
        code_end = len(bullet_lines) - 1
        for idx in range(code_start + 1, len(bullet_lines)):
            if bullet_lines[idx].strip().lower().startswith("analysis"):
                code_end = idx - 1
                break

        prefix = bullet_lines[:code_start]
        code = bullet_lines[code_start : code_end + 1]
        suffix = bullet_lines[code_end + 1 :]

        out.append(header)
        if prefix:
            for bl in prefix:
                out.append(f"- {bl}")
            out.append("")

        out.append("```text")
        for c in code:
            out.append(c.rstrip())
        out.append("```")
        out.append("")

        if suffix:
            for bl in suffix:
                out.append(f"- {bl}")
            out.append("")

    return out


def beautify_file(path: Path) -> Tuple[bool, str]:
    original = path.read_text(encoding="utf-8")
    if "## Slide-by-slide digestion" not in original:
        # Still rewrite common math fragments.
        updated = rewrite_math(original)
        changed = updated != original
        if changed:
            path.write_text(updated, encoding="utf-8")
        return changed, original

    lines = original.splitlines()

    # Locate slide digestion blocks.
    out_lines: List[str] = []
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].strip() == "## Slide-by-slide digestion":
            out_lines.append(lines[i])
            i += 1

            # Find end of this H2 section: next line that starts with "## " at column 0.
            start = i
            while i < n and not (lines[i].startswith("## ") and not lines[i].startswith("## Slide-by-slide digestion")):
                i += 1
            section = lines[start:i]
            transformed = transform_slide_by_slide(section)
            out_lines.extend(transformed)
            continue

        out_lines.append(lines[i])
        i += 1

    updated = "\n".join(out_lines) + "\n"
    updated = rewrite_math(updated)

    changed = updated != original
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed, original


def main(argv: List[str]) -> int:
    check_only = "--check" in argv
    files: List[Path] = []
    for folder in TOPIC_FOLDERS:
        if folder.exists():
            files.extend(sorted(folder.glob("*.md")))

    if not files:
        print("No markdown files found in Lectures/docs/*/*.md")
        return 1

    changed_files: List[str] = []
    for f in files:
        original = f.read_text(encoding="utf-8")
        updated = beautify_preview(original)

        if updated != original:
            changed_files.append(str(f))
            if not check_only:
                f.write_text(updated, encoding="utf-8")

    # Validate fences in changed files.
    bad_fences: List[str] = []
    for f in changed_files:
        p = Path(f)
        t = p.read_text(encoding="utf-8")
        if _count_fences(t) % 2 != 0:
            bad_fences.append(str(p))

    if bad_fences:
        print("Unbalanced code fences (odd ``` count) in:")
        for b in bad_fences:
            print(f" - {b}")
        return 2

    if check_only:
        print(f"Would change {len(changed_files)} files.")
    else:
        print(f"Changed {len(changed_files)} files.")
    return 0


def beautify_preview(original: str) -> str:
    if "## Slide-by-slide digestion" not in original:
        return rewrite_math(original)

    lines = original.splitlines()
    out_lines: List[str] = []
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].strip() == "## Slide-by-slide digestion":
            out_lines.append(lines[i])
            i += 1
            start = i
            while i < n and not (lines[i].startswith("## ") and not lines[i].startswith("## Slide-by-slide digestion")):
                i += 1
            section = lines[start:i]
            transformed = transform_slide_by_slide(section)
            out_lines.extend(transformed)
            continue

        out_lines.append(lines[i])
        i += 1

    updated = "\n".join(out_lines) + "\n"
    updated = rewrite_math(updated)
    return updated


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

