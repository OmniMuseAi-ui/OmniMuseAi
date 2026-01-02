
# OmniMuseAI — Open, Free, Omni‑Channel AI Orchestrator

> ⚠️ Reality check (important): No single AI can *guarantee outcomes*, *fully replace humans*, or *act autonomously in the real world without permissions*. OmniMuseAI is designed to **orchestrate tools, agents, and channels** to get as close as legally and technically possible **today**, for **free tiers**.

---

## What OmniMuseAI Is
An **open-source orchestration layer** that:
- Unifies multiple AI models (local + free APIs)
- Adds memory, task execution, agents, and tool use
- Connects to *every practical channel* (web, mobile, chat, voice, email, socials)
- Automates as much real-world action as is legally allowed
- Is deployable **right now**, **for $0**, using free tiers

---

## What It Does That Most AIs Don’t
- ✅ Multi‑agent task execution (planner, executor, reviewer)
- ✅ Persistent memory (local + cloud)
- ✅ Real actions via APIs (email, scheduling, scraping, posting)
- ✅ Emotional‑aware responses (sentiment + adaptive tone)
- ✅ Brutally honest mode (opt‑in)
- ✅ Context carryover across channels
- ✅ Modular “skills” system
- ✅ Works online AND offline (local LLM support)

---

## Architecture (High Level)

User (Any Channel)
        ↓
Gateway (FastAPI)
        ↓
Orchestrator
 ├─ Planner Agent
 ├─ Executor Agent
 ├─ Critic Agent
 ├─ Memory Engine
 ├─ Tool Router
 └─ Safety & Policy Layer
        ↓
Tools / APIs / Models

---

## Channels Supported
- Web App (browser)
- Mobile Web (PWA)
- Telegram Bot
- Discord Bot
- Slack Bot
- Email (SMTP/IMAP)
- Voice (Speech‑to‑Text + TTS)
- Local CLI
- API (REST)

---

## FREE MODELS YOU CAN USE
| Purpose | Model | Cost |
|------|------|------|
| Local LLM | Ollama (Llama 3 / Mistral) | $0 |
| Cloud LLM | Groq | Free tier |
| Cloud LLM | OpenRouter | Free models |
| Embeddings | SentenceTransformers | $0 |
| Speech | Whisper.cpp | $0 |
| TTS | Piper TTS | $0 |

---

## STEP‑BY‑STEP: DEPLOY RIGHT NOW (FREE)

### 1️⃣ Install Prerequisites
- Python 3.10+ → https://www.python.org/downloads/
- Git → https://git-scm.com/
- Node.js (for web UI) → https://nodejs.org/
- Docker (optional) → https://www.docker.com/

---

### 2️⃣ Install Ollama (Local AI)
👉 https://ollama.com/

After install:
```
ollama pull llama3
```

---

### 3️⃣ Clone the Project
```
git clone https://github.com/YOUR_USERNAME/OmniMuseAI.git
cd OmniMuseAI
```

---

### 4️⃣ Create Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 5️⃣ Run the API Server
```
uvicorn app.main:app --reload
```

Open:
👉 http://localhost:8000/docs

---

### 6️⃣ Enable Web UI (Optional)
```
cd web
npm install
npm run dev
```

---

### 7️⃣ Add Channels

#### Telegram Bot
- Create bot → https://t.me/BotFather
- Add token to `.env`
- Run `python channels/telegram_bot.py`

#### Discord Bot
- Create app → https://discord.com/developers/applications
- Add token
- Run `python channels/discord_bot.py`

---

### 8️⃣ Memory Setup (Free)
Local:
- SQLite (default)

Vector memory:
- FAISS (local)

---

### 9️⃣ Real‑World Actions
- Email → Gmail SMTP (free)
- Calendar → Google Calendar API
- Posting → Twitter/X, Reddit APIs
- Scraping → Playwright

---

### 10️⃣ Brutally Honest Mode
Set in `.env`:
```
HONEST_MODE=true
```

---

## Safety & Legal Notes
- No impersonation
- No illegal automation
- User must approve actions
- API rate limits respected

---

## Folder Structure
```
OmniMuseAI/
├─ app/
│  ├─ main.py
│  ├─ orchestrator.py
│  ├─ agents/
│  ├─ tools/
│  ├─ memory/
│  └─ policies/
├─ channels/
├─ web/
├─ requirements.txt
└─ README.md
```

---

## What This Still Can’t Do (Truth)
- Guarantee money or virality
- Break platform rules
- Act without your permissions
- Replace human judgment

---

## Roadmap
- Autonomous task chains
- Multi‑user memory
- On‑device mobile app
- Agent marketplace

---

## License
MIT — You can build, sell, and modify.

---

If you want, I can:
- Turn this into a **real GitHub repo**
- Add **full production code**
- Build **mobile apps**
- Add **monetization**
- Customize for **your exact goal**

Just say the word.
