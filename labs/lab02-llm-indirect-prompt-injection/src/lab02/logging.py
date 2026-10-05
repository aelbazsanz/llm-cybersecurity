from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4


LOG_SCHEMA_VERSION = "1.0"


def create_session_id() -> str:
    return uuid4().hex


def create_run_id() -> str:
    return uuid4().hex


def log_interaction(
    log_directory: str,
    *,
    lab_id: str,
    experiment_id: str | None,
    experiment_name: str | None,
    run_id: str,
    session_id: str,
    turn: int,
    model: str,
    attack_type: str,
    technique: str | None,
    source_type: str | None,
    system_prompt: str,
    user_prompt: str,
    response: str,
    duration_ms: int,
    success: bool,
    success_reason: str,
    detection_method: str | None,
) -> Path:
    directory = Path(log_directory)
    directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc)

    record = {
        "schema_version": LOG_SCHEMA_VERSION,
        "record_type": "interaction",
        "timestamp": timestamp.isoformat(),
        "lab_id": lab_id,
        "experiment_id": experiment_id,
        "experiment_name": experiment_name,
        "run_id": run_id,
        "session_id": session_id,
        "turn": turn,
        "model": model,
        "attack_type": attack_type,
        "technique": technique,
        "source_type": source_type,
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "response": response,
        "duration_ms": duration_ms,
        "success": success,
        "success_reason": success_reason,
        "detection_method": detection_method,
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
