"""SOP(Team) Framework - Main Agent Module."""

import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Model Setup ──────────────────────────────────
# Setup 1: Claude Models  → set SOP_SETUP=1
# Setup 2: Alibaba Models → set SOP_SETUP=2 (default)
SETUP = os.getenv("SOP_SETUP", "2")

if SETUP == "2":
    os.environ.setdefault("ANTHROPIC_BASE_URL", "https://api.alibaba-modelstudio.com/v1")
    os.environ["ANTHROPIC_API_KEY"] = os.getenv("ALIBABA_API_KEY") or os.getenv("ANTHROPIC_API_KEY", "")
    ACTIVE_MODELS = {
        "coordinator":     "kimi-k2.5",
        "product-manager": "qwen3.5-plus",
        "architect":       "MiniMax-M2.5",
        "engineer":        "qwen3-coder-next",
        "qa-engineer":     "glm-4.7",
        "devops":          "qwen3-coder-plus",
    }
else:
    ACTIVE_MODELS = {
        "coordinator":     "claude-opus-4-5",
        "product-manager": "claude-sonnet-4-5",
        "architect":       "claude-opus-4-5",
        "engineer":        "claude-sonnet-4-5",
        "qa-engineer":     "claude-haiku-4-5",
        "devops":          "claude-haiku-4-5",
    }

print(f"\n>> SOP(Team) Framework - Model Setup {SETUP}")
for role, model in ACTIVE_MODELS.items():
    print(f"   {role:<20} -> {model}")
print()
# ─────────────────────────────────────────────────

LOG_FILE = "./workspace/reports/SOP_LOG.md"


def log(message: str):
    """Log a message to both console and SOP log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    os.makedirs("./workspace/reports", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(entry)
    print(entry.strip())


async def run_sop_team(requirement: str):
    """Run the SOP team with the given requirement.

    Args:
        requirement: The software development requirement to process.

    Returns:
        None. Outputs are written to the workspace/ directory.
    """
    try:
        from claude_agent_sdk import query, ClaudeAgentOptions
    except ImportError:
        print("Installing claude-agent-sdk...")
        os.system("pip install claude-agent-sdk python-dotenv")
        from claude_agent_sdk import query, ClaudeAgentOptions

    log("=" * 60)
    log("SOP TEAM FRAMEWORK STARTED")
    log(f"Requirement: {requirement}")
    log("=" * 60)

    # Find coordinator agent definition
    package_dir = Path(__file__).parent
    coordinator_path = package_dir / "agents" / "coordinator.md"

    if coordinator_path.exists():
        with open(coordinator_path, "r") as f:
            coordinator_prompt = f.read()
    else:
        # Fallback to workspace-relative path
        coordinator_path = Path(".claude/agents/coordinator.md")
        if coordinator_path.exists():
            with open(coordinator_path, "r") as f:
                coordinator_prompt = f.read()
        else:
            coordinator_prompt = "You are the SOP Coordinator. Execute the full pipeline."

    try:
        async for message in query(
            prompt=f"""New development requirement:

{requirement}

Begin the SOP pipeline now. Execute all steps in sequence. Do not skip any step.""",
            options=ClaudeAgentOptions(
                allowed_tools=["Agent", "Read", "Write", "Edit", "Bash"],
                permission_mode="acceptEdits",
                system_prompt=coordinator_prompt,
                max_turns=100,
            ),
        ):
            if hasattr(message, 'content'):
                for block in message.content:
                    if hasattr(block, 'text') and block.text:
                        print(block.text)
                    elif hasattr(block, 'name'):
                        log(f"Invoking agent/tool: {block.name}")
            elif hasattr(message, 'subtype'):
                log(f"SOP TEAM FINISHED — Status: {message.subtype}")
    except Exception as e:
        log(f"ERROR: {str(e)}")
        print(f"\nError running SOP team: {e}")
        print("\nTo use this framework directly with Claude CLI:")
        print("  claude")
        print("  > Use the coordinator agent to process your requirement")


def main():
    """Main entry point for the sop-team CLI command."""
    if len(sys.argv) > 1:
        requirement = " ".join(sys.argv[1:])
    else:
        print("\n" + "=" * 50)
        print("  SOP TEAM FRAMEWORK")
        print("  Multi-Agent Software Development Pipeline")
        print("=" * 50)
        print()
        requirement = input("Enter your development requirement:\n> ")

    if requirement.strip():
        asyncio.run(run_sop_team(requirement))
    else:
        print("No requirement provided. Exiting.")


if __name__ == "__main__":
    main()