import streamlit as st
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set page config
st.set_page_config(page_title="Tell Me About Yourself Generator", layout="centered")
st.title("🌟 Tell Me About Yourself Generator")
st.markdown("Fill in the details below and click **Generate Introduction** to create a unique and engaging response!")

# Check for API Key
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API Key not found in environment variables. Please set GOOGLE_API_KEY.")
    st.stop()

# Configure Gemini AI
genai.configure(api_key=api_key)

# User Inputs
name = st.text_input("🌟 Fun Alias or Nickname", placeholder="e.g., Maverick")
country = st.text_input("🌍 Country of Origin", placeholder="e.g., USA")
job_role = st.text_input("💼 What’s your hustle?", placeholder="e.g., Software Engineer")
hobbies = st.text_input("🎨 Hobbies/Interests", placeholder="e.g., Gaming, Cooking, Painting")
fun_fact = st.text_input("🤩 Fun Fact or Unique Detail", placeholder="e.g., I once backpacked across Europe")
favorite = st.text_input("🔥 Favorite Emoji or Catchphrase", placeholder="e.g., 🚀 or 'Let's rock!'")

# Tone options
tone_options = ["Professional", "Casual", "Friendly", "Inspirational", "Humorous", "Confident", "Charming", "Energetic", "Laid-back"]
tone = st.selectbox("🎭 Tone", tone_options)

# LangChain Prompt Template
intro_prompt = """
You are a creative writer. Using the details below, generate a **unique and engaging "Tell Me About Yourself" introduction** in a {tone} tone:

- **Name (Fun Alias):** {name}
- **Country of Origin:** {country}
- **Job Role:** {job_role}
- **Hobbies/Interests:** {hobbies}
- **Fun Fact:** {fun_fact}
- **Favorite Emoji or Catchphrase:** {favorite}

Make it **interesting, natural, and conversational**. Ensure it reflects the selected tone and includes a fun, personal touch. 
"""

prompt_template = PromptTemplate(
    input_variables=["name", "country", "job_role", "hobbies", "fun_fact", "favorite", "tone"],
    template=intro_prompt
)

# LangChain LLM
llm_chain = LLMChain(
    prompt=prompt_template,
    llm=ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-latest",
        temperature=0.8,
        max_tokens=500
    )
)

# Generate Introduction
if st.button("🚀 Generate Introduction"):
    if not name or not country or not job_role or not hobbies or not fun_fact or not favorite:
        st.error("Please fill in all fields before generating your introduction.")
    else:
        with st.spinner("Generating your introduction..."):
            response = llm_chain.run({
                "name": name,
                "country": country,
                "job_role": job_role,
                "hobbies": hobbies,
                "fun_fact": fun_fact,
                "favorite": favorite,
                "tone": tone
            })

        st.subheader("🎤 Your Personalized Introduction:")
        st.write(response)

        # Download Option
        st.download_button(
            label="📥 Download Introduction",
            data=response,
            file_name="my_introduction.txt",
            mime="text/plain"
        )
# Footer for Credits (displayed at the end)
import streamlit as st

# Footer for Credits (displayed at the end)
st.markdown("""---""")
st.markdown(
    """
    <div style="background: linear-gradient(to right, blue, purple); padding: 15px; border-radius: 10px; text-align: center; margin-top: 20px; color: white;">
        <p style="font-size:18px;">Made with ❤️ by <b>Anubhav Verma</b></p>
        <p>Connect with me:</p>
        <a href="https://www.instagram.com/anubhvv" target="_blank" style="margin-right: 10px;">
            <img src="https://drive.google.com/file/d/1xY7kt2TBGm7yZOqU5pPBv4_LCjITqSY4/view?usp=sharing" width="30">
        </a>
        <a href="https://www.linkedin.com/in/anubhvv" target="_blank" style="margin-right: 10px;">
            <img src="https://drive.google.com/file/d/1Yr_lLF5ni3cLmRd7iGGBEYrIZvImYxAt/view?usp=sharing" width="30">
        </a>
        <a href="mailto:anubhav.verma360@gmail.com" target="_blank">
            <img src="https://drive.google.com/file/d/1hiRwNG3TUAkGJlop2CTZRTKoYf9r-FZG/view?usp=sharing" width="30">
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)
