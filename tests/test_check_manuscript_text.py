from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CHECKER = REPOSITORY_ROOT / "novel-writing" / "scripts" / "check_manuscript_text.py"


class ManuscriptCheckerCliTests(unittest.TestCase):
    def run_checker(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CHECKER), *args],
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def write_text(self, directory: Path, name: str, text: str) -> Path:
        path = directory / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_clean_text_and_allowed_latin_tokens_pass(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章 夜班\n\nDora看了一眼SMS，随后把手机收回口袋。\n",
            )

            result = self.run_checker(
                str(path), "--allow-token", "Dora", "--allow-token", "SMS"
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_clear_manuscript_contamination_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章\n\n以下接上文继续扩写。\n\n**她没有回答。**\n\n“门外有人。\n\ufffd\n",
            )

            result = self.run_checker(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertRegex(result.stdout, r"chapter\.txt:\d+: error: prompt-leak:")
        self.assertRegex(result.stdout, r"chapter\.txt:\d+: error: markdown-leak:")
        self.assertRegex(result.stdout, r"chapter\.txt:\d+: error: replacement-character:")
        self.assertRegex(result.stdout, r"chapter\.txt:\d+: warning: unbalanced-quote:")

    def test_warnings_only_fail_in_strict_mode(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章\n\n她低声说了一句 inexplicable foreign fragment，然后转身。   \n",
            )

            normal = self.run_checker(str(path))
            strict = self.run_checker(str(path), "--strict")

        self.assertEqual(normal.returncode, 0, normal.stdout + normal.stderr)
        self.assertIn("warning: latin-fragment:", normal.stdout)
        self.assertIn("warning: trailing-whitespace:", normal.stdout)
        self.assertEqual(strict.returncode, 1)

    def test_unbalanced_quote_is_heuristic_warning(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章\n\n“这句话会在下一段继续。\n",
            )

            normal = self.run_checker(str(path))
            strict = self.run_checker(str(path), "--strict")

        self.assertEqual(normal.returncode, 0, normal.stdout + normal.stderr)
        self.assertIn("warning: unbalanced-quote:", normal.stdout)
        self.assertEqual(strict.returncode, 1)

    def test_allowlist_file_suppresses_known_terms(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            directory = Path(raw_directory)
            path = self.write_text(
                directory,
                "chapter.txt",
                "第一章\n\nDora打开SMS，屏幕上显示PROJECT-X。\n",
            )
            allowlist = self.write_text(directory, "allowlist.txt", "Dora\nSMS\nPROJECT-X\n")

            result = self.run_checker(str(path), "--allowlist", str(allowlist), "--strict")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_directory_scan_does_not_scan_its_allowlist_as_manuscript(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            directory = Path(raw_directory)
            self.write_text(directory, "chapter.txt", "第一章\n\nDora关掉终端。\n")
            allowlist = self.write_text(
                directory,
                "names.txt",
                "Dora\ninexplicable foreign fragment\n",
            )

            result = self.run_checker(
                str(directory), "--allowlist", str(allowlist), "--strict"
            )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("1 file(s) checked", result.stdout)

    def test_adjacent_duplicate_paragraph_is_a_warning(self) -> None:
        paragraph = "她沿着长廊走到尽头，听见门后传来三次缓慢的敲击声。"
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                f"第一章\n\n{paragraph}\n\n{paragraph}\n",
            )

            result = self.run_checker(str(path), "--strict")

        self.assertEqual(result.returncode, 1)
        self.assertIn("warning: adjacent-duplicate:", result.stdout)

    def test_title_is_optional_unless_requested(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "夜雨落在窗沿上，她在黑暗里睁开眼睛。\n",
            )

            optional = self.run_checker(str(path))
            required = self.run_checker(str(path), "--require-title")

        self.assertEqual(optional.returncode, 0, optional.stdout + optional.stderr)
        self.assertEqual(required.returncode, 1)
        self.assertIn("error: missing-title:", required.stdout)

    def test_ordinary_dialogue_is_not_mistaken_for_a_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章\n\n“请继续。”她把记录本翻到下一页。\n",
            )

            result = self.run_checker(str(path), "--strict")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_ordinary_narration_with_yilu_chengwei_is_not_a_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章\n\n当地人一律称为旧港，地图上却仍写着原来的名字。\n",
            )

            result = self.run_checker(str(path), "--strict")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_common_title_punctuation_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.txt",
                "第一章：夜班\n\n雨落在急诊楼外。\n",
            )

            result = self.run_checker(str(path), "--require-title", "--strict")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_markdown_manuscript_allows_markdown_syntax(self) -> None:
        with tempfile.TemporaryDirectory() as raw_directory:
            path = self.write_text(
                Path(raw_directory),
                "chapter.md",
                "# 第一章 夜班\n\n她只说了**一句话**。\n",
            )

            result = self.run_checker(str(path), "--strict")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_input_returns_usage_error(self) -> None:
        result = self.run_checker("missing-manuscript.txt")

        self.assertEqual(result.returncode, 2)
        self.assertIn("not found", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()
