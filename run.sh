#!/bin/bash
# SOP Team Framework Launcher

echo "========================================"
echo "  SOP TEAM FRAMEWORK"
echo "  Multi-Agent Development Pipeline"
echo "========================================"
echo

if [ -z "$1" ]; then
    python agent.py
else
    python agent.py "$@"
fi