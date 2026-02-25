# Clase Dos - 24 de Febrero del 2026

# Repaso

* System Prompt
* Open Source vs Propietarios
* Google Colab
* Invocar LLM por API Key
  * OpenAI
  * Claude
  * Groq
    * Podiamos utilizar Modelos Open Source
* Formas de Invocar la API Key
  * Respuesta Unica
  * Chat Completion

 
# Google Colab

* Comentar Varias lineas : Ctrl+K+C
* Comentar Varias lineas : Ctrl+K+U

# Ejecurar un modelo Open Source Localmente 

* LMStudio : https://lmstudio.ai/
* Ollama : https://ollama.com/

# Ranking de Modelos de IA

* Un buen lugar para investigar y definir cual es el modelo subyacente que voy a utilizar para alimentar mi agente
> lmarena.ai
 
# Uso de la API key de Google

* Portal para el Usuario Final : https://gemini.google.com/app
* Portal para dev : https://aistudio.google.com/

1. Sacar la api key de Google
2. Ejecutar este codigo

```python
from google import genai

api_key = input("Ingrese su Api Key: ")
prompt = input("Ingrese su prompt: ")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
   model="gemini-2.5-flash",
   contents = prompt
)

print(response.text)

```

# Generando interfaces Gradio

> https://www.gradio.app/

* Instalo la libreria
  
```python
!pip install gradio
```

* Ejecuto mi hola mundo en Gradio

```python
import gradio as gr

def texto_a_mayusculas(texto):
  return texto.upper()

interfaz = gr.Interface(fn=texto_a_mayusculas, inputs="text", outputs="text")

interfaz.launch()
```

# Generando un chatbot simple con Gradio

> El siguiente codigo lo generamos dibujando la interfaz grafica deseada en el paint y dandole a claude (https://claude.ai/) el codigo anterior y le pedimos que genere la interfaz de la imagen con Gradio

```
import gradio as gr
from openai import OpenAI

api_key_global = None

def set_api_key(api_key):
    global api_key_global
    api_key_global = api_key
    return api_key

def procesar_prompt(prompt):
    try:
      global api_key_global

      if not api_key_global:
        return "Por favor, ingrese su API Key."

      client = OpenAI(
          api_key=api_key_global,
          base_url="https://api.groq.com/openai/v1",
      )

      response = client.responses.create(
          input=prompt,
          model="openai/gpt-oss-20b",
      )
    
      return response.output_text 

    except Exception as e:
      return f"Error: {e}"

with gr.Blocks(title="Demo Chatbot") as demo:
    gr.Markdown("## Demo Chatbot")

    api_key_input = gr.Textbox(
        label="API KEY",
        placeholder="Ingrese su API Key aquí...",
        type="password"
    )

    api_key_input.change(fn=set_api_key, inputs=api_key_input, outputs=[])

    respuesta_output = gr.Textbox(
        label="Respuesta LLM",
        lines=10,
        interactive=False
    )

    with gr.Row():
        prompt_input = gr.Textbox(
            label="PROMPT",
            placeholder="Escriba su prompt aquí...",
            scale=4
        )
        submit_btn = gr.Button("Submit", scale=1)

    submit_btn.click(
        fn=procesar_prompt,
        inputs=prompt_input,
        outputs=respuesta_output
    )

    prompt_input.submit(
        fn=procesar_prompt,
        inputs=prompt_input,
        outputs=respuesta_output
    )

demo.launch()
```

# Extra

* Para clonar las voces : https://coquitts.com/generate
# Repositorio de Modelos de IA Open Source

> 
