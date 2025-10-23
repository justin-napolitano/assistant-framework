import subprocess, os

WHITELIST = {
    "uptime": ["uptime"],
    "df": ["df", "-h", "/"],
    "docker-ps": ["docker", "ps", "--format", "table {{.Names}}\t{{.Status}}"],
}

def run_safe(cmd: str) -> str:
    key = cmd.strip()
    if key not in WHITELIST:
        raise ValueError(f"command not allowed: {key}")
    proc = subprocess.run(WHITELIST[key], capture_output=True, text=True, env=os.environ.copy())
    return proc.stdout.strip() or proc.stderr.strip()
