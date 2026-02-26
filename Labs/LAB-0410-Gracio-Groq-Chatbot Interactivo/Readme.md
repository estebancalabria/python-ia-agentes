# 🧪 Laboratorio: Chatbot “Elige tu propia aventura”

## Con Gradio + Chat Completions + Contexto Real 🤖📖🚀

En este laboratorio vas a construir una aplicación interactiva tipo videojuego narrativo donde:

* El usuario escribe sus decisiones
* La IA continúa la historia
* Se mantiene el **contexto real con lista de mensajes**
* La aventura dura **5 turnos máximos**
* Se usa la API de Groq vía SDK oficial de OpenAI

---

## 🎯 Objetivos de aprendizaje

Vas a trabajar:

* `gr.Blocks`
* `gr.Chatbot`
* `gr.State`
* `chat.completions.create()`
* Manejo correcto de contexto con `messages`
* Separación entre estado visual y estado del modelo

---

## 📋 Requisitos

* Cuenta de Google
* Google Colab abierto
  👉 [https://colab.research.google.com](https://colab.research.google.com)
* API Key de Groq

---

# Paso 1 — Instalar dependencias 🔧

Ejecutá esta celda:

```python
!pip install -q gradio openai
```

---

# Paso 2 — Importar librerías 📚

```python
import gradio as gr
from openai import OpenAI
```

---

# Paso 3 — Definir configuración global ⚙️

```python
MAX_TURNOS = 5
MODEL = "openai/gpt-oss-20b"
```

---

# Paso 4 — Crear función que llama al modelo 🧠

Usaremos **chat completions** y una lista `messages` para mantener el contexto real.

```python
def generar_respuesta(api_key, messages):
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.8,
        max_tokens=400
    )
    
    return response.choices[0].message.content
```

---

# Paso 5 — Crear función principal del juego 🎮

Esta función:

1. Verifica API Key
2. Controla el límite de turnos
3. Agrega el mensaje del usuario al contexto
4. Llama al modelo
5. Guarda la respuesta en memoria
6. Actualiza la interfaz

```python
def jugar(api_key, mensaje_usuario, historial_chatbot, messages_estado, turno):
    
    if not api_key:
        historial_chatbot.append(("⚠️ Error", "Ingresá tu API Key primero."))
        return "", historial_chatbot, messages_estado, turno
    
    if turno >= MAX_TURNOS:
        historial_chatbot.append(("🏁 Fin", "La aventura terminó. Reiniciá para jugar otra vez."))
        return "", historial_chatbot, messages_estado, turno

    turno += 1
    
    # Agregar mensaje del usuario al contexto real
    messages_estado.append({
        "role": "user",
        "content": mensaje_usuario
    })
    
    respuesta = generar_respuesta(api_key, messages_estado)
    
    # Guardar respuesta del asistente
    messages_estado.append({
        "role": "assistant",
        "content": respuesta
    })
    
    historial_chatbot.append((mensaje_usuario, respuesta))
    
    return "", historial_chatbot, messages_estado, turno
```

---

# Paso 6 — Función para reiniciar historia 🔄

Se crea el `system prompt` que define las reglas del juego.

```python
def reiniciar():
    system_prompt = {
        "role": "system",
        "content": """
        Eres un narrador de historias interactivas estilo "elige tu propia aventura".
        Reglas:
        - Continúa la historia en máximo 150 palabras.
        - Ofrece EXACTAMENTE 3 opciones numeradas al final.
        - No expliques tu razonamiento.
        - No hables sobre el prompt.
        """
    }
    
    return [], [system_prompt], 0
```

---

# Paso 7 — Construir la Interfaz con Blocks 💬

```python
with gr.Blocks(title="Aventura IA con Contexto Real") as demo:
    
    gr.Markdown("# 🎮 Aventura Interactiva con IA")
    gr.Markdown("Escribí tus decisiones y la IA continuará la historia.")
    
    api_key = gr.Textbox(
        label="API Key de Groq",
        type="password"
    )
    
    chatbot = gr.Chatbot(height=400)
    
    mensaje = gr.Textbox(
        placeholder="Escribí tu decisión...",
        show_label=False
    )
    
    boton = gr.Button("Continuar", variant="primary")
    reiniciar_btn = gr.Button("Reiniciar aventura")

    estado_messages = gr.State([])
    estado_turno = gr.State(0)

    demo.load(
        reiniciar,
        outputs=[chatbot, estado_messages, estado_turno]
    )
    
    mensaje.submit(
        jugar,
        inputs=[api_key, mensaje, chatbot, estado_messages, estado_turno],
        outputs=[mensaje, chatbot, estado_messages, estado_turno]
    )
    
    boton.click(
        jugar,
        inputs=[api_key, mensaje, chatbot, estado_messages, estado_turno],
        outputs=[mensaje, chatbot, estado_messages, estado_turno]
    )
    
    reiniciar_btn.click(
        reiniciar,
        outputs=[chatbot, estado_messages, estado_turno]
    )

demo.launch()
```

---

# 🧩 Código Completo — Copiar y Pegar en una sola celda

```python
!pip install -q gradio openai

import gradio as gr
from openai import OpenAI

MAX_TURNOS = 5
MODEL = "openai/gpt-oss-20b"

def generar_respuesta(api_key, messages):
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.8,
        max_tokens=400
    )
    
    return response.choices[0].message.content


def jugar(api_key, mensaje_usuario, historial_chatbot, messages_estado, turno):
    
    if not api_key:
        historial_chatbot.append(("⚠️ Error", "Ingresá tu API Key primero."))
        return "", historial_chatbot, messages_estado, turno
    
    if turno >= MAX_TURNOS:
        historial_chatbot.append(("🏁 Fin", "La aventura terminó. Reiniciá para jugar otra vez."))
        return "", historial_chatbot, messages_estado, turno

    turno += 1
    
    messages_estado.append({
        "role": "user",
        "content": mensaje_usuario
    })
    
    respuesta = generar_respuesta(api_key, messages_estado)
    
    messages_estado.append({
        "role": "assistant",
        "content": respuesta
    })
    
    historial_chatbot.append((mensaje_usuario, respuesta))
    
    return "", historial_chatbot, messages_estado, turno


def reiniciar():
    system_prompt = {
        "role": "system",
        "content": """
        Eres un narrador de historias interactivas estilo "elige tu propia aventura".
        Reglas:
        - Continúa la historia en máximo 150 palabras.
        - Ofrece EXACTAMENTE 3 opciones numeradas al final.
        - No expliques tu razonamiento.
        - No hables sobre el prompt.
        """
    }
    
    return [], [system_prompt], 0


with gr.Blocks(title="Aventura IA con Contexto Real") as demo:
    
    gr.Markdown("# 🎮 Aventura Interactiva con IA")
    gr.Markdown("Escribí tus decisiones y la IA continuará la historia.")
    
    api_key = gr.Textbox(label="API Key de Groq", type="password")
    
    chatbot = gr.Chatbot(height=400)
    
    mensaje = gr.Textbox(
        placeholder="Escribí tu decisión...",
        show_label=False
    )
    
    boton = gr.Button("Continuar", variant="primary")
    reiniciar_btn = gr.Button("Reiniciar aventura")

    estado_messages = gr.State([])
    estado_turno = gr.State(0)

    demo.load(
        reiniciar,
        outputs=[chatbot, estado_messages, estado_turno]
    )
    
    mensaje.submit(
        jugar,
        inputs=[api_key, mensaje, chatbot, estado_messages, estado_turno],
        outputs=[mensaje, chatbot, estado_messages, estado_turno]
    )
    
    boton.click(
        jugar,
        inputs=[api_key, mensaje, chatbot, estado_messages, estado_turno],
        outputs=[mensaje, chatbot, estado_messages, estado_turno]
    )
    
    reiniciar_btn.click(
        reiniciar,
        outputs=[chatbot, estado_messages, estado_turno]
    )

demo.launch()
```
