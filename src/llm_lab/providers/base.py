"""
The provider abstraction.

WHY THIS FILE EXISTS
--------------------
Every provider (Anthropic, OpenAI, Gemini, Ollama) has a different SDK shape.
If you scatter `client.messages.create(...)` across your codebase, you are
locked in. In Month 5 you will need provider failover (primary is down ->
switch to secondary, transparently). That is only possible if there is exactly
one seam in your code where "call an LLM" happens.

This is that seam. Everything above it speaks `LLMResponse`. Everything below
it speaks vendor SDK.

Notice what is in `LLMResponse` and ask yourself why each field is there.
Two of them exist purely so that you can answer "why was that slow?" and
"why did that cost so much?" six weeks from now.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any, Literal

Role = Literal["system", "user", "assistant"]


@dataclass
class Message:
    role: Role
    content: str


@dataclass
class LLMResponse:
    """The normalized result of one LLM call."""

    text: str
    model: str
    provider: str

    input_tokens: int
    output_tokens: int

    # Cached input tokens, where the provider reports them. You will care
    # about this a lot in Week 18. Default 0 if unsupported.
    cached_input_tokens: int = 0

    latency_ms: float = 0.0
    time_to_first_token_ms: float | None = None

    stop_reason: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


class LLMProvider(ABC):
    """Implement one subclass per vendor. Keep vendor types INSIDE the subclass."""

    name: str

    @abstractmethod
    async def complete(
        self,
        messages: list[Message],
        *,
        model: str,
        max_tokens: int = 1024,
        temperature: float = 1.0,
        top_p: float | None = None,
        system: str | None = None,
    ) -> LLMResponse:
        """Single non-streaming call.

        TODO(day 2): implement in your first provider.

        Requirements:
          - Measure wall-clock latency yourself. Do not trust the SDK.
          - Populate input_tokens / output_tokens from the response usage
            object, NOT from your own tokenizer estimate. Know the difference
            between the two and why they can disagree.
          - Store the raw response dict. You will want it when something
            surprising happens.
        """
        raise NotImplementedError

    @abstractmethod
    async def stream(
        self,
        messages: list[Message],
        *,
        model: str,
        max_tokens: int = 1024,
        temperature: float = 1.0,
        top_p: float | None = None,
        system: str | None = None,
    ) -> AsyncIterator[str]:
        """Yield text deltas as they arrive.

        TODO(day 5): implement.

        The hard part is not the streaming. The hard part is that you still
        need to return usage + latency at the END. Decide how: an attribute
        set on the provider after the stream drains, a final sentinel yield,
        or return an object that wraps the iterator. There is no single right
        answer -- pick one and write down in the README why you picked it.
        Interviewers ask about this exact design choice.
        """
        raise NotImplementedError

    @abstractmethod
    def count_tokens(self, text: str, *, model: str) -> int:
        """Local token estimate, no network call.

        TODO(day 3): implement.

        Why local: you need to know if a request will FIT before you send it.
        Asking the API costs a round trip and, if it doesn't fit, an error.
        """
        raise NotImplementedError
