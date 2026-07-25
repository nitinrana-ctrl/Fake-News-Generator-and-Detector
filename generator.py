import os
from dotenv import load_dotenv
from google import genai

print("NEW generator.py loaded")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

print("Using new google-genai SDK")

def generate_fake_headline(topic, tone):
    print("generate_fake_headline() called")
    
    prompt = f"""
Generate ONE fictional fake news headline.

Topic: {topic}
Tone: {tone}

Rules:
- Maximum 20 words.
- Return only the headline.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text.strip()


def generate_fake_article(topic, tone):
    prompt = f"""
Write a fictional fake news article.

Topic: {topic}
Tone: {tone}

Rules:
- 80 to 100 words.
- Write like a newspaper article.
- Make it fictional.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text.strip()