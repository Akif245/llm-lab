import os, time
from collections.abc import AsyncIterator

import httpx

from llm_lab.providers.base import LLMProvider, LLMResponse, Message

BASE = "https://generativelanguage.googleapis.com/v1beta/models"


class GeminiProvider(LLMProvider):
    name = "gemini"

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not set")
        self._client = httpx.AsyncClient(timeout=60)

    def _to_gemini(self, messages: list[Message], system: str | None) -> dict:
        """Translate our Message list -> Gemini's payload shape.

        TODO. This is the whole lesson. Handle:
          - role "assistant" -> "model"
          - role "system" in the list -> hoist to system_instruction
          - content string -> {"parts": [{"text": ...}]}
        """
        # raise NotImplementedError
        payload = {
            "contents" : []
        }
        if system:
            payload["system_instruction"] = {
        # "parts": [
        #     {
        #         "text": system
        #     }
        # ]
        ROLE_MAP = {"user": "user", "assistant": "model"}

        for m in messages:
            if m.role == "system":
                # you already decided how to handle this — apply that here
                continue
            if m.role not in ROLE_MAP:
                raise ValueError(f"unsupported role: {m.role}")
            payload["contents"].append({
                "role": ROLE_MAP[m.role],
                
                "parts": [{"text": m.content}],
            })
    }
        return payload 
        
       
        

    async def complete(self, messages, *, model, max_tokens=1024,
                       temperature=1.0, top_p=None, system=None) -> LLMResponse:
        """TODO. Measure latency yourself. Pull usage from usageMetadata."""
        raise NotImplementedError

    async def stream(self, messages, *, model, **kw) -> AsyncIterator[str]:
        raise NotImplementedError  # Day 5

    def count_tokens(self, text: str, *, model: str) -> int:
        raise NotImplementedError  # Day 3

    

if __name__ == "__main__":
    from llm_lab.providers.base import Message

    provider = GeminiProvider(api_key="dummy")

    payload = provider._to_gemini(
        messages=[
            Message(role="user", content="hi")
        ],
        system="be terse"
    )

    print(payload)