from crewai import Task

class NewsletterTasks:
    def __init__(self, agent):
        self.agent = agent

    def research_task(self):
        return Task(
            description="Search for the top 5 most important AI news stories today. Use the search tool to find current news.",
            expected_output="A list of 5 AI news items with titles and brief descriptions",
            agent=self.agent.researcher()
        )

    def write_task(self, context):
        return Task(
            description="Write a 300-word summary of the AI news research findings",
            expected_output="A well-written 300-word article in Chinese about today's top AI news",
            agent=self.agent.writer(),
            context=context
        )

    def review_task(self, context):
        return Task(
            description="Review the article for accuracy, clarity, and quality",
            expected_output="A revised version of the article with any necessary corrections",
            agent=self.agent.reviewer(),
            context=context
        )
