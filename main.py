import sys

from src.newsletter_crew.runner import run_newsletter, save_markdown


DEFAULT_TOPIC = "AI"

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TOPIC

    print("=== AI Newsletter Crew ===")
    print(f"Topic: {topic} News")
    print("Starting crew...\n")

    result = run_newsletter(topic)
    output_path = save_markdown(result, topic)

    print("\n=== Final Result ===")
    print(f"Result saved to {output_path}")
