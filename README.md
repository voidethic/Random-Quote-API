<div align="center">
  <img src="https://img.shields.io/badge/RandomQuote%20API-✨-brightgreen?style=for-the-badge" alt="Random Quote API ✨">
  <h1>Random Quote API ✨</h1>
  <p>
    <strong>Free & beautiful REST API</strong> for hand-curated motivational, programming, life & wisdom quotes.<br>
    Built with <strong>FastAPI</strong> – automatic interactive docs, blazing fast, production-ready.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/github/license/YOUR-USERNAME/InspireQuoteAPI?style=flat-square" alt="License: MIT">
    <img src="https://img.shields.io/github/stars/YOUR-USERNAME/InspireQuoteAPI?style=flat-square&color=yellow" alt="Stars">
  </p>

  <a href="https://your-inspirequoteapi.onrender.com/docs">
    <img src="https://img.shields.io/badge/Live%20Demo-Open%20Swagger%20UI-FF4081?style=flat-square&logo=fastapi&logoColor=white" alt="Live Demo">
  </a>
</div>

## Why You'll Love It
- **Instant inspiration** – one endpoint, endless motivation
- **Categories** (motivational, programming, funny, wisdom...)
- **Multiple quotes** in one call
- **Interactive docs** – try it live with Swagger UI
- **Free deploy** ready (Render, Railway, Vercel Python...)
- Great for: GitHub README widgets, Discord/Telegram bots, daily quote apps, blogs, portfolios

## Quick Start

```bash
git clone https://github.com/YOUR-USERNAME/InspireQuoteAPI.git
cd Random-Quote-API 

# Install
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload --port 8000
```
Now open in your browser:

- http://localhost:8000/quote       → one random quote  
- http://localhost:8000/quote/5     → five random quotes  
- http://localhost:8000/docs        → beautiful interactive playground (Swagger UI)

## 📜 API Endpoints

| Method | Endpoint            | Description                          | Example Response Fields              |
|--------|---------------------|--------------------------------------|--------------------------------------|
| GET    | `/`                 | Welcome & API information            | message, endpoints                   |
| GET    | `/quote`            | One random quote                     | quote, author, category              |
| GET    | `/quote/{count}`    | Multiple random quotes (1–20)        | quotes (array), count                |

## 🛠️ Deploy Free in 5 Minutes (Render.com Recommended)

1. Fork this repository  
2. Go to https://render.com → New → Web Service → Connect your GitHub repo  
3. Configure:  
   - **Runtime**: Python  
   - **Build Command**: `pip install -r requirements.txt`  
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`  
4. Click **Deploy** → you’ll get a live URL like:  
   `https://your-random-quote-api.onrender.com`  
5. Update this README with your live link!

## 🤝 Contributing

Love quotes? Want to make this project even better?

- Add more curated quotes to `quotes.py`  
- Suggest or implement new features:  
  - Search by author or category  
  - Voting/rating system  
  - Database support (SQLite/JSON file)  
  - Rate limiting  
  - Multiple categories filter  

Steps:  
1. Fork & clone the repo  
2. Create your branch (`git checkout -b feature/add-quotes`)  
3. Commit your changes  
4. Push and open a Pull Request  

Every great quote or improvement is welcome! 🌟

## 📄 License

[MIT License](LICENSE) — free to use, modify, and share.

---

**If this API gave you even one good quote today — drop a ⭐ !**  
Your star helps others discover it 🚀
