## **Day 1 – Getting Started with GenAI (Gemini)**

Welcome to **Day 1** of your Generative AI journey! 🎉
Today, we’ll learn how to set up **Google Gemini API** and send our first AI request from Python.

---

### **📌 What You’ll Learn**

* What an API key is and why it’s needed
* How to connect to Google Gemini in Python
* How to send a text prompt and receive an AI-generated response

---

### **🛠️ Setup Instructions**

#### 1. Create a Project Folder

```bash
mkdir Gen-AI
cd Gen-AI
mkdir Day1
```

#### 2. Create a Virtual Environment

```bash
python -m venv genai_env
```

#### 3. Activate Virtual Environment

* **Windows**

  ```bash
  genai_env\Scripts\activate
  ```
* **Mac/Linux**

  ```bash
  source genai_env/bin/activate
  ```

#### 4. Install Required Libraries

```bash
pip install google-generativeai python-dotenv
```

---

### **🔑 Get Your Gemini API Key**

1. Visit [Google AI Studio API Keys](https://aistudio.google.com/app/apikey)
2. Click **Create API Key**
3. Copy the key

---

### **📄 Create `.env` File**

Inside your project folder, create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### **📜 Code Example – `test_gemini.py`**

```python
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose the model
model = genai.GenerativeModel("gemini-pro")

# Your prompt
prompt = "Hello Gemini! Can you give me 3 creative ideas for a Python project?"

# Generate AI response
response = model.generate_content(prompt)

# Output result
print("Gemini Response:")
print(response.text)
```

---

### **▶️ Run the Script**

```bash
python Day1/test_gemini.py
```

---

### **✅ Expected Output**

```
Gemini Response:
1. A weather chatbot that answers in pirate language.
2. An AI-based recipe suggester based on fridge items.
3. A fun quiz app that generates questions using AI.
```

---

### **🎯 Day 1 Goal**

By the end of today:

* You understand how to install and use the Gemini Python SDK
* You know how to store and use API keys securely
* You can send a prompt and get a response from a GenAI model

