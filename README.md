# 🤖 AI Chatbot using Google Gemini

A modern AI chatbot built with **Streamlit** and **Google Gemini 2.5 Flash**. The application provides an interactive chat interface with conversation memory, streaming responses, and a clean user experience.

---

## 🚀 Demo

> Coming Soon (AWS Deployment)

---

## 📸 Screenshots

### Home Page

![Home](screenshots/home.png)

### Chat Interface

![Chat](screenshots/chat.png)

---

# ✨ Features

- 🤖 Google Gemini 2.5 Flash Integration
- 💬 Multi-turn Conversation
- ⚡ Streaming Typing Effect
- 🧠 Session-based Chat Memory
- 🎨 Clean Streamlit UI
- 🔐 Secure API Key using `.env`
- 📱 Responsive Layout
- ⚠️ Error Handling
- 📊 Response Time Display

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| UI | Streamlit |
| LLM | Google Gemini 2.5 Flash |
| SDK | google-genai |
| Environment | python-dotenv |
| Version Control | Git & GitHub |
| Package Manager | uv |

---

# 📂 Project Structure

```text
AI_Chatbot/
│
├── assets/
├── screenshots/
│
├── utils/
│   ├── gemini.py
│   ├── constants.py
│   └── database.py
│
├── app.py
├── config.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .gitignore
└── .python-version
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/prashantkadu25/AI_Chatbot.git
```

Move into the project folder.

```bash
cd AI_Chatbot
```

---

## Create Virtual Environment

Using uv

```bash
uv venv
```

Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser at

```
http://localhost:8501
```

---

# 🏗️ Architecture

```text
                User
                  │
                  ▼
          Streamlit UI
                  │
                  ▼
          Google Gemini API
                  │
                  ▼
           AI Response
                  │
                  ▼
            Streamlit UI
```

---

# 🧠 Key Concepts

- Large Language Models (LLMs)
- Prompt Engineering
- Conversation Memory
- Environment Variables
- Streamlit Session State
- API Integration

---

# 📈 Future Improvements

- Persistent Chat History
- User Authentication
- PDF Chat (RAG)
- Voice Input
- Image Understanding
- Multiple AI Models
- Docker Support
- AWS Deployment
- CI/CD Pipeline

---

# 💼 Resume Highlights

- Developed an AI chatbot using Google Gemini 2.5 Flash and Streamlit.
- Built an interactive chat interface with session-based conversation memory.
- Secured API credentials using environment variables.
- Managed source code using Git and GitHub.
- Prepared the application for cloud deployment on AWS.

---

# 👨‍💻 Author

**Prashant Kadu**

- GitHub: https://github.com/prashantkadu25
- LinkedIn: *https://www.linkedin.com/prashant-kadu9966*

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
