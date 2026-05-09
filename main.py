from src.newsletter_crew.crew import create_crew

if __name__ == "__main__":
    print("=== AI Newsletter Crew ===")
    print("Topic: AI News")
    print("Starting crew...\n")

    crew = create_crew()
    result = crew.kickoff(inputs={"topic": "AI"})

    with open("newsletter_output.md", "w", encoding="utf-8") as f:
        f.write("# AI Newsletter\n\n")
        f.write(str(result))

    print("\n=== Final Result ===")
    print("Result saved to newsletter_output.md")
