import streamlit as st
from components.story_generation import generate_story
from components.image_generation import generate_image
from components.speech_generation import generate_speech
import io

def main():
    st.title("Story Sphere ")

    prompt = st.text_area("Enter a story theme or idea:")
    system_prompt = st.text_input(
        "Enter image style/instructions (optional):",
        "Digital art, vibrant colors, cinematic style, highly detailed"
    )

    if st.button("Generate Story"):
        if prompt.strip():
            with st.spinner("Generating story..."):
                story = generate_story(prompt)
            if story:
                st.subheader("📖 Story")
                st.write(story)

                with st.spinner("Generating image..."):
                    image_data = generate_image(prompt, system_prompt=system_prompt)
                    if image_data:
                        st.image(image_data, caption="Generated Image", width="stretch")

                        buf = io.BytesIO()
                        image_data.save(buf, format="PNG")
                        st.download_button(
                            label="Download Image",
                            data=buf.getvalue(),
                            file_name="generated_image.png",
                            mime="image/png"
                        )

                with st.spinner("Generating narration..."):
                    audio_path = generate_speech(story)
                    if audio_path:
                        st.audio(audio_path)

                        with open(audio_path, "rb") as f:
                            st.download_button(
                                label="Download Audio",
                                data=f,
                                file_name="story_audio.mp3",
                                mime="audio/mpeg"
                            )
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
