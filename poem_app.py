import streamlit as st
from poem_generator import load_generator, generate_poem

st.set_page_config(page_title="AI Poem Generator", layout="centered")
st.title("🎨 AI Poem Generator")
st.caption("Let GPT-2 write creative poems on your favorite topics!")

with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Choose Model", ["gpt2", "gpt2-medium", "EleutherAI/gpt-neo-125M"])
    style = st.selectbox("Poem Style", ["Default", "Romantic", "Haiku", "Horror", "Inspirational"])
    max_length = st.slider("Max Length", 50, 250, 100)

@st.cache_resource
def get_generator(name):
    return load_generator(model_name=name)

generator = get_generator(model_name)

topic = st.text_input("Enter a topic for the poem:")

if topic:
    with st.spinner("Generating your poem..."):
        poem = generate_poem(topic, generator, style, max_length)
    st.markdown("### ✨ Here's your poem:")
    st.text(poem)
