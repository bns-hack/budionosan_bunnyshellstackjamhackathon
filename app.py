import vertexai
import streamlit as st
import os 

from google.cloud import aiplatform
from vertexai.preview.language_models import TextGenerationModel

aiplatform.init(project="YOUR_PROJECT_ID", location="YOUR_GCP_LOCATION")
vertexai.init(project="YOUR_PROJECT_ID", location="YOUR_GCP_LOCATION")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="application_default_credentials.json"

st.set_page_config(layout="wide",page_title="AnythingGPT")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.sidebar.image("https://i.imgur.com/OKEzjmM.png")

tab1, tab2 = st.tabs(["AnythingGPT", "AnythingGPT FAQ"])

with tab1:
    st.info("AnythingGPT are is GPT application that you need such as writing, marketing, ask anything and many more.")

    prompt = st.text_input("What do you want to ask?")

    if st.button("Submit"):
        if not prompt.strip():
            st.warning("Please fill your question.")
        else:
            model = TextGenerationModel.from_pretrained("text-bison@001")
            response = model.predict(
                prompt,
                temperature=0.5,
                max_output_tokens=256
            )
            with st.expander("See answer"):
                st.write(response.text)

with tab2:
    st.info("AnythingGPT are is GPT application that you need such as writing, marketing, ask anything and many more.")
    st.info("AnythingGPT is running use English only.")
    st.info("How to use AnythingGPT?")
    st.info("1. You must have idea anything.")
    st.info("2. Write your idea in the text input.")
    st.info("3. Click 'Submit' button then click 'See answer' and you get the answer.")
