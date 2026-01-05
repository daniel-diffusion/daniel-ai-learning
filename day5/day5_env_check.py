import os
from dotenv import load_dotenv

load_dotenv()

#api_key = os.getenv("OPENAI_API_KEY")
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
if not azure_api_key:
    print("Warning: AZURE_OPENAI_API_KEY environment variable is not set.")
else:
    print(f"AZURE_OPENAI_API_KEY is set: {azure_api_key[:21]}...")