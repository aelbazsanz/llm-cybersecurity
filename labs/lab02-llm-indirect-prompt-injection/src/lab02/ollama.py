from dataclasses import dataclass
import time

import httpx


@dataclass(frozen=True)
class ChatResult:
    response: str
    model: str
    duration_ms: int


class OllamaClient:
    def __init__(self, host: str, model: str, system_prompt: str) -> None:
        self._host = host
        self._model = model
        self._system_prompt = system_prompt

    def chat(self, user_prompt: str) -> ChatResult:
        start = time.monotonic()

        payload = {
            "model": self._model,
            "messages": [
                {"role": "system", "content": self._system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
        }

        with httpx.Client(timeout=120) as client:
            response = client.post(
                f"{self._host}/api/chat",
                json=payload,
            )
            response.raise_for_status()
            data = response.json()

        elapsed_ms = int((time.monotonic() - start) * 1000)

        return ChatResult(
            response=data["message"]["content"],
            model=data.get("model", self._model),
            duration_ms=elapsed_ms,
        )
