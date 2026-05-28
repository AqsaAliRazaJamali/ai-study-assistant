import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEYS_POOL = [
    os.getenv("GEMINI_KEY_1", ""),
    os.getenv("GEMINI_KEY_2", ""),
    os.getenv("GEMINI_KEY_3", ""),
    os.getenv("GEMINI_KEY_4", ""),
    os.getenv("GEMINI_API_KEY", "") # Standard fallback key
]

def init_gemini():
    """Initializes the model dynamically using the currently active key index."""
    valid_keys = [k for k in API_KEYS_POOL if k]
    st.session_state.valid_keys_pool = valid_keys
    
    if "current_key_index" not in st.session_state:
        st.session_state.current_key_index = 0
        
    if not valid_keys:
        st.error("🔑 If no Gemini Key is found! Please check your variables.")
        st.stop()
        
    idx = st.session_state.current_key_index
    genai.configure(api_key=valid_keys[idx])
    
    return genai.GenerativeModel('gemini-2.5-flash-lite')


def switch_to_next_key():
    """Engine to seamlessly switch to the next available API key in the background."""
    pool = st.session_state.get("valid_keys_pool", [])
    if len(pool) > 1:
        st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(pool)
        return True
    return False 
