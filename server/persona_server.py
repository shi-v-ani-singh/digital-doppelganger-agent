from agents.persona_builder import persona_builder_agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

app = to_a2a(persona_builder_agent, port=8001)
