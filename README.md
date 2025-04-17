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

1️⃣ Install Ollama on Windows
- Download Ollama for Windows from the official website:
👉 https://ollama.com
- Install the application using the installer.
- Once installed, open Command Prompt and run:
      ollama pull llama3.2

Note: Model performance depends on your system configuration.
Choose a model that's suitable for your CPU. You can ask ChatGPT or Gemini which Ollama model works best for your hardware.

2️⃣ Start Ollama
- Make sure the Ollama background service is running. You can check this by running:
      ollama run llama3.2

Note: If the model isn't already downloaded, Ollama will automatically download it the first time you run this command.

3️⃣ Run TypoGenie
- Ensure you have Python 3.10 or higher installed on Windows.
👉 Download from https://www.python.org/downloads/windows/
- Open Command Prompt inside the TypoGenie project folder.
- Install the required dependencies:
      pip install -r requirements.txt
- Start TypoGenie:
      python main.py
- In the popup that appears, click the settings icon ⚙️.
- Enter the model name (e.g., llama3.2) based on the model you've installed via Ollama.

✅ If you're using ChatGPT or Gemini, you'll need to provide your API key in the settings.

🎉 Congratulations!
TypoGenie is now running in the background and will automatically fix your copied text whenever you press Ctrl+C.

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
