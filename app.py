import os
from google import genai
from google.genai import types
import gradio as gr

# 1. Check for Render environment variable
api_key = os.getenv("GEMINI_API_KEY")

# 2. If running in Colab and key isn't set in environment, load from Colab Secrets
if not api_key:
    try:
        from google.colab import userdata
        api_key = userdata.get("GEMINI_API_KEY")
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("GEMINI_API_KEY missing! Set it in Colab Secrets or Render Environment Variables.")

client = genai.Client(api_key=api_key)

personalities = {
  "Friendly": "You are a friendly, enthusiastic, and highly encouraging Study Assistant. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding.",
  "Academic": "You are a strictly academic, highly detailed, and professional university Professor. Use precise, formal terminology, cite key concepts and structure your response. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding."
}

def study_assistant(question, persona):
    system_prompt = personalities[persona]

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=1000
        ),
        contents=question
    )
    return response.text

demo = gr.Interface(
    fn=study_assistant,
    inputs=[
        gr.Textbox(lines=4, placeholder="Ask a question...", label="Question"),
        gr.Dropdown(choices=list(personalities.keys()), value="Friendly", label="Personality")
    ],
    outputs=gr.Textbox(lines=10, label="Response"),
    title="Study Assistant",
    description="Ask a question and get an answer from your AI study assistant with a chosen personality."
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
