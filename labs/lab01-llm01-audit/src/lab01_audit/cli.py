import argparse

from lab01_audit.findings import (
    create_direct_prompt_injection_finding,
)
from lab01_audit.loader import load_interactions


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit evidence for LLM01:2025 Prompt Injection"
    )

    parser.add_argument(
        "--evidence",
        required=True,
        help="Directory containing JSONL evidence files",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    interactions = load_interactions(args.evidence)

    finding = create_direct_prompt_injection_finding(
        interactions
    )

    print("LLM01:2025 Audit")
    print("=" * 40)
    print()

    print(f"Finding: {finding.finding_id}")
    print(f"Title:   {finding.title}")
    print(f"Status:  {finding.status}")
    print()

    print(f"Lab:          {finding.lab_id}")
    print(f"Experiments:  {len(finding.experiments)}")
    print(f"Runs:         {len(finding.runs)}")
    print(f"Sessions:     {len(finding.sessions)}")
    print()

    print("Models:")

    for model in finding.models:
        print(f"  - {model}")

    print()

    print("Attack types:")

    for attack_type in finding.attack_types:
        print(f"  - {attack_type}")

    print()

    print("Techniques:")

    for technique in finding.techniques:
        print(f"  - {technique}")

    print()

    print(
        "Attack interactions: "
        f"{finding.total_attack_interactions}"
    )

    print(
        "Successful attacks:  "
        f"{finding.successful_attack_interactions}"
    )

    print(
        "Baseline interactions: "
        f"{len(finding.baseline_evidence)}"
    )

    print()

    print("Impact:")
    print(f"  {finding.impact}")


if __name__ == "__main__":
    main()