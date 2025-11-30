from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from config import retry_config

keyword_finder = Agent(
    name="KeywordFinder",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
Extract exactly 5 personality traits or keywords from the user's writing samples.
Return them as a JSON list.
""",
    output_key="found_keywords",
)
