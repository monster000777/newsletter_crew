from typing import TYPE_CHECKING

from crewai import Task

if TYPE_CHECKING:
    from .agents import NewsletterAgents


class NewsletterTasks:
    """新闻通讯 Task 工厂类"""

    def __init__(self, agents: "NewsletterAgents") -> None:
        self.agents = agents

    def research_task(self) -> Task:
        """创建研究任务"""
        has_search_tool = self.agents.search_tool is not None
        description = (
            "Search for the top 5 most important {topic} news stories today. "
            "Use the search tool to find current news."
            if has_search_tool
            else "Identify the top 5 most important recent {topic} news stories. "
            "If no search tool is available, clearly state when you are uncertain about recency."
        )

        return Task(
            description=description,
            expected_output="A list of 5 {topic} news items with titles and brief descriptions",
            agent=self.agents.researcher(),
        )

    def write_task(self, context: list[Task]) -> Task:
        """创建写作任务"""
        return Task(
            description="Write a 300-word summary of the {topic} news research findings",
            expected_output="A well-written 300-word article in Chinese about today's top {topic} news",
            agent=self.agents.writer(),
            context=context,
        )

    def review_task(self, context: list[Task]) -> Task:
        """创建审核任务"""
        return Task(
            description="Review the {topic} article for accuracy, clarity, and quality",
            expected_output="A revised version of the {topic} article with any necessary corrections",
            agent=self.agents.reviewer(),
            context=context,
        )
