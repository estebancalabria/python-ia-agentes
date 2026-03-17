# Clase Ocho - 17 de Marzo del 2025

# Repao

* STT (Speach to text)
    * Ingrado con Gradio (componente gr.Audio)
* Integracion de RAG con un LLM
* Introduccion a la parte Tools

# Herramientas

> https://anythingllm.com/

# Colab de la clase

> https://colab.research.google.com/drive/1JaEqtyJMMEOZZ0jvm-4ncPpKKJiom2LN?usp=sharing

# Tools

* Primero hay que definir las herramientas como funciones de python
```python
import random

def obtener_clima(ciudad):
    temperaturas = [-5, 0, 5 , 10, 15, 20, 25, 30]
    condicion = ["soleado", "nublado", "lluvioso", "tormenta", "nieve"]

    clima = {
        "ciudad": ciudad,
        "temperatura": random.choice(temperaturas),
        "condicion" : random.choice(condicion)
    }
    return clima
```

* Despues hay que crear un diccionario/json para informarle al llm (que soporte herramientas) cuales son las que tiene disponible
```python
tools =  [
    {
        "type" : "function",
        "function" : {
            "name" : "obtener_clima",
            "description" : "Obtener el clima en una ciudad",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "ciudad" : {
                        "type" : "string",
                        "description" : "Nombre de la ciudad"
                    }
                },
                "required" : ["ciudad"]
           }
        }
    }
]
```

* Luego si el modelo lo requiere vamos a invocar localmente las herramienta que el llm me pide
```python
from openai import OpenAI
import json


api_key = input("Ingrese su api key")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key = api_key
)

system_prompt = """
Eres un agente especializado en el clima.
Solo respondes preguntas relacionadas con el clima.
Si te preguntan algo que no tiene que ver con el clima rechaza amablemente la peticion
"""

prompt = input("Ingrese su prompt")

messages = [
        {
            "role" : "system",
            "content" : system_prompt
        },
        {
            "role" : "user",
            "content" : prompt
        }
    ]

respuesta = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = messages,
    tools = tools,
    tool_choice = "auto"
)

if respuesta.choices[0].message.tool_calls:

    tool_call = respuesta.choices[0].message.tool_calls[0]
    tool_name = tool_call.function.name
    tool_args = tool_call.function.arguments
    print(f"El modelo necesita llamar a la herramienta {tool_name} con parametros {tool_args}")

    ciudad = eval(tool_args).get("ciudad")
    
    if tool_name == "obtener_clima":
        clima = obtener_clima(ciudad)

        messages.append(respuesta.choices[0].message)

        messages.append(
            {
                "role" : "tool",
                "tool_call_id" : respuesta.choices[0].message.tool_calls[0].id,
                "content" : json.dumps(clima)
            })

        respuesta = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = messages,
            tools = tools,
            tool_choice = "auto"
        )

        ##print(respuesta.model_dump_json(indent=2))
        print(respuesta.choices[0].message.content)
    else:
      print(respuesta.choices[0].message.content)
```

* El ejemplo anterior es como dicactico pero no contempla si el modelo necesita ejecutar varias herramientas y si en con la respuesta de las herramientas necesita ejecutar otras herramientas en forma encadenada
* Gracias claude que me ayudo a armar mas rapido (https://claude.ai/share/37088ea8-9431-48f8-90cf-06c34f2b6e5f)  

```python
from openai import OpenAI
import json

api_key = input("Ingrese su api key: ")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

system_prompt = """
Eres un agente especializado en el clima.
Solo respondes preguntas relacionadas con el clima.
Si te preguntan algo que no tiene que ver con el clima rechaza amablemente la peticion
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": input("Ingrese su prompt: ")}
]

respuesta = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

while respuesta.choices[0].message.tool_calls:
    messages.append(respuesta.choices[0].message)

    for tool_call in respuesta.choices[0].message.tool_calls:
        tool_name = tool_call.function.name
        tool_args = tool_call.function.arguments
        print(f"El modelo necesita llamar a la herramienta {tool_name} con parametros {tool_args}")

        ciudad = eval(tool_args).get("ciudad")

        if tool_name == "obtener_clima":
            clima = obtener_clima(ciudad)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(clima)
        })

    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

print(respuesta.choices[0].message.content)
```

* 
