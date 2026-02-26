# 🚀 Laboratorio: Usar un modelo de Hugging Face en Google Colab

## 🎯 Objetivo

Cargar y ejecutar el modelo **GPT-2** desde Hugging Face en Google Colab usando `pipeline`.

Modelo a utilizar:
Hugging Face →
OpenAI GPT-2
[https://huggingface.co/openai-community/gpt2](https://huggingface.co/openai-community/gpt2)

---

## 🧭 Paso 1 – Ir al modelo

1. Abrir el siguiente enlace:
   👉 [https://huggingface.co/openai-community/gpt2](https://huggingface.co/openai-community/gpt2)

2. Hacer clic en el botón **"Use this model"** (arriba a la derecha).

3. Seleccionar **Colab**.

---

## 🧪 Paso 2 – Instalar dependencias (si no están instaladas)

En la primera celda de Colab ejecutar:

```python
!pip install transformers
```

---

## 🧠 Paso 3 – Ejecutar el modelo

Agregar una nueva celda con el siguiente código:

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="openai-community/gpt2")

resultado = pipe(
    "La inteligencia artificial en educación permitirá",
    max_length=60,
    do_sample=True,
    temperature=0.8
)

print(resultado[0]["generated_text"])
```

Ejecutar la celda.

---

## 🔁 Paso 4 – Experimentar

Modificar:

* El prompt
* `max_length`
* `temperature`

Ejemplo:

```python
resultado = pipe(
    "En el futuro los programadores trabajarán con IA para",
    max_length=80,
    temperature=1.0
)
```

---

## ✅ Resultado esperado

El modelo generará texto continuando la frase ingresada.

---

# 🏁 Fin del laboratorio
