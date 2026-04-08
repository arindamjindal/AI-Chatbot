from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(messages):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content