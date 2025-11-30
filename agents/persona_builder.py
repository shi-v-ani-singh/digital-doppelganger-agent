from google.adk.agents import SequentialAgent, ParallelAgent

from agents.tone_finder import tone_finder
from agents.keyword_finder import keyword_finder
from agents.style_finder import style_finder
from agents.persona_aggregator import persona_aggregator_agent

parallel_persona_team = ParallelAgent(
    name="ParallelPersonaTeam",
    sub_agents=[tone_finder, keyword_finder, style_finder],
)

persona_builder_agent = SequentialAgent(
    name="persona_builder_system",
    sub_agents=[parallel_persona_team, persona_aggregator_agent],
)
