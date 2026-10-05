from pathlib import Path

from lab01_audit.findings import Finding


def generate_report(finding: Finding) -> str:
    """Generate a human-readable Markdown audit report from a finding."""

    status_label = {
        "confirmed": "Confirmed",
        "not_confirmed": "Not Confirmed",
    }.get(finding.status, finding.status)

    lines: list[str] = []

    lines.append("# LLM01:2025 Audit Report")
    lines.append("")
    lines.append("## Finding")
    lines.append("")
    lines.append(f"**Finding ID:** {finding.finding_id}")
    lines.append(f"**Title:** {finding.title}")
    lines.append(f"**Status:** {status_label}")
    lines.append(f"**Lab ID:** {finding.lab_id}")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("| --- | --- |")
    lines.append(f"| Experiments | {len(finding.experiments)} |")
    lines.append(f"| Runs | {len(finding.runs)} |")
    lines.append(f"| Sessions | {len(finding.sessions)} |")
    lines.append(f"| Models | {len(finding.models)} |")
    lines.append(
        f"| Attack interactions | "
        f"{finding.total_attack_interactions} |"
    )
    lines.append(
        f"| Successful attacks | "
        f"{finding.successful_attack_interactions} |"
    )
    lines.append(
        f"| Baseline interactions | "
        f"{len(finding.baseline_evidence)} |"
    )
    lines.append("")

    lines.append("## Models Tested")
    lines.append("")

    for model in finding.models:
        lines.append(f"- {model}")

    lines.append("")

    lines.append("## Attack Types")
    lines.append("")

    for attack_type in finding.attack_types:
        lines.append(f"- {attack_type}")

    lines.append("")

    lines.append("## Techniques")
    lines.append("")

    for technique in finding.techniques:
        lines.append(f"- {technique}")

    lines.append("")

    lines.append("## Impact")
    lines.append("")
    lines.append(finding.impact)
    lines.append("")

    if finding.mappings:
        lines.append("## Security Framework Mappings")
        lines.append("")
        lines.append("| Framework | Identifier | Name | Relationship |")
        lines.append("| --- | --- | --- | --- |")

        for mapping in finding.mappings:
            lines.append(
                f"| {mapping.framework} | {mapping.identifier} | "
                f"{mapping.name} | {mapping.relationship} |"
            )

        lines.append("")

        for mapping in finding.mappings:
            lines.append(f"### {mapping.framework} — {mapping.identifier}")
            lines.append("")
            lines.append(f"**Name:** {mapping.name}")
            lines.append(f"**Relationship:** {mapping.relationship}")
            lines.append("")
            lines.append("**Rationale:**")
            lines.append("")
            lines.append(mapping.rationale)
            lines.append("")

    if finding.mitigations:
        lines.append("## Recommended Mitigations")
        lines.append("")

        for mitigation in finding.mitigations:
            lines.append(f"- {mitigation}")

        lines.append("")

    lines.append("## Attack Evidence")
    lines.append("")

    for interaction in finding.attack_evidence:
        lines.append(_format_interaction(interaction))

    lines.append("")

    lines.append("## Baseline Evidence")
    lines.append("")

    for interaction in finding.baseline_evidence:
        lines.append(_format_interaction(interaction))

    lines.append("")

    return "\n".join(lines)


def _format_interaction(interaction) -> str:
    """Format a single interaction as a Markdown blockquote section."""

    lines: list[str] = []

    lines.append(
        f"- **Experiment:** {interaction.experiment_id or 'none'}"
    )
    lines.append(f"- **Run:** {interaction.run_id}")
    lines.append(f"- **Session:** {interaction.session_id}")
    lines.append(f"- **Turn:** {interaction.turn}")
    lines.append(f"- **Model:** {interaction.model}")
    lines.append(f"- **Technique:** {interaction.technique or 'none'}")
    lines.append(f"- **Duration:** {interaction.duration_ms} ms")
    lines.append(
        f"- **Success:** {interaction.success} "
        f"({interaction.success_reason})"
    )
    lines.append("")

    if interaction.success:
        lines.append("**User prompt:**")
    else:
        lines.append("**User prompt:**")

    lines.append("")
    lines.append(f"<blockquote>")
    lines.append(interaction.user_prompt)
    lines.append(f"</blockquote>")
    lines.append("")

    lines.append("**Model response:**")
    lines.append("")
    lines.append(f"<blockquote>")
    lines.append(interaction.response)
    lines.append(f"</blockquote>")
    lines.append("")

    return "\n".join(lines)


def write_report(finding: Finding, report_directory: str) -> Path:
    """Generate a report and write it to the given directory."""

    directory = Path(report_directory)
    directory.mkdir(parents=True, exist_ok=True)

    content = generate_report(finding)
    path = directory / f"{finding.finding_id}.md"

    path.write_text(content, encoding="utf-8")

    return path


def copy_evidence(source_files: list[Path], evidence_directory: str) -> None:
    """Copy the original JSONL evidence files into the audit evidence directory."""

    directory = Path(evidence_directory)
    directory.mkdir(parents=True, exist_ok=True)

    for source in source_files:
        destination = directory / source.name

        if source.resolve() != destination.resolve():
            destination.write_bytes(source.read_bytes())
