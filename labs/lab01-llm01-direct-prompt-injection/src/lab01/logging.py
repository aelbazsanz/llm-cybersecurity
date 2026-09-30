from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4


def create_session_id() -> str:
    return uuid4().hex


def log_interaction(
    log_directory: str,
    *,
    session_id: str,
    turn: int,
    model: str,
    attack_type: str,
    technique: str | None,
    system_prompt: str,
    user_prompt: str,
    response: str,
    duration_ms: int,
    success: bool,
    success_reason: str,
) -> Path:
    directory = Path(log_directory)
    directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc)

    record = {
        "timestamp": timestamp.isoformat(),
        "session_id": session_id,
        "turn": turn,
        "model": model,
        "attack_type": attack_type,
        "technique": technique,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "response": response,
        "duration_ms": duration_ms,
        "success": success,
        "success_reason": success_reason,
    }

    path = directory / f"{session_id}.jsonl"

    with path.open("a", encoding="utf-8") as file:
        file.write(
            json.dumps(
                record,
                ensure_ascii=False,
            )
        )
        file.write("\n")

    return path
