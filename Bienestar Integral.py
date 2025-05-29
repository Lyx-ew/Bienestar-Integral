import streamlit as st
import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'TU_CLAVE_DE_API_AQUI'

st.title("🤖 Chatbot de Autocuidado")

# Inicializa el historial de la conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Muestra el historial de la conversación
for msg in st.session_state.messages:
    st.write(f"**{msg['role'].capitalize()}:** {msg['content']}")

# Entrada del usuario
user_input = st.text_input("Tú:", "")

if user_input:
    # Agrega el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Genera la respuesta del asistente
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content.strip()

    # Agrega la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    # Muestra la respuesta del asistente
    st.write(f"**Asistente:** {assistant_reply}")