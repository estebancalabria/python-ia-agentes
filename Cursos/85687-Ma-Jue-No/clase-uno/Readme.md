# Clase Uno - 19 de Febrero de 2026

## Roadmap del curso

* Agentes
* Desarrollos de Agentes en Python
* Prompt Engineriging para agentes
* JSON
* Google Colab
* Librerias de Python
  * Gradio
  * Streamlit
  * TTS (Text to Speech)
*  Modelos de Lenguaje
    *  Propietarios
    *  Open source
* Llama a tools (tool use)
* RAG (Retrival AuGmetned Generation) 
* Desarrollo de Agentes con Proveedores en la nube (Ej azure)

## Agentes

* Agentes Conversacionales tipo ChatBot
    * Que funcionan por voz
* Agentes autonomos
* Multi-Agentes


## Modelos de Lenguaje

  * Propietarios
    * GPT, Gemini, Claude (Para programar)
  * Open Source
    * Gemma
    * Groq

 * Todos los proveedores de LLM tienen dos web
   * ChatGPT
     * Usuario Final : chatgpt.com
     * Para DEV : platform.openai.com
   * Claude
     * Usuario Final : claude.ai
     * Para DEV : https://platform.claude.com/
   * Google
    * Usuario Final:
    * Para Dev:
   * Groq (con q)
     * Usuario Final : https://chat.groq.com/
     * Para DEV : https://console.groq.com/
   * https://openrouter.ai/ (tiene opciones gratuitas)

* Utilizar un Modelo de Lenguaje Localmente
  * Es necesario por un tema de complaliance para agentes que requieren trabajar con Informacion Sensible
  * https://lmstudio.ai/
  * https://ollama.com/

* System Prompt : Instrucciones iniciales que se le da a la IA para indicar como responda.

## Groq

*  https://chat.groq.com/

## Google Colab

* Entorno para desarrollar en python directamente online
> https://colab.google/

* Google colab de la clase : https://colab.research.google.com/drive/1MHgZxiDRcuj-hllr1xW5qjnLqEAjMd1N?usp=sharing

## Mi primera invocacion a la api de Groq

```python
from openai import OpenAI
import os

api_key = input("Ingrese su Api Key: ")
prompt = input("Ingrese su prompt: ")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input=prompt,
    model="openai/gpt-oss-20b",
)

print(response.output_text)

```

## Invocacion con contexto

```python
from openai import OpenAI
import os

api_key = input("Ingrese su Api Key: ")
prompt = input("Ingrese su prompt: ")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=  [
        { "role": "system", "content": "Eres un asistente que contesta mal. Cuando te hacen una pregunta respondela directamente. En pocas palabras de forma incorrecta" },
        { "role" : "user", "content": prompt }
    ]
)

print(response.choices[0].message.content)
```

## Chat Incremental 

```python
from openai import OpenAI
import os

api_key = input("Ingrese su Api Key: ")

messages = [
        { "role": "system", "content": "Eres un contador de palabras. Devuelves cuantas palabras en total viene diciendo el usuario" },
]

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

prompt = input("Ingrese su prompt: ")

while prompt != "salir":
  
  messages.append({ "role" : "user", "content": prompt })
  
  response = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=  messages
  )

  print(response.choices[0].message.content)

  messages.append({ "role" : "assistant", "content": response.choices[0].message.content })

  prompt = input("Ingrese otro prompt: ")

```
