# Clase Tres - 26 de Febero del 2026

# Repaso

* Ejecutar un modelo de lenguaje Open Source : ollama, lmstudio
  * Hugging Face (https://huggingface.co/)
* Ejemplo de uso de la api Key de Google
* Gradio
  * Integramos gradio con la llamada a una api key

# Arquitectura

* Agentes
  * Ejecutar el LLM Local
    * (Con una pc potente que lo soporte)
    * Podes ejecutar modelos no cesurados GPT-J
  * Deplegar un LLM en alguna solucion cloude
    * Amazon, Azure, Google
  * Utilizar la api key
    * (sin informacion sensible)

# Chatbot en Gradio

> https://colab.research.google.com/drive/1kohUhz0fBm062t3-1Ju1hTcsQ5KPM1po?usp=sharing

```python
import gradio as gr
from openai import OpenAI

MODEL = "openai/gpt-oss-20b"
SYSTEM_PROMPT = """
Eres un narrador de historias interactivas del estilo "Elige tu propia aventura".

Reglas obligatorias:

1. Debes escribir una historia breve (máximo 300 palabras por turno).
2. Al final de cada turno debes ofrecer exactamente 3 opciones numeradas (1, 2, 3). Devuelve la lista de opciones numeradas
2.1. Si el usuario elige algo que no est dentro de las opciones responde "OPCION NO RECONOCIDA. Vuelve a intentar"
3. El usuario solo puede responder con el número de una opción.
4. Una de las opciones puede conducir a la muerte del personaje.
5. La historia debe finalizar en un máximo de 5 decisiones del usuario.
6. Cuando la historia termine debes escribir únicamente: FIN
7. Si el usuario elige una opción inválida, pídele que elija 1, 2 o 3 sin avanzar la historia.
8. No expliques reglas. No hagas comentarios fuera de la narración.
9. Responder la hstoria en español

Comienza la historia ahora.
Devuelve solamente la narracion sin acotar nada mas
"""

def generar_respuesta(api_key, messages):
  client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

  response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    max_tokens=500
  )

  return response.choices[0].message.content


def procesar_mensaje(api_key, mensaje, historial, historial_de_chatgpt):
  if historial is None:
    historial = []

  if not api_key:
    historial.append((mensaje, "Debe definir su api key"))
    return "", historial, historial_de_chatgpt

  historial_de_chatgpt.append({ "role" : "user", "content" : mensaje })
  respuesta_ia = generar_respuesta(api_key, historial_de_chatgpt)
  historial_de_chatgpt.append({ "role" : "assistant", "content" : respuesta_ia })
                                   
  historial.append((mensaje, respuesta_ia))
  
  return "", historial,  historial_de_chatgpt

with gr.Blocks() as demo:
  gr.Markdown("# Elije tu propia aventura con IA");
  api_key = gr.Textbox(label="API Key", type="password")

  chatbot = gr.Chatbot(height=300)
  
  with gr.Row():
    mensaje = gr.Textbox(show_label=False, placeholder="Escribe un mensaje...", scale=8)
    boton_enviar = gr.Button("Enviar")

  historial = gr.State([])
  historial_para_chatgpt = gr.State([
      { "role" : "system", "content" : SYSTEM_PROMPT }
  ])

  boton_enviar.click(
      fn=procesar_mensaje,
      inputs=[api_key, mensaje, historial, historial_para_chatgpt],
      outputs=[mensaje, chatbot, historial_para_chatgpt]
  )

  mensaje.submit(
      fn=procesar_mensaje,
      inputs=[api_key, mensaje, historial, historial_para_chatgpt],
      outputs=[mensaje, chatbot, historial_para_chatgpt]
  )

demo.launch()
```

# Recurso para aprender Machine Learning

* El recurso mas importante del mundo para aprender Machine Learning, deep learning...
  
> https://www.kaggle.com/


# Usar modelos de Hugging Face

> https://huggingface.co/

```python
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2")

print ("Colon descubrio")
resultado = pipe(
    "Colon descubrio",
    max_length = 4
)

print("-----------")
print(resultado[0]["generated_text"])
print("-----------")
```
