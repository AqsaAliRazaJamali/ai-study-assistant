# 🚀 AI Study Assistant – Multi-Model Learning Platform

An interactive, cloud-based AI Study Assistant that allows users to upload documents (PDF/Word) and chat with them using state-of-the-art Large Language Models (LLMs). This application provides a seamless learning experience by combining advanced document parsing with real-time model switching capabilities.

👉 **Live Application:** [ai-study-assistant-aqsa.streamlit.app](https://ai-study-assistant-aqsa.streamlit.app) 

---

## 🌟 Key Features

* **Multi-Model Selection:** Toggle instantly between **Gemini Pro** (Google) and **Groq Cloud** inference engines depending on your requirements.
* **Smart Document Parser:** Automated and robust text extraction from both **PDF (`.pdf`)** and **Word (`.docx`)** files.
* **Interactive Chat Dashboard:** A clean, responsive user interface built using Streamlit with real-time conversational streaming.
* **Secure Key Management:** Production-ready backend architecture using encrypted environment variables and Streamlit Secrets (`secrets.toml`).

---

## 🛠️ Technical Stack

* **Frontend & Dashboard:** Streamlit (Python)
* **AI & LLM Integration:** Google Generative AI SDK, Groq Cloud API
* **File Handling Libraries:** `pypdf`, `docx2txt`
* **Version Control & Hosting:** Git, GitHub, Streamlit Cloud

---

## 📂 Project Structure
```plaintext
ai-study-assistant/
│
├── .streamlit/
│   └── secrets.toml               # Local API keys configuration (Not uploaded to GitHub)
│
├── components/
│   ├── chatbot.py            
│   ├── explainer.py         
│   ├── quiz_generator.py     
│   └── summarizer.py         
│
├── utils/
│   ├── api_config.py         
│   ├── file_handler.py      
│   └── prompts.py            
│
├── app.py                    
├── requirements.txt         
└── README.md                 
```



## 💻 Local Setup & Installation

Follow these steps to get this project running locally on your environment:

### 1. Clone the Repository
```bash
git clone https://github.com/aqsaalirazajamali/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Keys

Create a file named:

```plaintext
.streamlit/secrets.toml
```

Add your API keys:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
GROQ_API_KEY = "your_groq_api_key"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```plaintext
http://localhost:8501
```

---

## 📚 Use Cases

- Study assistance
- Research note summarization
- AI tutoring
- Exam preparation
- Quiz generation
- Concept clarification

---

## 👩‍💻 Author

Aqsa Jamali
