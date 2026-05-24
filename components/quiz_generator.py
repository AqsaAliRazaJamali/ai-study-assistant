import streamlit as st
import json
import re
from utils.file_handler import extract_text_from_file
from utils.prompts import SYSTEM_PROMPTS

def render_quiz_generator(model):
    st.header("🧠 Automated Quiz Generator")
    
    # Shared input management block
    uploaded_file = st.file_uploader("Upload Topic Reference File (.pdf, .txt, .docx)", type=["pdf", "txt", "docx"], key="quiz_upload")
    topic_input = st.text_input("Or, specify a specific topic directly:", placeholder="e.g., Mitosis Cell Division cycles")

    context_material = ""
    if uploaded_file:
        context_material = extract_text_from_file(uploaded_file)
    elif topic_input:
        context_material = f"Topic of focus: {topic_input}"

    if context_material:
        st.markdown("---")
        # Interactive quiz configuration variables
        q_type = st.selectbox("Quiz Type Structure:", ["Multiple Choice Questions (MCQs)", "True/False"])
        num_questions = st.slider("Quantity of Questions:", min_value=3, max_value=10, value=5)
        
        if st.button("🚀 Generate Evaluation Engine", use_container_width=True):
            # Enforce structured JSON schemas directly via prompts
            json_format_spec = (
                '[\n  {\n    "question": "Question text definition?",\n    "options": ["Choice A", "Choice B", "Choice C", "Choice D"],\n    "answer": "Exact correct Choice string value matched matching option value exactly"\n  }\n]'
                if q_type == "Multiple Choice Questions (MCQs)" else
                '[\n  {\n    "question": "Statement formulation text?",\n    "options": ["True", "False"],\n    "answer": "True"\n  }\n]'
            )

            generation_prompt = f"""
            {SYSTEM_PROMPTS['quiz_generator']}
            
            Generate exactly {num_questions} questions of type: {q_type}.
            Based on this source text matrix:
            \"\"\"{context_material[:4000]}\"\"\"
            
            Your return string MUST be an explicit, single parser-valid raw JSON array matching this syntax template:
            {json_format_spec}
            Do not enclose inside markdown backticks blocks or write prefix text. Return clean json array text block.
            """
            
            with st.spinner("Compiling academic items..."):
                try:
                    response = model.generate_content(generation_prompt)
                    # Content cleaning to ensure standard JSON structure string output validation passes
                    clean_text = re.sub(r"^```json|```$", "", response.text.strip(), flags=re.MULTILINE).strip()
                    st.session_state.active_quiz = json.loads(clean_text)
                    st.session_state.quiz_answers_submitted = False
                    st.session_state.user_quiz_selections = {}
                except Exception as e:
                    st.error("Failed parsing structured data engine matrix format. Please execute request again.")
                    st.toast(f"System Log Debug Detail: {e}")

        # Active evaluation testing layout rendering framework
        if "active_quiz" in st.session_state:
            st.subheader("📝 Dynamic Evaluation Interface")
            
            with st.form("quiz_submission_form"):
                for idx, item in enumerate(st.session_state.active_quiz):
                    st.markdown(f"**Q{idx+1}: {item['question']}**")
                    st.session_state.user_quiz_selections[idx] = st.radio(
                        "Select response option:", 
                        options=item["options"], 
                        key=f"q_radio_{idx}"
                    )
                    st.markdown("<br>", unsafe_allow_html=True)

                submit_btn = st.form_submit_button("Submit Assessment Selections")
                
                if submit_btn:
                    st.session_state.quiz_answers_submitted = True

            if st.session_state.get("quiz_answers_submitted", False):
                st.markdown("---")
                st.subheader("📊 Performance Vector Feedback")
                score = 0
                total = len(st.session_state.active_quiz)
                
                for idx, item in enumerate(st.session_state.active_quiz):
                    user_ans = st.session_state.user_quiz_selections.get(idx)
                    correct_ans = item["answer"]
                    
                    if user_ans == correct_ans:
                        score += 1
                        st.success(f"✓ **Question {idx+1}**: Correct! You selected: '{user_ans}'")
                    else:
                        st.error(f"✗ **Question {idx+1}**: Incorrect choice. You picked '{user_ans}'. \n\n **Correct vector:** '{correct_ans}'")
                
                pct = int((score / total) * 100)
                st.metric("Final Score Metric Valuation", f"{score} / {total}", f"{pct}% Achievement rate")