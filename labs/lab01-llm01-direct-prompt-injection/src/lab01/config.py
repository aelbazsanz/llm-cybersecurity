from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Config:
    ollama_host: str
    ollama_model: str
    log_directory: str

    @classmethod
    def from_environment(cls) -> "Config":
        return cls(
            ollama_host=os.getenv(
                "OLLAMA_HOST",
                "http://localhost:11434",
            ),
            ollama_model=os.getenv(
                "OLLAMA_MODEL",
                "qwen3:8b",
            ),
            log_directory=os.getenv(
                "LAB_LOG_DIRECTORY",
                "logs",
            ),
        )
