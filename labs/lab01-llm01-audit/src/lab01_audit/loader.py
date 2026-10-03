from dataclasses import dataclass
import json
from pathlib import Path


@dataclass(frozen=True)
class Interaction:
    schema_version: str
    record_type: str
    timestamp: str
    lab_id: str
    experiment_id: str | None
    experiment_name: str | None
    run_id: str
    session_id: str
    turn: int
    model: str
    attack_type: str
    technique: str | None
    system_prompt: str
    user_prompt: str
    response: str
    duration_ms: int
    success: bool
    success_reason: str
    detection_method: str | None


def load_interactions(evidence_directory: str) -> list[Interaction]:
    directory = Path(evidence_directory)

    if not directory.exists():
        raise FileNotFoundError(
            f"Evidence directory does not exist: {directory}"
        )

    if not directory.is_dir():
        raise NotADirectoryError(
            f"Evidence path is not a directory: {directory}"
        )

    interactions: list[Interaction] = []

    for path in sorted(directory.glob("*.jsonl")):
        with path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    data = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON in {path}:{line_number}"
                    ) from exc

                interactions.append(
                    Interaction(
                        schema_version=data["schema_version"],
                        record_type=data["record_type"],
                        timestamp=data["timestamp"],
                        lab_id=data["lab_id"],
                        experiment_id=data["experiment_id"],
                        experiment_name=data["experiment_name"],
                        run_id=data["run_id"],
                        session_id=data["session_id"],
                        turn=data["turn"],
                        model=data["model"],
                        attack_type=data["attack_type"],
                        technique=data["technique"],
                        system_prompt=data["system_prompt"],
                        user_prompt=data["user_prompt"],
                        response=data["response"],
                        duration_ms=data["duration_ms"],
                        success=data["success"],
                        success_reason=data["success_reason"],
                        detection_method=data["detection_method"],
                    )
                )

    return interactions