# Laboratorio: Usar la API de Gemini en Google Colab (SDK oficial nuevo)

Este laboratorio te guía para usar la API de Gemini desde Google Colab utilizando el nuevo SDK oficial `google.genai`.

---

## Requisitos previos

- Tener una cuenta en Google AI Studio (https://aistudio.google.com/)
- Tener una cuenta de Google
- Generar una API Key

---

## Paso 1: Obtener tu API Key

1. Ir a https://aistudio.google.com/
2. Iniciar sesión.
3. Hacer clic en **Get API key**.
4. Crear una nueva API key.
5. Copiarla.

> ⚠️ No compartas tu API key ni la subas a repositorios públicos.

---

## Paso 2: Abrir Google Colab

1. Ir a https://colab.google/
2. Hacer clic en **Nuevo notebook**.

---

## Paso 3: Instalar la librería oficial

Crear una celda y ejecutar:

&lt;code&gt;
!pip install -q google-genai
&lt;/code&gt;

---

## Paso 4: Crear la celda principal

Asegúrate de que tu notebook contenga exactamente lo siguiente en una sola celda:

```python
from google import genai

# Pedir datos al usuario
api_key = input("Ingrese su API key: ")
prompt = input("Ingrese su prompt: ")

# Crear cliente
client = genai.Client(api_key=api_key)

# Generar contenido
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

# Mostrar resultado
print("\nRespuesta del modelo:\n")
print(response.text)
```

---

## Paso 5: Ejecutar

1. Ejecutar la celda.
2. Pegar la API key cuando se solicite.
3. Escribir el prompt.
4. Ver la respuesta generada.

---

¡Listo! Ahora puedes experimentar con Gemini desde Google Colab.
