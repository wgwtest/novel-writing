from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPOSITORY_ROOT / "novel-writing"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
OUTLINE_REFERENCE = SKILL_ROOT / "references" / "story-outline-and-causal-summary.md"


class StoryOutlineContractTests(unittest.TestCase):
    def test_skill_routes_long_form_outline_work_to_the_outline_reference(self) -> None:
        skill_text = SKILL_FILE.read_text(encoding="utf-8")

        self.assertIn("references/story-outline-and-causal-summary.md", skill_text)
        self.assertRegex(skill_text, r"volume|whole-story|story synopsis|canon")

    def test_outline_reference_defines_the_required_information_layers(self) -> None:
        outline_text = OUTLINE_REFERENCE.read_text(encoding="utf-8").casefold()

        for required_term in (
            "pre-story state",
            "story start",
            "causal bridge",
            "character knowledge",
            "author truth",
            "reveal boundary",
        ):
            with self.subTest(required_term=required_term):
                self.assertIn(required_term, outline_text)

    def test_outline_reference_requires_terms_to_be_anchored_before_use(self) -> None:
        outline_text = OUTLINE_REFERENCE.read_text(encoding="utf-8").casefold()

        self.assertIn("anchor a place, group, system, or important person before", outline_text)
        self.assertIn("necessary cause", outline_text)
        self.assertIn("encyclopedic completeness", outline_text)


if __name__ == "__main__":
    unittest.main()
