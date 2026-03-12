# Clase Siete - 12 de Marzo del 2026

# Repaso

* VoiceAI
  * Fundamentos y usos
  * TTS (Text to Speech)
    * Javascript - SpeechSynthesis
    * Liberia Python - gTTs
    * Modelos OS - Ejecutado con el Framrwork CoquiTTS - TTS (No me funciono en Colab)
    * Api Key - Hicimos un ejemplo en Groq
    * Proveedores Cloud - Azure, Google Vertex
    * Api premium como ElevenLabs
  * STT (Speech to Text)
    * Javascript - SpeechRecognizer
    * Libreria Python - speechRecognizer
    * Modelos OS - Como VibeVoice (Mas reciente de MS) - https://huggingface.co/microsoft/VibeVoice-ASR
    * Api Key - Hicimos un ejemplo en Groq
    * Proveedores Cloud - Azure
* Un google Colab que maneje STT
* Criterio cuando conviene elegir cada uno

# Colab de la clase

> https://colab.research.google.com/drive/1ZCyfPm8KMAfBzuUKcX8CJMgkRtV_ImdB?usp=sharing

# Ejemplo que quedo pendiente de la clase

```python
import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment
import os



def procesar_request(audio_usuario):
    try:
      reconocedor = sr.Recognizer()

      mi_archivo = AudioSegment.from_file(audio_usuario)
      mi_archivo.export("/tmp/temp.wav", format="wav")
      
      with sr.AudioFile("/tmp/temp.wav") as fuente:
        audio = reconocedor.record(fuente)

      texto = reconocedor.recognize_google(audio, language="es-ES")
    except  Exception as e:
        texto = e

    # Opcional: borrar archivo temporal
    #if audio_usuario != audio_wav:
    #    os.remove(audio_wav)

    return texto


iface = gr.Interface(
    fn=procesar_request,
    inputs=[
        gr.Audio(label="Habla con el agente", type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="El usuario Dijo"),
    ]
)

iface.launch()
```

# Integracion de un RAG con un LLM



# Tools
