# 🧪 Laboratorio: Text-to-Speech con gTTS 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema sencillo de Text-to-Speech (TTS)** que:

* ✍️ Recibe texto del usuario
* 🔊 Genera un archivo de audio en formato MP3 usando gTTS
* 🎧 Permite reproducir el audio directamente en Google Colab

Todo esto usando únicamente:

* Python
* gTTS
* IPython.display para reproducir audio

⚠️ Sin interfaces web complejas, solo consola y Colab.

---

## 📋 Requisitos

* Python 3.9+
* Pip instalado
* Conocimientos básicos de Python

---

## 🔧 Paso 1: Instalar dependencias

Desde la terminal de Colab:

```bash
pip install gtts
```

> 💡 Si querés manipular audio más adelante, también se puede instalar `pydub`:
>
> ```bash
> pip install pydub
> ```

---

## 📚 Paso 2: Importar bibliotecas

```python
from gtts import gTTS
from IPython.display import Audio
```

---

## 💡 Paso 3: Definir texto de ejemplo

Este es el texto que nuestro sistema podrá convertir a audio:

```python
texto = "Hola, este es un ejemplo usando gTTS en Google Colab."
```

---

## 💻 Paso 4: Crear el objeto gTTS

```python
# Crear objeto TTS en español
tts = gTTS(text=texto, lang='es')
```

> 🧠 `gTTS` toma el texto y lo convierte en un objeto de audio que podemos guardar o reproducir.

---

## 🔢 Paso 5: Guardar el audio en un archivo

```python
archivo_audio = "ejemplo.mp3"
tts.save(archivo_audio)
```

> ⚡ Ahora tenemos un archivo MP3 con la voz generada a partir del texto.

---

## 🔍 Paso 6: Reproducir el audio en Colab

```python
Audio(archivo_audio, autoplay=True)
```

> 🎧 El audio se reproducirá directamente en la notebook.

---

## 💡 Paso 7: Pedir texto al usuario

Podemos permitir que el usuario ingrese cualquier texto para convertirlo a voz:

```python
entrada_usuario = input("Ingrese el texto que quiere convertir a audio: ")

# Crear audio
tts_usuario = gTTS(text=entrada_usuario, lang='es')
archivo_usuario = "usuario.mp3"
tts_usuario.save(archivo_usuario)

# Reproducir audio
Audio(archivo_usuario, autoplay=True)
```

> ✅ Ahora el sistema TTS es interactivo.

---

## 💻 Paso 8: Ejemplo de manipulación con pydub (opcional)

Si instalamos `pydub`, podemos modificar el audio, por ejemplo cambiar volumen:

```python
from pydub import AudioSegment

# Cargar audio generado
audio = AudioSegment.from_mp3("usuario.mp3")

# Reducir volumen en 10 dB
audio = audio - 10

# Guardar audio modificado
audio.export("usuario_bajo.mp3", format="mp3")

# Reproducir audio modificado
Audio("usuario_bajo.mp3", autoplay=True)
```

> 🔊 Esto permite ajustar el audio antes de reproducirlo.

---

## 🧩 Código Completo Actualizado

```python
from gtts import gTTS
from IPython.display import Audio
from pydub import AudioSegment

# Paso 1: Texto inicial
texto = "Hola, este es un ejemplo usando gTTS en Google Colab."

# Crear y guardar audio
tts = gTTS(text=texto, lang='es')
archivo_audio = "ejemplo.mp3"
tts.save(archivo_audio)

# Reproducir audio
Audio(archivo_audio, autoplay=True)

# Paso 2: Texto ingresado por usuario
entrada_usuario = input("Ingrese el texto que quiere convertir a audio: ")

# Crear y guardar audio del usuario
tts_usuario = gTTS(text=entrada_usuario, lang='es')
archivo_usuario = "usuario.mp3"
tts_usuario.save(archivo_usuario)

# Reproducir audio
Audio(archivo_usuario, autoplay=True)

# Paso 3: (Opcional) manipulación con pydub
audio = AudioSegment.from_mp3("usuario.mp3")
audio = audio - 10  # reducir volumen
audio.export("usuario_bajo.mp3", format="mp3")
Audio("usuario_bajo.mp3", autoplay=True)
```

---

## 🎉 Conclusión

Con este laboratorio ahora tienes un **sistema TTS básico en Colab**:

* ✅ Convierte texto a audio en español
* ✅ Permite entrada interactiva del usuario
* ✅ Puede manipular audio con pydub
* ✅ Todo en Python, sin complejidades de interfaces web

> 💡 Tip: Podés combinar varios textos en un solo audio usando `pydub` para crear narraciones más largas.
