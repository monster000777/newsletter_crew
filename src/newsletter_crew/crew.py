from crewai import Crew, Process
from src.newsletter_crew.agents import NewsletterAgents
from src.newsletter_crew.tasks import NewsletterTasks

def get_crew():
    agents = NewsletterAgents()
    tasks = NewsletterTasks(agents)

    research = tasks.research_task()
    write = tasks.write_task(context=[research])
    review = tasks.review_task(context=[write])

    return Crew(
        agents=[
            agents.researcher(),
            agents.writer(),
            agents.reviewer()
        ],
        tasks=[research, write, review],
        process=Process.sequential,
        verbose=True
    )

crew = get_crew()
