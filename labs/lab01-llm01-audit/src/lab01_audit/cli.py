import argparse
from pathlib import Path

from lab01_audit.findings import (
    create_direct_prompt_injection_finding,
)
from lab01_audit.loader import load_interactions
from lab01_audit.report import (
    generate_report,
    write_report,
    copy_evidence,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit evidence for LLM01:2025 Prompt Injection"
    )

    parser.add_argument(
        "--evidence",
        required=True,
        help="Directory containing JSONL evidence files from attack laboratory",
    )

    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory for output files (reports and evidence). "
        "Defaults to the audit laboratory's local 'evidence/' and 'reports/' directories.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    interactions = load_interactions(args.evidence)

    finding = create_direct_prompt_injection_finding(
        interactions
    )

    # Determine output directories - default to audit lab's own directories
    audit_lab_dir = Path(__file__).parent.parent.parent
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = audit_lab_dir

    reports_dir = output_dir / "reports"
    evidence_dir = output_dir / "evidence"

    # Copy original evidence files for traceability
    source_files = list(Path(args.evidence).glob("*.jsonl"))
    copy_evidence(source_files, str(evidence_dir))

    # Write the audit report
    report_path = write_report(finding, str(reports_dir))

    # Display summary
    status_label = {
        "confirmed": "Confirmed",
        "not_confirmed": "Not Confirmed",
    }.get(finding.status, finding.status)

    print("LLM01:2025 Audit")
    print("=" * 40)
    print()

    print(f"Finding: {finding.finding_id}")
    print(f"Title:   {finding.title}")
    print(f"Status:  {status_label}")
    print()

    print(f"Evidence directory: {evidence_dir}")
    print(f"Report: {report_path}")
    print()

    # Print structured overview
    print("Overview:")
    print(f"  Experiments: {len(finding.experiments)}")
    print(f"  Runs: {len(finding.runs)}")
    print(f"  Sessions: {len(finding.sessions)}")
    print(f"  Models: {len(finding.models)}")
    print(f"  Attack types: {', '.join(finding.attack_types)}")
    print(f"  Techniques: {', '.join(finding.techniques)}")
    print(f"  Total interactions: {finding.total_attack_interactions}")
    print(f"  Successful attacks: {finding.successful_attack_interactions}")
    print(f"  Baseline interactions: {len(finding.baseline_evidence)}")
    print(f"  Impact: {finding.impact}")
    print()

    # Print framework mappings
    if finding.mappings:
        print("Framework Mappings:")
        for mapping in finding.mappings:
            print(f"  - {mapping.framework}: {mapping.identifier} — {mapping.name}")
        print()

    print("Generated reports are in:", reports_dir)
    print("Evidence is stored in:", evidence_dir)
    print("Reports are not committed to the repository (local only).")


if __name__ == "__main__":
    main()