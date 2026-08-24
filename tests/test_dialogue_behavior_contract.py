from __future__ import annotations

import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPOSITORY_ROOT / "novel-writing"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
DIALOGUE_REFERENCE = SKILL_ROOT / "references" / "dialogue-and-behavior.md"
PLANNING_REFERENCE = SKILL_ROOT / "references" / "planning.md"


class DialogueBehaviorContractTests(unittest.TestCase):
    def test_skill_routes_drafting_and_review_to_dialogue_behavior_guidance(self) -> None:
        skill_text = SKILL_FILE.read_text(encoding="utf-8")

        self.assertIn("references/dialogue-and-behavior.md", skill_text)
        self.assertIn("Dialogue Must Happen Through Behavior", skill_text)

    def test_reference_distinguishes_functional_beats_from_surface_motion(self) -> None:
        reference_text = DIALOGUE_REFERENCE.read_text(encoding="utf-8").casefold()

        for required_term in (
            "functional action",
            "decorative action",
            "procedural action",
            "reaction changes the next beat",
            "meeting",
            "laboratory",
        ):
            with self.subTest(required_term=required_term):
                self.assertIn(required_term, reference_text)

    def test_reference_rejects_mechanical_emotion_tags_as_a_repair(self) -> None:
        reference_text = DIALOGUE_REFERENCE.read_text(encoding="utf-8").casefold()

        self.assertIn("emotion labels are not a substitute", reference_text)
        self.assertIn("rapid dialogue may remain untagged", reference_text)
        self.assertIn("action density is not a quality target", reference_text)
        self.assertIn("do not distribute beats evenly", reference_text)

    def test_planning_requires_behavior_design_before_assigning_speeches(self) -> None:
        planning_text = PLANNING_REFERENCE.read_text(encoding="utf-8").casefold()

        self.assertIn("dialogue behavior map", planning_text)
        self.assertIn("do not preassign a speech to every participant", planning_text)


if __name__ == "__main__":
    unittest.main()
