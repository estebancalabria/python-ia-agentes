# 🧪 Laboratorio: Text-to-Speech con Groq en Colab 🎙️

## 📝 Introducción

En este laboratorio vamos a:

* Pedir al usuario su **Groq API Key**
* Convertir texto a audio usando **`canopylabs/orpheus-v1-english`**
* Guardar el audio en un archivo WAV
* ⚠️ **Importante:** antes de usar el modelo, el usuario debe aceptar los términos de uso en Groq

---

## 📋 Requisitos

* Python 3.9+
* Conexión a Internet
* Groq API Key activa
* Conocimientos básicos de Python

---

## ⚠️ Paso previo: aceptar términos del modelo

Antes de ejecutar el laboratorio, abrí este enlace en tu navegador:

[Aceptar términos de `canopylabs/orpheus-v1-english`](https://console.groq.com/playground?model=canopylabs%2Forpheus-v1-english)

* Iniciá sesión con tu cuenta de Groq
* Aceptá los términos del modelo
* Solo después de eso la API permitirá generar audio

> Si no aceptás los términos, aparecerá un error **BadRequestError: model_terms_required**.

---

## 🔧 Paso 1: Instalar dependencias

```bash
pip install groq
```

---

## 📚 Paso 2: Importar bibliotecas

```python
from groq import Groq
```

---

## 🔑 Paso 3: Pedir API Key al usuario

```python
# Pedir API Key directamente
api_key = input("Ingrese su Groq API Key: ")
```

---

## 💡 Paso 4: Configurar modelo y texto

```python
# Archivo de salida
speech_file_path = "orpheus-english.wav"

# Modelo y voz
model = "canopylabs/orpheus-v1-english"
voice = "troy"

# Texto a convertir
text = input("Ingrese el texto que desea convertir a audio: ")

# Formato de salida
response_format = "wav"
```

---

## 💻 Paso 5: Generar audio con Groq

```python
# Inicializar cliente con la API Key
client = Groq(api_key=api_key)

# Llamar al endpoint de TTS
response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

# Guardar archivo
response.write_to_file(speech_file_path)
print(f"Archivo de audio generado correctamente: {speech_file_path}")
```

---

## 🧩 Código completo resumido

```python
from groq import Groq

# 1️⃣ Pedir API Key al usuario
api_key = input("Ingrese su Groq API Key: ")

# ⚠️ Asegúrate de aceptar los términos del modelo en:
# https://console.groq.com/playground?model=canopylabs%2Forpheus-v1-english

# 2️⃣ Configuración
speech_file_path = "orpheus-english.wav"
model = "canopylabs/orpheus-v1-english"
voice = "troy"
text = input("Ingrese el texto que desea convertir a audio: ")
response_format = "wav"

# 3️⃣ Inicializar cliente y generar audio
client = Groq(api_key=api_key)
response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

# 4️⃣ Guardar archivo
response.write_to_file(speech_file_path)
print(f"Archivo de audio generado correctamente: {speech_file_path}")
```

---

✅ **Con este laboratorio actualizado**:

* El usuario ingresa la API Key directamente
* Se aclara que **hay que aceptar los términos del modelo** antes de usarlo
* Se genera un archivo WAV listo para escuchar o usar en proyectos
