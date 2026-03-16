La **Diffusers** es una librería de **Python desarrollada por Hugging Face** que permite **usar modelos de difusión para generar contenido**, principalmente **imágenes a partir de texto (text-to-image)**.

Es una de las herramientas más usadas para trabajar con modelos como:

* Stable Diffusion
* FLUX.1
* DALL·E (algunas variantes compatibles)

---

# 🧠 Idea simple

La librería **Diffusers** te da una **forma sencilla de cargar y ejecutar modelos generativos** basados en **difusión**.

Los **modelos de difusión** funcionan así:

1. Empiezan con **ruido aleatorio**
2. Van **quitando ruido paso a paso**
3. Hasta que aparece una **imagen coherente que coincide con el prompt**

Ese proceso se llama **Diffusion Model**.

---

# 🧑‍💻 Qué hace la librería en la práctica

Con muy poco código podés:

* cargar modelos generativos
* generar imágenes
* hacer image-to-image
* inpainting (editar partes de una imagen)
* controlar parámetros del modelo

Ejemplo típico:

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
).to("cuda")

image = pipe("a robot drinking coffee").images[0]
```

La librería se encarga de:

* descargar el modelo
* preparar GPU
* ejecutar el proceso de difusión
* devolver la imagen

---

# ⚙️ Componentes internos de Diffusers

Un pipeline suele tener:

1️⃣ **Text encoder**
Convierte el prompt en vectores.

2️⃣ **UNet**
La red neuronal que va **quitando el ruido**.

3️⃣ **Scheduler**
Define **cómo se elimina el ruido paso a paso**.

4️⃣ **VAE (decoder)**
Convierte los datos latentes en **imagen final**.

---

# 📦 Por qué es tan usada

Ventajas:

* open source
* compatible con **PyTorch**
* funciona en **Google Colab**
* soporta muchos modelos

Por eso se usa mucho para enseñar **IA generativa en Python**.

---

# 🎓 Cómo explicarlo fácil en una clase

Yo lo resumiría así:

> **Diffusers es la librería de Python que permite ejecutar modelos generativos de imágenes basados en difusión de forma simple.**

En una slide queda perfecto:

```
Prompt → Diffusers → Modelo → Imagen
```
