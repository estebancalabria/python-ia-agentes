# 🧪 Laboratorio: Agente de Voz con Groq LLM en Google Colab 🎤🤖🔊

## 📝 Introducción

En este laboratorio vamos a construir un **agente de voz** que funciona directamente en **Google Colab** usando **Gradio** y **Groq LLM** con la librería oficial `openai`.

El agente permitirá:

* 🎤 Capturar la voz del usuario desde el navegador
* 🧠 Consultar **Groq LLM** con el modelo `openai/gpt-oss-20b`
* 🔊 Responder con texto y audio
* 🔑 Ingresar la **API Key de Groq** directamente desde la interfaz

Este laboratorio está diseñado **paso a paso** para que sea didáctico y fácil de seguir.

---

## 📋 Requisitos

* Cuenta de Google y acceso a Google Colab
* Micrófono
* Una **API Key válida de Groq**
* Conocimientos básicos de Python

---

## 🔧 Paso 1: Instalar dependencias

Primero, instalamos todas las librerías necesarias para el laboratorio:

```python
!pip install gradio gtts SpeechRecognition openai pydub
```

> ⚡ `gradio` para la interfaz interactiva, `gtts` para Text-to-Speech, `SpeechRecognition` para Speech-to-Text, `pydub` para manejar archivos de audio y `openai` para conectarse a Groq LLM.

---

## 💡 Paso 2: Configurar la función para consultar Groq LLM

Usaremos la librería oficial `openai` para conectarnos a Groq y enviar prompts al modelo `openai/gpt-oss-20b`.

```python
from openai import OpenAI

def consultar_llm_groq(prompt, api_key):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )
    response = client.responses.create(
        input=prompt,
        model="openai/gpt-oss-20b"
    )
    return response.output_text
```

> 🔑 La API Key se pasará como argumento desde Gradio, no usamos variables de entorno.

---

## 🎤 Paso 3: Convertir audio a texto (STT)

Creamos la función para convertir la voz del usuario en texto usando **SpeechRecognition** y **pydub**:

```python
import speech_recognition as sr
from pydub import AudioSegment

def audio_a_texto(audio_path):
    # Convertimos a WAV
    audio = AudioSegment.from_file(audio_path)
    audio.export("/tmp/temp.wav", format="wav")
    
    recognizer = sr.Recognizer()
    with sr.AudioFile("/tmp/temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            texto = recognizer.recognize_google(audio_data, language="es-ES")
            return texto
        except sr.UnknownValueError:
            return "No pude entender el audio."
        except sr.RequestError as e:
            return f"Error del servicio STT: {e}"
```

> ⚡ Esta función toma el archivo de audio que entrega Gradio y lo convierte a texto en español.

---

## 🔊 Paso 4: Convertir texto a audio (TTS)

Usamos **gTTS** para generar un archivo de audio a partir de la respuesta del modelo:

```python
from gtts import gTTS
import io

def texto_a_audio(texto):
    tts = gTTS(texto, lang="es")
    path = "/tmp/respuesta.mp3"
    tts.save(path)
    return path
```

> 🔈 Esta función guarda un archivo temporal que luego Gradio reproducirá.

---

## ▶️ Paso 5: Integrar todo en Gradio

Creamos la interfaz completa con un **Audio input para el micrófono** y un **Textbox para la API Key**:

```python
import gradio as gr

def agente_voz(audio_usuario, api_key):
    texto_usuario = audio_a_texto(audio_usuario)
    respuesta = consultar_llm_groq(texto_usuario, api_key)
    audio_respuesta = texto_a_audio(respuesta)
    return texto_usuario, respuesta, audio_respuesta

iface = gr.Interface(
    fn=agente_voz,
    inputs=[
        gr.Audio(label="Habla con el agente", type="filepath"),
        gr.Textbox(label="API Key de Groq", type="password", placeholder="Ingresa tu API Key")
    ],
    outputs=[
        gr.Textbox(label="Texto del Usuario"),
        gr.Textbox(label="Respuesta del Agente"),
        gr.Audio(label="Respuesta en Audio", type="filepath")
    ],
    title="🧪 Agente de Voz con Groq LLM en Colab",
    description="Habla con el agente, ingresa tu API Key y el modelo responde con texto y audio."
)

iface.launch()
```

> ✅ Ahora el laboratorio está completamente funcional, compatible con la versión más reciente de Gradio.

---

## 💻 Código Completo del Laboratorio

### Celda 1: Instalar dependencias

```python
!pip install gradio gtts SpeechRecognition openai pydub
```

### Celda 2: Código completo del agente

```python
from openai import OpenAI
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
import gradio as gr

# Función para consultar Groq LLM
def consultar_llm_groq(prompt, api_key):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )
    response = client.responses.create(
        input=prompt,
        model="openai/gpt-oss-20b"
    )
    return response.output_text

# STT: audio a texto
def audio_a_texto(audio_path):
    audio = AudioSegment.from_file(audio_path)
    audio.export("/tmp/temp.wav", format="wav")
    recognizer = sr.Recognizer()
    with sr.AudioFile("/tmp/temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            texto = recognizer.recognize_google(audio_data, language="es-ES")
            return texto
        except sr.UnknownValueError:
            return "No pude entender el audio."
        except sr.RequestError as e:
            return f"Error del servicio STT: {e}"

# TTS: texto a audio
def texto_a_audio(texto):
    tts = gTTS(texto, lang="es")
    path = "/tmp/respuesta.mp3"
    tts.save(path)
    return path

# Función principal del agente
def agente_voz(audio_usuario, api_key):
    texto_usuario = audio_a_texto(audio_usuario)
    respuesta = consultar_llm_groq(texto_usuario, api_key)
    audio_respuesta = texto_a_audio(respuesta)
    return texto_usuario, respuesta, audio_respuesta

# Interfaz Gradio
iface = gr.Interface(
    fn=agente_voz,
    inputs=[
        gr.Audio(label="Habla con el agente", type="filepath"),
        gr.Textbox(label="API Key de Groq", type="password", placeholder="Ingresa tu API Key")
    ],
    outputs=[
        gr.Textbox(label="Texto del Usuario"),
        gr.Textbox(label="Respuesta del Agente"),
        gr.Audio(label="Respuesta en Audio", type="filepath")
    ],
    title="🧪 Agente de Voz con Groq LLM en Colab",
    description="Habla con el agente, ingresa tu API Key y el modelo responde con texto y audio."
)

iface.launch()
```
