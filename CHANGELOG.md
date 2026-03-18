# Changelog

All notable changes to the SOP(Team) Framework will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-19

### Added
- Initial release of SOP(Team) Framework
- Multi-agent pipeline: Product Manager → Architect → Engineer → QA → DevOps
- Support for both Alibaba Coding Plan and Claude models
- Dual model setup with SOP_SETUP environment variable
- Coordinator agent for orchestrating the full pipeline
- Comprehensive PRD generation with standard sections
- System architecture design with technology selection
- Production-quality code implementation
- Test generation and execution
- Deployment documentation and configs

### Agents
- `coordinator` - Master SOP orchestrator (kimi-k2.5 / claude-opus-4-5)
- `product-manager` - Requirements analysis (qwen3.5-plus / claude-sonnet-4-5)
- `architect` - System design (MiniMax-M2.5 / claude-opus-4-5)
- `engineer` - Code implementation (qwen3-coder-next / claude-sonnet-4-5)
- `qa-engineer` - Testing (glm-4.7 / claude-haiku-4-5)
- `devops` - Deployment planning (qwen3-coder-plus / claude-haiku-4-5)

### Features
- Fully generic framework - no technology assumptions
- Sequential SOP pipeline with strict ordering
- Automatic retry on failures
- Comprehensive logging to SOP_LOG.md
- Support for any software project type

[0.1.0]: https://github.com/shalinda-j/SOP-Team/releases/tag/v0.1.0