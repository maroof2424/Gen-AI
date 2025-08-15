import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """
You are a professional storyteller.
Write a 100-word bedtime story for kids about a robot who learns to dance.
Make it funny and heartwarming.
"""

response = model.generate_content(prompt)
print("\n--- Story ---\n")
print(response.text)

