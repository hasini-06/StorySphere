import streamlit as st
from huggingface_hub import InferenceClient
# from PIL import Image

def generate_image(prompt: str, system_prompt: str = None):
    """
    Generate a realistic image from a text prompt using Stable Diffusion via Hugging Face InferenceClient.
    The `system_prompt` adds realism and controls the style or mood.
    Returns a PIL.Image.Image object or None if generation fails.
    """

    if not prompt.strip():
        st.warning("Please enter a valid prompt for the image.")
        return None

    try:
        api_key = st.secrets["huggingface"]["api_key"]
        client = InferenceClient(api_key=api_key)

        model = "stabilityai/stable-diffusion-xl-base-1.0"

        if not system_prompt:
            system_prompt = (
                "emotional storytelling illustration, expressive character art, "
                "animated story scene with depth and feeling, warm and cool lighting contrast, "
                "narrative-focused composition, characters showing clear emotions, "
                "detailed environment that tells a story, cinematic storyboard style, "
                "Disney Pixar emotional storytelling, meaningful atmosphere, "
                "touching scene with visual narrative, soft painterly style"
            )

        final_prompt = f"{system_prompt}. {prompt}"

        image = client.text_to_image(
            model=model,
            prompt=final_prompt,
            width=768,  
            height=768,
            num_inference_steps=35,  
            guidance_scale=8.5       
        )

        return image  

    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None


