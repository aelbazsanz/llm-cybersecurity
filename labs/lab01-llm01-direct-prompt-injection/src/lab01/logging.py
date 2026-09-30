from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4


def log_interaction(
    log_directory: str,
    *,
    model: str,
    attack_type: str,
    technique: str | None,
    system_prompt: str,
    user_prompt: str,
    response: str,
    duration_ms: int,
) -> Path:
    directory = Path(log_directory)
    directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc)
    session_id = uuid4().hex

    record = {
        "timestamp": timestamp.isoformat(),
        "session_id": session_id,
        "model": model,
        "attack_type": attack_type,
        "technique": technique,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "response": response,
        "duration_ms": duration_ms,
    }

    filename = (
        f"{timestamp.strftime('%Y%m%dT%H%M%SZ')}"
        f"-{session_id}.jsonl"
    )

    path = directory / filename

    with path.open("w", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False))
        file.write("\n")

    return path
