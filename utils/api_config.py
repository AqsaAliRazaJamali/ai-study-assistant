import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# --- PRODUCTION ENVIRONMENT VARIABLE MAPPING ---
# Code mein koi bhi key hardcode (paste) NA karein.
# Hum inko cloud dashboard se dynamically read karenge.
API_KEYS_POOL = [
    os.getenv("GEMINI_KEY_1", ""),
    os.getenv("GEMINI_KEY_2", ""),
    os.getenv("GEMINI_KEY_3", ""),
    os.getenv("GEMINI_KEY_4", "")
]

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
COHERE_API_KEY = os.getenv("COHERE_API_KEY", "")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")

def init_gemini():
    """Initializes and returns a baseline model configuration safely for production."""
    # Filter out empty None values safely
    valid_keys = [k for k in API_KEYS_POOL if k]
    
    # Check if a default standard env variable exists as a backup
    if os.getenv("GEMINI_API_KEY"):
        valid_keys.insert(0, os.getenv("GEMINI_API_KEY"))
        
    st.session_state.valid_keys_pool = valid_keys
    if "current_key_index" not in st.session_state:
        st.session_state.current_key_index = 0
        
    if valid_keys:
        try:
            genai.configure(api_key=valid_keys[st.session_state.current_key_index])
            return genai.GenerativeModel('gemini-2.5-flash')
        except Exception:
            pass
            
    # Dummy placeholder so components don't throw NoneType errors on start
    return genai.GenerativeModel('gemini-2.5-flash')