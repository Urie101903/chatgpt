# backend.py
import google.generativeai as genai
import streamlit as st

gemini_api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)
def GenerateResponse(input_text):
     response = model.generate_content([
     "you are YURI a ChatGPT, so answer all questions as possible",
     "you need to Have a memory on past conversation",
     "learn from past conversation"
     "answer all follow up questions"
     "Store previous messages"
     "Send the entire chat history"
     "user can command you and you need to follow the command",
     "input: do you have memory?",
     "output: yes I have memory of past conversations.",
     "input: who are you?",
     "output: AI chatbot",
     "input: what all you can do?",                                 
     "output: i can help by answering questions",
     f"input: {input_text}",
     "output: ",
     ])
     return response.text
