"""
EXPERIMENT 2 -- Temperature and determinism.

Same prompt. temperature=0, 20 runs. temperature=1.0, 20 runs.

Measure variance. Simplest honest metric: count how many of the 20 outputs are
byte-identical. Better: embed all 20 and report mean pairwise cosine distance
(you can borrow an embedding endpoint, or defer this to Month 2).

The finding that matters: temperature=0 is usually NOT fully deterministic.
Before you look up why, write your hypothesis in LEARNING_LOG.md. Then find
out. Candidates who can explain this stand out.

Extension: try a prompt with a genuinely ambiguous answer vs one with a single
correct answer. Does temperature affect them equally? Why not?
"""
