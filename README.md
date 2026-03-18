# SOP(Team) Framework

A generic, reusable multi-agent software development framework powered by Claude Code subagents. Inspired by MetaGPT, this framework orchestrates a complete software team: Product Manager → Architect → Engineer → QA → DevOps.

## Overview

This framework implements a strict SOP (Standard Operating Procedure) pipeline that transforms any software requirement into complete deliverables:

```
Requirement Input
       ↓
Product Manager → PRD.md
       ↓
Architect → ARCHITECTURE.md + TASKS.md
       ↓
Engineer → src/ (all code)
       ↓
QA Engineer → tests/ + QA_REPORT.md
       ↓
DevOps → DEPLOYMENT.md + deploy/
       ↓
Final Report → FINAL_REPORT.md
```

## Features

- **Fully Generic**: No assumptions about technology, industry, or project type
- **Sequential Pipeline**: Strict SOP ensures consistent, high-quality output
- **Multi-Agent**: Specialized agents for each phase of development
- **Self-Contained**: All outputs written to the workspace directory
- **Retry Logic**: Failed steps are automatically retried

## Quick Start

### Option 1 — Python SDK
```bash
pip install -r requirements.txt
python agent.py "Build a REST API for user authentication"
```

### Option 2 — Shell Script
```bash
chmod +x run.sh
./run.sh "Create a data pipeline for ETL processing"
```

### Option 3 — Direct Claude CLI
```bash
claude
> Use the coordinator agent at .claude/agents/coordinator.md
> Then provide your requirement
```

## Agents

### Agent Models

Setup 2 — Alibaba Coding Plan (Default):
    coordinator     → kimi-k2.5          (SWE-Bench 76.8% — agentic orchestration)
    product-manager → qwen3.5-plus       (Deep Thinking + Vision — requirement analysis)
    architect       → MiniMax-M2.5       (SWE-Bench 80.2% — strongest design model)
    engineer        → qwen3-coder-next   (SWE-Bench 70.6% — purpose-built coding)
    qa-engineer     → glm-4.7            (SWE-Bench 73.8% — strong bug detection)
    devops          → qwen3-coder-plus   (Lightweight — fast config generation)

Setup 1 — Claude Models (Fallback):
    coordinator     → claude-opus-4-5    (SWE-Bench 80.9%)
    product-manager → claude-sonnet-4-5  (SWE-Bench 77.2%)
    architect       → claude-opus-4-5    (SWE-Bench 80.9%)
    engineer        → claude-sonnet-4-5  (SWE-Bench 77.2%)
    qa-engineer     → claude-haiku-4-5   (Fast + cheap)
    devops          → claude-haiku-4-5   (Fast + cheap)

### Switching Setups

To use Alibaba models (Setup 2 — default):
    export ALIBABA_API_KEY=your-alibaba-coding-plan-key
    python agent.py "your requirement"

To use Claude models (Setup 1 — fallback):
    export SOP_SETUP=1
    export ANTHROPIC_API_KEY=your-anthropic-key
    python agent.py "your requirement"

## Output Files

All outputs are written to the `workspace/` directory:

```
workspace/
├── docs/
│   ├── PRD.md              # Product Requirements Document
│   ├── ARCHITECTURE.md     # System Architecture
│   ├── TASKS.md            # Implementation Tasks
│   ├── CODE_SUMMARY.md     # Code Documentation
│   └── DEPLOYMENT.md       # Deployment Guide
├── src/                    # All source code
├── tests/                  # All test files
├── reports/
│   ├── QA_REPORT.md        # Test Results
│   ├── FINAL_REPORT.md     # Complete Summary
│   └── SOP_LOG.md          # Execution Log
└── deploy/                 # Deployment configs
```

## The SOP

1. **Requirements Phase** — Product Manager analyzes and documents requirements
2. **Architecture Phase** — Architect designs the complete system
3. **Implementation Phase** — Engineer writes production-quality code
4. **QA Phase** — QA Engineer writes tests, runs them, reports results
5. **Deployment Phase** — DevOps creates deployment documentation and configs
6. **Final Report** — Coordinator summarizes everything

## Directory Structure

```
sop-team-framework/
├── .claude/
│   └── agents/
│       ├── coordinator.md      # Master orchestrator
│       ├── product-manager.md  # PRD writer
│       ├── architect.md        # System designer
│       ├── engineer.md         # Code implementer
│       ├── qa-engineer.md      # Test writer
│       └── devops.md           # Deployment planner
├── workspace/
│   ├── docs/                   # Documentation output
│   ├── src/                    # Source code output
│   ├── tests/                  # Test files output
│   ├── reports/                # Reports output
│   └── deploy/                 # Deployment configs
├── agent.py                    # Python entry point
├── run.sh                      # Shell launcher
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Usage Examples

```bash
# Web application
python agent.py "Build a blog platform with user authentication and comments"

# API development
python agent.py "Create a GraphQL API for an e-commerce product catalog"

# Data pipeline
python agent.py "Build an ETL pipeline that processes CSV files into a PostgreSQL database"

# Mobile backend
python agent.py "Design and implement a backend API for a fitness tracking mobile app"

# Automation
python agent.py "Create an automated invoice generation and email system"
```

## Requirements

- Python 3.8+
- `claude-agent-sdk` (auto-installed if missing)
- `python-dotenv`

## Environment Variables

Set these in a `.env` file if using the Python SDK:

```
ALIBABA_API_KEY=your-alibaba-coding-plan-key
```

For Claude models, set:
```
SOP_SETUP=1
ANTHROPIC_API_KEY=your-anthropic-key
```

## License

MIT License — Free to use, modify, and distribute.