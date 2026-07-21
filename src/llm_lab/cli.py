"""
CLI entry point.

TODO(day 1: get --help working. day 2+: fill in.)

Target UX:
    llm-lab chat --provider anthropic --model <model> --stream
    llm-lab chat --provider ollama --model qwen2.5 --temperature 0
    llm-lab tokens "some text" --model <model>
    llm-lab budget conversation.json --model <model>

Every completed call should print a one-line footer to stderr, e.g.:
    [anthropic/<model>] in=1,204 out=318 cached=0 | 2.41s (ttft 0.31s) | $0.0058

That footer is the whole habit. Once cost and latency are always visible,
you stop making expensive mistakes without noticing.
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="llm-lab", description="LLM primitives lab")
    p.add_argument("--version", action="store_true")
    sub = p.add_subparsers(dest="command")

    chat = sub.add_parser("chat", help="one-shot or interactive completion")
    chat.add_argument("--provider", required=True)
    chat.add_argument("--model", required=True)
    chat.add_argument("--temperature", type=float, default=1.0)
    chat.add_argument("--max-tokens", type=int, default=1024)
    chat.add_argument("--stream", action="store_true")
    chat.add_argument("--system", default=None)

    tokens = sub.add_parser("tokens", help="count tokens in text")
    tokens.add_argument("text")
    tokens.add_argument("--model", required=True)

    budget = sub.add_parser("budget", help="context budget report for a conversation")
    budget.add_argument("path")
    budget.add_argument("--model", required=True)

    return p


def main() -> None:
    args = build_parser().parse_args()
    if args.version:
        from llm_lab import __version__

        print(__version__)
        return
    # TODO: dispatch to the right handler.
    raise SystemExit("not implemented yet -- that's your job")


if __name__ == "__main__":
    main()
