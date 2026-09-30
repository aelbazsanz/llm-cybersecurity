# Lab 01 — LLM01:2025 Direct Prompt Injection

## Overview

This laboratory demonstrates direct prompt injection against a Large Language Model (LLM).

The objective is to understand how user-controlled instructions can conflict with application-defined instructions and how an LLM may respond when those instructions are manipulated.

The lab uses Ollama as the local inference backend and provides a small Python client to interact with the model and record the results.

## Objectives

By completing this laboratory, you will:

* Understand the mechanics of direct prompt injection.
* Establish a baseline interaction with the target LLM.
* Test different direct prompt injection techniques.
* Observe how the model responds to conflicting instructions.
* Capture reproducible interaction logs.
* Analyze successful and unsuccessful injection attempts.
* Develop and test mitigation strategies.

## Scope

This lab focuses exclusively on **direct prompt injection**.

The initial laboratory progression is:

1. Baseline interaction
2. Instruction override
3. Persona and role manipulation
4. Instruction extraction
5. Multi-turn injection
6. Mitigation and re-testing

Indirect prompt injection is covered separately in Lab 02.

## Architecture

```text
+-------------------------+
| Python Lab Client       |
|                         |
| System Prompt           |
| User Prompt             |
+------------+------------+
             |
             | HTTP
             v
+-------------------------+
| Ollama                  |
|                         |
| Local LLM               |
| Configured model        |
+------------+------------+
             |
             v
+-------------------------+
| Interaction Logs        |
|                         |
| JSONL                   |
+-------------------------+
```

## Prerequisites

* Python 3.12+
* `uv`
* Docker
* Docker Compose
* Ollama infrastructure running
* A local Ollama model, such as `qwen3:8b`

## Configuration

The lab reads the following environment variables:

```text
OLLAMA_HOST
OLLAMA_MODEL
LAB_LOG_DIRECTORY
```

Defaults:

```text
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen3:8b
LAB_LOG_DIRECTORY=logs
```

For example:

```bash
export OLLAMA_HOST=http://localhost:11434
export OLLAMA_MODEL=qwen3:8b
```

## Installation

From this directory:

```bash
uv sync
```

## Baseline

Before executing any attack, establish a normal interaction with the model:

```bash
uv run lab01
```

Use a benign prompt such as:

```text
What is prompt injection in the context of large language models?
```

The interaction should produce a model response and create a JSONL record under:

```text
logs/
```

Inspect the generated log with:

```bash
cat logs/*.jsonl | jq
```

## Attack Techniques

### 1. Instruction Override

Attempt to override the application's existing instructions through a user-controlled prompt.

### 2. Persona and Role Manipulation

Attempt to persuade the model to adopt a different role or persona whose instructions conflict with the original application instructions.

### 3. Instruction Extraction

Attempt to make the model disclose information contained in its system-level instructions.

The laboratory uses a controlled canary value to make extraction attempts measurable.

### 4. Multi-Turn Injection

Study how instructions introduced across multiple conversation turns can influence subsequ
