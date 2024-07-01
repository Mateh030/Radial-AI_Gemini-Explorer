
import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project="gemini-explorer-426816"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    model_name="gemini-pro",
    generation_config=config
)

chat = model.start_chat()

#Example
user_input = "How are you today?"
response = chat.send_message(user_input)
print("Gemini's response:", response)

user_input1 = "Tell me a joke"
response1 = chat.send_message(user_input1)
print("Gemini's response:", response1)