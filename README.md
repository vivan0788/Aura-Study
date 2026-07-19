# ⚡ Aura Study – AI Instant Insights Agent

> **An AI-powered document analysis and research assistant built for hackathons.**
>
> Upload any **PDF** or **image** to instantly extract key insights, generate practice questions, and chat with the document using AI.

---

## ✨ Features

- 📄 Upload PDF and document images
- ⚡ AI-powered document summarization
- 🧠 Extracts 4–5 key insights automatically
- 📝 Generates context-based mock practice questions
- 💬 Interactive AI chat based on uploaded document
- 🎨 Clean, responsive, and modern user interface
- 🚀 Fast and optimized for hackathon demonstrations

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)

### Backend
- Python
- Flask
- Flask-CORS
- PyPDF
- Gunicorn

### AI Integration
- OpenAI API 

### Deployment
- Vercel (Frontend)
- Render (Backend)

---

## 📂 Project Structure

```text
ai-instant-insights-agent/
│
├── backend/
│   ├── app.py
│   ├── ai_helper.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── vercel.json
│
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vivan0788/Aura-Study.git

cd aura-study
```

---

## ⚙️ Backend Setup

Move to the backend directory.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the **backend** folder.

```env
OPENAI_API_KEY=your_openai_api_key

# OR

GEMINI_API_KEY=your_gemini_api_key

# OR

HF_API_KEY=your_huggingface_api_key
```

---

## ▶️ Run Backend

```bash
python app.py
```

Backend will run at

```
https://aura-study.onrender.com
```

---

## 💻 Frontend Setup

Open

```
frontend/js/app.js
```

Update the backend URL.

```javascript
const BACKEND_URL = "https://aura-study.onrender.com/api";
```

Now open

```
frontend/index.html
```

in your browser.

---

# 🌍 Deployment

## 🚀 Backend (Render)

1. Push the project to GitHub.
2. Create a **Render Web Service**.
3. Select the repository.
4. Set:

**Root Directory**

```
backend
```

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

Add your API key inside **Environment Variables**.

Example

```
OPENAI_API_KEY=xxxxxxxx
```

After deployment you'll get something like

```
https://your-app.onrender.com
```

---

## 🚀 Frontend (Vercel)

Update

```javascript
const BACKEND_URL = "https://your-app.onrender.com/api";
```

Then

- Import GitHub Repository
- Set Root Directory

```
frontend
```

Deploy 🎉

---

## 📸 Application Workflow

```text
User Uploads PDF/Image
          │
          ▼
Document Processing
          │
          ▼
AI Analysis
          │
 ┌────────┼────────┐
 ▼        ▼        ▼
Summary  Questions  AI Chat
          │
          ▼
 Display Results
```

---

## 🎯 Use Cases

- 📚 Students
- 🏫 Teachers
- 🎓 Exam Preparation
- 📄 Research Papers
- 💼 Business Reports
- 🧠 Quick Document Review

---

## 📦 Dependencies

```
Flask
Flask-CORS
PyPDF
Gunicorn
python-dotenv
OpenAI
```

Install using

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- 📄 Multiple PDF support
- 🌐 OCR for scanned documents
- 🎤 Voice interaction
- 🌍 Multi-language support
- 📥 Export summaries as PDF
- ☁️ User authentication
- 📚 Chat history
- 📱 Progressive Web App (PWA)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Developer

**Avinash Sahani**

💻 Passionate Software Developer & B.Tech CS Student

GitHub:
https://github.com/vivan0788

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
