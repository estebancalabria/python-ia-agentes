# Laboratorio: Crear un Chatbot con Gradio en Google Colab 🤖🚀

---

## Introducción 📝

En este laboratorio, vas a construir una interfaz de chatbot similar a ChatGPT usando Gradio en Google Colab.

Aprenderás:

* Cómo usar `Blocks`
* Cómo usar `Chatbot`
* Cómo manejar estado con `gr.State`
* Cómo manejar eventos (`.submit()` y `.click()`)

---

## Requisitos 📋

* Cuenta de Google
* Conocimientos básicos de Python
* Google Colab abierto:
  👉 [https://colab.research.google.com](https://colab.research.google.com)

---

# Paso 1: Instalar Gradio 🔧

Ejecuta esta celda:

```python
!pip install -q gradio
```

---

# Paso 2: Importar Librerías 📚

```python
import gradio as gr
```

---

# Paso 3: Crear la Lógica del Chatbot 🧠

Vamos a crear una función que:

* Reciba el mensaje
* Reciba el historial
* Agregue una respuesta
* Devuelva el historial actualizado

```python
def responder(mensaje, historial):
    if historial is None:
        historial = []
    
    # Respuesta simple (modo demo)
    respuesta = f"🤖 Dijiste: {mensaje}"
    
    historial.append((mensaje, respuesta))
    
    return "", historial
```

---

# Paso 4: Construir la Interfaz del Chatbot 💬

Ahora vamos a crear una interfaz estilo ChatGPT usando `Blocks`.

```python
with gr.Blocks(title="Chatbot Demo Curso IA") as demo:
    
    gr.Markdown("# 🤖 Chatbot Demo con Gradio")
    gr.Markdown("Este es un chatbot simple creado en Google Colab.")
    
    chatbot = gr.Chatbot(height=400)
    
    with gr.Row():
        mensaje = gr.Textbox(
            placeholder="Escribí tu mensaje...",
            show_label=False,
            scale=8
        )
        boton_enviar = gr.Button("Enviar", variant="primary", scale=1)

    estado = gr.State([])

    # Enviar con Enter
    mensaje.submit(
        responder,
        inputs=[mensaje, estado],
        outputs=[mensaje, chatbot]
    )

    # Enviar con botón
    boton_enviar.click(
        responder,
        inputs=[mensaje, estado],
        outputs=[mensaje, chatbot]
    )
```

---

# Paso 5: Lanzar la Aplicación 🚀

```python
demo.launch()
```

---

# Código Completo 🧩 (Copiar y pegar en una sola celda)

```python
# Instalar Gradio
!pip install -q gradio

import gradio as gr

def responder(mensaje, historial):
    if historial is None:
        historial = []
    
    respuesta = f"🤖 Dijiste: {mensaje}"
    historial.append((mensaje, respuesta))
    
    return "", historial

with gr.Blocks(title="Chatbot Demo Curso IA") as demo:
    
    gr.Markdown("# 🤖 Chatbot Demo con Gradio")
    gr.Markdown("Este es un chatbot simple creado en Google Colab.")
    
    chatbot = gr.Chatbot(height=400)
    
    with gr.Row():
        mensaje = gr.Textbox(
            placeholder="Escribí tu mensaje...",
            show_label=False,
            scale=8
        )
        boton_enviar = gr.Button("Enviar", variant="primary", scale=1)

    estado = gr.State([])

    mensaje.submit(
        responder,
        inputs=[mensaje, estado],
        outputs=[mensaje, chatbot]
    )

    boton_enviar.click(
        responder,
        inputs=[mensaje, estado],
        outputs=[mensaje, chatbot]
    )

demo.launch()
```

---

# Qué está pasando (Explicación para clase) 🎓

## 1️⃣ UI Declarativa

`gr.Blocks()` define la interfaz.

## 2️⃣ Chatbot Component

`gr.Chatbot()` renderiza los mensajes en formato conversación.

## 3️⃣ Estado

`gr.State([])` guarda el historial.

## 4️⃣ Eventos

* `.submit()` → tecla Enter
* `.click()` → botón Enviar

## 5️⃣ Flujo Reactivo

Usuario → función Python → actualización del frontend

---

# Desafío Extra 🔥

Modificá la función para que:

* Responda en mayúsculas
* Simule que "piensa"
* Devuelva la hora actual
* Limite el historial a 5 mensajes
* Agregue botón "Limpiar conversación"

