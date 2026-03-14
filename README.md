# commitgpt ⚡

> AI-powered commit messages, standups, and PR descriptions — generated from your git diff in 2 seconds.

![PyPI](https://img.shields.io/pypi/v/commitgpt)
![Python](https://img.shields.io/pypi/pyversions/commitgpt)
![License](https://img.shields.io/github/license/nikeshsundar/commitgpt)

---

## The problem

Every day as a developer you waste time writing:

- `git commit -m "fix"` — lazy, meaningless commit messages
- Standup updates — "what did I do yesterday??"
- PR descriptions — explaining your changes all over again

**commitgpt fixes all 3 with one command.**

---

## Demo
```
$ git add .
$ cmt

✨ feat(auth): add Google OAuth2 login with session timeout

- Implemented OAuth2 flow using Google provider
- Sessions expire after 30 mins of inactivity
- Fixed bug where users stayed logged in after password change
- Added redirect to dashboard on successful login
```

---

## Install
```bash
pip install commitgpt
```

---

## Setup

You only need ONE of these. Pick whichever you prefer:

---

### Option 1 — GitHub Token (FREE, recommended)

Best for beginners. No credit card. 150 requests/day free.

- Go to [github.com](https://github.com) → Settings
- Click **Developer Settings** → **Personal Access Tokens** → **Tokens (classic)**
- Click **Generate new token (classic)**
- Give it any name, no scopes needed
- Copy the token starting with `ghp_`

Create a `.env` file in your project:
```
GITHUB_TOKEN=ghp_your_token_here
```

---

### Option 2 — Gemini (FREE, best free option)

Best free option. 1,500 requests/day free. No credit card.

- Go to [aistudio.google.com](https://aistudio.google.com)
- Click **Get API Key** → **Create API key**
- Copy the key starting with `AIza`

Create a `.env` file in your project:
```
GEMINI_API_KEY=AIza_your_key_here
```

---

### Option 3 — OpenAI (Paid)

Best quality. Costs roughly $0.001 per request.

- Go to [platform.openai.com](https://platform.openai.com)
- Click **API Keys** → **Create new secret key**
- Copy the key starting with `sk-proj-`

Create a `.env` file in your project:
```
OPENAI_API_KEY=sk-proj-your_key_here
```

---

### Option 4 — Anthropic Claude (Paid)

Great quality. Costs roughly $0.001 per request.

- Go to [console.anthropic.com](https://console.anthropic.com)
- Click **API Keys** → **Create Key**
- Copy the key starting with `sk-ant-`

Create a `.env` file in your project:
```
ANTHROPIC_API_KEY=sk-ant-your_key_here
```

---

### Make your token permanent

So you never have to set it again every time you open terminal:

**Mac/Linux:**
```bash
echo 'export GITHUB_TOKEN=ghp_yourtoken' >> ~/.zshrc
source ~/.zshrc
```

**Windows:**
```bash
setx GITHUB_TOKEN "ghp_yourtoken"
```

---

## Usage

### Commit message
```bash
git add .
cmt
```

### Daily standup
```bash
cmt standup
```
Output:
```
Yesterday: Implemented OAuth2 login flow, fixed session expiry bug
Today: Writing tests for auth middleware, reviewing PR #42
Blockers: None
```

### PR description
```bash
cmt pr
```
Output:
```
## What changed
Added Google OAuth2 login with automatic session timeout after 30 minutes.

## Why
Users were being kept logged in indefinitely, creating a security risk.

## Testing
- Manual: tested login, logout, session expiry
- Unit: auth middleware coverage at 94%
- Edge: concurrent login sessions handled correctly
```

### Extra flags
```bash
cmt --emoji     # adds emoji to commit message
cmt --copy      # copies output to clipboard automatically
```

---

## How the tool picks your API

You don't need to configure anything. Just put your key in `.env` and the tool automatically detects it in this order:
```
GITHUB_TOKEN      → GitHub Models (gpt-4o-mini)
GEMINI_API_KEY    → Gemini 2.0 Flash
OPENAI_API_KEY    → OpenAI gpt-4o-mini
ANTHROPIC_API_KEY → Claude Haiku
```

First key found = that provider gets used.

---

## Requirements

- Python 3.8+
- Git installed
- Any one API key from the options above

---

## Troubleshooting

**`cmt: command not found`**
```bash
pip install commitgpt
```

**`Error: No API key found`**
Make sure your `.env` file exists with one of these:
```
GITHUB_TOKEN=ghp_...
GEMINI_API_KEY=AIza...
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
```

**`Not a git repository`**
You need to be inside a git project. Run `git init` first.

**`No staged changes found`**
Run `git add .` before running `cmt`

**`pip install fails`**
Make sure Python 3.8+ is installed:
```bash
python --version
```

---

## Contributing

Pull requests are welcome! Here's how:

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Use commitgpt to write your own commit message 😄
5. Push and open a PR

---

## License

MIT — free to use, modify and distribute.

---

Made by [nikeshsundar](https://github.com/nikeshsundar) — tired of writing "fix" as a commit message.
