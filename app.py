import re
import streamlit as st
from spellchecker import SpellChecker

st.set_page_config(
    page_title="AI-Powered Autocorrect Tool",
    page_icon="✨",
    layout="centered"
)

spell = SpellChecker()

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
}

.title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.result-box {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    color: black;
    font-size: 18px;
    margin-top: 10px;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
}
</style>
""", unsafe_allow_html=True)

if "text_value" not in st.session_state:
    st.session_state.text_value = ""

if "result" not in st.session_state:
    st.session_state.result = ""

def clear_text():
    st.session_state.text_value = ""
    st.session_state.result = ""

st.markdown(
    "<h1 class='title'>✨ AI-Powered Autocorrect Tool</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Correct spelling mistakes instantly.</p>",
    unsafe_allow_html=True
)

text = st.text_area(
    "Enter your text:",
    key="text_value",
    height=180,
    placeholder="Example: hii im larning pythn"
)

col1, col2 = st.columns(2)

with col1:
    correct_btn = st.button("🔍 Autocorrect")

with col2:
    st.button("🔄 New Text", on_click=clear_text)

if correct_btn:
    if text.strip():

        words = re.findall(r"\w+|\W+", text)

        corrected_words = []

        custom_words = {
            "pythn": "python",
            "machne": "machine",
            "learnng": "learning",
            "larning": "learning",
            "buoy": "boy",
            "hii": "hi",
            "im": "i'm",
            "hav": "have",
            "alot": "a lot",
            "assingments": "assignments",
            "complet": "complete",
            "befor": "before",
            "tomorow": "tomorrow"
        }

        for token in words:
            if token.isalpha():

                lower_token = token.lower()

                if lower_token in custom_words:
                    corrected_words.append(custom_words[lower_token])
                else:
                    suggestion = spell.correction(token)
                    corrected_words.append(suggestion if suggestion else token)

            else:
                corrected_words.append(token)

        corrected_text = "".join(corrected_words)

        if corrected_text:
            corrected_text = corrected_text[0].upper() + corrected_text[1:]

        st.session_state.result = corrected_text

if st.session_state.result:
    st.markdown("### ✅ Corrected Text")

    st.markdown(
        f"""
        <div class="result-box">
        {st.session_state.result}
        </div>
        """,
        unsafe_allow_html=True
    )