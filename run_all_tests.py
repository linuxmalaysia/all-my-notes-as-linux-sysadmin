
import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output for emojis in Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ANSI color codes for terminal output
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def print_banner(text):
    print(f"{CYAN}======================================{RESET}")
    print(f"{CYAN}{text}{RESET}")
    print(f"{CYAN}======================================{RESET}")

import os

def run_step(step_name, command, cwd):
    print(f"\n{CYAN}[*] Executing: {step_name}...{RESET}")
    try:
        # Use shell=True on Windows for npm since it's a cmd/bat wrapper
        is_shell = sys.platform.startswith('win') and command[0] == 'npm'
        env = {**os.environ, "CI": "true"}
        result = subprocess.run(command, cwd=cwd, check=True, shell=is_shell, env=env, stdin=subprocess.DEVNULL)
        print(f"{GREEN}✔ {step_name} passed.{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}✘ {step_name} failed! Check output above.{RESET}")
        sys.exit(e.returncode)

def main():
    root_dir = Path.cwd()
    
    print_banner("🚀 INITIALIZING FULL TEST SUITE")
    
    # 1. Run Python pytest
    # Assuming uv and pytest are available in the project environment
    run_step(
        "Python Compliance Tests (pytest)",
        [sys.executable, "-m", "pytest", "tests/"],
        root_dir
    )
    
    # 2. Run Node.js Jest
    jest_bin = root_dir / "node_modules" / "jest" / "bin" / "jest.js"
    if jest_bin.exists():
        run_step(
            "JavaScript Jest Tests (Jest CI)",
            ["node", str(jest_bin), "--ci"],
            root_dir
        )
    else:
        run_step(
            "JavaScript Jest Tests (npm test)",
            ["npm", "test"],
            root_dir
        )
    
    print(f"\n{GREEN}======================================{RESET}")
    print(f"{GREEN}🎉 100% COMPLIANCE ACHIEVED!{RESET}")
    print(f"{GREEN}======================================{RESET}")

if __name__ == '__main__':
    main()
