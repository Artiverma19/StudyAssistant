# 🎓 AI-Powered Study Assistant

An interactive, AI-driven study companion built using Python, Google's Gemini API (`gemini-3.6-flash`), and Gradio. The assistant helps students break down complex concepts into simple, digestible explanations with customizable teaching personas (e.g., *Friendly & Encouraging* vs. *Formal & Academic*).

🚀 **Live Demo:** [https://study-assistant-efa4.onrender.com](https://study-assistant-efa4.onrender.com)

---

## ✨ Key Features

* **Customizable Teaching Personas**:
  * **Friendly**: Encouraging and enthusiastic, using beginner-friendly analogies and real-world examples with follow-up comprehension questions.
  * **Academic**: Precise and formal, structured like a university professor with formal terminology.
* **Powered by Gemini 3.6 Flash**: Built on Google's fast and intelligent `gemini-3.6-flash` model via the official `google-genai` SDK.
* **Interactive Gradio Interface**: Simple web UI providing real-time answers, customizable prompt options, and clear formatting.
* **Production-Ready & Cloud-Deployed**: Hosted on **Render** with dynamic port binding (`0.0.0.0:$PORT`) and secure environment variable handling.
* **Cross-Platform Compatibility**: Automatically supports both Google Colab Secrets (`google.colab.userdata`) during development and environment variables (`os.getenv`) in production.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **AI Engine & SDK:** `google-genai` (Model: `gemini-3.6-flash`)
* **UI Framework:** Gradio
* **Hosting / Cloud:** Render Web Service
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
.
├── app.py             # Core Gradio application & Gemini API integration script
├── requirements.txt   # Dependency file (gradio, google-genai)
└── README.md          # Project documentation
