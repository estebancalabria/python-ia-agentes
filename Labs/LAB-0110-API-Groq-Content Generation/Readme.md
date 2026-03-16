# Laboratorio: Usar Content Generation de Groq en Google Colab

Este laboratorio te guía para usar la API de Groq desde Google Colab utilizando el endpoint **responses.create** (Content Generation).

---

## Requisitos previos

- Tener una cuenta en https://console.groq.com/
- Tener una cuenta de Google para acceder a Colab

---

## Paso 1: Obtener tu API Key en Groq

1. Ve a https://console.groq.com/
2. Inicia sesión o crea una cuenta.
3. Dirígete a la sección **API Keys**.
4. Haz clic en **Create API Key**.
5. Copia la clave generada (ej. `gsk_xxxx...`).

⚠️ No compartas tu API key ni la subas a repositorios públicos.

---

## Paso 2: Abrir Google Colab

1. Ve a https://colab.google/
2. Haz clic en **Nuevo notebook**.

---

## Paso 3: Instalar la biblioteca `openai`

1. Crear una celda nueva con el botón "+"
2. Ejecuta esta celda:

&lt;code&gt;
!pip install openai
&lt;/code&gt;

---

## Paso 4: Crear y ejecutar la celda principal (Content Generation)

Asegúrate de que tu notebook contenga exactamente lo siguiente en una sola celda:

```python
from openai import OpenAI

# Pedir la API key y el prompt al usuario
api_key = input("Ingrese su API key: ")
prompt = input("Ingrese su prompt: ")

# Configurar el cliente
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Llamar al modelo usando responses.create
response = client.responses.create(
    input=prompt,
    model="openai/gpt-oss-20b",
)

# Mostrar la respuesta
print("\nRespuesta del modelo:")
print(response.output_text)
```

---

## Paso 5: Ejecutar

1. Ejecuta la celda.
2. Cuando se te pida, pega tu API key y presiona Enter.
3. Luego escribe tu prompt (por ejemplo: "Explain the importance of fast language models") y presiona Enter.
4. Verás la respuesta generada por el modelo.

---

¡Listo! Ahora puedes usar Content Generation con Groq desde Google Colab.
