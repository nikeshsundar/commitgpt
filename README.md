<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=50&color=00D4FF¢er=true&vCenter=true&height=80&width=500&lines=commitgpt" alt="commitgpt">
</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-00D4FF?style=for-the-badge&logo=version&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-FF6B6B?style=for-the-badge&logo=license&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.8+-00D4FF?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Open%20Source-%F0%9F%92%9A-green?style=for-the-badge&logo=opensource&logoColor=white">
</p>
---
<div align="center">
![commitgpt Banner](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2D2D2D,26,00D4FF&height=300§ion=header&text=AI-Powered+Git+Commit+Messages&fontSize=55&animation=fadeIn&align=center)
</div>
---
> ⚡ AI-powered commit messages, standups, and PR descriptions — generated from your git diff in 2 seconds.
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Lightning.png" width="30"/> The Problem
</h2>
Every day as a developer you waste time writing:
| ❌ | ✅ |
|----|-----|
| `git commit -m "fix"` — lazy, meaningless | **commitgpt** generates descriptive messages |
| Standup updates — "what did I do yesterday??" | **commitgpt** writes standups for you |
| PR descriptions — explaining changes all over again | **commitgpt** creates detailed PR descriptions |
**commitgpt fixes all 3 with one command.**
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Desktop%20Computer.png" width="30"/> Demo
</h2>
```bash
$ git add .
$ cmt
✨ feat(auth): add Google OAuth2 login with session timeout
- Implemented OAuth2 flow using Google provider
- Sessions expire after 30 mins of inactivity
- Fixed bug where users stayed logged in after password change
- Added redirect to dashboard on successful login
```
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="30"/> Install
</h2>
```bash
pip install commitgpt-nikesh
```
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Key.png" width="30"/> Setup
</h2>
You only need **ONE** of these. Pick whichever you prefer:
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
**Mac/Linux:**
```bash
echo 'export GITHUB_TOKEN=ghp_yourtoken' >> ~/.zshrc
source ~/.zshrc
```
**Windows:**
```cmd
setx GITHUB_TOKEN "ghp_yourtoken"
```
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Clipboard.png" width="30"/> Usage
</h2>
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
```markdown
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
| Flag | Description |
|------|-------------|
| `--emoji` | adds emoji to commit message |
| `--copy` | copies output to clipboard automatically |
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Brain.png" width="30"/> How the tool picks your API
</h2>
You don't need to configure anything. Just put your key in `.env` and the tool automatically detects it in this order:
```
GITHUB_TOKEN     → GitHub Models (gpt-4o-mini)
GEMINI_API_KEY   → Gemini 2.0 Flash
OPENAI_API_KEY   → OpenAI gpt-4o-mini
ANTHROPIC_API_KEY → Claude Haiku
```
First key found = that provider gets used.
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Check%20Box.png" width="30"/> Requirements
</h2>
| Requirement | Description |
|-------------|-------------|
| 🐍 Python | 3.8+ |
| 📦 Git | Installed |
| 🔑 API Key | Any one from the options above |
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Warning.png" width="30"/> Troubleshooting
</h2>
| Problem | Solution |
|---------|----------|
| `cmt: command not found` | `pip install commitgpt` |
| `Error: No API key found` | Ensure `.env` file exists with one of: `GITHUB_TOKEN`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, or `ANTHROPIC_API_KEY` |
| `Not a git repository` | Run `git init` first |
| `No staged changes found` | Run `git add .` before running `cmt` |
| `pip install fails` | Verify Python 3.8+: `python --version` |
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Handshake.png" width="30"/> Contributing
</h2>
Pull requests are welcome! Here's how:
1. Fork the repo
2. Create a branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Use commitgpt to write your own commit message 😄
4. Push and open a PR
---
<h2>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Page%20Facing%20Up.png" width="30"/> License
</h2>
> MIT — free to use, modify and distribute.
---
<div align="center">
![Star Badge](https://img.shields.io/github/stars/nikeshsundar/commitgpt?style=social)
![Fork Badge](https://img.shields.io/github/forks/nikeshsundar/commitgpt?style=social)
![Watch Badge](https://img.shields.io/github/watchers/nikeshsundar/commitgpt?style=social)
**Made with ❤️ by [Nikesh Sundar](https://github.com/nikeshsundar)**
![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2D2D2D,26,00D4FF&height=100§ion=footer)
</div>
