Perfecto. Vamos a armar un **laboratorio paso a paso** de RAG usando **FAISS local** y **Python puro** (sin Gradio ni Colab), usando `input()` y `print()` para que los alumnos puedan probarlo en cualquier entorno. También incluimos el link oficial a FAISS.

---

# Laboratorio: Sistema RAG Básico con FAISS Local 🧠

## Introducción 📝

En este laboratorio aprenderás a crear un **sistema RAG (Retrieval-Augmented Generation)** que:

* Cargue documentos
* Genere embeddings usando **Sentence-Transformers**
* Almacene embeddings en una base de datos vectorial **local con FAISS**
* Recupere los documentos más relevantes según la pregunta del usuario

Todo esto **sin depender de OpenAI ni servicios en la nube**, usando solo Python y FAISS.

🔗 Más info sobre FAISS: [https://faiss.ai/index.html](https://faiss.ai/index.html)

---

## Requisitos 📋

* Python 3.x instalado
* Librerías: `sentence-transformers`, `faiss-cpu`, `numpy`

Instalación:
!pip install sentence-transformers faiss-cpu numpy

---

## Paso 1: Importar librerías 📚

```python
from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np
```

* `SentenceTransformer` → genera embeddings de tus documentos y preguntas
* `faiss` → almacena embeddings y realiza búsquedas rápidas
* `numpy` → para manipular vectores y matrices

---

## Paso 2: Configurar el modelo de embeddings 💡

```python
# Modelo para generar embeddings
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

**Explicación:**
`all-MiniLM-L6-v2` es un modelo pequeño y rápido que genera vectores semánticos de alta calidad, ideal para laboratorios y prototipos.

---

## Paso 3: Crear documentos de ejemplo 📄

```python
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "FAISS permite búsquedas rápidas de vectores de alta dimensión.",
    "Los modelos de lenguaje usan embeddings para encontrar información relevante.",
    "Gradio permite crear interfaces web para modelos de ML.",
    "RAG combina recuperación de información y generación de texto."
]
```

**Explicación:**
Estos documentos serán nuestra base de conocimiento para la recuperación de contexto.

---

## Paso 4: Generar embeddings de los documentos 💾

```python
# Generar embeddings y convertir a numpy array
embeddings_docs = modelo_embeddings.encode(documentos, convert_to_numpy=True)
```

**Explicación:**

* Cada documento se convierte en un vector de números.
* Estos vectores se almacenarán en FAISS para consultas rápidas.

---

## Paso 5: Crear índice FAISS 🔍

```python
d = embeddings_docs.shape[1]  # dimensión de los embeddings
index = faiss.IndexFlatL2(d)  # índice en memoria usando distancia L2
index.add(embeddings_docs)    # agregar todos los embeddings de los documentos
```

**Explicación:**

* `IndexFlatL2` calcula la **distancia euclidiana** entre vectores.
* `add()` agrega todos los embeddings de los documentos al índice.
* FAISS ahora puede responder consultas de manera muy eficiente.

---

## Paso 6: Función para recuperar documentos relevantes 🧠

```python
def recuperar_contexto(pregunta, top_k=2):
    # Generar embedding de la pregunta
    embedding_pregunta = modelo_embeddings.encode([pregunta], convert_to_numpy=True)
    
    # Buscar top-k documentos más cercanos
    D, I = index.search(embedding_pregunta, top_k)
    
    # Retornar los documentos relevantes
    contexto = "\n".join([documentos[i] for i in I[0]])
    return contexto
```

**Explicación:**

* `search()` devuelve la distancia y los índices de los `top_k` documentos más cercanos.
* Con `I[0]` obtenemos los índices y construimos un string con los documentos relevantes.

---

## Paso 7: Función para consultar el sistema RAG 📝

```python
def consulta_rag():
    pregunta = input("Escribe tu pregunta: ")
    contexto = recuperar_contexto(pregunta)
    print("\nContexto relevante encontrado:")
    print(contexto)
```

**Explicación:**

* Usamos `input()` para que el usuario escriba la pregunta.
* Mostramos los documentos más relevantes usando `print()`.
* Este flujo simula un sistema RAG simple, pero funcional.

---

## Paso 8: Ejecutar el laboratorio 🚀

```python
while True:
    consulta_rag()
    cont = input("\n¿Querés hacer otra pregunta? (s/n): ")
    if cont.lower() != 's':
        break
```

**Explicación:**

* Permitimos múltiples consultas consecutivas.
* La sesión termina cuando el usuario responde "n".

---

## Código Completo 🧩

```python
# Laboratorio RAG con FAISS

from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np

# Modelo de embeddings
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')

# Documentos de ejemplo
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "FAISS permite búsquedas rápidas de vectores de alta dimensión.",
    "Los modelos de lenguaje usan embeddings para encontrar información relevante.",
    "Gradio permite crear interfaces web para modelos de ML.",
    "RAG combina recuperación de información y generación de texto."
]

# Generar embeddings
embeddings_docs = modelo_embeddings.encode(documentos, convert_to_numpy=True)

# Crear índice FAISS
d = embeddings_docs.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings_docs)

# Función para recuperar documentos relevantes
def recuperar_contexto(pregunta, top_k=2):
    embedding_pregunta = modelo_embeddings.encode([pregunta], convert_to_numpy=True)
    D, I = index.search(embedding_pregunta, top_k)
    contexto = "\n".join([documentos[i] for i in I[0]])
    return contexto

# Función para consultar el sistema RAG
def consulta_rag():
    pregunta = input("Escribe tu pregunta: ")
    contexto = recuperar_contexto(pregunta)
    print("\nContexto relevante encontrado:")
    print(contexto)

# Ejecutar laboratorio
while True:
    consulta_rag()
    cont = input("\n¿Querés hacer otra pregunta? (s/n): ")
    if cont.lower() != 's':
        break
```

---

✅ **Listo!** Ahora tenés un laboratorio completo paso a paso para tus alumnos usando **FAISS local**, sin Gradio, con explicaciones en cada paso y un código final para copiar y pegar.

\¿Querés que haga esa versión también?
