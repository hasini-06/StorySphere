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
                        "You are a talented storyteller who writes complete, emotionally engaging stories. "
                        "Use simple and clear English so anyone can understand, but make the story expressive and full of feeling. "
                        "Add vivid descriptions that help readers picture the scene. "
                        "IMPORTANT: Every story MUST have three clear parts:\n"
                        "1. Beginning - Set up the characters and situation\n"
                        "2. Middle - Develop the conflict or journey with natural dialogue\n"
                        "3. Ending - Provide a satisfying, complete conclusion with resolution and meaningful message\n"
                        "The ending should feel final and complete, not abrupt or open-ended. "
                        "Give the story emotional closure that leaves readers feeling satisfied."
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
