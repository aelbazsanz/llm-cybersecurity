from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Config:
    ollama_host: str
    ollama_model: str
    log_directory: str
    output_directory: str
    mitigation_strategy: str

    @classmethod
    def from_environment(cls) -> "Config":
        return cls(
            ollama_host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            ollama_model=os.getenv("OLLAMA_MODEL", "qwen3:8b"),
            log_directory=os.getenv("LAB01_MIG_LOG_DIRECTORY", "logs"),
            output_directory=os.getenv("LAB01_MIG_OUTPUT_DIRECTORY", "output"),
            mitigation_strategy=os.getenv(
                "LAB01_MIG_STRATEGY",
                "output-validation",
            ),
        )
