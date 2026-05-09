from pathlib import Path

from .crew import create_crew


DEFAULT_OUTPUT_PATH = "newsletter_output.md"


def normalize_topic(topic: str) -> str:
    """Return a usable topic string for crew execution."""
    cleaned_topic = topic.strip()
    if not cleaned_topic:
        raise ValueError("Topic must not be empty.")
    return cleaned_topic


def run_newsletter(topic: str) -> str:
    """Run the newsletter crew and return the final content."""
    normalized_topic = normalize_topic(topic)
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": normalized_topic})
    return str(result)


def save_markdown(content: str, topic: str, output_path: str = DEFAULT_OUTPUT_PATH) -> str:
    """Persist newsletter content as markdown and return the file path."""
    normalized_topic = normalize_topic(topic)
    path = Path(output_path)
    path.write_text(f"# {normalized_topic} Newsletter\n\n{content}", encoding="utf-8")
    return str(path)
