import streamlit as st
from openai import OpenAI

st.title("🚀 Chat con Groq")

# Inicializar estados
if "api_key" not in st.session_state:
    st.session_state.api_key = None

if "historial" not in st.session_state:
    st.session_state.historial = []

# Input API Key
st.subheader("🔑 Configurar API Key")

api_key_input = st.text_input(
    "Ingresa tu GROQ_API_KEY",
    type="password"
)

if st.button("Establecer API Key"):
    st.session_state.api_key = api_key_input
    st.success("✅ API Key configurada")

# Mostrar historial del chat
for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# Input de mensaje
mensaje_usuario = st.chat_input("Escribe tu mensaje")

if mensaje_usuario:

    if not st.session_state.api_key:
        st.error("❌ Debes configurar primero tu API Key.")
    else:

        # Guardar mensaje del usuario
        st.session_state.historial.append({
            "role": "user",
            "content": mensaje_usuario
        })

        with st.chat_message("user"):
            st.markdown(mensaje_usuario)

        # Cliente Groq
        client = OpenAI(
            api_key=st.session_state.api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        respuesta = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=st.session_state.historial
        )

        respuesta_texto = respuesta.choices[0].message.content

        # Mostrar respuesta
        with st.chat_message("assistant"):
            st.markdown(respuesta_texto)

        # Guardar respuesta
        st.session_state.historial.append({
            "role": "assistant",
            "content": respuesta_texto
        })

# Botón para limpiar conversación
if st.button("🧹 Limpiar conversación"):
    st.session_state.historial = []
    st.rerun()