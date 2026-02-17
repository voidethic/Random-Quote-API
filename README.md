<div align="center">

  <h1>Random Quote API ✨</h1>

  <p>
    <strong>Free, fast & open REST API</strong> delivering hand-curated motivational, funny, and programming quotes.<br>
    Built with <strong>FastAPI</strong> — modern, high-performance, automatic docs included.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/github/license/YOUR-USERNAME/Random-Quote-API?style=for-the-badge" alt="License">
    <img src="https://img.shields.io/github/stars/YOUR-USERNAME/Random-Quote-API?style=for-the-badge&color=yellow" alt="Stars">
  </p>

  <a href="https://your-random-quote-api.onrender.com/docs">
    <img src="https://img.shields.io/badge/Live%20Demo-View%20Swagger%20UI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="Live Demo">
  </a>

</div>

## 🌟 Why this API?

- One endpoint → instant random quote
- Multiple quotes in one call (up to 20)
- Categories: motivational, programming, funny, general...
- Interactive docs (Swagger + ReDoc) out of the box
- Ready for free hosting (Render, Railway, Fly.io)
- Perfect for: widgets, slack bots, daily motivation apps, blogs, portfolios

## 🚀 Quick Start (Local)

```bash
# 1. Clone
git clone https://github.com/YOUR-USERNAME/Random-Quote-API.git
cd Random-Quote-API

# 2. Install
pip install -r requirements.txt

# 3. Run (auto-reload for dev)
uvicorn main:app --reload --port 8000
