#!/usr/bin/env python3
"""Check plain-text fiction manuscripts for deterministic contamination risks."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable, Sequence


TEXT_EXTENSIONS = {".txt", ".md", ".markdown", ".text"}
TITLE_PATTERN = re.compile(
    r"^(?:第.{1,20}章(?:[\s:：—–-]|$)|chapter\s+\S+)", re.IGNORECASE
)
LATIN_TOKEN_PATTERN = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*")
LATIN_SEQUENCE_PATTERN = re.compile(
    r"[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*(?:[ \t]+[A-Za-z][A-Za-z0-9]*(?:[-'][A-Za-z0-9]+)*)+"
)
PROMPT_PATTERNS = tuple(
    re.compile(pattern)
    for pattern in (
        r"以下接上文",
        r"(?:下文|后文|全文|本章)(?:中)?一律称(?:为|作)?",
        r"写到章末",
        r"请(?:接着|继续)(?:上文|下文|本章|正文)(?:扩写|改写|写作)?",
        r"请(?:扩写|改写|润色|输出)(?:以下|上述|本章|正文)",
        r"不要输出(?:解释|分析|标题|说明)",
    )
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    severity: str
    rule_id: str
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.severity}: {self.rule_id}: {self.message}"


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check plain-text fiction for encoding damage, prompt or Markdown leakage, suspicious Latin fragments, quote imbalance, duplication, and whitespace."
    )
    parser.add_argument("target", type=Path, help="A manuscript file or directory")
    parser.add_argument(
        "--allow-token",
        action="append",
        default=[],
        metavar="TOKEN",
        help="Allow one Latin token; may be repeated",
    )
    parser.add_argument(
        "--allowlist",
        action="append",
        default=[],
        type=Path,
        metavar="FILE",
        help="UTF-8 file containing one allowed token per line; may be repeated",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exit code 1 when warnings are present",
    )
    parser.add_argument(
        "--require-title",
        action="store_true",
        help="Require the first non-empty line to look like a chapter title",
    )
    return parser.parse_args(argv)


def load_allowlist(paths: Iterable[Path], tokens: Iterable[str]) -> set[str]:
    allowed = {token.casefold() for token in tokens if token.strip()}
    for path in paths:
        if not path.is_file():
            raise OSError(f"Allowlist not found: {path}")
        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            token = raw_line.strip()
            if token and not token.startswith("#"):
                allowed.add(token.casefold())
    return allowed


def iter_manuscripts(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(
            path
            for path in target.rglob("*")
            if path.is_file() and path.suffix.casefold() in TEXT_EXTENSIONS
        )
    raise OSError(f"Target not found: {target}")


def line_number_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def normalize_paragraph(text: str) -> str:
    return re.sub(r"[\W_]+", "", text, flags=re.UNICODE).casefold()


def paragraph_spans(lines: list[str]) -> list[tuple[int, str]]:
    paragraphs: list[tuple[int, str]] = []
    start = 0
    buffer: list[str] = []
    for number, line in enumerate(lines, start=1):
        if line.strip():
            if not buffer:
                start = number
            buffer.append(line.strip())
        elif buffer:
            paragraphs.append((start, " ".join(buffer)))
            buffer = []
    if buffer:
        paragraphs.append((start, " ".join(buffer)))
    return paragraphs


def check_latin_fragments(path: Path, line_number: int, line: str, allowed: set[str]) -> list[Finding]:
    findings: list[Finding] = []

    def unallowed_tokens(fragment: str) -> list[str]:
        return [
            token
            for token in LATIN_TOKEN_PATTERN.findall(fragment)
            if token.casefold() not in allowed
        ]

    covered: list[tuple[int, int]] = []
    for match in LATIN_SEQUENCE_PATTERN.finditer(line):
        tokens = unallowed_tokens(match.group(0))
        if len(tokens) >= 2:
            covered.append(match.span())
            findings.append(
                Finding(
                    path,
                    line_number,
                    "warning",
                    "latin-fragment",
                    f"suspicious Latin phrase: {match.group(0)!r}",
                )
            )

    for match in LATIN_TOKEN_PATTERN.finditer(line):
        if any(start <= match.start() and match.end() <= end for start, end in covered):
            continue
        token = match.group(0)
        if token.casefold() not in allowed and len(token) >= 12:
            findings.append(
                Finding(
                    path,
                    line_number,
                    "warning",
                    "latin-fragment",
                    f"unusually long Latin token: {token!r}",
                )
            )
    return findings


def check_file(path: Path, allowed: set[str], require_title: bool) -> list[Finding]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines(keepends=True)
    findings: list[Finding] = []
    is_markdown = path.suffix.casefold() in {".md", ".markdown"}

    for number, line_with_ending in enumerate(lines, start=1):
        line = line_with_ending.rstrip("\r\n")
        if "\ufffd" in line:
            findings.append(
                Finding(path, number, "error", "replacement-character", "Unicode replacement character found")
            )
        if line != line.rstrip(" \t"):
            findings.append(
                Finding(path, number, "warning", "trailing-whitespace", "trailing spaces or tabs")
            )
        if any(pattern.search(line) for pattern in PROMPT_PATTERNS):
            findings.append(
                Finding(path, number, "error", "prompt-leak", "possible editing or generation instruction")
            )
        if not is_markdown and (
            "```" in line or re.search(r"\*\*\S.*?\*\*|__\S.*?__", line)
        ):
            findings.append(
                Finding(path, number, "error", "markdown-leak", "code fence or emphasis markup in plain text")
            )
        elif not is_markdown and re.match(r"^\s{0,3}#{1,6}\s+\S", line):
            findings.append(
                Finding(path, number, "warning", "markdown-heading", "Markdown heading marker in manuscript")
            )
        findings.extend(check_latin_fragments(path, number, line, allowed))

    opening_count = text.count("“")
    closing_count = text.count("”")
    if opening_count != closing_count:
        first_offset = min(
            (offset for offset in (text.find("“"), text.find("”")) if offset >= 0),
            default=0,
        )
        findings.append(
            Finding(
                path,
                line_number_at(text, first_offset),
                "warning",
                "unbalanced-quote",
                f"Chinese double quotes are unbalanced ({opening_count} opening, {closing_count} closing)",
            )
        )

    paragraphs = paragraph_spans(text.splitlines())
    for (previous_line, previous), (current_line, current) in zip(paragraphs, paragraphs[1:]):
        previous_normalized = normalize_paragraph(previous)
        current_normalized = normalize_paragraph(current)
        if min(len(previous_normalized), len(current_normalized)) < 20:
            continue
        similarity = SequenceMatcher(None, previous_normalized, current_normalized).ratio()
        if similarity >= 0.94:
            findings.append(
                Finding(
                    path,
                    current_line,
                    "warning",
                    "adjacent-duplicate",
                    f"paragraph is {similarity:.0%} similar to paragraph at line {previous_line}",
                )
            )

    if require_title:
        first_nonempty = next(
            ((number, line.strip()) for number, line in enumerate(text.splitlines(), start=1) if line.strip()),
            (1, ""),
        )
        title_candidate = re.sub(r"^#{1,6}\s+", "", first_nonempty[1]) if is_markdown else first_nonempty[1]
        if not TITLE_PATTERN.match(title_candidate):
            findings.append(
                Finding(path, first_nonempty[0], "error", "missing-title", "chapter title not found")
            )

    return findings


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    try:
        allowed = load_allowlist(args.allowlist, args.allow_token)
        allowlist_paths = {path.resolve() for path in args.allowlist}
        manuscripts = [
            path for path in iter_manuscripts(args.target) if path.resolve() not in allowlist_paths
        ]
        if not manuscripts:
            raise OSError(f"No supported text files found under: {args.target}")
        findings = [
            finding
            for manuscript in manuscripts
            for finding in check_file(manuscript, allowed, args.require_title)
        ]
    except (OSError, UnicodeError) as error:
        print(str(error), file=sys.stderr)
        return 2

    for finding in sorted(findings, key=lambda item: (str(item.path), item.line, item.rule_id)):
        print(finding.render())

    errors = sum(finding.severity == "error" for finding in findings)
    warnings = sum(finding.severity == "warning" for finding in findings)
    if not findings:
        print(f"PASS: {len(manuscripts)} file(s) checked; no findings.")
    else:
        print(f"SUMMARY: {len(manuscripts)} file(s), {errors} error(s), {warnings} warning(s).")

    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
