# **Day 2 – OpenAI/Gemini API Basics**

## **Topics Covered**

* Introduction to using AI APIs in Python
* Difference between **System** and **User** messages
* Setting up environment variables for API security
* Sending multiple prompts and receiving responses

---

## **Steps**

### **1. Install Required Packages**

```bash
pip install google-generativeai python-dotenv
```

---

### **2. Create a `.env` File**

Add your Gemini API key inside `.env`:

```env
GEMINI_API_KEY=your_real_api_key_here
```

---

### **3. Add `.gitignore`**

```gitignore
.env
```

---

### **4. Python Script**

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model and start chat
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Send first message
response = chat.send_message("Explain Python variables simply with an example.")
print(response.text)

# Send follow-up
follow_up = chat.send_message("Give me a short quiz about it.")
print(follow_up.text)
```

---

### **5. Run the Script**

```bash
python day2_gemini.py
```

---

## **Learning Goals**

* Understand API authentication
* Learn how to send and receive chat messages with Gemini
* Practice prompt engineering basics
* Keep your API keys secure using `.env`

---
