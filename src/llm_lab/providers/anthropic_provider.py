"""
TODO(day 2): Implement AnthropicProvider.

Read: https://docs.claude.com/en/api/messages
Install: `uv add anthropic`

Gotchas to notice (each one is a small lesson):
  1. The system prompt is a TOP-LEVEL parameter, not a message with
     role="system". Different from OpenAI. Your `Message` dataclass allows
     role="system" -- decide how you translate it, and be consistent.
  2. `max_tokens` is REQUIRED here. It is optional elsewhere. Think about
     what a sensible default is and what happens when you hit the cap
     (check stop_reason).
  3. Usage lives on `response.usage`. Look for the cache-related fields.

Do NOT copy an implementation. Write it, break it, read the error, fix it.
"""

from llm_lab.providers.base import LLMProvider


class AnthropicProvider(LLMProvider):
    name = "anthropic"
    # TODO: __init__ (api key from env, construct AsyncAnthropic client)
    # TODO: complete()
    # TODO: stream()
    # TODO: count_tokens()
