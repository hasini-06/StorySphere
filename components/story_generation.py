import streamlit as st
from groq import Groq

def generate_story(prompt: str, max_tokens: int = 400, temperature: float = 0.8):
    """
    Generate creative and realistic stories using Groq's Llama model.
    """
    try:
        client = Groq(api_key=st.secrets["groq"]["api_key"])

        model = "llama-3.3-70b-versatile"

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a talented storyteller who writes in a realistic yet emotional style. "
                        "Use simple and clear English so anyone can understand, but make the story engaging, expressive, and full of feeling. "
                        "Add a touch of imagination and vivid descriptions that help readers picture the scene. "
                        "Stories should have natural dialogue, a clear beginning and end, and a meaningful message. "
                        "Avoid robotic or routine-like storytelling."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            model=model,
            temperature=temperature, 
            max_tokens=max_tokens,
        )

        story = chat_completion.choices[0].message.content.strip()
        return story

    except Exception as e:
        st.error(f"Error generating story: {e}")
        return None
