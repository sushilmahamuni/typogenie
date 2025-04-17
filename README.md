# 🧞 TypoGenie

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Mac%20%7C%20Linux-green)
![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)

> AI-powered clipboard assistant that silently fixes grammar and optimizes code while you copy — then magically improves it when you paste.  
---

## ✨ What is TypoGenie?

TypoGenie runs in the background, monitoring your clipboard.  
When you copy text (Ctrl+C), it automatically:
- Fixes grammar and spelling using AI
- Replaces the clipboard with the improved version
- Lets you paste cleaner, smarter text (Ctrl+V)

It's like having a personal AI genie at your fingertips. 🧞‍♂️

---

## 🧰 Setup Instructions

### 1️⃣ Download Ollama Locally  
Install the Ollama model from the official website:  
👉 [Download llama3.2:latest](https://ollama.com/library/llama3.2:latest)

Note: These models purely depend on your system configuration. Please use only the ones that are best suited for your setup. You can also ask ChatGPT or Gemini to suggest the most compatible ollama models based on your CPU details.

---

### 2️⃣ Start Ollama  
After installation, make sure Ollama application is running.  

Next then run below command it will download the model if not present:
- ollama run llama3.2


### 3️⃣ Run TypoGenie  
Make sure you have **Python 3.10** installed.  

Install required dependency
  pip install -r requirements.txt

Then run:
  python main.py

- Select settings icon⚙️ from popup menu. type model name like llama3.2 based on the model you've installed. if chatgpt or gemini then keys are required.

Congratulations! TypoGenie is now running in the background and will automatically fix your copied text

---

## ⚙️ Settings Panel

Click the ⚙️ icon in the popup to:
- Choose your AI model: **Ollama**, **ChatGPT**, or **Gemini**
- type model name like llama3.2 based on the model you've installed. if chatgpt or gemini then keys are required.
- Enter API keys if using ChatGPT/Gemini
- Customize default settings

---

## ⌨️ Hotkeys

| Key Combo          | Action                       |
|--------------------|------------------------------|
| `Ctrl + C`         | Copy (TypoGenie will correct)|
| `Ctrl + Shift + E` | Toggle TypoGenie on/off      |

---

## 🧠 Smart Behavior

- Ignores very short or unimportant clipboard text
- Automatically skips re-correction of already processed text
- Corrects silently without interrupting your workflow

---

## 🔒 Privacy First

- All corrections happen **locally** by default (Ollama)
- API-based models (ChatGPT, Gemini) only activate when you choose them
- **Your clipboard is never shared online** unless you configure it that way

---

## 💬 Feedback & Contributions

Have feedback or want to contribute?  
Open an issue, fork the repo, or submit a pull request!

---

### © 2024 TypoGenie – Your text, your magic. 🧞‍♂️
