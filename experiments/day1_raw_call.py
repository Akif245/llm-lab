"""Day 1: see the wire format before any SDK hides it."""
import json, os, time
import httpx
from dotenv import load_dotenv

load_dotenv()

# MODEL = "gemini-2.5-flash"
# MODEL = "gemini-3.5-flash"
MODEL = "gemini-3.5-flash-lite"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

payload = {
    "system_instruction": {"parts": [{"text": "You are terse."}]},
    "contents": [
        {"role": "system", "parts": [{"text": "You are terse."}]},

        {"role": "user", "parts": [{"text": "Explain what a token is in two sentences."}]}
    ],
    "generationConfig": {"maxOutputTokens": 200, "temperature": 1.0},
}

start = time.perf_counter()
r = httpx.post(
    url,
    headers={
        "x-goog-api-key": os.environ["GOOGLE_API_KEY"],
        "content-type": "application/json",
    },
    json=payload,
    timeout=60,
)
elapsed = time.perf_counter() - start

print(f"HTTP {r.status_code}   {elapsed:.2f}s\n")
print(json.dumps(r.json(), indent=2))

os.makedirs("runs", exist_ok=True)
with open("runs/day1_raw_response.json", "w") as f:
    json.dump(r.json(), f, indent=2)