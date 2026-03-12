# 🧪 Laboratorio: Sistema RAG Básico con ChromaDB (Persistente) 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema RAG básico pero persistente** usando:

* Python
* Hugging Face
* SentenceTransformers
* ChromaDB

A diferencia del laboratorio anterior:

✅ Los documentos se guardan en disco
✅ No se pierden al cerrar el programa
✅ No usamos OpenAI

Todo funciona en consola.

---

# 📋 Requisitos

* Python 3.9+
* Pip instalado

---

# 🔧 Paso 1: Instalar dependencias

```bash
pip install chromadb sentence-transformers
```

---

# 📚 Paso 2: Importar bibliotecas

```python
import chromadb
from sentence_transformers import SentenceTransformer
```

---

# 💡 Paso 3: Crear cliente persistente

Aquí está la diferencia clave.

Chroma permite persistencia automática indicando una carpeta:

```python
client = chromadb.PersistentClient(path="./mi_base_rag")
```

👉 Esto crea una carpeta `mi_base_rag` donde se guardan los vectores.

---

# 🧠 Paso 4: Cargar modelo de embeddings

```python
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

Creamos una función para que Chroma use este modelo:

```python
def generar_embedding(textos):
    return modelo_embeddings.encode(textos).tolist()
```

---

# 📄 Paso 5: Crear colección

```python
collection = client.get_or_create_collection(
    name="documentos",
    embedding_function=generar_embedding
)
```

Si no existe → la crea
Si ya existe → la reutiliza

Persistencia automática ✅

---

# 📥 Paso 6: Agregar documentos (solo la primera vez)

```python
if collection.count() == 0:
    
    documentos = [
        "Python es un lenguaje de programación muy popular.",
        "SentenceTransformers permite generar embeddings fácilmente.",
        "Los sistemas RAG combinan recuperación de información con generación de texto."
    ]
    
    collection.add(
        documents=documentos,
        ids=["doc1", "doc2", "doc3"]
    )
    
    print("Documentos cargados por primera vez.\n")
```

Si ejecutás el script otra vez
→ No vuelve a cargar duplicados.

---

# 🔍 Paso 7: Función de recuperación

```python
def recuperar_contexto(pregunta, top_k=2):
    
    resultados = collection.query(
        query_texts=[pregunta],
        n_results=top_k
    )
    
    documentos_relevantes = resultados["documents"][0]
    
    contexto = "\n".join(documentos_relevantes)
    return contexto
```

Observá que:

👉 No calculamos similitud manual
👉 Chroma lo hace internamente

---

# 🧠 Paso 8: Loop interactivo

```python
def iniciar_rag():
    print("====================================")
    print(" Sistema RAG con ChromaDB ")
    print(" Persistente y en Consola ")
    print(" Escribe 'salir' para terminar")
    print("====================================\n")
    
    while True:
        pregunta = input("Tu pregunta: ")
        
        if pregunta.lower() == "salir":
            print("Saliendo del sistema...")
            break
        
        contexto = recuperar_contexto(pregunta)
        
        print("\n--- Contexto relevante encontrado ---")
        print(contexto)
        print("--------------------------------------\n")
```

---

# 🚀 Paso 9: Ejecutar

```python
if __name__ == "__main__":
    iniciar_rag()
```

---

# 🧩 Código Completo

```python
# pip install chromadb sentence-transformers

import chromadb
from sentence_transformers import SentenceTransformer

# 1️⃣ Cliente persistente
client = chromadb.PersistentClient(path="./mi_base_rag")

# 2️⃣ Modelo embeddings
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')

def generar_embedding(textos):
    return modelo_embeddings.encode(textos).tolist()

# 3️⃣ Colección
collection = client.get_or_create_collection(
    name="documentos",
    embedding_function=generar_embedding
)

# 4️⃣ Cargar documentos solo si no existen
if collection.count() == 0:
    
    documentos = [
        "Python es un lenguaje de programación muy popular.",
        "SentenceTransformers permite generar embeddings fácilmente.",
        "Los sistemas RAG combinan recuperación de información con generación de texto."
    ]
    
    collection.add(
        documents=documentos,
        ids=["doc1", "doc2", "doc3"]
    )
    
    print("Documentos cargados por primera vez.\n")

# 5️⃣ Función de recuperación
def recuperar_contexto(pregunta, top_k=2):
    
    resultados = collection.query(
        query_texts=[pregunta],
        n_results=top_k
    )
    
    documentos_relevantes = resultados["documents"][0]
    
    contexto = "\n".join(documentos_relevantes)
    return contexto

# 6️⃣ Loop principal
def iniciar_rag():
    print("====================================")
    print(" Sistema RAG con ChromaDB ")
    print(" Persistente y en Consola ")
    print(" Escribe 'salir' para terminar")
    print("====================================\n")
    
    while True:
        pregunta = input("Tu pregunta: ")
        
        if pregunta.lower() == "salir":
            print("Saliendo del sistema...")
            break
        
        contexto = recuperar_contexto(pregunta)
        
        print("\n--- Contexto relevante encontrado ---")
        print(contexto)
        print("--------------------------------------\n")

# 7️⃣ Ejecutar
if __name__ == "__main__":
    iniciar_rag()
```

---

# 🎯 Qué cambió respecto al laboratorio anterior

| RAG simple          | RAG con Chroma |
| ------------------- | -------------- |
| RAM                 | Disco          |
| Embeddings manuales | Automáticos    |
| Similaridad manual  | Automática     |
| No persistente      | Persistente    |

---

# 🏁 Conclusión

Ahora tenés un:

✅ RAG persistente
✅ Base vectorial real
✅ Sin OpenAI
✅ Ejecutable desde terminal
✅ Más cercano a producción

