from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Somewhere near the top of your code
css_animations = """
<style>
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade-in {
  animation: fadeIn 0.8s ease forwards;
}
</style>
"""
st.markdown(css_animations, unsafe_allow_html=True)

# Load a success Lottie animation once
success_lottie_url = "https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json"
success_lottie = load_lottie_url(success_lottie_url)

def show_explanation_and_questions():
    # ... existing logic
    if answered_count == total_questions:
        st.success("All done!")
        # Lottie success animation
        st_lottie(success_lottie, height=250)
        return

    # For each question:
    for i, case in enumerate(usage_cases):
        # Use fade-in container
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.write(f"**{case['title']}**")
        st.write(case['question'])
        # ... text_input, etc.
        st.markdown("</div>", unsafe_allow_html=True)
