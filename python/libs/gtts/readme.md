# 📢 gTTS — Google Text‑to‑Speech (Python)

## 📌 ¿Qué es `gTTS`?

`gTTS` (Google Text‑to‑Speech) es una librería de Python que permite convertir **texto en audio (voz)** utilizando el motor de síntesis de voz de **Google Translate**.  
Es simple, rápida y útil para generar archivos de audio a partir de texto para tareas de accesibilidad, asistentes de voz, lectura automatizada, bots, pruebas, etc.

📎 Documentación oficial: https://gtts.readthedocs.io/en/latest/

---

## 👤 ¿Quién creó `gTTS`?

La librería fue desarrollada por **Pierre‑Yves Ritschard** y colaboradores como una implementación Python de la interfaz de texto a voz disponible en Google Translate.  
Es de código abierto y está publicada en PyPI bajo licencia permissiva.

---

## ⚙️ Requisitos

* Python 3.5 o superior
* Conexión a Internet (usa el servicio de Google Translate)
* Pip para instalar dependencias

---

## 🚀 Cómo instalar

Desde tu terminal o entorno de desarrollo:

```bash
pip install gtts
````

Si querés también reproducir el audio dentro de una notebook (Colab / Jupyter), podés instalar:

```bash
pip install ipython
```

---

## 📦 ¿Qué hace `gTTS`?

La librería toma como entrada:

* Un **texto** (string)
* Un **idioma** (`lang`)
* Opcionalmente otras configuraciones de voz

Y genera un **archivo de audio** (MP3) con la voz sintetizada.

---

## 🧠 Conceptos clave

| Parámetro | Qué hace                                   |
| --------- | ------------------------------------------ |
| `text`    | El texto que querés convertir a voz        |
| `lang`    | Código de idioma (ej. `"es"` para español) |
| `slow`    | Velocidad de lectura (`True` o `False`)    |

---

## 📘 Uso básico

Ejemplo mínimo para generar un archivo MP3:

```python
from gtts import gTTS

texto = "Hola, este es un ejemplo con gTTS"
tts = gTTS(text=texto, lang="es")

# Guardar en archivo
tts.save("salida.mp3")
```

---

## 📌 Métodos y propiedades más comunes

### 🔹 `gTTS(text, lang, slow=False)`

Constructor principal.
**Parámetros:**

* `text` (str): texto a sintetizar
* `lang` (str): código de idioma (por ejemplo, `"es"`, `"en"`, `"fr"`)
* `slow` (bool): si se quiere leer más despacio

Ejemplo:

```python
tts = gTTS("Texto de prueba", lang="en", slow=True)
```

---

### 🔹 `save(filename)`

Guarda el audio en un archivo local:

```python
tts.save("mi_audio.mp3")
```

---

### 🔹 `write_to_fp(file_object)`

Escribe el audio directamente en un objeto file‑like:

```python
with open("archivo.mp3", "wb") as f:
    tts.write_to_fp(f)
```

---

## 🎧 Reproducción de audio en notebooks

Si estás en Jupyter o Colab:

```python
from IPython.display import Audio
Audio("salida.mp3", autoplay=True)
```

---

## 🗣️ Idiomas soportados

La librería soporta múltiples códigos de idiomas, algunos ejemplos:

| Idioma    | Código |
| --------- | ------ |
| Español   | `"es"` |
| Inglés    | `"en"` |
| Italiano  | `"it"` |
| Portugués | `"pt"` |
| Alemán    | `"de"` |
| Francés   | `"fr"` |

Podés ver la lista completa en la documentación oficial.

---

## 🧪 Ejemplo completo

```python
from gtts import gTTS

texto = """
Bienvenido al ejemplo de gTTS.
Este texto será convertido a audio usando Google Text to Speech."""
tts = gTTS(text=texto, lang="es", slow=False)

tts.save("bienvenida.mp3")
print("Archivo de audio generado: bienvenida.mp3")
```

---

## ⚠️ Limitaciones

* Requiere conexión a Internet
* Dependiente del servicio de Google Translate
* No es un modelo local de voz, sino un wrapper con API pública

---

## 🧡 Contribuir

Si querés colaborar con mejoras, podés visitar:

* 📍 Repositorio oficial en GitHub
* 📄 Documentación completa: [https://gtts.readthedocs.io/en/latest/](https://gtts.readthedocs.io/en/latest/)

---

## 📦 Licencia

`gTTS` es software de código abierto bajo licencias permisivas.

