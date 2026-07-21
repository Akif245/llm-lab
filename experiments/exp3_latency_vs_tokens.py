"""
EXPERIMENT 3 -- What actually drives latency.

Fix input at ~2000 tokens. Vary max_tokens: 50, 200, 500, 1000, 2000.
Force the model to actually USE the budget (ask for a long output), otherwise
you are measuring the cap, not the generation.

Record: total latency, time-to-first-token, tokens/sec.
Plot latency vs output tokens. Then plot latency vs INPUT tokens (hold output
fixed at 200, vary input 500 -> 8000).

Two lines. One is steep, one is nearly flat. Know which and why.

This chart is the answer to "why is your agent slow?" for the next two years.
Put it in your blog post. Put it in your README.
"""
