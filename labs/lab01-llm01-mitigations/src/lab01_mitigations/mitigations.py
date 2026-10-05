"""
Mitigation strategies for LLM01:2025 Direct Prompt Injection.

This module implements mitigation strategies that can be applied to
model outputs to prevent disclosure of the laboratory canary
(LLM-CYBER-LAB-001).

The primary mitigation is **output validation**, which checks whether
the model response contains the canary value. If the canary is detected,
the response is replaced with a safe fallback message.

Output validation is recommended by MITRE ATLAS as a mitigation for
AML.T0051.000 (LLM Prompt Injection: Direct).
"""

from lab01_mitigations.evaluator import CANARY, MitigationResult, validate_output


def apply_output_validation(response: str) -> MitigationResult:
    """
    Apply output validation to a model response.

    This is the primary mitigation for this laboratory. It inspects the
    model output for the laboratory canary and, if found, replaces the
    response with a safe fallback message.

    Args:
        response: The raw model response.

    Returns:
        A MitigationResult containing the raw response, the validated
        response, whether the canary was disclosed, and whether the
        mitigation was applied.
    """
    return validate_output(response)


MITIGATION_STRATEGIES = {
    "output-validation": apply_output_validation,
}


def get_mitigation(strategy: str):
    """Return the mitigation function for the given strategy name."""
    if strategy not in MITIGATION_STRATEGIES:
        raise ValueError(
            f"Unknown mitigation strategy: {strategy}. "
            f"Available: {', '.join(MITIGATION_STRATEGIES)}"
        )
    return MITIGATION_STRATEGIES[strategy]


# The laboratory canary value used by this mitigation lab.
# It must match the canary used by the attack laboratory.
MITIGATION_CANARY = CANARY