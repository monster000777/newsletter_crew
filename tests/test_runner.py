from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from src.newsletter_crew.runner import normalize_topic, run_newsletter, save_markdown


class RunnerTests(TestCase):
    def test_normalize_topic_rejects_empty_value(self) -> None:
        with self.assertRaises(ValueError):
            normalize_topic("   ")

    @patch("src.newsletter_crew.runner.create_crew")
    def test_run_newsletter_uses_normalized_topic(self, mock_create_crew) -> None:
        crew = mock_create_crew.return_value
        crew.kickoff.return_value = "newsletter body"

        result = run_newsletter(" AI ")

        self.assertEqual(result, "newsletter body")
        crew.kickoff.assert_called_once_with(inputs={"topic": "AI"})

    def test_save_markdown_writes_expected_content(self) -> None:
        with TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "test_output.md"

            saved_path = save_markdown("Body", "AI", str(output_path))

            self.assertEqual(saved_path, str(output_path))
            self.assertEqual(output_path.read_text(encoding="utf-8"), "# AI Newsletter\n\nBody")
