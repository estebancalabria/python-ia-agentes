# Clase Nueve - 19 de Marzo 2026

# Repaso

* Herramientas
  * Anything LLM
  * Cursor
  * Claude Desktop
* Tool Calling
  * Buscar modelos que permitan tool calling
  * Utilizar la api de chat completion (la que mantiene el historial de chat)
  * Informar al modelo de lenguaje con que herramienta cuenta
  * El agente es que llama a la herramienta e informa al llm el resultado como parte de la conversacion del chat
* MCP
  * Model Context Protocol
  * Debo usar algun Cliente MCP (Cursor, Claude Desktop, AnythingLLM)
  * Servidores MCP
      * Programar el nuestro (no lo hicimos)
      * Utilizar uno que ya exista y hay coomo un moton de MCP disponibles (playwright, filesystem, etc)

# Agentes

* Tipos de Agente
    * Agente conversacional / Bot
    * Agente automatizacion
        * Mucho con n8n 

# Colab de la clase

> https://colab.research.google.com/drive/1dQKShASFdxMJ8pJYWQWDHOgT0hllHz5N?usp=sharing

# Generacion de Interfaces con Streamlit (local)

* Altarnativa a Colab mas pro
> https://streamlit.io/

* Para instalarlo
```cmd
pip install streamlit openai
```

```cmd
streamlit --version
Streamlit, version 1.55.0
```

* (Pueden instalarlo en un entorno virtual)

* El codigo de nuestro chatbot en streamlit
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
            model="llama-3.3-70b-versatile",
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

* Para ejecutarlo

```cmd
streamlit run app.py
```

Ir al navegador en la url que se propone

```
http://localhost:8501
```

# Generacion de Imagenes

* Alternativas
  * Modelos Propietarios
    * Api de OpenaAI tenemos a Gpt-Image
    * Nano bannano de google mediante api
  * Modelos Open Source
    * Estan en hugging face
        * https://huggingface.co/black-forest-labs/FLUX.1-dev

## Generacion de Imagenes con Modelos Open Source

* En colab cambiar el entorno de ejecucion para que use GPU

```python
!pip install diffusers transformers accelerate torch sentencepiece
```

```python
import torch
from diffusers import DiffusionPipeline

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.bfloat16
).to("cuda")

prompt = "A cute kitten and a cute dog fighting"
image = pipe(prompt).images[0]

image
```
  
# Code Execution

```python
from openai import OpenAI
import json

def ejecutar_codigo(codigo):
    """
    Ejecuta código Python seguro en un entorno controlado y devuelve el resultado.
    """
    resultado = None
    try:
        entorno = {}
        exec(codigo, {}, entorno)
        resultado = entorno.get("resultado", "No se definió variable 'resultado'")
    except Exception as e:
        resultado = f"Error en ejecución: {e}"
    return resultado

api_key = input("Ingrese su api key")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key = api_key
)

system_prompt = """
Eres un asistente que puede generar y ejecutar codigo en python para calculos estadisticos
Solo puedes responder generando codigo en python que defina una variable llamada resultado
No escribas texgo explicativo, solo el codigo en python listo para ejecutar
No utilices ni markdown, ni citas con ```, solamente devuelve texto
"""

prompt = input("Ingrese sus datos separado por comma que el modelo los analizara")

respuesta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages= [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"Los datos a analizar son {prompt}"
        }
    ]
)

codigo_python = respuesta.choices[0].message.content

print("-----------------")
print(codigo_python)
print("-----------------")

resultado = ejecutar_codigo(codigo_python)

print(f"Resultado ejecucion {resultado}")

```

# Un caso real de un agente no conversacional

