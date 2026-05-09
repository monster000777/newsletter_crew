from crewai import Agent
from crewai_tools import SerperDevTool
from src.newsletter_crew.config import OPENAI_MODEL, SERPER_API_KEY


class NewsletterAgents:
    """新闻通讯 Agent 工厂类"""

    def __init__(self) -> None:
        self._search_tool: SerperDevTool | None = None

    @property
    def search_tool(self) -> SerperDevTool | None:
        """懒加载搜索工具"""
        if self._search_tool is None and SERPER_API_KEY:
            self._search_tool = SerperDevTool(api_key=SERPER_API_KEY)
        return self._search_tool

    def researcher(self) -> Agent:
        """创建研究员 Agent"""
        tools = [self.search_tool] if self.search_tool else []
        return Agent(
            role="Senior Market Researcher",
            goal="Research and gather the latest and most important news and trends",
            backstory="You work at a leading tech research firm. You are expert at finding the most relevant and trending news.",
            llm=OPENAI_MODEL,
            verbose=True,
            tools=tools,
        )

    def writer(self) -> Agent:
        """创建作家 Agent"""
        return Agent(
            role="Content Writer",
            goal="Write a clear and engaging summary of the research findings",
            backstory="You are an experienced tech journalist who writes clear and engaging summaries.",
            llm=OPENAI_MODEL,
            verbose=True,
            allow_delegation=False,
        )

    def reviewer(self) -> Agent:
        """创建审核员 Agent"""
        return Agent(
            role="Editor & Fact Checker",
            goal="Review the article for accuracy and quality",
            backstory="You are a meticulous editor with 10 years of experience in tech journalism.",
            llm=OPENAI_MODEL,
            verbose=True,
            allow_delegation=False,
        )
