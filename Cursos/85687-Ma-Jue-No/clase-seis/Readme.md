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
* Por Api Key : OpenAI, Groq, Usando por Uso
* Liberias de Python Standard...
* Modelos open Source con algun Framework...
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
