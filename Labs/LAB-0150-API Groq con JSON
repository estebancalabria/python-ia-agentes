# Laboratorio: Usar la API de Groq en Google Colab (Salida en JSON)

Este laboratorio te guía para usar la API de Groq desde Google Colab, ingresando tu clave API y el prompt directamente en tiempo de ejecución, y obteniendo la respuesta estructurada en formato JSON.

---

## Requisitos previos

* Tener una cuenta en [https://console.groq.com/](https://console.groq.com/)
* Tener una cuenta de Google para acceder a Colab

---

## Paso 1: Obtener tu API Key en Groq

1. Ve a [https://console.groq.com/](https://console.groq.com/)
2. Inicia sesión o crea una cuenta si no tienes una.
3. En el panel de la consola, busca la sección **API Keys**.
4. Haz clic en **Create API Key**.
5. Copia la clave generada (ej. `gsk_xxxx...`).

> ⚠️ **Advertencia**: Al ingresar la clave manualmente, NO la compartas ni la guardes en archivos públicos.

---

## Paso 2: Abrir Google Colab

1. Ve a [https://colab.research.google.com/](https://colab.research.google.com/)
2. Haz clic en **Nuevo notebook**.

---

## Paso 3: Instalar la biblioteca `openai`

1. Crear una celda nueva con el botón "+"
2. Ejecuta esta celda:

<code>
!pip install openai
</code>

---

## Paso 4: Crear y ejecutar la celda principal

Asegúrate de que tu notebook contenga EXACTAMENTE lo siguiente en una sola celda de código:

<code>
from openai import OpenAI
import json

# Pedir la API key y el prompt al usuario

api_key = input("Ingrese su API key: ")
prompt = input("Ingrese su prompt: ")

# Instrucción para forzar salida JSON

system_instruction = """
Responde únicamente en formato JSON válido.
El JSON debe tener la siguiente estructura:

{
"resumen": "string",
"puntos_clave": ["string", "string", "string"],
"conclusion": "string"
}

No agregues texto fuera del JSON.
"""

# Configurar el cliente

client = OpenAI(
api_key=api_key,
base_url="[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)"
)

# Llamar al modelo

response = client.chat.completions.create(
model="llama3-8b-8192",
messages=[
{"role": "system", "content": system_instruction},
{"role": "user", "content": prompt}
],
temperature=0
)

# Obtener respuesta del modelo

raw_content = response.choices[0].message.content

# Intentar parsear el JSON

try:
parsed_json = json.loads(raw_content)
print("\nJSON estructurado:")
print(json.dumps(parsed_json, indent=4, ensure_ascii=False))
except json.JSONDecodeError:
print("\nLa respuesta no fue un JSON válido. Respuesta cruda:")
print(raw_content) </code>

---

## Paso 5: Ver el código completo junto

Si quieres tener todo el flujo listo para copiar en un único bloque (incluyendo la instalación), puedes usar lo siguiente en una sola celda:

<code>
# Instalar dependencia
!pip install openai

from openai import OpenAI
import json

# Pedir la API key y el prompt al usuario

api_key = input("Ingrese su API key: ")
prompt = input("Ingrese su prompt: ")

system_instruction = """
Responde únicamente en formato JSON válido.
El JSON debe tener la siguiente estructura:

{
"resumen": "string",
"puntos_clave": ["string", "string", "string"],
"conclusion": "string"
}

No agregues texto fuera del JSON.
"""

client = OpenAI(
api_key=api_key,
base_url="[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)"
)

response = client.chat.completions.create(
model="llama3-8b-8192",
messages=[
{"role": "system", "content": system_instruction},
{"role": "user", "content": prompt}
],
temperature=0
)

raw_content = response.choices[0].message.content

try:
parsed_json = json.loads(raw_content)
print("\nJSON estructurado:")
print(json.dumps(parsed_json, indent=4, ensure_ascii=False))
except json.JSONDecodeError:
print("\nLa respuesta no fue un JSON válido. Respuesta cruda:")
print(raw_content) </code>

---

## Paso 6: Ejecutar

1. Ejecuta la celda.
2. Cuando se te pida, pega tu API key y presiona Enter.
3. Luego, escribe tu prompt (por ejemplo:
   "Explain the importance of fast language models") y presiona Enter.
4. Verás la respuesta estructurada en formato JSON.

---
