# LLM Cybersecurity

A hands-on cybersecurity laboratory focused on **Large Language Models (LLMs)** and their associated security risks.

The project follows an incremental approach: each laboratory introduces a specific LLM security concept, demonstrates it through a reproducible attack scenario, analyzes the underlying security issue, and explores appropriate mitigations.

The main goal is to develop practical knowledge of LLM security while mapping the exercises to established security frameworks such as **OWASP Top 10 for LLM Applications** and **MITRE ATLAS**.

---

## Project Goals

This project aims to:

* Understand the security risks associated with Large Language Models.
* Reproduce LLM security vulnerabilities in controlled environments.
* Develop practical offensive and defensive LLM security skills.
* Analyze attacks from both an application and model perspective.
* Map vulnerabilities and attack techniques to established security frameworks.
* Build reusable and reproducible security laboratories.
* Progress from simple LLM interactions to more complex LLM-based applications.

The laboratories are intentionally developed incrementally so that concepts introduced in earlier exercises can be reused in later ones.

---

## Project Structure

```text
llm-cybersecurity/
├── infrastructure/
│   ├── docker-compose.yml
│   ├── .env.example
│   └── INFRASTRUCTURE.md
│
├── labs/
│   ├── lab01-llm01-direct-prompt-injection/     # Attack laboratory
│   ├── lab01-llm01-audit/                       # Audit laboratory
│   └── ...
│
├── README.md
├── CLAUDE.md
└── .gitignore
```

### `infrastructure/`

Contains services and resources shared across laboratories.

The initial infrastructure provides a local **Ollama** instance running in Docker. This allows the laboratories to use local LLMs without depending on external APIs.

The infrastructure is intended to be shared between laboratories rather than duplicated inside each lab.

See [`infrastructure/INFRASTRUCTURE.md`](infrastructure/INFRASTRUCTURE.md) for setup and usage instructions.

### `labs/`

Contains the individual security laboratories.

Each laboratory is designed to be as self-contained and reproducible as possible and includes its own documentation, Python environment and application code.

Two types of laboratories exist:

* **Attack laboratories** — reproduce LLM security vulnerabilities and generate JSONL evidence.
* **Audit laboratories** — analyze the JSONL evidence, generate structured findings, and map them to security frameworks.

The audit laboratory is an independent project: it consumes evidence from the attack laboratory and stores its own output locally (in `evidence/` and `reports/`), which are excluded from version control.

---

## Technology Stack

The project currently uses:

* **Python**
* **uv** for Python project and dependency management
* **Docker / Docker Compose**
* **Ollama** for local LLM inference
* **Git** for version control

Additional technologies may be introduced as the laboratories become more advanced.

---

## Security Frameworks

The laboratories are primarily mapped against:

### OWASP Top 10 for LLM Applications

The **OWASP Top 10 for LLM Applications** provides the main vulnerability taxonomy used throughout the project.

The current focus is the **2025 edition**.

Laboratories will reference the corresponding OWASP category whenever applicable.

### MITRE ATLAS

Where an attack or technique can be mapped to **MITRE ATLAS**, the relevant technique will also be documented.

The objective is not simply to reproduce an attack, but to understand how it fits into a broader adversarial framework.

---

## Laboratory Methodology

Laboratories follow a common methodology whenever applicable:

```text
1. Understand
      ↓
2. Deploy
      ↓
3. Attack
      ↓
4. Observe
      ↓
5. Analyze
      ↓
6. Mitigate
      ↓
7. Re-test
      ↓
8. Map to security frameworks
```

Each laboratory should answer the following questions:

1. **What is the vulnerability?**
2. **Why does it occur?**
3. **How can it be exploited?**
4. **What is the security impact?**
5. **What evidence demonstrates the vulnerability?**
6. **What mitigations can be applied?**
7. **How effective are those mitigations?**
8. **How does the vulnerability map to OWASP and/or MITRE ATLAS?**

The first version of a laboratory may intentionally contain a vulnerable implementation. Mitigations are then introduced as part of the exercise rather than hiding the vulnerability from the beginning.

---

## Laboratories

| Lab | Topic | OWASP | Type |
| --- | --- | --- | --- |
| [Lab 01](labs/lab01-llm01-direct-prompt-injection/) | Direct Prompt Injection | LLM01:2025 | Attack |
| [Lab 01 Audit](labs/lab01-llm01-audit/) | Findings & Framework Mapping | LLM01:2025, LLM02:2025 | Audit |
| [Lab 01 Mitigations](labs/lab01-llm01-mitigations/) | Output Validation Mitigation | LLM01:2025 | Mitigation |
| ... | ... | ... | ... |

This table will be extended as new laboratories are added.

Each attack laboratory is typically paired with an audit laboratory. The attack laboratory reproduces the vulnerability and generates JSONL evidence; the audit laboratory analyzes that evidence, generates structured findings, and maps them to security frameworks.

---

## Environment

The project is developed and tested using Linux environments.

The main local development tools are:

```text
Python
uv
Docker
Docker Compose
Git
```

LLM inference is provided by Ollama.

The exact model used by a laboratory should be documented in that laboratory's README, since results may vary between models and model versions.

---

## Responsible Use

All attacks and security tests in this repository are intended to be performed against **controlled laboratory environments**.

The techniques demonstrated here should only be used against systems for which you have explicit authorization to perform security testing.

The purpose of this project is education, security research, defensive development, and authorized security assessment.

---

## Project Status

This project is under active development.

The initial phase focuses on fundamental LLM security vulnerabilities and progressively introduces more complex LLM application architectures.

Future laboratories may cover areas such as:

* Prompt Injection
* Sensitive Information Disclosure
* Supply Chain vulnerabilities
* Data and Model Poisoning
* Improper Output Handling
* Excessive Agency
* System Prompt Leakage
* Vector and Embedding weaknesses
* RAG security
* Model denial of service
* Insecure LLM application architectures
* Multi-step and multi-turn attacks

The exact scope and ordering may evolve as the project develops.

---

## Related Project

This repository is complementary to a separate hands-on project focused on **AI Agent cybersecurity**.

The two projects share a similar philosophy and laboratory methodology, but address different security boundaries:

```text
LLM Cybersecurity
        │
        └── LLM
             ├── Prompts
             ├── Context
             ├── Model behavior
             ├── Outputs
             └── LLM applications


AI Agent Cybersecurity
        │
        └── Agent
             ├── LLM
             ├── Tools
             ├── Memory
             ├── State
             ├── External systems
             └── Autonomous actions
```

The LLM project therefore focuses first on the security properties of the model and LLM-based applications, while the agent project focuses on the additional attack surface introduced by autonomous agents and their capabilities.

---

## Repository Conventions

Laboratory directories follow this naming convention:

```text
labXX-<topic>
```

For example:

```text
lab01-llm01-prompt-injection
lab02-...
lab03-...
```

Each laboratory should contain its own `README.md` documenting:

* Objective
* Scenario
* Architecture
* Prerequisites
* Setup
* Exercise
* Attack
* Analysis
* Mitigation
* Security framework mapping
* References

---

## Disclaimer

This repository is intended for educational and authorized security research purposes.

The author is not responsible for misuse of the techniques, code, or information contained in this repository.
