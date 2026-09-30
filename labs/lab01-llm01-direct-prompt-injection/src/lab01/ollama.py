from dataclasses import dataclass
import time

import httpx


@dataclass(frozen=True)
class ChatResult:
    model: str
    response: str
    duration_ms: int


class OllamaClient:
    def __init__(self, host: str, model: str) -> None:
        self.host = host.rstrip("/")
        self.model = model

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> ChatResult:
        payload = {
            "model": self.model,
            "stream": False,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        }

        start = time.perf_counter()

        response = httpx.post(
            f"{self.host}/api/chat",
            json=payload,
            timeout=300.0,
        )

        duration_ms = round(
            (time.perf_counter() - start) * 1000
        )

        response.raise_for_status()

        data = response.json()

        return ChatResult(
            model=data["model"],
            response=data["message"]["content"],
            duration_ms=duration_ms,
        )
