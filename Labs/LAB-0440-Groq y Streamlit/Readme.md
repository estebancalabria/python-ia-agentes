# 🧪 Laboratorio: Crear una interfaz de chat con Streamlit y la API de Groq

Este laboratorio te guía para crear una aplicación de chat usando **Streamlit** y la **API de Groq**, ingresando manualmente la API Key.

---

## 🎯 Requisitos previos

* Tener cuenta en [https://console.groq.com/](https://console.groq.com/)
* Tener Python instalado (o usar un entorno local / Codespaces)
* Tener tu `GROQ_API_KEY`

---

## 🔑 Paso 1: Obtener tu API Key en Groq

1. Ir a [https://console.groq.com/](https://console.groq.com/)
2. Crear una API Key
3. Copiarla (ej: `gsk_xxxxxxxxx`)

---

## 📦 Paso 2: Instalar dependencias

En tu terminal:

```bash
pip install streamlit openai
```

---

## 🧠 Paso 3: Crear la aplicación

Crea un archivo llamado:

```
app.py
```

Y pega el siguiente código:

```python
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Chat con Groq", page_icon="🚀")

st.title("🚀 Chat con Groq (Streamlit)")

# Inicializar estado
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "api_key" not in st.session_state:
    st.session_state.api_key = None


# Sidebar para API Key
st.sidebar.header("Configuración")
api_key_input = st.sidebar.text_input(
    "🔑 Ingresa tu GROQ_API_KEY",
    type="password"
)

if st.sidebar.button("Establecer API Key"):
    st.session_state.api_key = api_key_input
    st.sidebar.success("API Key configurada correctamente")


# Función para llamar a Groq
def consultar_groq(prompt):

    if not st.session_state.api_key:
        return "❌ Primero debes configurar tu API Key."

    try:
        client = OpenAI(
            api_key=st.session_state.api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "Eres un asistente útil y conciso."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"


# Mostrar historial
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Input de usuario
if prompt := st.chat_input("Escribe tu mensaje..."):

    # Guardar mensaje usuario
    st.session_state.chat_history.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtener respuesta
    respuesta = consultar_groq(prompt)

    # Guardar respuesta
    st.session_state.chat_history.append(
        {"role": "assistant", "content": respuesta}
    )

    with st.chat_message("assistant"):
        st.markdown(respuesta)


# Botón limpiar
if st.button("🧹 Limpiar conversación"):
    st.session_state.chat_history = []
    st.rerun()
```

---

## ▶️ Paso 4: Ejecutar la aplicación

Desde la terminal:

```bash
streamlit run app.py
```

Se abrirá automáticamente en:

```
http://localhost:8501
```

1. Ingresas tu API Key en la barra lateral.
2. Empiezas a chatear.
3. Puedes limpiar la conversación.

---

# 🧩 Diferencia pedagógica vs Gradio

| Gradio                            | Streamlit                                 |
| --------------------------------- | ----------------------------------------- |
| Más simple y rápido para demos    | Más orientado a apps reales               |
| Ideal para prototipos             | Ideal para dashboards y productos         |
| Estructura declarativa con Blocks | Estructura basada en ejecución por script |
