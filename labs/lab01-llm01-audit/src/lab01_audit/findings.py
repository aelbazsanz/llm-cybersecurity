from dataclasses import dataclass

from lab01_audit.loader import Interaction


@dataclass(frozen=True)
class Finding:
    finding_id: str
    title: str
    lab_id: str
    status: str

    experiments: tuple[str, ...]
    runs: tuple[str, ...]
    sessions: tuple[str, ...]
    models: tuple[str, ...]

    attack_types: tuple[str, ...]
    techniques: tuple[str, ...]

    total_attack_interactions: int
    successful_attack_interactions: int

    attack_evidence: tuple[Interaction, ...]
    baseline_evidence: tuple[Interaction, ...]

    impact: str


def create_direct_prompt_injection_finding(
    interactions: list[Interaction],
) -> Finding:
    if not interactions:
        raise ValueError(
            "No interactions available to create a finding."
        )

    baseline = [
        interaction
        for interaction in interactions
        if interaction.attack_type == "baseline"
    ]

    attack = [
        interaction
        for interaction in interactions
        if interaction.attack_type == "direct-prompt-injection"
    ]

    successful_attack = [
        interaction
        for interaction in attack
        if interaction.success
    ]

    experiments = sorted(
        {
            interaction.experiment_id
            for interaction in attack
            if interaction.experiment_id is not None
        }
    )

    runs = sorted(
        {
            interaction.run_id
            for interaction in attack
        }
    )

    sessions = sorted(
        {
            interaction.session_id
            for interaction in attack
        }
    )

    models = sorted(
        {
            interaction.model
            for interaction in attack
        }
    )

    attack_types = sorted(
        {
            interaction.attack_type
            for interaction in attack
        }
    )

    techniques = sorted(
        {
            interaction.technique
            for interaction in attack
            if interaction.technique is not None
        }
    )

    if successful_attack:
        status = "confirmed"
        impact = (
            "Protected laboratory information was disclosed "
            "in model output during direct prompt injection "
            "experiments."
        )
    else:
        status = "not_confirmed"
        impact = (
            "No protected information was detected in the "
            "observed direct prompt injection outputs."
        )

    return Finding(
        finding_id="LLM01-DPI-001",
        title=(
            "Direct prompt injection causes protected "
            "information disclosure"
        ),
        lab_id=attack[0].lab_id if attack else interactions[0].lab_id,
        status=status,
        experiments=tuple(experiments),
        runs=tuple(runs),
        sessions=tuple(sessions),
        models=tuple(models),
        attack_types=tuple(attack_types),
        techniques=tuple(techniques),
        total_attack_interactions=len(attack),
        successful_attack_interactions=len(successful_attack),
        attack_evidence=tuple(successful_attack),
        baseline_evidence=tuple(baseline),
        impact=impact,
    )