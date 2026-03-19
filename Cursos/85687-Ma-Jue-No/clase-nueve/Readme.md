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

