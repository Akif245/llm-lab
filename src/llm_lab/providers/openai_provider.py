"""
TODO(day 4): Implement a SECOND provider.

Use OpenAI, Gemini, or Ollama -- pick whichever you have access to. Ollama is
free and forces you to think about local inference, which matters if you ever
work somewhere data can't leave the building.

The point of day 4 is not "learn a second SDK". The point is to discover which
parts of your `base.py` abstraction were secretly Anthropic-shaped. You WILL
find at least one. Write it down in the README under "Leaky abstractions I
found". That note is interview material.
"""

from llm_lab.providers.base import LLMProvider


class OpenAIProvider(LLMProvider):
    name = "openai"
    # TODO: same four methods.
