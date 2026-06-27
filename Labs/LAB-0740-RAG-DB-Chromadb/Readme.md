# 🧪 Laboratorio: Sistema RAG Básico con ChromaDB (Persistente)

## 📝 Introducción

En este laboratorio construimos un **sistema RAG persistente** usando:

* Python
* SentenceTransformers
* ChromaDB

✅ Los documentos se guardan en disco  
✅ No se pierden al cerrar el programa  
✅ Sin OpenAI  
✅ Todo en consola, sin funciones wrapper

---

## 📋 Requisitos

* Python 3.9+
* Pip instalado

---

## 🔧 Paso 1: Instalar dependencias

```bash
pip install chromadb sentence-transformers
```

---

## 📚 Paso 2: Importar bibliotecas y cargar el modelo

```python
import chromadb
from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer('all-MiniLM-L6-v2')
```

---

## 💾 Paso 3: Definir documentos y generar embeddings

```python
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "SentenceTransformers permite generar embeddings fácilmente.",
    "Los sistemas RAG combinan recuperación de información con generación de texto."
]

embeddings = modelo.encode(documentos).tolist()
```

👉 `encode()` devuelve un array de NumPy. Con `.tolist()` lo convertimos a lista de Python, que es lo que espera ChromaDB.

---

## 🗄️ Paso 4: Crear cliente persistente y colección

```python
client = chromadb.PersistentClient(path="./db4")

collection = client.create_collection(name="faq")
```

👉 `PersistentClient` guarda todo en la carpeta `./db4`. La próxima vez que ejecutes el script, los datos siguen ahí.

> ⚠️ Si ya existe la colección (segunda ejecución), `create_collection` va a fallar. Podés reemplazarlo por `get_or_create_collection` para evitar el error.

---

## 📥 Paso 5: Indexar los documentos

```python
collection.add(
    documents=documentos,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documentos))]
)
```

👉 Los `ids` son strings obligatorios. Acá los generamos automáticamente: `"0"`, `"1"`, `"2"`.

---

## 🔍 Paso 6: Hacer una consulta

```python
pregunta = input("Pregunta: ")

embedding_pregunta = modelo.encode([pregunta]).tolist()

resultado = collection.query(
    query_embeddings=embedding_pregunta,
    n_results=3
)

print(resultado["documents"][0])
```

👉 `resultado["documents"]` es una lista de listas (una por cada query). Como mandamos una sola pregunta, accedemos al índice `[0]` para obtener los documentos relevantes.

---

## 🧩 Código Completo

```python
# pip install chromadb sentence-transformers

import chromadb
from sentence_transformers import SentenceTransformer

# 1️⃣ Modelo de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# 2️⃣ Documentos y sus embeddings
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "SentenceTransformers permite generar embeddings fácilmente.",
    "Los sistemas RAG combinan recuperación de información con generación de texto."
]

embeddings = modelo.encode(documentos).tolist()

# 3️⃣ Cliente persistente
client = chromadb.PersistentClient(path="./db4")

# 4️⃣ Colección
collection = client.create_collection(name="faq")

# 5️⃣ Indexar documentos
collection.add(
    documents=documentos,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documentos))]
)

# 6️⃣ Consulta
pregunta = input("Pregunta: ")

embedding_pregunta = modelo.encode([pregunta]).tolist()

resultado = collection.query(
    query_embeddings=embedding_pregunta,
    n_results=3
)

print(resultado["documents"][0])
```

---

## 🎯 Diferencias respecto a la versión anterior

| Versión anterior | Esta versión |
|---|---|
| Embeddings delegados a Chroma | Embeddings generados manualmente con `encode()` |
| Funciones wrapper (`recuperar_contexto`, `iniciar_rag`) | Código directo, sin funciones |
| `query_texts` | `query_embeddings` |
| Loop interactivo | Una sola consulta |

---

## 🏁 Conclusión

✅ RAG persistente en disco  
✅ Control explícito de los embeddings  
✅ Sin funciones wrapper: cada paso visible  
✅ Sin OpenAI  
✅ Base para escalar a pipelines más complejos
