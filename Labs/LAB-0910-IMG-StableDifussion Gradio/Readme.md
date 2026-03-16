# Laboratorio: LAB-0910-IMG-StableDifussion Gradio

En este laboratorio aprenderás a **crear una interfaz web para generar imágenes con Inteligencia Artificial** utilizando **Gradio** en **Google Colab**.

Usaremos un **modelo de difusión** para generar imágenes a partir de texto y construiremos una **pequeña aplicación web** donde el usuario podrá escribir un prompt y generar imágenes de forma interactiva.

---

## Requisitos previos

* Tener una cuenta de Google
* Acceder a **Google Colab**
* Tener conexión a internet

---

## Paso 1: Abrir Google Colab

1. Ve a [https://colab.google/](https://colab.google/)
2. Haz clic en **Nuevo notebook**.

---

## Paso 2: Habilitar el uso de GPU

La generación de imágenes requiere **aceleración por GPU**.

1. En el menú superior selecciona **Entorno de ejecución**.
2. Haz clic en **Cambiar tipo de entorno de ejecución**.
3. En **Acelerador de hardware**, selecciona **GPU**.
4. Haz clic en **Guardar**.

Si no habilitas la GPU, el modelo será extremadamente lento o puede no ejecutarse correctamente.

---

## Paso 3: Instalar las bibliotecas necesarias

1. Crear una celda nueva con el botón **"+"**.
2. Ejecuta la siguiente celda:

```
!pip install diffusers transformers accelerate torch sentencepiece gradio
```

Estas bibliotecas permitirán:

* Descargar el modelo desde Hugging Face
* Ejecutar el modelo de difusión
* Crear una interfaz web interactiva

---

## Paso 4: Crear la aplicación con Gradio

Crea una nueva celda y agrega el siguiente código:

```python
import torch
import gradio as gr
from diffusers import DiffusionPipeline

# Cargar el modelo
pipe = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.bfloat16
).to("cuda")

# Función que genera la imagen
def generar_imagen(prompt):
    image = pipe(prompt).images[0]
    return image

# Crear interfaz
app = gr.Interface(
    fn=generar_imagen,
    inputs=gr.Textbox(label="Prompt", placeholder="Describe la imagen que quieres generar"),
    outputs=gr.Image(label="Imagen generada"),
    title="Generador de Imágenes con IA",
    description="Escribe un prompt y genera una imagen utilizando un modelo de difusión"
)

app.launch()
```

---

## Paso 5: Ejecutar la aplicación

1. Ejecuta la celda.
2. La primera vez que se ejecuta:

   * El modelo será **descargado desde Hugging Face**.
   * Esto puede tardar algunos minutos.

Una vez iniciado, **Gradio generará una interfaz web interactiva**.

En Colab aparecerá un **link para abrir la aplicación**.

---

## Paso 6: Generar imágenes desde la interfaz

1. Escribe un prompt en el campo de texto.

Ejemplo:

```
a cat astronaut riding a bicycle on mars
```

2. Haz clic en **Submit**.
3. El modelo generará la imagen.

---

## Paso 7: Probar distintos prompts

Puedes experimentar con diferentes descripciones.

Ejemplos:

```
a futuristic city at sunset, cyberpunk style
```

```
a robot drinking coffee in Buenos Aires, watercolor style
```

```
an ancient magical library, fantasy illustration
```

Cada prompt generará una imagen diferente.

---

## Resultado esperado

Al finalizar este laboratorio habrás aprendido a:

* Generar imágenes con **modelos de difusión**
* Crear una **interfaz web con Gradio**
* Construir una pequeña aplicación de **IA generativa**

Ahora puedes interactuar con el modelo de generación de imágenes desde una **interfaz gráfica en tu navegador**.
