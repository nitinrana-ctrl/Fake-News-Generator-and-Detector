import os
from dotenv import load_dotenv
from google import genai

print("NEW generator.py loaded")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Using new google-genai SDK")

def generate_fake_headline(topic, tone):
    prompt = f"""
Generate a fictional fake news headline.

Topic: {topic}
Tone: {tone}

Rules:
- Make it realistic and attention-grabbing.
- Keep it under 20 words.
- Return only the headline.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text.strip()
        else:
            return "⚠️ No response received from Gemini AI."

    except Exception as e:
        print(f"Gemini Error: {e}")
        return (
            "⚠️ Gemini AI is currently unavailable due to high demand.\n\n"
            "Please try again after a few moments."
        )

def generate_fake_article(topic, tone):
    prompt = f"""
Generate a fictional fake news article.

Topic: {topic}
Tone: {tone}

Rules:
- Around 150–200 words.
- Make it sound like a newspaper article.
- Do not include any disclaimer.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text.strip()
        else:
            return "⚠️ No response received from Gemini AI."

    except Exception as e:
        print(f"Gemini Error: {e}")
        return (
            "⚠️ Gemini AI is currently unavailable due to high demand.\n\n"
            "Please try again after a few moments."
        )
        
        