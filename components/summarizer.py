import streamlit as st
from utils.file_handler import extract_text_from_file
from utils.prompts import SYSTEM_PROMPTS

def render_summarizer(model):
    st.header("📝 Notes Summarizer")
    
    # Context ingestion options
    source_type = st.radio("Choose Source Input Style:", ["Paste Raw Text", "Upload Document File"])
    raw_text = ""

    if source_type == "Paste Raw Text":
        raw_text = st.text_area("Drop your notes here:", height=250, placeholder="Paste study guides, book chapters, or messy raw notes...")
    else:
        uploaded_file = st.file_uploader("Upload Notes (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])
        if uploaded_file:
            with st.spinner("Extracting textual dataset components..."):
                raw_text = extract_text_from_file(uploaded_file)
            st.success("Context loaded successfully!")

    if raw_text:
        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Configuration")
            summary_style = st.selectbox(
                "Select Architecture Output Type:",
                ["Short Summary", "Bullet-Point Summary", "Detailed Explanation Summary", "Exam Revision Notes"]
            )
            process_btn = st.button("✨ Synthesize Material", use_container_width=True)

        with col2:
            st.subheader("Output Interface")
            if process_btn:
                prompt = f"""
                {SYSTEM_PROMPTS['summarizer']}
                
                Format requested: {summary_style}
                
                Text to process:
                \"\"\"{raw_text}\"\"\"
                """
                with st.spinner("Compiling insights..."):
                    try:
                        response = model.generate_content(prompt)
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"API Error: {e}")
            else:
                st.info("Configure settings on the left and click synthesize to see your summarized notes.")