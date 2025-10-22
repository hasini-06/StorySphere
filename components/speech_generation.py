from gtts import gTTS
import streamlit as st
import tempfile
import os

def generate_speech(text):
    try:
        tts = gTTS(text=text, lang="en")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        st.error(f"Speech generation failed: {e}")
        return None
