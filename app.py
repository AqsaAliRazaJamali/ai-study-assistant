import streamlit as st

# Application orchestration configuration definitions
st.set_page_config(
    page_title="AI Study Assistant Workspace",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.api_config import init_gemini
from components.chatbot import render_chatbot
from components.summarizer import render_summarizer
from components.quiz_generator import render_quiz_generator
from components.explainer import render_explainer

# Apply Global custom theme CSS styles injects manually for custom elements styling enhancements
st.markdown("""
    <style>
        .main .block-container { padding-top: 2rem; }
        .stButton>button { border-radius: 8px; transition: all 0.3s ease; }
        .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        div[data-testid="stMetricValue"] { font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

def main():
    # Model client initialization layer configuration integration
    model = init_gemini()
    
    # Sidebar application context navigation
    with st.sidebar:
        st.title("🎓 Study Suite")
        st.markdown("Your custom production-ready AI learning companion dashboard pipeline space system interface.")
        st.markdown("---")
        
        navigation_dest = st.radio(
            "Select Functional Module Matrix:",
            ["🏛️ Home Suite", "💬 AI Tutor Room", "📝 Synthesize Notes", "🧠 Assessment Engine", "💡 Concept Explainer"]
        )
        
        st.markdown("---")
        st.caption("⚡ Model Subsystem Core Engine: `Gemini 1.5 Flash` processing layer configuration profiles verified.")

    # Application router view controls distribution framework
    if navigation_dest == "🏛️ Home Suite":
        render_home_dashboard()
    elif navigation_dest == "💬 AI Tutor Room":
        render_chatbot(model)
    elif navigation_dest == "📝 Synthesize Notes":
        render_summarizer(model)
    elif navigation_dest == "🧠 Assessment Engine":
        render_quiz_generator(model)
    elif navigation_dest == "💡 Concept Explainer":
        render_explainer(model)

def render_home_dashboard():
    st.title("🚀 Welcome to your AI Study Assistant Workspace")
    st.markdown("An advanced LLM application platform engineered to optimize modern learning workflows using state-of-the-art natural language processing architectures.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🌟 Main Functional Modalities
        * **AI Tutor Mode:** Direct conversational socratic loops that don't just output flat solutions but teach patterns interactively.
        * **Document Context Summarizer:** Raw PDF/TXT ingestion framework designed to optimize study guide output formatting profiles.
        * **Automated Assessment Quiz System:** Transform unstructured knowledge documents directly into structured interactive validation assessments.
        * **Concept Transformer Explainer:** Tailor conceptual cognitive loads precisely ranging across 4 custom level targets.
        """)
        
    with col2:
        st.info("💡 **Portfolio Project Execution Blueprint Notice**\n\nThis implementation setup completely separates orchestration logic layers directly away from execution contexts components, implementing systematic strict prompt validation guidelines to avoid operational structural failures and hallucinations across all workspace nodes.")

if __name__ == "__main__":
    main()