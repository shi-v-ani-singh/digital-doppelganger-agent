from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from config import retry_config
from agents.persona_builder import persona_builder_agent

persona_storage_remote = RemoteA2aAgent(
    name="persona_storage_remote",
    agent_card="http://127.0.0.1:8001/.well-known/agent-card.json"
)

executor_agent = Agent(
    name="ExecutorAgent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction="""
1. Call persona_builder_system_local to generate persona_summary.
2. Call persona_storage_remote and send persona_summary.
3. Retrieve stored persona.
4. Answer the user using the persona.
""",
    sub_agents=[persona_builder_agent, persona_storage_remote],
)
