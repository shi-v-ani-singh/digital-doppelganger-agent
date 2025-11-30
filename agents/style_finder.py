from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from config import retry_config

style_finder = Agent(
    name="StyleFinder",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
Analyse the user's writing samples and summarize their writing style
in 2-3 descriptive words.
""",
    output_key="found_style",
)
