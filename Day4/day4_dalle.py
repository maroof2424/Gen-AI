import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model="gpt-image-1",
    prompt="A futuristic city with flying cars at sunset",
    size="1024x1024"  
)

image_url = response.data[0].url
print("Generated Image URL:", image_url)
