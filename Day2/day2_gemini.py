import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

response = chat.send_message("Explain Python variables simply with an example.")
print(response.text)

follow_up = chat.send_message("Give me a short quiz about it.")
print(follow_up.text)
