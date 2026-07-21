"""
Cost accounting.

TODO(day 3): implement `estimate_cost`.

Prices are NOT hardcoded here on purpose. They change, and a roadmap that
hardcodes them is wrong within a month. Go read each provider's pricing page
yourself and fill in pricing.toml. Doing this once by hand is how the numbers
become intuitive.

Note the unit trap: providers quote price PER MILLION TOKENS. Getting this
wrong by 1000x is the single most common bug in student cost trackers.
"""

from dataclasses import dataclass


@dataclass
class ModelPricing:
    """USD per 1,000,000 tokens."""

    input_per_mtok: float
    output_per_mtok: float
    cached_input_per_mtok: float | None = None


def load_pricing(path: str = "pricing.toml") -> dict[str, ModelPricing]:
    """TODO: parse pricing.toml -> {model_name: ModelPricing}."""
    raise NotImplementedError


def estimate_cost(
    *,
    input_tokens: int,
    output_tokens: int,
    cached_input_tokens: int = 0,
    pricing: ModelPricing,
) -> float:
    """Return USD cost of one call.

    TODO. Make tests/test_cost.py pass.

    Question to answer in your LEARNING_LOG before you write this:
    if cached_input_tokens is 500 and input_tokens is 2000, is the cached
    500 included in the 2000 or additional to it? Check the docs. Guessing
    here produces a cost tracker that is quietly wrong.
    """
    raise NotImplementedError
