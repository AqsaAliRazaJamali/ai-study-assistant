import os
import streamlit as st
import google.generativeai as genai
from groq import Groq
from dotenv import load_dotenv
import cohere
from utils.prompts import SYSTEM_PROMPTS
import google.api_core.exceptions as google_exceptions
from utils.api_config import init_gemini, switch_to_next_key

load_dotenv()

DIRECT_GEMINI_KEY = st.secrets.get("GEMINI_API_KEY", "")
DIRECT_GROQ_KEY   = st.secrets.get("GROQ_API_KEY", "")

try:
    from mistralai import Mistral
    MISTRAL_AVAILABLE = True
except Exception:
    MISTRAL_AVAILABLE = False


def render_chatbot(model_placeholder=None):
    st.title("💬 Interactive AI Tutor")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display conversational log history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_prompt := st.chat_input("Ask your academic question..."):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            # Rebuild history payload for Gemini's structural format safely
            gemini_history = []
            for msg in st.session_state.chat_history[:-1]:
                role = "user" if msg["role"] == "user" else "model"
                gemini_history.append({"role": role, "parts": [msg["content"]]})
            
            # --- TRY ENGINE LOOP ---
            try:
                # 1. Initialize the model using the current active key index
                model_engine = init_gemini()
                
                # Create chat instance and apply system tutoring instructions explicitly
                chat_session = model_engine.start_chat(history=gemini_history)
                
                # Inject System Instructions safely into the context runtime execution
                enriched_prompt = f"{SYSTEM_PROMPTS.get('tutor', '')}\n\nUser Question: {user_prompt}"
                
                response = chat_session.send_message(enriched_prompt, stream=True)
                for chunk in response:
                    full_response += chunk.text
                    response_placeholder.markdown(full_response + "▌")
                response_placeholder.markdown(full_response)
                
            except google_exceptions.ResourceExhausted:
                # 2. Catch the 429 quota error cleanly in the background
                with st.spinner("🔄 High traffic on current node. Switching to backup server..."):
                    if switch_to_next_key():
                        try:
                            # 3. Re-initialize with the next fresh key from your pool
                            model_engine_backup = init_gemini()
                            chat_session_backup = model_engine_backup.start_chat(history=gemini_history)
                            
                            # Re-run explicit prompt context on the backup cluster safely
                            backup_prompt = f"{SYSTEM_PROMPTS.get('tutor', '')}\n\nUser Question: {user_prompt}"
                            response_backup = chat_session_backup.send_message(backup_prompt)
                            
                            full_response = response_backup.text
                            response_placeholder.markdown(full_response)
                        except (google_exceptions.ResourceExhausted, Exception):
                            # Safe fallback if backup key is ALSO exhausted right now
                            full_response = "🤖 *The backup channel is also experiencing high volume. Please resubmit this prompt in 10 seconds.*"
                            response_placeholder.markdown(full_response)
                    else:
                        full_response = "🤖 *All available free-tier backup key pools have reached daily capacities. Please try again later.*"
                        response_placeholder.markdown(full_response)
                        
            except Exception as e:
                st.error(f"Unexpected connection error: {e}")
                full_response = "Apologies, an execution failure occurred handling the AI module."
                response_placeholder.markdown(full_response)
            
        st.session_state.chat_history.append({"role": "assistant", "content": full_response})
        st.rerun()
