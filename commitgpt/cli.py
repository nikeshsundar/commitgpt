import sys
import click
import pyperclip
from dotenv import load_dotenv

from .git import get_staged_diff, get_recent_log, get_pr_diff, GitError
from .ai import generate_text, AIError
from .prompts import COMMIT_PROMPT, STANDUP_PROMPT, PR_PROMPT

load_dotenv()

@click.group(invoke_without_command=True)
@click.option('--copy', is_flag=True, help="Copy output to clipboard")
@click.option('--emoji', is_flag=True, help="Add emoji to commit message")
@click.pass_context
def cli(ctx, copy, emoji):
    """CommitGPT: Auto-generate commit messages, standups, and PR descriptions."""
    if ctx.invoked_subcommand is None:
        generate_commit(copy, emoji)
    else:
        ctx.ensure_object(dict)
        ctx.obj['copy'] = copy
        ctx.obj['emoji'] = emoji


def generate_commit(copy: bool, emoji: bool):
    try:
        diff = get_staged_diff()
        click.echo("Generating commit message...")
        message = generate_text(COMMIT_PROMPT, diff, emoji=emoji)
        click.echo("\n" + message + "\n")
        if copy:
            pyperclip.copy(message)
            click.echo("Copied to clipboard!")
    except (GitError, AIError) as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)

@cli.command()
@click.pass_context
def standup(ctx):
    """Generate a daily standup based on last 24h commits."""
    try:
        log = get_recent_log()
        click.echo("Generating standup...")
        message = generate_text(STANDUP_PROMPT, log)
        click.echo("\n" + message + "\n")
        if ctx.obj.get('copy'):
            pyperclip.copy(message)
            click.echo("Copied to clipboard!")
    except (GitError, AIError) as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
@click.pass_context
def pr(ctx):
    """Generate a PR description from diff main...HEAD."""
    try:
        diff = get_pr_diff()
        click.echo("Generating PR description...")
        message = generate_text(PR_PROMPT, diff)
        click.echo("\n" + message + "\n")
        if ctx.obj.get('copy'):
            pyperclip.copy(message)
            click.echo("Copied to clipboard!")
    except (GitError, AIError) as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
