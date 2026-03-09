# 📢 Text-to-Speech (TTS)

## 📌 ¿Qué es TTS?

**Text-to-Speech (TTS)** es la tecnología que convierte **texto en audio hablado**.  
Se utiliza en múltiples escenarios:

* Asistentes de voz (Alexa, Google Assistant, Siri)  
* Lectores automáticos de libros o documentos  
* Aplicaciones de accesibilidad para personas con dificultades visuales  
* Bots y chatbots que hablan  
* Generación de contenido multimedia  

---

## 1️⃣ Librerías nativas en JavaScript

### Web Speech API (`speechSynthesis`)

* Funciona directamente en **navegadores modernos**  
* Permite convertir texto a voz en tiempo real sin servidor externo  
* Limitaciones: depende del navegador y de las voces instaladas en el sistema  

**Ejemplo:**

```javascript
const utterance = new SpeechSynthesisUtterance("Hola, esto es TTS");
speechSynthesis.speak(utterance);
````

---

## 2️⃣ Librerías Python

### 🔹 gTTS (Google Text-to-Speech)

* Usa Google Translate
* Necesita internet
* Genera archivos MP3
* Documentación oficial: [gTTS Docs](https://gtts.readthedocs.io/en/latest/)

**Ejemplo:**

```python
from gtts import gTTS

texto = "Hola, este es un ejemplo con gTTS"
tts = gTTS(text=texto, lang="es")
tts.save("salida.mp3")
```

### 🔹 pyttsx3

* Funciona **offline**, usa voces del sistema
* Permite cambiar velocidad, volumen y voz
* Dependiente del sistema operativo

```python
import pyttsx3
engine = pyttsx3.init()
engine.say("Hola, esto es pyttsx3")
engine.runAndWait()
```

### 🔹 espeak / espeak-ng

* Motor TTS de código abierto
* Funciona offline
* Control avanzado de pronunciación y múltiples idiomas

---

## 3️⃣ APIs de TTS en la nube

* **OpenAI, Azure Cognitive Services, Google Cloud TTS, Amazon Polly**
* Voces naturales, múltiples idiomas, acentos, emociones
* Requiere conexión a Internet y API Key
* Ejemplo conceptual:

```python
# OpenAI TTS conceptual
# Enviar texto -> recibir MP3/WAV de salida
```

---

## 4️⃣ Modelos de TTS Open Source

* **Coqui TTS** (fork de Mozilla TTS)

  * Offline, Python, voces personalizables
* **Tacotron / Tacotron2 + WaveGlow / HiFi-GAN**

  * Deep learning, voces muy realistas
  * Necesita GPU para entrenamiento o inferencia rápida

---

## 5️⃣ Otros enfoques

* **SSML (Speech Synthesis Markup Language)**

  * Permite controlar pausas, entonación, pronunciación, velocidad y emoción
  * Soportado en muchas APIs cloud (Polly, Azure, Google Cloud)

* **TTS híbrido con animaciones**

  * Genera voz sincronizada con avatares digitales
  * Ejemplo: Ready Player Me + TTS

---

## 💡 Comparación rápida de métodos

| Método                                | Online   | Offline | Realismo | Control de voz |
| ------------------------------------- | -------- | ------- | -------- | -------------- |
| Web Speech API (JS)                   | Sí       | No      | Medio    | Limitado       |
| gTTS (Python)                         | Sí       | No      | Medio    | Limitado       |
| pyttsx3 / espeak                      | No       | Sí      | Bajo     | Medio          |
| APIs Cloud (OpenAI, Polly, etc.)      | Sí       | No      | Alto     | Alto           |
| Modelos Open Source (Coqui, Tacotron) | Opcional | Sí      | Muy alto | Muy alto       |

---

## 🔧 Instalación en Python

```bash
# gTTS
pip install gtts

# pyttsx3
pip install pyttsx3

# pydub (opcional, para convertir MP3 a WAV)
pip install pydub

# speech_recognition (si quieres usar STT)
pip install SpeechRecognition
```

---

## 🧪 Ejemplos de uso combinados (TTS + STT)

```python
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr

# 1️⃣ Texto a convertir
texto = "Hola, este es un ejemplo de TTS y STT"

# 2️⃣ Generar audio con gTTS
tts = gTTS(text=texto, lang="es")
tts.save("ejemplo.mp3")

# 3️⃣ Convertir a WAV
AudioSegment.from_mp3("ejemplo.mp3").export("ejemplo.wav", format="wav")

# 4️⃣ Reconocer audio con speech_recognition
r = sr.Recognizer()
with sr.AudioFile("ejemplo.wav") as source:
    audio_data = r.record(source)

try:
    texto_reconocido = r.recognize_google(audio_data, language="es-ES")
    print("Texto reconocido:", texto_reconocido)
except sr.UnknownValueError:
    print("No se entendió el audio")
except sr.RequestError as e:
    print("Error con el servicio de reconocimiento; {0}".format(e))
```

---

## 📎 Recursos y documentación

* [Documentación oficial gTTS](https://gtts.readthedocs.io/en/latest/)
* [pyttsx3 en PyPI](https://pypi.org/project/pyttsx3/)
* [SSML – Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/ssml.html)
* [Mozilla TTS / Coqui](https://github.com/coqui-ai/TTS)

---

## ⚠️ Conclusión

TTS permite convertir texto a voz en múltiples formas: **offline, online, open source o con APIs comerciales**.
La elección depende de:

* Nivel de realismo que quieras
* Disponibilidad de internet
* Idioma y acentos
* Control sobre velocidad, pausas y entonación

Con este README tenés un **resumen completo de todas las opciones de TTS actuales**.

