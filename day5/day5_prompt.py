import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

topic = input("Enter a topic you want to learn about: ")
prompt = f"""
Explain {topic} 
    1) in simple terms 
    2) use analogies
    3) provide practical examples
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
)
print(response.output_text)
