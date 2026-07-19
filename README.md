# ⚡ AI Instant Insights Agent (Aura Study)

An AI-powered document analysis and research assistant built for Hackathons. This application allows users to upload any PDF or image file to instantly extract core insights, generate interactive mock practice questions, and chat dynamically with the document context in real-time.

---

## 🚀 Key Features
- **Zero Friction UI:** Drag & Drop interface to upload PDFs and Document Images.
- **Smart Insights Generation:** Automatically parses document text and summarizes 4-5 core highlights.
- **Mock Assessment:** Dynamically compiles 3 context-relevant practice questions for exam or review prep.
- **Contextual Document Chat:** Interactive chat window to ask specific queries based strictly on the uploaded file contents.
- **Production-Ready & Optimized:** High-performance architecture built for fast responses during live judging.

---

## 📂 Project Architecture

```text
ai-instant-assistant/
├── backend/
│   ├── app.py                      # Flask Application Server with CORS & Routes
│   ├── ai_helper.py                # AI Inference Service Logic (OpenAI/Gemini/HF)
│   └── requirements.txt            # Production Level Backend Dependencies
├── frontend/
│   ├── css/
│   │   └── style.css               # Premium Modern Dark-Themed UI Layout
│   ├── js/
│   │   └── app.js                  # Asynchronous State Controller & API Fetch Handler
│   ├── index.html                  # Main Web Dashboard
│   └── vercel.json                 # Vercel Deployment & URL Routing Config
└── README.md                       # Comprehensive Project Documentation
