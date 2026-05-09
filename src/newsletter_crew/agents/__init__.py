from crewai import Agent
from crewai_tools import SerperDevTool
from src.newsletter_crew.config import OPENAI_MODEL, SERPER_API_KEY

class NewsletterAgents:
    def __init__(self):
        self._search_tool = None

    @property
    def search_tool(self):
        if self._search_tool is None and SERPER_API_KEY:
            self._search_tool = SerperDevTool(api_key=SERPER_API_KEY)
        return self._search_tool

    def researcher(self):
        agent_config = {
            "role": "Senior Market Researcher",
            "goal": "Research and gather the latest and most important AI news and trends",
            "backstory": "You work at a leading tech research firm. You are expert at finding the most relevant and trending news.",
            "llm": OPENAI_MODEL,
            "verbose": True
        }
        if self.search_tool:
            agent_config["tools"] = [self.search_tool]
        return Agent(**agent_config)

    def writer(self):
        return Agent(
            role="Content Writer",
            goal="Write a clear and engaging 300-word summary of the AI news",
            backstory="You are an experienced tech journalist who writes clear and engaging summaries.",
            llm=OPENAI_MODEL,
            verbose=True,
            allow_delegation=False
        )

    def reviewer(self):
        return Agent(
            role="Editor & Fact Checker",
            goal="Review the article for accuracy and quality",
            backstory="You are a meticulous editor with 10 years of experience in tech journalism.",
            llm=OPENAI_MODEL,
            verbose=True,
            allow_delegation=False
        )
