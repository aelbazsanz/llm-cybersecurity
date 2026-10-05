from dataclasses import dataclass


@dataclass(frozen=True)
class FrameworkMapping:
    framework: str
    identifier: str
    name: str
    relationship: str
    rationale: str


DIRECT_PROMPT_INJECTION_MAPPINGS = (
    FrameworkMapping(
        framework="OWASP",
        identifier="LLM01:2025",
        name="Prompt Injection",
        relationship="primary_vulnerability",
        rationale=(
            "The observed attacks use direct user-supplied "
            "instructions to alter model behavior and bypass "
            "the intended system instructions."
        ),
    ),
    FrameworkMapping(
        framework="OWASP",
        identifier="LLM02:2025",
        name="Sensitive Information Disclosure",
        relationship="observed_impact",
        rationale=(
            "The direct prompt injection experiments resulted "
            "in disclosure of the protected laboratory canary."
        ),
    ),
    FrameworkMapping(
        framework="MITRE ATLAS",
        identifier="AML.T0051.000",
        name="LLM Prompt Injection: Direct",
        relationship="attack_technique",
        rationale=(
            "The experiments use direct prompt injection "
            "against the language model."
        ),
    ),
)