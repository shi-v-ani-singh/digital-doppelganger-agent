from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from config import retry_config

persona_aggregator_agent = Agent(
    name="PersonaAgreggatorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""
Combine the outputs into a single persona JSON:

Tone: {found_tone}
Keywords: {found_keywords}
Style: {found_style}

Return JSON with keys: "tone", "keywords", "style".
""",
    output_key="persona_summary",
)
