import streamlit as st

# Application configuration - Premium Clean Dashboard
st.set_page_config(
    page_title="AI Study Suite | Premium Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

from utils.api_config import init_gemini
from components.chatbot import render_chatbot
from components.summarizer import render_summarizer
from components.quiz_generator import render_quiz_generator
from components.explainer import render_explainer

# Elegant & Clean High-Contrast CSS Injection
st.markdown("""
    <style>
        /* Overall layout and container styling */
        .main .block-container { padding-top: 2.5rem; max-width: 1050px; }
        
        /* Minimalist & High-Contrast Welcome Area (No confusing backgrounds) */
        .welcome-banner {
            text-align: center;
            margin-bottom: 40px;
            padding: 1rem;
        }
        
        .app-title {
            font-size: 42px !important;
            font-weight: 800 !important;
            letter-spacing: -1px !important;
            /* Premium Electric Blue/Purple Gradient Text */
            background: linear-gradient(135deg, #1E40AF 0%, #6D28D9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px !important;
        }
        
        .app-tagline {
            font-size: 18px !important;
            font-weight: 500 !important;
            color: #334155 !important; /* Deep Charcoal Gray - 100% readable and clean */
            max-width: 700px;
            margin: 0 auto !important;
            line-height: 1.6;
        }

        /* 2x2 Grid Card Buttons */
        div.stButton > button {
            width: 100% !important;
            height: 130px !important;
            background: #1E293B !important; /* Dark Slate Blue Background */
            color: #FFFFFF !important;
            border: 1px solid #334155 !important;
            border-radius: 16px !important;
            padding: 15px !important;
            transition: all 0.25s ease-in-out !important;
        }
        
        /* Card Action Hover State */
        div.stButton > button:hover {
            transform: translateY(-4px) !important;
            background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%) !important; 
            border-color: #60A5FA !important;
            box-shadow: 0 15px 25px -5px rgba(37, 99, 235, 0.25) !important;
        }

        /* Back Action Button Alignment */
        .back-btn div.stButton > button {
            height: 40px !important;
            width: auto !important;
            background: #334155 !important;
            font-size: 14px !important;
            border-radius: 8px !important;
            padding: 5px 20px !important;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    model = init_gemini()
    
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "🏠 Home Dashboard"
        
    with st.sidebar:
        st.markdown("# 🎓 Study Suite")
        st.caption("Workspace Management Interface")
        st.markdown("---")
        sidebar_options = ["🏠 Home Dashboard", "💬 AI Tutor Room", "📝 Synthesize Notes", "🧠 Assessment Engine", "💡 Concept Explainer"]
        st.session_state.active_tab = st.radio(
            "Quick Select:",
            sidebar_options,
            index=sidebar_options.index(st.session_state.active_tab)
        )

    if st.session_state.active_tab == "🏠 Home Dashboard":
        render_sleek_dashboard()
    elif st.session_state.active_tab == "💬 AI Tutor Room":
        render_back_navigation()
        render_chatbot(model)
    elif st.session_state.active_tab == "📝 Synthesize Notes":
        render_back_navigation()
        render_summarizer(model)
    elif st.session_state.active_tab == "🧠 Assessment Engine":
        render_back_navigation()
        render_quiz_generator(model)
    elif st.session_state.active_tab == "💡 Concept Explainer":
        render_back_navigation()
        render_explainer(model)

def render_back_navigation():
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("⬅️ Return to Dashboard"):
        st.session_state.active_tab = "🏠 Home Dashboard"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

def render_sleek_dashboard():
    # Clean typography banner with gradient effect text
    st.markdown("""
        <div class="welcome-banner">
            <h1 class="app-title">Welcome to Your AI Study Workspace</h1>
            <p class="app-tagline">
                An advanced multi-model engineering platform built to optimize modern learning workflows. 
                Select a workspace node below to launch your session.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Responsive Grid Display Layout
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("**💬 AI TUTOR ROOM**")
        if st.button("Launch Interactive Tutor\n\nSocratic-style conversational loops built to teach core computational patterns."):
            st.session_state.active_tab = "💬 AI Tutor Room"
            st.rerun()
        st.write("") 
        
        st.markdown("**🧠 ASSESSMENT ENGINE**")
        if st.button("Launch Quiz Generator\n\nTransform uploaded unstructured notes directly into interactive multi-level verification quizzes."):
            st.session_state.active_tab = "🧠 Assessment Engine"
            st.rerun()
            
    with col2:
        st.markdown("**📝 SYNTHESIZE NOTES**")
        if st.button("Launch Document Summarizer\n\nIngest raw PDF and TXT data segments directly into clean, comprehensive study guides."):
            st.session_state.active_tab = "📝 Synthesize Notes"
            st.rerun()
        st.write("") 
        
        st.markdown("**💡 CONCEPT EXPLAINER**")
        if st.button("Launch Cognitive Explainer\n\nDeconstruct complex theoretical concepts across 4 custom cognitive depth targets."):
            st.session_state.active_tab = "💡 Concept Explainer"
            st.rerun()

    st.write("")
    st.write("")
    st.write("---")
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 13px;'>🔒 CORE SUBSYSTEM ENGINES ACTIVE | POWERED BY GEMINI 1.5 FLASH</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
