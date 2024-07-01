# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:23:02 2024

@author: mateh
"""
import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, ChatSession

# Inicializa Vertex AI con tu proyecto
project = "gemini-explorer-426816"
vertexai.init(project=project)

# Configuración del modelo
config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    model_name="gemini-pro",
    generation_config=config
)

def start_chat_session():
    return model.start_chat()

# Función para procesar la respuesta del modelo
def process_response(response):
    # Ejemplo de personalización: añadir información adicional
    additional_info = " - Procesado con Vertex AI"
    return response.text + additional_info

# Función para enviar un mensaje y obtener la respuesta
def llm_function(chat, query):
    response = chat.send_message(query)  # Enviar la consulta del usuario y obtener la respuesta
    processed_response = process_response(response)  # Procesar la respuesta según sea necesario
    return processed_response

# Inicializar la aplicación de Streamlit
st.title("Chat con Vertex AI")

# Inicializar la sesión de chat si no existe en el estado de la sesión
if "chat_session" not in st.session_state:
    st.session_state.chat_session = start_chat_session()

# Lista de mensajes en el estado de la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Form for user input
with st.form(key='my_form', clear_on_submit=True):
    user_name=st.text_input("Please enter your name")
    submit_button = st.form_submit_button(label='Enviar')

# Capture user's name
#user_name=st.text_input("Please enter your name")

# Capture user's name
if len(st.session_state.messages)==0:
    if user_name:
        initial_prompt=f"Hey {user_name}, I´m ReX, your interactive assitant powered by google gemini. Let's vibe together with emojis!"
        llm_function(st.session_state.chat_session, initial_prompt)
        
    #initial_prompt="Welcome i´m ReX, an assistant powered by google gemini :´v"
    response2=llm_function(st.session_state.chat_session, initial_prompt)
    st.session_state.messages.append(f"Tú: {initial_prompt}")
    st.session_state.messages.append(f"Bot: {response2}")
    
# Submit button
if st.button("Submit"):
    st.write(f"Hello, {user_name}!")

# Display ReX's response with the user's name
if user_name:
    st.write(f"Hey {user_name}, I'm ReX, your interactive assistant")

# Mostrar los mensajes en la aplicación
if st.session_state.messages:
    for message in st.session_state.messages:
        st.write(message)
