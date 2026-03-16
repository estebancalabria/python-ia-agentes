# Laboratorio: Crear una Interfaz de Chat con Streamlit y la API de Groq 🤖🚀

En este laboratorio vas a crear una **aplicación de chat tipo ChatGPT** usando **Streamlit** y la **API de Groq**.

La aplicación permitirá:

- Ingresar la **API Key de Groq**
- Enviar mensajes al modelo
- Mostrar respuestas del modelo
- Mantener el historial de conversación

Todo ejecutándose **localmente con Streamlit**.

---

# Requisitos previos 📋

Antes de comenzar necesitas:

- Tener una cuenta en **Groq Console**
- Tener **Python instalado**
- Tener conocimientos básicos de Python

---

# Paso 1: Obtener tu API Key en Groq 🔑

1. Ve a:

https://console.groq.com/

2. Inicia sesión o crea una cuenta.

3. Ve a **API Keys**.

4. Crea una nueva clave.

5. Copia la clave (ejemplo):

```

gsk_xxxxxxxxxxxxxxxxx

````

---

# Paso 2: Crear la Carpeta del Proyecto 📁

Crea una carpeta para el laboratorio:

```bash
streamlit-groq-chat
````

Entra en la carpeta:

```bash
cd streamlit-groq-chat
```

---

# Paso 3: Instalar Dependencias 🔧

Instala las librerías necesarias:

```bash
pip install streamlit openai
```

---

# Paso 4: Crear el Archivo de la Aplicación 📄

Crea un archivo llamado:

```
app.py
```

---

# Paso 5: Crear la Aplicación de Chat con Streamlit 💬

Copia el siguiente código dentro de `app.py`.

```python
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
            model="llama3-8b-8192",
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
```

---

# Paso 6: Ejecutar la Aplicación 🚀

Desde la terminal ejecuta:

```bash
streamlit run app.py
```

Streamlit iniciará un servidor local y verás algo como:

```
Local URL: http://localhost:8501
```

Abre esa dirección en tu navegador.

---

# Cómo usar la aplicación 💡

1️⃣ Ingresa tu **GROQ_API_KEY**

2️⃣ Presiona **Establecer API Key**

3️⃣ Escribe un mensaje en el chat

4️⃣ El modelo responderá usando **Groq**

---

# Código Completo 🧩

```python
import streamlit as st
from openai import OpenAI

st.title("🚀 Chat con Groq")

if "api_key" not in st.session_state:
    st.session_state.api_key = None

if "historial" not in st.session_state:
    st.session_state.historial = []

st.subheader("🔑 Configurar API Key")

api_key_input = st.text_input(
    "Ingresa tu GROQ_API_KEY",
    type="password"
)

if st.button("Establecer API Key"):
    st.session_state.api_key = api_key_input
    st.success("✅ API Key configurada")

for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

mensaje_usuario = st.chat_input("Escribe tu mensaje")

if mensaje_usuario:

    if not st.session_state.api_key:
        st.error("❌ Debes configurar primero tu API Key.")
    else:

        st.session_state.historial.append({
            "role": "user",
            "content": mensaje_usuario
        })

        with st.chat_message("user"):
            st.markdown(mensaje_usuario)

        client = OpenAI(
            api_key=st.session_state.api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        respuesta = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=st.session_state.historial
        )

        respuesta_texto = respuesta.choices[0].message.content

        with st.chat_message("assistant"):
            st.markdown(respuesta_texto)

        st.session_state.historial.append({
            "role": "assistant",
            "content": respuesta_texto
        })

if st.button("🧹 Limpiar conversación"):
    st.session_state.historial = []
    st.rerun()
```

---

# Qué está pasando (Explicación para clase) 🎓

## 1️⃣ Streamlit UI

Streamlit genera la interfaz web directamente desde Python.

Componentes utilizados:

* `st.chat_input()` → campo para escribir mensajes
* `st.chat_message()` → renderizar conversación
* `st.session_state` → guardar estado

---

## 2️⃣ Historial de conversación

El historial se guarda en:

```
st.session_state.historial
```

Esto permite enviar el **contexto completo al modelo**.

---

## 3️⃣ Cliente de Groq

Se usa la librería `openai` apuntando al endpoint de Groq:

```
base_url="https://api.groq.com/openai/v1"
```

---

## 4️⃣ Flujo de la aplicación

```
Usuario escribe mensaje
        ↓
Streamlit captura input
        ↓
Se envía a Groq API
        ↓
Groq genera respuesta
        ↓
Streamlit actualiza la interfaz
```

