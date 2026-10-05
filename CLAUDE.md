# LLM Cybersecurity Project - CLAUDE.md

This file provides context for working with the llm-cybersecurity project, which is structured as incremental laboratories for learning cybersecurity in LLM applications.

## Project Overview

The llm-cybersecurity project is a hands-on cybersecurity laboratory focused on **Large Language Models (LLMs)** and their associated security risks. It follows an incremental approach where each laboratory introduces a specific LLM security concept, demonstrates it through a reproducible attack scenario, analyzes the underlying security issue, and explores appropriate mitigations.

## Project Structure

```
llm-cybersecurity/
├── infrastructure/
│   ├── docker-compose.yml
│   ├── .env.example
│   └── INFRASTRUCTURE.md
│
├── labs/
│   ├── lab01-llm01-direct-prompt-injection/     # Attack laboratory
│   ├── lab01-llm01-audit/                       # Audit laboratory  
│   └── [future labs will follow labXX-<topic> naming]
│
├── README.md
├── .gitignore
└── CLAUDE.md (this file)
```

### Infrastructure (`infrastructure/`)

Contains services and resources shared across laboratories:
- Provides a local Ollama instance running in Docker
- Exposes Ollama API on port 11434
- Configuration via `.env` file (OLLAMA_MODEL, OLLAMA_HOST_PORT)
- Persistent storage for Ollama models in Docker volume
- Shared between laboratories rather than duplicated

### Laboratories (`labs/`)

Each laboratory is self-contained and includes:
- Documentation (README.md)
- Python application code
- uv dependency management
- Logging and evidence generation

#### Current Laboratories

1. **lab01-llm01-direct-prompt-injection** - Attack laboratory for studying Direct Prompt Injection (OWASP LLM01:2025)
   - Uses local Ollama instance with configurable model (default: qwen3:8b)
   - Laboratory secret/canary: `LLM-CYBER-LAB-001`
   - Supports multiple attack techniques:
     - instruction-override
     - persona-role-manipulation  
     - instruction-extraction
     - multi-turn-injection
   - Generates JSONL evidence logs in `logs/` directory

2. **lab01-llm01-audit** - Audit laboratory for analyzing evidence from the attack laboratory
   - Transforms raw JSONL evidence into structured security findings
   - Maps findings to security frameworks (OWASP Top 10 for LLM Applications, MITRE ATLAS)
   - Generates local audit reports
   - Designed to be reusable across future laboratories

## Laboratory Methodology

Laboratories follow this common methodology:

```text
1. Understand      ↓
2. Deploy          ↓
3. Attack          ↓
4. Observe         ↓
5. Analyze         ↓
6. Mitigate        ↓
7. Re-test         ↓
8. Map to frameworks
```

Each laboratory should answer:
1. What is the vulnerability?
2. Why does it occur?
3. How can it be exploited?
4. What is the security impact?
5. What evidence demonstrates the vulnerability?
6. What mitigations can be applied?
7. How effective are those mitigations?
8. How does the vulnerability map to OWASP and/or MITRE ATLAS?

## Technology Stack

- **Python 3.12+**
- **uv** for Python project and dependency management
- **Docker / Docker Compose** for infrastructure orchestration
- **Ollama** for local LLM inference
- **Git** for version control

## Evidence and Logging

- Attack laboratories generate JSONL evidence logs (`*.jsonl` files)
- Each session gets a unique `session_id`
- Each interaction/log entry includes:
  - Timestamp, session_id, turn number
  - Model, attack_type, technique
  - System prompt, user prompt, model response
  - Duration, success status, success reason
  - Detection method
- Logs are intentionally kept local and excluded from Git (via .gitignore)
- Audit laboratories consume these JSONL files to generate findings

## Security Frameworks

Laboratories are mapped against:
- **OWASP Top 10 for LLM Applications** (2025 edition)
- **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems)

## Adding New Laboratories

When creating new laboratories, follow these conventions:

1. **Naming**: `labXX-<topic>` where XX is sequential number
2. **Structure**: Each lab should contain:
   - README.md with objective, scenario, architecture, prerequisites, setup, exercise, attack, analysis, mitigation, security framework mapping, references
   - Source code in `src/` directory
   - pyproject.toml for dependencies and entry points
   - Dependency groups for dev dependencies (pytest, etc.)
3. **Isolation**: Labs should be self-contained but can use shared infrastructure
4. **Audit Labs**: For each attack lab (`labXX-<topic>`), consider creating a corresponding audit lab (`labXX-<topic>-audit`) that:
   - Consumes JSONL evidence from the attack lab
   - Generates structured findings
   - Maps to security frameworks
   - Produces local reports

## Implementation Guidelines

When implementing new features or laboratories:

1. **Reproducibility**: Design experiments to be reproducible with clear setup instructions
2. **Evidence-first**: Start from observed evidence rather than predefined conclusions
3. **Traceability**: Ensure findings can be traced back to specific experiments and interactions
4. **No forced mappings**: Only map to frameworks when the relationship is justified by evidence
5. **Separation of concerns**: Keep attack and audit laboratories separate but complementary
6. **Responsible use**: All techniques should only be used in controlled, authorized environments
7. **Configuration**: Use environment variables for configurable items (models, ports, etc.)
8. **Dependencies**: Use uv for dependency management; keep runtime dependencies minimal
9. **Logging**: Follow the established JSONL logging schema for consistency

## Working with this Project

### Setting up Infrastructure

From project root:
```bash
cd infrastructure
docker compose up -d
# Verify: curl http://localhost:11434/api/tags
```

### Running an Attack Laboratory

```bash
cd labs/lab01-llm01-direct-prompt-injection
uv sync
uv run lab01 --help  # See available options
# Example: uv run lab01 --attack-type direct-prompt-injection --technique instruction-override
```

### Running an Audit Laboratory

```bash
cd labs/lab01-llm01-audit
uv sync
uv run lab01-audit --evidence ../lab01-llm01-direct-prompt-injection/logs
```

### Creating a New Laboratory

1. Create directory: `labs/labXX-<topic>/`
2. Copy structure from existing lab (README, src/, pyproject.toml)
3. Update names, descriptions, and implement specific functionality
4. Add to README.md laboratories table
5. Consider creating corresponding audit lab

### Important Notes

- Local data (logs, reports, evidence) is intentionally excluded from version control
- Each user generates their own evidence and reports from their own experiments
- The repository provides the methodology and tooling, not fixed experiment results
- Always follow responsible use principles - only test systems you own or have explicit authorization to assess