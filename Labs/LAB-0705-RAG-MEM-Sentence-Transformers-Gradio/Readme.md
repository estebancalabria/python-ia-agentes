# Laboratorio: Sistema RAG Básico con Gradio 🚀

## Introducción 📝

En este laboratorio, aprenderemos a crear un **sistema RAG (Retrieval-Augmented Generation) básico** que:

- Cargue documentos
- Genere embeddings
- Recupere información relevante según la pregunta

Todo esto **sin usar OpenAI**, solo Python y [Gradio](https://gradio.app).

## Requisitos 📋

- Cuenta de Google para usar Google Colab
- Conocimientos básicos de Python

## Paso 1: Configurar el Entorno 🔧

Instalamos las librerías necesarias:

'''python!pip install gradio
!pip install sentence-transformers</code>

## Paso 2: Importar Bibliotecas 📚

```python
import gradio as gr
from sentence_transformers import SentenceTransformer, util
```

## Paso 3: Configurar el Modelo de Embeddings 💡

```python
# Modelo para generar embeddings
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

## Paso 4: Cargar Documentos 📄

Para este ejemplo, creamos algunos documentos de prueba:

```python
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "Gradio permite crear interfaces web para tus modelos de machine learning.",
    "Los modelos de lenguaje pueden usar embeddings para buscar información relevante."
]

# Generar embeddings de los documentos
embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)
```

## Paso 5: Función de Recuperación de Contexto 🔍

```python
def recuperar_contexto(pregunta, top_k=2):
    # Generar embedding de la pregunta
    embedding_pregunta = modelo_embeddings.encode(pregunta, convert_to_tensor=True)
    
    # Calcular similitud coseno
    resultados = util.cos_sim(embedding_pregunta, embeddings_docs)[0]
    
    # Obtener los índices de los documentos más similares
    top_indices = resultados.topk(top_k).indices
    
    # Retornar los documentos relevantes
    contexto = "\n".join([documentos[i] for i in top_indices])
    return contexto
```

## Paso 6: Función para Consultar el Sistema RAG 🧠

```python
def consulta_rag(pregunta):
    contexto = recuperar_contexto(pregunta)
    respuesta = f"Contexto relevante encontrado:\n{contexto}"
    return respuesta
```

## Paso 7: Crear la Interfaz con Gradio 🌟

```python
interfaz = gr.Interface(
    fn=consulta_rag,
    inputs="text",
    outputs="text",
    title="Sistema RAG Básico",
    description="Introduce una pregunta y el sistema mostrará los fragmentos más relevantes de los documentos."
)
```

## Paso 8: Lanzar la Interfaz 🚀

```python
interfaz.launch()
```

## Código Completo 🧩

```python

!pip install gradio
!pip install sentence-transformers

import gradio as gr
from sentence_transformers import SentenceTransformer, util

# Configurar modelo de embeddings
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')

# Documentos de ejemplo
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "Gradio permite crear interfaces web para tus modelos de machine learning.",
    "Los modelos de lenguaje pueden usar embeddings para buscar información relevante."
]

# Generar embeddings de los documentos
embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)

# Función de recuperación de contexto
def recuperar_contexto(pregunta, top_k=2):
    embedding_pregunta = modelo_embeddings.encode(pregunta, convert_to_tensor=True)
    resultados = util.cos_sim(embedding_pregunta, embeddings_docs)[0]
    top_indices = resultados.topk(top_k).indices
    contexto = "\n".join([documentos[i] for i in top_indices])
    return contexto

# Función de consulta RAG
def consulta_rag(pregunta):
    contexto = recuperar_contexto(pregunta)
    respuesta = f"Contexto relevante encontrado:\n{contexto}"
    return respuesta

# Crear interfaz Gradio
interfaz = gr.Interface(
    fn=consulta_rag,
    inputs="text",
    outputs="text",
    title="Sistema RAG Básico",
    description="Introduce una pregunta y el sistema mostrará los fragmentos más relevantes de los documentos."
)

# Lanzar interfaz
interfaz.launch()
```

## Conclusión 🎉

¡Listo! Ahora tienes un **sistema RAG básico sin depender de OpenAI**.  

- Puedes probar con tus propios documentos
- Hacer preguntas y ver qué fragmentos son más relevantes
- Ideal para laboratorios y experimentación inicial con embeddings y recuperación de información. 🚀
