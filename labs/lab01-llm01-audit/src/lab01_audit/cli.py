import argparse

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

    experiment_ids = {
        interaction.experiment_id
        for interaction in interactions
        if interaction.experiment_id is not None
    }

    run_ids = {
        interaction.run_id
        for interaction in interactions
    }

    session_ids = {
        interaction.session_id
        for interaction in interactions
    }

    models = sorted(
        {
            interaction.model
            for interaction in interactions
        }
    )

    successful_interactions = sum(
        interaction.success
        for interaction in interactions
    )

    print("LLM01:2025 Audit")
    print("=" * 40)
    print()
    print(f"Evidence directory: {args.evidence}")
    print()
    print(f"Interactions: {len(interactions)}")
    print(f"Experiments:  {len(experiment_ids)}")
    print(f"Runs:         {len(run_ids)}")
    print(f"Sessions:     {len(session_ids)}")
    print(
        f"Successful:   {successful_interactions}"
    )
    print(
        f"Failed:       {len(interactions) - successful_interactions}"
    )
    print()
    print("Models:")

    for model in models:
        print(f"  - {model}")


if __name__ == "__main__":
    main()