from dataclasses import dataclass
import time

import httpx


@dataclass(frozen=True)
class ChatResult:
    model: str
    response: str
    duration_ms: int


class OllamaClient:
    def __init__(
        self,
        host: str,
        model: str,
        system_prompt: str,
    ) -> None:
        self.host = host.rstrip("/")
        self.model = model

        self.messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

    def chat(self, user_prompt: str) -> ChatResult:
        self.messages.append(
            {
                "role": "user",
                "content": user_prompt,
            }
        )

        payload = {
            "model": self.model,
            "stream": False,
            "messages": self.messages,
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

        assistant_response = data["message"]["content"]

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_response,
            }
        )

        return ChatResult(
            model=data["model"],
            response=assistant_response,
            duration_ms=duration_ms,
        )
