# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:49:13 2024

@author: mateh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:35:26 2024

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

chat = model.start_chat()

def process_response(response):
    additional_info="- Procesado con vertex AI"
    return response.text + additional_info

def llm_function(chat, query):
    #chat.send_message(query) # Send the user's query to the chat session
    response = chat.send_message(query) # Retrieve the response from the chat session
    processed_response = process_response(response)# Process the response as needed
    #st.write(processed_response) # Display the processed response in the Streamlit app
    #st.session_state.messages.append(processed_response) # Update the session state with the messages
    return processed_response

# Example usage
st.title("Chat con Vertex AI")

if "messages" not in st.session_state: # Lista de mensajes en el estado de la sesión
    st.session_state.messages=[]

with st.form(key="my_form",clear_on_submit=True): # Formulario para la entrada del usuario
    user_input=st.text_input("Hola, ¿como estas?. Escribe tu consulta.")
    submit_button=st.form_submit_button(label="Enviar")

if submit_button and user_input: # Manejo del envío de formulario
    response=llm_function(chat, user_input)
    st.session_state.messages.append(f"Tu: {user_input}")
    st.session_state.messages.append(f"Bot: {response}")

if st.session_state.messages: # Mostrar los mensajes en la aplicación
    for message in st.session_state.messages:
        st.write(message)