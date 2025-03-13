# Tell Me About Yourself Agent

Generate a detailed intro instantly!

A Streamlit application that generates a personalized "Tell Me About Yourself" introduction using user inputs and an LLM backend. The app collects details like a fun alias, country of origin, job role, hobbies, fun facts, and tone to build a detailed prompt. This prompt is then used to generate an engaging, custom self-introduction via Gemini LLM through LangChain.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://intro-agent.streamlit.app/)

## Features

- **Interactive UI:** A friendly interface built with Streamlit.
- **Detailed Input Collection:** Fields for fun alias, country, job role, hobbies/interests, fun fact, and favorite emoji/catchphrase.
- **Dynamic Prompt Generation:** Automatically creates a detailed prompt based on your inputs.
- **LLM Integration:** Ready to connect with Gemini LLM (via LangChain) for generating custom responses.
- **Secure API Key Management:** Uses environment variables to securely manage your Google API key.
