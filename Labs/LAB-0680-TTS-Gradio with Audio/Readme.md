# 🧪 Laboratorio: Speech-to-Text con Gradio y SpeechRecognition 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema sencillo de Speech-to-Text (STT)** que:

* 🎤 Recibe audio del usuario a través de una interfaz web de Gradio
* 📝 Convierte el audio en texto usando la librería `SpeechRecognition`
* 💻 Muestra el texto transcrito en pantalla

Todo esto usando únicamente:

* Python
* Gradio
* SpeechRecognition
* Pydub para manejo de audio

⚠️ No necesitamos configuraciones complejas, solo Python y Colab/entorno local.

---

## 📋 Requisitos

* Python 3.9+
* Pip instalado
* Conocimientos básicos de Python

---

## 🔧 Paso 1: Instalar dependencias

Desde la terminal de Colab o tu entorno local:

```bash
pip install gradio
pip install SpeechRecognition
pip install pydub
```

> 💡 `pydub` nos permitirá convertir audio a WAV si el archivo original no está en ese formato.

---

## 📚 Paso 2: Importar bibliotecas

```python
import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment
import os
```

> 🧠 `sr` nos permite reconocer la voz y convertirla a texto.
> `AudioSegment` se usa para manipular archivos de audio y convertir formatos.

---

## 💡 Paso 3: Definir la función de procesamiento de audio

Esta función recibe el archivo de audio del usuario y devuelve el texto reconocido:

```python
def procesar_request(audio_usuario):
    """
    Convierte un archivo de audio a texto usando SpeechRecognition
    """
    try:
        # Convertir a WAV si es necesario
        audio = AudioSegment.from_file(audio_usuario)
        audio.export("/tmp/temp.wav", format="wav")

        # Inicializar el reconocedor
        reconocedor = sr.Recognizer()
        with sr.AudioFile("/tmp/temp.wav") as source:
            audio_data = reconocedor.record(source)

        # Reconocer texto usando Google Speech Recognition
        texto = reconocedor.recognize_google(audio_data, language="es-ES")

    except sr.UnknownValueError:
        texto = "No pude entender el audio."
    except sr.RequestError as e:
        texto = f"Error en el servicio de reconocimiento: {e}"
    except Exception as e:
        texto = f"Ocurrió un error: {e}"

    # Borrar archivo temporal
    if os.path.exists("/tmp/temp.wav"):
        os.remove("/tmp/temp.wav")

    return texto
```

> 🔍 Explicación:
>
> 1. Convertimos cualquier archivo de audio a WAV para compatibilidad.
> 2. Usamos `Recognizer` y `AudioFile` de SpeechRecognition para leer el audio.
> 3. `recognize_google` envía el audio a la API de Google para obtener texto en español.
> 4. Manejo de errores y limpieza del archivo temporal.

---

## 💻 Paso 4: Crear la interfaz web con Gradio

```python
iface = gr.Interface(
    fn=procesar_request,
    inputs=[
        gr.Audio(label="Habla con el agente", type="filepath"),
    ],
    outputs=[
        gr.Textbox(label="El usuario dijo"),
    ],
    title="Speech-to-Text con Gradio",
    description="Subí un archivo de audio o hablá directamente, y la aplicación lo convertirá a texto."
)

iface.launch()
```

> 🎨 Gradio nos permite crear la interfaz interactiva sin necesidad de HTML/JS.
> El usuario puede grabar o subir audio directamente desde el navegador.

---

## 🧩 Código completo resumido

```python
import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment
import os

def procesar_request(audio_usuario):
    try:
        audio = AudioSegment.from_file(audio_usuario)
        audio.export("/tmp/temp.wav", format="wav")

        reconocedor = sr.Recognizer()
        with sr.AudioFile("/tmp/temp.wav") as source:
            audio_data = reconocedor.record(source)

        texto = reconocedor.recognize_google(audio_data, language="es-ES")

    except sr.UnknownValueError:
        texto = "No pude entender el audio."
    except sr.RequestError as e:
        texto = f"Error en el servicio de reconocimiento: {e}"
    except Exception as e:
        texto = f"Ocurrió un error: {e}"

    if os.path.exists("/tmp/temp.wav"):
        os.remove("/tmp/temp.wav")

    return texto

iface = gr.Interface(
    fn=procesar_request,
    inputs=[gr.Audio(label="Habla con el agente", type="filepath")],
    outputs=[gr.Textbox(label="El usuario dijo")],
    title="Speech-to-Text con Gradio",
    description="Subí un archivo de audio o hablá directamente, y la aplicación lo convertirá a texto."
)

iface.launch()
```

---

## 🎉 Conclusión

Con este laboratorio ahora tienes un **sistema de Speech-to-Text funcional en Python y Gradio**:

* ✅ Convierte audio a texto en español
* ✅ Permite entrada interactiva desde navegador o archivo
* ✅ Maneja errores y archivos temporales automáticamente
* ✅ Todo listo con pocas líneas de código

> 💡 Tip: Podés integrar esta función dentro de un chatbot o sistema de asistencia virtual para capturar la voz del usuario y procesarla automáticamente.
