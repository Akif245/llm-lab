# llm-lab

Week 1 of my AI Agent Engineering roadmap. A small CLI for calling LLM providers
through one interface, with token counting, cost accounting, and latency
measurement built in from the first commit.

Not a library anyone should depend on. An instrument for measuring things I was
about to take on faith.

## Status

Skeleton. Implementing across week of _____.

## Setup

```bash
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
cp .env.example .env   # add your keys
pytest                 # currently failing -- that's the spec
```

## Usage (target)

```bash
llm-lab chat --provider anthropic --model <model> --stream
llm-lab tokens "hello world" --model <model>
llm-lab budget conversation.json --model <model>
```

## Build order

- [ ] Day 1 — env, repo, `base.py` interface, `--help` works
- [ ] Day 2 — provider #1, non-streaming, real API call
- [ ] Day 3 — token counting + cost, `pytest` green
- [ ] Day 4 — provider #2 behind the same interface
- [ ] Day 5 — streaming, time-to-first-token
- [ ] Day 6 — experiments 1–3
- [ ] Day 7 — refactor, write-up, push

---

## Notes to fill in as I go

### Design decisions

**How I returned usage from a streaming call, and why**
> (Day 5. Three options: attribute set after drain, sentinel yield, wrapper
> object. Pick one, justify it in 3 sentences.)

**How I mapped `role="system"` across providers**
> (Day 4.)

### Leaky abstractions I found
> (Day 4. What in `base.py` turned out to be secretly shaped like provider #1?)

### Measurements

**Local token count vs API-reported input_tokens**
> Delta: ___ %. Cause: ___

**Is temperature=0 deterministic?**
> My hypothesis before testing: ___
> What I measured: ___
> Actual reason: ___

**Latency vs output tokens**
> Slope: ___ ms per output token.
> Latency vs input tokens slope: ___ ms per 1000 input tokens.
> Ratio: ___

### What broke and what I learned
> (One entry per day. This becomes interview material -- don't skip it.)
