import gradio as gr
from chatbot import ask_chatgpt

def chat_interface(user_input):
    return ask_chatgpt(user_input)

gr.ChatInterface(fn=chat_interface, title="Groq Chatbot 💬").launch()
