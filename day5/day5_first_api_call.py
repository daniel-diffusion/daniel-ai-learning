import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
You are phisycs teacher.
Explain a blackhole in simple terms for a colleage student.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
)
print(response.output_text)
