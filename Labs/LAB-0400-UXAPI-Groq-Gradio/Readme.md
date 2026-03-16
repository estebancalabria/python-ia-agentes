# Laboratorio: Crear una interfaz de chat con Gradio y la API de Groq

Este laboratorio te guía para crear una aplicación de chat en tiempo real usando **Gradio** y la **API de Groq**, con entrada manual de la clave API y el prompt.

---

## Requisitos previos

- Tener una cuenta en [Groq Console](https://console.groq.com/)
- Tener Python instalado localmente (o usar Colab/Notebook con interfaz gráfica compatible)

---

## Paso 1: Obtener tu API Key en Groq

1. Ve a [https://console.groq.com/](https://console.groq.com/)
2. Inicia sesión o crea una cuenta.
3. Ve a **API Keys** y crea una nueva clave.
4. Copia la clave (ej. `gsk_xxxx...`).

---

## Paso 2: Instalar dependencias

Ejecuta en tu terminal o en una celda si usas Colab/Notebook:

```python
!pip install gradio openai
```

---

## Paso 3: Crear la aplicación Gradio

Crea una nueva celda de código (o archivo `.py`) y pega el siguiente código:

```
import gradio as gr
from openai import OpenAI

# Almacena la API key globalmente (solo para este ejemplo simple)
api_key_global = None

def establecer_api_key(api_key):
    global api_key_global
    api_key_global = api_key
    return "✅ API Key configurada. Ahora puedes chatear."

def procesar_prompt(prompt):
    global api_key_global
    if not api_key_global:
        return "❌ Por favor, ingresa primero tu API Key."
    
    try:
        client = OpenAI(
            api_key=api_key_global,
            base_url="https://api.groq.com/openai/v1"
        )
        respuesta = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "Eres un asistente útil y conciso."},
                {"role": "user", "content": prompt}
            ]
        )
        return respuesta.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Interfaz Gradio con dos entradas: API Key y Chat
with gr.Blocks() as iface:
    gr.Markdown("# 🚀 Chat con Groq (ingresa tu API Key)")
    
    with gr.Row():
        api_input = gr.Textbox(label="🔑 Ingresa tu GROQ_API_KEY", type="password")
        api_btn = gr.Button("Establecer API Key")
    
    chatbot = gr.Chatbot(label="💬 Chat")
    msg = gr.Textbox(label="Escribe tu mensaje", placeholder="Ej: ¿Por qué son rápidos los modelos de Groq?")
    clear = gr.Button("Limpiar conversación")
    
    # Estado para mantener el historial
    chat_state = gr.State([])

    def responder(message, history):
        bot_response = procesar_prompt(message)
        history.append((message, bot_response))
        return "", history

    def limpiar():
        return [], []

    msg.submit(responder, [msg, chatbot], [msg, chatbot])
    clear.click(limpiar, None, [chatbot, chat_state])
    api_btn.click(establecer_api_key, api_input, api_input)

iface.launch()
```

---

## Paso 4: Iniciar una celda nueva

1. Si estás en **Google Colab**, haz clic en **+ Código** para crear una nueva celda.
2. Pega el código en esa celda.
3. Ejecútala. Aparecerá un enlace local (ej. `http://127.0.0.1:7860`) o un enlace público si Colab lo permite.
4. Abre el enlace en una nueva pestaña.
5. Ingresa tu API Key y comienza a chatear.

> 💡 **Nota**: En Colab, la interfaz Gradio puede requerir hacer clic en el enlace y luego seleccionar **"Acceder a la aplicación externa"**.

¡Listo! Tienes un chat interactivo con Groq usando Gradio.
'''
