# Laboratorio: Tool Use con Groq y Google Colab (Cliente de Clima)

Este laboratorio muestra cómo implementar **Tool Use (uso de herramientas)** utilizando la API de Groq desde Google Colab.

El asistente estará configurado para **responder únicamente preguntas sobre el clima**, utilizando una herramienta que simula la obtención del clima de una ciudad.

Se utilizará el modelo:

**Llama 3.3 70B Versatile**

Ver documentación del modelo:
[https://console.groq.com/docs/model/llama-3.3-70b-versatile](https://console.groq.com/docs/model/llama-3.3-70b-versatile)

Este modelo es un LLM de **70 mil millones de parámetros optimizado para conversación, razonamiento y uso de herramientas (tool use)**.

---

# Requisitos previos

* Tener una cuenta en **Groq**
* Tener una **API Key**
* Tener una cuenta de **Google**
* Acceso a **Google Colab**

---

# Paso 1: Obtener la API Key de Groq

1. Ir a
   [https://console.groq.com/](https://console.groq.com/)

2. Iniciar sesión.

3. Ir a **API Keys**.

4. Hacer clic en **Create API Key**.

5. Copiar la clave generada.

Ejemplo:

```python
gsk_xxxxxxxxxxxxxxxxx
```

---

# Paso 2: Crear un Notebook en Google Colab

1. Ir a

[https://colab.google/](https://colab.google/)

2. Crear un **Nuevo Notebook**.

---

# Paso 3: Instalar las dependencias

Crear una celda y ejecutar:

```python
!pip install openai
```

---

# Paso 4: Definir el System Prompt

El comportamiento del asistente se controla con un **system prompt** guardado en una variable.

El asistente **solo responderá preguntas relacionadas con el clima**.

```python
system_prompt = "Eres un asistente especializado en el clima. Solo puedes responder preguntas relacionadas con el clima."
```

---

# Paso 5: Crear una función simulada de clima

Para simplificar el laboratorio, la función **no llama a una API real**.
En cambio, devuelve **un clima aleatorio**.

Crear la función:

```python
import random

def obtener_clima(ciudad):

    temperaturas = [18, 21, 25, 30, 15]
    condiciones = ["soleado", "nublado", "lluvioso", "ventoso"]

    clima = {
        "ciudad": ciudad,
        "temperatura": random.choice(temperaturas),
        "condicion": random.choice(condiciones)
    }

    return clima
```

---

# Paso 6: Definir la Tool

El modelo necesita conocer la herramienta disponible.

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "obtener_clima",
            "description": "Obtiene el clima actual de una ciudad",
            "parameters": {
                "type": "object",
                "properties": {
                    "ciudad": {
                        "type": "string",
                        "description": "Nombre de la ciudad"
                    }
                },
                "required": ["ciudad"]
            }
        }
    }
]
```

---

# Paso 7: Crear el cliente de Groq

El cliente utiliza la **API compatible con OpenAI**.

```python
from openai import OpenAI

api_key = input("Ingrese su API key: ")
prompt_usuario = input("Haga una pregunta sobre el clima: ")

cliente = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
```

---

# Paso 8: Primera llamada al modelo

El modelo decidirá si necesita utilizar la herramienta.

```python
respuesta = cliente.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_usuario}
    ],
    tools=tools,
    tool_choice="auto"
)

mensaje = respuesta.choices[0].message
```

---

# Paso 9: Ejecutar la Tool si el modelo la solicita

Si el modelo decide usar la herramienta, se ejecuta la función.

```python
import json

if mensaje.tool_calls:

    tool_call = mensaje.tool_calls[0]

    argumentos = json.loads(tool_call.function.arguments)

    ciudad = argumentos["ciudad"]

    datos_clima = obtener_clima(ciudad)
```

---

# Paso 10: Enviar el resultado de la Tool al modelo

El modelo recibe el resultado de la función para generar la respuesta final.

```python
    segunda_respuesta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_usuario},
            mensaje,
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(datos_clima)
            }
        ]
    )

    print(segunda_respuesta.choices[0].message.content)

else:

    print(mensaje.content)
```

---

# Ejemplo de Prompt

Ejecutar el laboratorio y probar con:

```python
¿Cuál es el clima en Buenos Aires?
```

---

# Código completo del laboratorio

```python
!pip install openai

from openai import OpenAI
import json
import random

system_prompt = "Eres un asistente especializado en el clima. Solo puedes responder preguntas relacionadas con el clima."

def obtener_clima(ciudad):

    temperaturas = [18, 21, 25, 30, 15]
    condiciones = ["soleado", "nublado", "lluvioso", "ventoso"]

    clima = {
        "ciudad": ciudad,
        "temperatura": random.choice(temperaturas),
        "condicion": random.choice(condiciones)
    }

    return clima


tools = [
    {
        "type": "function",
        "function": {
            "name": "obtener_clima",
            "description": "Obtiene el clima actual de una ciudad",
            "parameters": {
                "type": "object",
                "properties": {
                    "ciudad": {
                        "type": "string",
                        "description": "Nombre de la ciudad"
                    }
                },
                "required": ["ciudad"]
            }
        }
    }
]

api_key = input("Ingrese su API key: ")
prompt_usuario = input("Haga una pregunta sobre el clima: ")

cliente = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

respuesta = cliente.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_usuario}
    ],
    tools=tools,
    tool_choice="auto"
)

mensaje = respuesta.choices[0].message

if mensaje.tool_calls:

    tool_call = mensaje.tool_calls[0]

    argumentos = json.loads(tool_call.function.arguments)

    ciudad = argumentos["ciudad"]

    datos_clima = obtener_clima(ciudad)

    segunda_respuesta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_usuario},
            mensaje,
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(datos_clima)
            }
        ]
    )

    print(segunda_respuesta.choices[0].message.content)

else:

    print(mensaje.content)
```
