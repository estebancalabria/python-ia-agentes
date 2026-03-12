# 🧪 Laboratorio: Embeddings y Búsqueda Semántica con Gemini 🚀

## 📝 Introducción

En este laboratorio aprenderemos a usar **embeddings de Gemini** para:

* 🔢 Convertir texto en vectores numéricos
* 📊 Medir similitud semántica entre textos
* 🔎 Recuperar documentos relevantes según una pregunta

Esto es la **base de los sistemas RAG (Retrieval-Augmented Generation)**.

Trabajaremos usando:

* 🐍 Python
* 🤖 API de Gemini
* 📊 Scikit-learn

⚠️ Todo se ejecutará **desde la consola**, sin interfaces web.

---

## 📚 Referencia Oficial

Este laboratorio está basado en la documentación oficial de Gemini:

🔗 [https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419](https://ai.google.dev/gemini-api/docs/embeddings?hl=es-419)

Para usar la API necesitas crear una **API Key** en:

🔑 [https://aistudio.google.com/api-keys](https://aistudio.google.com/api-keys)

---

# 📋 Requisitos

* Python 3.9+
* Pip instalado
* API Key de Gemini

---

# 🔧 Paso 1: Instalar dependencias

En la terminal:

```bash
pip install google-genai pandas scikit-learn
```

---

# 📚 Paso 2: Importar bibliotecas

```python
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
```

---

# 🔑 Paso 3: Ingresar la API Key

Pedimos la API key al usuario para autenticarnos contra Gemini.

```python
from google import genai

api_key = input("Ingrese API Key: ")

client = genai.Client(api_key=api_key)
```

---

# 🔢 Paso 4: Generar un embedding simple

Un **embedding** es un vector numérico que representa el significado de un texto.

```python
from google import genai

api_key=input("Ingrese Api Key")
client = genai.Client(api_key=api_key)

result = client.models.embed_content(
        model="gemini-embedding-001",
        contents="What is the meaning of life?"
)

print(result.embeddings)
```

Salida aproximada:

```
[Embedding(values=[0.0123, -0.0932, ...])]
```

⚡ Ese vector puede tener **más de 700 dimensiones**.

---

# 📚 Paso 5: Generar embeddings de múltiples textos

También podemos generar embeddings para varios textos al mismo tiempo.

```python
from google import genai

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-001",
        contents= [
            "What is the meaning of life?",
            "What is the purpose of existence?",
            "How do I bake a cake?"
        ]
)

for embedding in result.embeddings:
    print(embedding)
```

Cada texto tendrá su propio vector.

---

# 📊 Paso 6: Medir similitud entre textos

Ahora vamos a calcular **qué tan parecidos son los textos entre sí** usando **cosine similarity**.

```python
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

# Create a 3x3 table to show the similarity matrix
df = pd.DataFrame(
    cosine_similarity([e.values for e in result.embeddings]),
    index=texts,
    columns=texts,
)

print(df)
```

Salida aproximada:

|                      | meaning of life | purpose of existence | bake a cake |
| -------------------- | --------------- | -------------------- | ----------- |
| meaning of life      | 1.00            | 0.89                 | 0.12        |
| purpose of existence | 0.89            | 1.00                 | 0.10        |
| bake a cake          | 0.12            | 0.10                 | 1.00        |

💡 Observamos que:

* **meaning of life** y **purpose of existence** son muy similares
* **bake a cake** es completamente distinto

---

# 🔎 Paso 7: Recuperación de documentos (Mini RAG)

Ahora construiremos un pequeño sistema que:

1️⃣ Guarda documentos
2️⃣ Genera embeddings
3️⃣ Busca el más relevante según una pregunta

---

## 📄 Documentos

```python
documentos = [
    "Python es un lenguaje de programación muy popular",
    "La inteligencia artificial utiliza modelos entrenados con datos",
    "La pizza se cocina en horno a alta temperatura",
    "Los embeddings permiten comparar significado de textos"
]
```

---

## 🔢 Generar embeddings de documentos

```python
result_docs = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documentos,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

embeddings_docs = [e.values for e in result_docs.embeddings]
```

---

## ❓ Pregunta del usuario

```python
pregunta = input("Ingrese su pregunta: ")
```

---

## 🔢 Generar embedding de la pregunta

```python
embedding_pregunta = client.models.embed_content(
    model="gemini-embedding-001",
    contents=pregunta,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

embedding_pregunta = embedding_pregunta.embeddings[0].values
```

---

## 📊 Calcular similitud

```python
similitudes = cosine_similarity(
    [embedding_pregunta],
    embeddings_docs
)[0]
```

---

## 🏆 Obtener el documento más relevante

```python
indice_mejor = similitudes.argmax()

print("\nDocumento más relevante:")
print(documentos[indice_mejor])
```

---

# 💻 Código Completo

```python
from google import genai
from google.genai import types
from sklearn.metrics.pairwise import cosine_similarity

# API Key
api_key = input("Ingrese API Key: ")
client = genai.Client(api_key=api_key)

# Documentos
documentos = [
    "Python es un lenguaje de programación muy popular",
    "La inteligencia artificial utiliza modelos entrenados con datos",
    "La pizza se cocina en horno a alta temperatura",
    "Los embeddings permiten comparar significado de textos"
]

# Embeddings de documentos
result_docs = client.models.embed_content(
    model="gemini-embedding-001",
    contents=documentos,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

embeddings_docs = [e.values for e in result_docs.embeddings]

# Pregunta
pregunta = input("Ingrese su pregunta: ")

# Embedding de la pregunta
embedding_pregunta = client.models.embed_content(
    model="gemini-embedding-001",
    contents=pregunta,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

embedding_pregunta = embedding_pregunta.embeddings[0].values

# Similitud
similitudes = cosine_similarity(
    [embedding_pregunta],
    embeddings_docs
)[0]

# Documento más relevante
indice_mejor = similitudes.argmax()

print("\nDocumento más relevante:")
print(documentos[indice_mejor])
```

---

# ▶️ Ejemplo de ejecución

### Pregunta

```
¿Para qué sirven los embeddings?
```

### Resultado

```
Documento más relevante:
Los embeddings permiten comparar significado de textos
```

---

# 🎉 Conclusión

En este laboratorio aprendiste a:

* 🔢 Generar embeddings con **Gemini**
* 📊 Calcular **similitud semántica**
* 🔎 Recuperar documentos relevantes
* 🧠 Entender la base de los sistemas **RAG**

💡 Este mismo mecanismo es el que usan:

* ChatGPT Retrieval
* Sistemas de búsqueda semántica
* Chatbots con documentos
* RAG con PDFs
