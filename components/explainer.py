import streamlit as st
from utils.prompts import get_explainer_prompt

def render_explainer(model):
    st.header("💡 Advanced Concept Explainer")
    st.caption("Deconstruct obscure concepts, complex formulas, or highly nested paragraphs instantly.")

    target_material = st.text_area("Input abstract concept, formula context, or paragraph block:", height=150, placeholder="e.g., Quantum Entanglement or Keynesian Multiplier mechanics...")
    
    if target_material:
        st.subheader("Tailor Explanation Model Parameters")
        
        level = st.select_slider(
            "Select Target Audience Comprehension Level Matrix Profile:",
            options=["Beginner", "Intermediate", "Advanced", "Real-World Analogy"]
        )
        
        if st.button("⚙️ Transform Concept Framework", use_container_width=True):
            full_compiled_prompt = get_explainer_prompt(level, target_material)
            
            with st.spinner("Reframing structural concept parameters..."):
                try:
                    response = model.generate_content(full_compiled_prompt)
                    st.markdown("---")
                    st.info(f"💡 Visualizing Context Refactored as: **{level} Output Framework**")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Engine payload execution breakdown error: {e}")