# 🧞 TypoGenie

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Mac%20%7C%20Linux-green)
![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)

> AI-powered clipboard assistant that silently fixes grammar and optimizes code while you copy — then magically improves it when you paste.  
> **Currently supports Windows only.**

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
👉 [Download llama3.2:3b](https://ollama.com/library/llama3.2:3b)

---

### 2️⃣ Start Ollama  
After installation, make sure Ollama is running.  

To check Open your terminal and run:
- ollama run llama3.2
- you can close this after checking


### 3️⃣ Run TypoGenie  
- Download and extract the `TypoGenie-Windows.zip`
- Double-click `TypoGenie.exe`
- Let the magic begin! 🪄  
TypoGenie will start correcting your copied text automatically.

---

## ⚙️ Settings Panel

Click the ⚙️ icon in the popup to:
- Choose your AI model: **Ollama**, **ChatGPT**, or **Gemini**
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
