"""
These tests are the SPEC. They fail right now. Make them pass.

Writing tests before implementation feels slow. It is not. In Week 15 you will
build eval suites, which are the same idea applied to non-deterministic
outputs. Get the reflex now while the outputs are still deterministic.
"""

import pytest

from llm_lab.cost import ModelPricing, estimate_cost


def test_simple_cost():
    pricing = ModelPricing(input_per_mtok=3.0, output_per_mtok=15.0)
    cost = estimate_cost(input_tokens=1_000_000, output_tokens=0, pricing=pricing)
    assert cost == pytest.approx(3.0)


def test_output_costs_more():
    """Output tokens are typically 3-5x the price of input tokens.
    This asymmetry drives almost every cost decision you will make."""
    pricing = ModelPricing(input_per_mtok=3.0, output_per_mtok=15.0)
    a = estimate_cost(input_tokens=10_000, output_tokens=0, pricing=pricing)
    b = estimate_cost(input_tokens=0, output_tokens=10_000, pricing=pricing)
    assert b == pytest.approx(5 * a)


def test_realistic_small_call():
    pricing = ModelPricing(input_per_mtok=3.0, output_per_mtok=15.0)
    cost = estimate_cost(input_tokens=1_200, output_tokens=300, pricing=pricing)
    assert cost == pytest.approx(0.0081, rel=1e-3)


def test_cached_tokens_are_cheaper():
    """Cache reads are usually ~10% of normal input price. This is the single
    biggest cost lever in agent systems -- see Week 18."""
    pricing = ModelPricing(
        input_per_mtok=3.0, output_per_mtok=15.0, cached_input_per_mtok=0.3
    )
    uncached = estimate_cost(input_tokens=100_000, output_tokens=0, pricing=pricing)
    cached = estimate_cost(
        input_tokens=0, output_tokens=0, cached_input_tokens=100_000, pricing=pricing
    )
    assert cached < uncached / 5


def test_zero_tokens_is_free():
    pricing = ModelPricing(input_per_mtok=3.0, output_per_mtok=15.0)
    assert estimate_cost(input_tokens=0, output_tokens=0, pricing=pricing) == 0.0
