from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from config import retry_config

tone_finder = Agent(
    name="ToneFinder",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
Extract the user's tone in one word from the writing samples.
Return it as a simple string like 'playful', 'serious', etc.
""",
    output_key="found_tone",
)
