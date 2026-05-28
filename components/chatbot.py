import streamlit as st
import google.generativeai as genai
from groq import Groq
import os
from dotenv import load_dotenv
import cohere
from utils.prompts import SYSTEM_PROMPTS
load_dotenv()

DIRECT_GEMINI_KEY = st.secrets.get("GEMINI_API_KEY", "")
DIRECT_GROQ_KEY   = st.secrets.get("GROQ_API_KEY", "")

try:
    from mistralai import Mistral
    MISTRAL_AVAILABLE = True
except Exception:
    MISTRAL_AVAILABLE = False

def render_chatbot(model_placeholder):
    st.header("💬 AI Tutor")
    st.caption("Exploring concepts together...")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat history display
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("What concept are we exploring today?"):
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        prompt_with_context = f"{SYSTEM_PROMPTS['tutor']}\n\nUser Question: {user_input}"
        
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            success = False

            # --- TRY ENGINE 1: GEMINI (Optimized to Flash-Lite) ---
            if DIRECT_GEMINI_KEY and not DIRECT_GEMINI_KEY.startswith("YAHAN_"):
                try:
                    genai.configure(api_key=DIRECT_GEMINI_KEY)
                   
                    dynamic_model = genai.GenerativeModel('gemini-2.5-flash-lite')
                    
                    contents_payload = [{"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} for m in st.session_state.chat_history[:-1]]
                    chat_session = dynamic_model.start_chat(history=contents_payload)
                    
                    response_stream = chat_session.send_message(prompt_with_context, stream=True)
                    for chunk in response_stream:
                        full_response += chunk.text
                        response_placeholder.markdown(full_response + "▌")
                    response_placeholder.markdown(full_response)
                    success = True
                except Exception:
                    
                    pass

            # --- TRY ENGINE 2: GROQ FALLBACK ---
            if not success and DIRECT_GROQ_KEY and not DIRECT_GROQ_KEY.startswith("YAHAN_"):
                # Inform the user seamlessly without breaking the layout
                with st.spinner("Routing query through backup high-speed node..."):
                    try:
                        client = Groq(api_key=DIRECT_GROQ_KEY)
                        groq_messages = [{"role": "system", "content": SYSTEM_PROMPTS['tutor']}]
                        for msg in st.session_state.chat_history:
                            groq_messages.append({"role": msg["role"], "content": msg["content"]})

                        completion = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=groq_messages,
                            stream=True
                        )
                        for chunk in completion:
                            if chunk.choices[0].delta.content:
                                full_response += chunk.choices[0].delta.content
                                response_placeholder.markdown(full_response + "▌")
                        response_placeholder.markdown(full_response)
                        success = True
                    except Exception:
                        pass

            # If both options completely fail
            if not success:
                st.error("❌ High traffic detected across all learning channels. Please try submitting your question again in 10-15 seconds.")

        if success:
            st.session_state.chat_history.append({"role": "assistant", "content": full_response})
            st.rerun()
