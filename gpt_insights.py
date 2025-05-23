import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_strategic_insights(prompt, max_tokens=1000):
    response = openai.ChatCompletion.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "You are a strategic forecasting assistant for Sentient HR Services."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.3
    )
    return response['choices'][0]['message']['content']