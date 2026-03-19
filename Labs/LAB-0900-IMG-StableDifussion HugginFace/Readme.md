# Laboratorio: LAB-0900-IMG-StableDifussion HugginFace

En este laboratorio aprenderás a **generar imágenes con Inteligencia Artificial** utilizando **modelos de difusión** desde **Python en Google Colab**.

Usaremos un modelo moderno disponible en **Hugging Face** para generar una imagen a partir de un **prompt de texto**.

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

La generación de imágenes con modelos de difusión requiere **aceleración por GPU**.

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
!pip install diffusers transformers accelerate torch sentencepiece
```

Estas bibliotecas permiten descargar y ejecutar modelos generativos desde **Hugging Face**.

---

## Paso 4: Crear la celda principal de generación de imágenes

Crea una nueva celda y agrega el siguiente código:

```python
import torch
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.bfloat16
).to("cuda")

prompt = "a cat astronaut riding a bicycle on mars"

image = pipe(prompt).images[0]

image
```

---

## Paso 5: Ejecutar el modelo

1. Ejecuta la celda.
2. La primera vez que se ejecuta:

   * El modelo será **descargado desde Hugging Face**.
   * Esto puede tardar algunos minutos.
3. Una vez descargado, el modelo generará la imagen.

El resultado aparecerá directamente debajo de la celda.

---

## Paso 6: Probar distintos prompts

Modifica la variable **prompt** para generar nuevas imágenes.

Ejemplos:

```
prompt = "a futuristic city at sunset, cyberpunk style"
```

```
prompt = "a medieval castle floating in the sky, fantasy illustration"
```

```
prompt = "a robot drinking coffee in Buenos Aires, watercolor style"
```

Cada ejecución generará una imagen diferente basada en el texto.

---

## Paso 7: Experimentar

Puedes probar diferentes descripciones para observar cómo el modelo interpreta los prompts.

Algunas ideas:

* estilos artísticos
* paisajes
* escenas futuristas
* personajes fantásticos

Ejemplo:

```
prompt = "an ancient library full of magical books, cinematic lighting"
```

---

## Resultado esperado

Al ejecutar el notebook deberías poder:

* Generar imágenes desde texto
* Cambiar el prompt y obtener resultados distintos
* Ejecutar modelos de **IA generativa** directamente desde **Python**

¡Listo! Ahora sabes cómo generar imágenes utilizando **modelos de difusión en Google Colab con Hugging Face**.
