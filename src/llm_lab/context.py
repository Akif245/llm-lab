"""
Context budgeting -- Experiment 1.

TODO(day 3 / Saturday): implement.

This module answers: "given this conversation and this model, how close am I
to the limit, and what gets dropped first?"

It looks trivial. It is the seed of everything you build in Week 10 (memory
and compaction). Take it seriously.
"""

from dataclasses import dataclass

from llm_lab.providers.base import Message


@dataclass
class ContextReport:
    used_tokens: int
    limit_tokens: int
    reserved_for_output: int

    @property
    def available(self) -> int:
        return self.limit_tokens - self.used_tokens - self.reserved_for_output

    @property
    def utilization(self) -> float:
        return self.used_tokens / self.limit_tokens


def report(
    messages: list[Message],
    *,
    limit_tokens: int,
    reserved_for_output: int = 1024,
    count_tokens,
) -> ContextReport:
    """TODO.

    Subtlety worth chasing down: the token count of a conversation is NOT the
    sum of token counts of each message's text. There is per-message and
    per-turn overhead from the chat template. Measure the discrepancy for
    yourself: count a 10-message conversation locally, send it, compare to the
    usage the API reports. Record the delta in your LEARNING_LOG.
    """
    raise NotImplementedError


def plan_eviction(messages: list[Message], *, target_tokens: int, count_tokens):
    """Return which messages you would drop, in order, to fit target_tokens.

    TODO. Naive answer: drop oldest first.
    Now ask: what if message[0] is the system prompt? What if message[3] is
    where the user stated the actual goal? Implement naive first, then write
    down in the README why naive is wrong. You will fix it properly in Week 10.
    """
    raise NotImplementedError
