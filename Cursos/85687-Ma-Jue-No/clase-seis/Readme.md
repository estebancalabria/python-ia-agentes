# Clase Seis - 10 de Marzo del 2026

## Repaso

* RAG
  * Dividir un texto largo en chunks logicos
  * Ejemplo con Gradio
  * Base de Datos Vectoriales
      * Faiss
          * Memoria
          * Persistencia

## Colab del dia

> https://colab.research.google.com/drive/1SUm_g5BNOAxTYCz0Iz3Hlqd1wETbyDgw?usp=sharing

# Voice AI (Text-To-Speech y Speech-To-Text)

## Formas de Implenentar VoiceAI

* Javascript
* Liberias de Python Standard...
* Modelos open Source con algun Framework...
* Usando un proveedor externo (con API Key)
	* Por Api Key : OpenAI, Groq, Usando por Uso
	* Usar proveedores especializados como ElevenLabs
	* Usar algun proveedor Cloud

## Javascript

### Speech-To-Text

'''html
<!DOCTYPE html>
<html>

<body>
  <h2> Speech to Text</h2>
  <button id="start">Hablar</button>
  <p id="salida"></p>

<script>
  const stt = new SpeechRecognition();
  stt.lang = "es-ES"
  stt.continuous = false;
  stt.interimResults = false;
  
  stt.onresult = (event) => {
    const texto = event.results[0][0].transcript;
    document.getElementById("salida").innerText += texto
  }
  
  document.getElementById("start").onclick = () => {
  	stt.start();
  }
</script>
</body>

</html>
'''

### Text-To-Speech

```html
<!DOCTYPE html>
<html>

<body>

<button id="hablar" onclick="hablar()">Hablar</button>

<script>

function hablar(){
	const texto = "Hola. Soy una IA. Y estoy hablando. Que tal?"
    
    const tts = new SpeechSynthesisUtterance(texto);
    tts.lang = "es-ES";
    tts.pitch = 1;
    tts.rate = 1;
    speechSynthesis.speak(tts);
}    
 
</script>
</body>

</html>
```

## Librerias de Python Estandard

### Text-to-Speech (gTTS)

```python
!pip install gTTS
```

```python
from gtts import gTTS
from IPython.display import Audio

texto = "Hola. Bienvenidos al curso de Desarrollo de Agentes con Python. Les doy la bienvenida"
tts = gTTS(texto, lang="es")
tts.save("Saludo.mp3")

Audio("Saludo.mp3")
```

### Speech-To-Text (speechRecognizer)

```python
!pip install SpeechRecognition
```

```python
import speech_recognition as sr

reconocedor = sr.Recognizer()

#Se puede usar el microfono
#with sr.Microphone() as source:
#    print("Di algo...")

with sr.AudioFile("ejemplo.wav") as source:
  audio_data = reconocedor.record(source)
  
try:
  texto = reconocedor.recognize_google(audio_data, language="es-ES")
  print(texto)
except:
  print("Texto no reconocido")
```

## Utilizando modelos Open Source y el framework Coquitts

* Ver Codigo de ejemplo : https://huggingface.co/coqui/XTTS-v2

##  Utilizando por ejemplo Groq

### Speech to Text

* Sacar una api key de Groq : https://console.groq.com/keys
* Instalar la libreria de Groq
```python
!pip install groq
```
* Luego el codigo (que salio de la documentacion de groq)
```python
import os
import json
from groq import Groq

api_key = input("Enter your API key: ")

# Initialize the Groq client
client = Groq(api_key=api_key)

# Specify the path to the audio file
filename = "ejemplo.wav"

# Open the audio file
with open(filename, "rb") as file:
    # Create a transcription of the audio file
    transcription = client.audio.transcriptions.create(
      file=file, # Required audio file
      model="whisper-large-v3-turbo", # Required model to use for transcription
      prompt="Specify context or spelling",  # Optional
      response_format="verbose_json",  # Optional
      timestamp_granularities = ["word", "segment"], # Optional (must set response_format to "json" to use and can specify "word", "segment" (default), or both)
      language="es",  # Optional
      temperature=0.0  # Optional
    )
    # To print only the transcription text, you'd use print(transcription.text) (here we're printing the entire transcription object to access timestamps)
    print(json.dumps(transcription, indent=2, default=str))
```

### Text to Speech

* Ver https://console.groq.com/docs/text-to-speech/orpheus
```python
import os
from groq import Groq
from IPython.display import Audio


api_key = input("Enter your API key: ")

# Initialize the Groq client
client = Groq(api_key=api_key)

speech_file_path = "orpheus-english.wav" 
model = "canopylabs/orpheus-v1-english"
voice = "troy"
text = "Welcome to Orpheus text-to-speech. [cheerful] This is an example of high-quality English audio generation [dramatic] with vocal directions support."
response_format = "wav"

response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

response.write_to_file(speech_file_path)

Audio(speech_file_path)
```

## Con Una interfaz Gradio (CORREGIMOS)

```python
import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment
import os

reconocedor = sr.Recognizer()

def procesar_request(audio_usuario):

    print("Procesando audio del usuario...")

    # Convertimos a WAV si no lo está (por ejemplo si viene en MP3/OGG)
    if not audio_usuario.endswith(".wav"):
        audio_wav = "temp_audio.wav"
        sonido = AudioSegment.from_file(audio_usuario)
        sonido.export(audio_wav, format="wav")
    else:
        audio_wav = audio_usuario

    # Inicializamos el reconocedor
    reconocedor = sr.Recognizer()
    with sr.AudioFile(audio_wav) as source:
        audio = reconocedor.record(source)

    try:
        texto = reconocedor.recognize_google(audio, language="es-ES")
    except sr.UnknownValueError:
        texto = "No pude entender el audio."
    except sr.RequestError as e:
        texto = f"Error en el servicio de reconocimiento: {e}"

    # Opcional: borrar archivo temporal
    if audio_usuario != audio_wav:
        os.remove(audio_wav)

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

> PARA LA PROXIMA CORREGIR ESTE CODIGO Y HACERLO TODO CONVERSACIONAL.
