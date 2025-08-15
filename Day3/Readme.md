# **Day 3 – Prompt Engineering Intro**

### **Topics**

* **Role-based prompts** – Instruct the AI to act as a specific role (teacher, developer, poet, etc.) for better results.
* **Zero-shot prompting** – Give the AI a task without examples.
* **Few-shot prompting** – Give the AI a task with 1–3 examples for better accuracy.

---

## **Theory**

### **1. Role-based Prompts**

Instead of asking:

```
Write a story about a cat.
```

Ask:

```
You are a creative children's author. Write a short, fun story about a cat who wants to learn cooking.
```

**Why?** The AI adopts the “role” and tailors tone, vocabulary, and style.

---

### **2. Zero-shot Prompting**

* **Definition:** Ask the AI to perform a task without giving examples.
* **Example:**

```
Summarize this text in one sentence: "Python is an interpreted, high-level programming language."
```

---

### **3. Few-shot Prompting**

* **Definition:** Give 1–3 examples so the AI knows the expected style/output.
* **Example:**

```
Translate the following words from English to Urdu:
Dog → کتا
Cat → بلی
Bird → پرندہ
Lion →
```

---

## **Mini Project – AI Storyteller Script**

**File:** `day3_storyteller.py`

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-1.5-flash")

# Role-based storytelling
prompt = """
You are a professional storyteller.
Write a 100-word bedtime story for kids about a robot who learns to dance.
Make it funny and heartwarming.
"""

response = model.generate_content(prompt)
print("\n--- Story ---\n")
print(response.text)
```

---

## **Day 3 Tasks**

* Experiment with **different roles** (teacher, scientist, comedian, etc.).
* Try **zero-shot** and **few-shot** on the same question — compare results.
* Save your best **story outputs** in a file.

---