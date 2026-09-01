# 🚀 AI Study Assistant – Multi-Model Learning Platform

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?logo=google&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?logo=groq&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
![PDF](https://img.shields.io/badge/PDF_Processing-DC143C?logo=adobeacrobatreader&logoColor=white)
![DOCX](https://img.shields.io/badge/DOCX_Parsing-2B579A?logo=microsoftword&logoColor=white)
![Issues](https://img.shields.io/github/issues/AqsaAliRazaJamali/ai-study-assistant)

An interactive, Cloud-based AI Study Assistant that allows users to upload Documents (PDF/Word) and Chat with them using state-of-the-art Large Language Models (LLMs). This application provides a seamless learning experience by combining advanced document parsing with Real-time model switching capabilities.

👉 **Live Application:** [ai-study-assistant-aqsa.streamlit.app](https://ai-study-assistant-aqsa.streamlit.app) 

---

## 🌟 Key Features

* **Multi-Model Selection:** Toggle instantly between **Gemini Pro** (Google) and **Groq Cloud** inference engines depending on your requirements.
* **Smart Document Parser:** Automated and robust text extraction from both **PDF (`.pdf`)** and **Word (`.docx`)** files.
* **Interactive Chat Dashboard:** A clean, responsive user interface built using Streamlit with real-time conversational streaming.
* **Secure Key Management:** Production-ready backend architecture using encrypted Environment variables and streamlit secrets (`secrets.toml`).

---

## 🎨 Interactive Workspace Matrix

I have re-engineered the user experience from a Single-Page chat view into a premium **4-Node Interactive Workspace Dashboard** featuring smooth hover scaling effects and automated component routing:

* **💬 AI Tutor Room:** Socratic-style conversational assistant designed to teach core patterns.
* **📝 Synthesize Notes:** Document parsing hub that turns raw files into structured study guides.
* **🧠 Assessment Engine:** Generates instant review quizzes directly from your uploaded materials.
* **💡 Concept Explainer:** Breaks down deep theoretical topics across 4 customizable complexity depths.
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
