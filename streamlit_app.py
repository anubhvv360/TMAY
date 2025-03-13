import streamlit as st
import os

# Function to create the detailed prompt using the provided inputs
def generate_prompt(name, country, job_role, hobbies, fun_fact, favorite, tone):
    prompt = (
        f"Using the following details, draft a 'Tell Me About Yourself' introduction:\n\n"
        f"Name (Fun Alias): {name}\n"
        f"Country of Origin: {country}\n"
        f"Job Role (What's your hustle?): {job_role}\n"
        f"Hobbies/Interests: {hobbies}\n"
        f"Fun Fact/Unique Detail: {fun_fact}\n"
        f"Favorite Emoji or Catchphrase: {favorite}\n"
        f"Tone: {tone}\n\n"
        f"Please generate an engaging and personalized self-introduction that reflects a {tone.lower()} tone. "
        f"Be sure to incorporate the fun alias, background, professional hustle, personal interests, and that quirky detail. "
        f"Finish with a creative touch using the favorite emoji or catchphrase."
    )
    return prompt

# Streamlit App Layout
st.set_page_config(page_title="Tell Me About Yourself Generator", layout="centered")
st.title("Tell Me About Yourself Generator")
st.markdown("Fill in the details below and click **Generate Introduction** to draft your personalized response.")

# User Inputs
name = st.text_input("Name (Fun Alias or Nickname)", placeholder="e.g., Maverick")
country = st.text_input("Country of Origin", placeholder="e.g., USA")
job_role = st.text_input("Job Role (What’s your hustle?)", placeholder="e.g., Software Engineer")
hobbies = st.text_input("Hobbies/Interests", placeholder="e.g., Gaming, Cooking, Painting")
fun_fact = st.text_input("Fun Fact or Unique Detail", placeholder="e.g., I once backpacked across Europe")
favorite = st.text_input("Favorite Emoji or Catchphrase", placeholder="e.g., 🚀 or 'Let's rock!'")

# Tone dropdown with additional options
tone_options = [
    "Professional", 
    "Casual", 
    "Friendly", 
    "Inspirational", 
    "Humorous", 
    "Confident", 
    "Charming",
    "Energetic",
    "Laid-back"
]
tone = st.selectbox("Tone", tone_options)

# Generate button and output section
if st.button("Generate Introduction"):
    # Build the prompt
    prompt = generate_prompt(name, country, job_role, hobbies, fun_fact, favorite, tone)
    
    st.subheader("Detailed Prompt")
    st.code(prompt, language="text")
    
    # Retrieve the API key from the environment variable
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Google API Key not found in environment variables. Please set GOOGLE_API_KEY.")
    else:
        # Here, you would typically integrate with LangChain and your Gemini LLM
        # For example, using a chain that takes in the prompt and returns a generated response.
        # Since the actual integration depends on your setup, we'll simulate a response.
        
        # Simulated response (replace this with your Gemini LLM integration code)
        simulated_response = (
            f"Hi there, I'm {name}! Born in {country}, I thrive as a {job_role}. "
            f"When I'm not on the clock, you can find me indulging in my love for {hobbies}. "
            f"One quirky fact about me is that {fun_fact}. And as a finishing touch, "
            f"my personal mantra is '{favorite}'—always keeping it {tone.lower()} and genuine."
        )
        
        st.subheader("Generated Introduction")
        st.write(simulated_response)
