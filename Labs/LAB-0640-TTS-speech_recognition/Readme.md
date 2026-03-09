# 🧪 Laboratorio: Speech-to-Text con `speech_recognition` usando `ejemplo.wav` 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema básico de STT** que:

* 🔊 Usa el archivo `ejemplo.wav` ya presente en el entorno
* 🔢 Convierte el audio a texto usando Google Web Speech API
* 📋 Muestra el texto reconocido en consola

⚠️ No necesitamos subir archivos ni usar enlaces externos.

---

## 📋 Requisitos

* Python 3.9+
* Pip instalado
* Conocimientos básicos de Python
* Archivo `ejemplo.wav` ya disponible en el entorno

---

## 🔧 Paso 1: Instalar dependencias

```bash
pip install SpeechRecognition pydub
```

> `pydub` solo es necesario si se quisiera convertir otros formatos a WAV.

---

## 📚 Paso 2: Importar bibliotecas

```python
import speech_recognition as sr
from pydub import AudioSegment
```

---

## 💻 Paso 3: Reconocimiento de voz desde `ejemplo.wav`

```python
# Crear objeto reconocedor
r = sr.Recognizer()

# Abrir el archivo WAV
with sr.AudioFile("ejemplo.wav") as source:
    audio_data = r.record(source)  # Leer todo el archivo

# Convertir audio a texto
try:
    texto = r.recognize_google(audio_data, language="es-ES")  # Español
    print("Texto reconocido:", texto)
except sr.UnknownValueError:
    print("No se entendió el audio")
except sr.RequestError as e:
    print("Error con el servicio de reconocimiento; {0}".format(e))
```

> ⚡ Esto convierte el audio de `ejemplo.wav` a texto usando la API de Google.

---

## 💡 Paso 4: Tips y buenas prácticas

* Para archivos grandes, podés procesarlos por fragmentos usando:

```python
with sr.AudioFile("ejemplo.wav") as source:
    while True:
        audio_data = r.record(source, duration=10)  # bloques de 10s
        if len(audio_data.frame_data) == 0:
            break
        texto = r.recognize_google(audio_data, language="es-ES")
        print(texto)
```

* Cambiar `language="en-US"` si tu audio está en inglés.
* `pydub` sirve para convertir MP3 u otros formatos a WAV si fuera necesario.

---

## 🧩 Código completo resumido

```python
import speech_recognition as sr
from pydub import AudioSegment

# Crear reconocedor
r = sr.Recognizer()

# Abrir archivo WAV ya existente
with sr.AudioFile("ejemplo.wav") as source:
    audio_data = r.record(source)  # Leer todo el archivo

# Reconocer audio
try:
    texto = r.recognize_google(audio_data, language="es-ES")
    print("Texto reconocido:", texto)
except sr.UnknownValueError:
    print("No se entendió el audio")
except sr.RequestError as e:
    print("Error con el servicio de reconocimiento; {0}".format(e))
```

---

## 🎉 Conclusión

Con este laboratorio:

* ✅ Convertís `ejemplo.wav` a texto directamente
* ✅ Funciona en Colab sin subir archivos ni enlaces externos
* ✅ 100% listo para pruebas y didáctico paso a paso

> 💡 Tip: Podés combinar esto con `gTTS` para hacer un **ciclo texto → voz → texto** completamente dentro de Colab.

