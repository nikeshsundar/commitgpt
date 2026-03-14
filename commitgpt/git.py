import subprocess

class GitError(RuntimeError):
    pass

def _run_git(args: list[str]) -> str:
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        raise GitError("Not in a git repository.")
    
    process = subprocess.run(["git", *args], capture_output=True, text=True)
    if process.returncode != 0:
        raise GitError(process.stderr.strip() or "Unknown git error")
    return process.stdout.strip()

def get_staged_diff() -> str:
    diff = _run_git(["diff", "--staged"])
    if not diff:
        raise GitError("No staged changes found. Did you forget to git add?")
    return diff

def get_recent_log() -> str:
    log = _run_git(["log", "--since=24 hours ago", "--oneline"])
    if not log:
        raise GitError("No commits found in the last 24 hours.")
    return log

def get_pr_diff() -> str:
    try:
        diff = _run_git(["diff", "main...HEAD"])
    except GitError:
        try:
            diff = _run_git(["diff", "master...HEAD"])
        except GitError:
            raise GitError("Could not diff against main or master.")
    
    if not diff:
        raise GitError("No differences found between main/master and HEAD.")
    return diff
