# 🧪 Laboratorio: Ciclo Completo TTS → STT en Colab 🎙️

## 📝 Introducción

En este laboratorio vamos a:

* ✍️ Convertir un texto a audio con `gTTS`
* 🔊 Guardar el audio como `ejemplo.wav`
* 🎧 Reconocer el audio con `speech_recognition`
* 🖥️ Mostrar el texto transcrito en consola

⚠️ Todo funciona en **Colab** y **sin subir archivos externos**.

---

## 🔧 Paso 1: Instalar dependencias

```bash
pip install gtts pydub SpeechRecognition
```

> `pydub` permite convertir de MP3 a WAV, porque `gTTS` genera MP3 por defecto.

---

## 📚 Paso 2: Importar bibliotecas

```python
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr
```

---

## 💡 Paso 3: Crear audio con gTTS

```python
# Texto a convertir en audio
texto_a_convertir = "Hola, este es un ejemplo de prueba para TTS y STT en Colab."

# Generar audio con gTTS
tts = gTTS(text=texto_a_convertir, lang="es")
tts.save("ejemplo.mp3")

# Convertir a WAV para speech_recognition
AudioSegment.from_mp3("ejemplo.mp3").export("ejemplo.wav", format="wav")

print("Archivo ejemplo.wav generado correctamente.")
```

---

## 💻 Paso 4: Reconocer el audio con speech_recognition

```python
# Crear reconocedor
r = sr.Recognizer()

# Abrir el archivo WAV generado
with sr.AudioFile("ejemplo.wav") as source:
    audio_data = r.record(source)  # Leer todo el archivo

# Reconocer audio
try:
    texto_reconocido = r.recognize_google(audio_data, language="es-ES")
    print("Texto reconocido:", texto_reconocido)
except sr.UnknownValueError:
    print("No se entendió el audio")
except sr.RequestError as e:
    print("Error con el servicio de reconocimiento; {0}".format(e))
```

---

## 🧩 Código completo resumido

```python
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr

# Texto a convertir
texto_a_convertir = "Hola, este es un ejemplo de prueba para TTS y STT en Colab."

# 1️⃣ Generar audio con gTTS
tts = gTTS(text=texto_a_convertir, lang="es")
tts.save("ejemplo.mp3")

# 2️⃣ Convertir a WAV
AudioSegment.from_mp3("ejemplo.mp3").export("ejemplo.wav", format="wav")
print("Archivo ejemplo.wav generado correctamente.")

# 3️⃣ Reconocer el audio con speech_recognition
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

## 🎉 Conclusión

Con este laboratorio:

* ✅ Generás audio a partir de texto con `gTTS`
* ✅ Convertís a WAV para STT
* ✅ Reconocés el audio con `speech_recognition`
* ✅ Tenés un **ciclo completo TTS → STT** funcionando en Colab

> 💡 Tip: Podés cambiar el texto o el idioma (`lang="en"` para inglés) y ver cómo cambia el reconocimiento.

