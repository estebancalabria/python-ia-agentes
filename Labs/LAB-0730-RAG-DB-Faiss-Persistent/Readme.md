# 🧠 Laboratorio: RAG con FAISS Persistente (2 Celdas)

Usaremos:

* SentenceTransformers
* FAISS

Todo local. Sin nube. Sin OpenAI.

---

# 📦 Requisitos

```bash
pip install sentence-transformers faiss-cpu numpy
```

---

# 🧱 CELDA 1 — Indexar todos los documentos de `/data/`

⚠️ Esta celda se ejecuta solo cuando:

* Agregás nuevos archivos
* O querés regenerar la base

---

```python
# ======================================
# CELDA 1 - INDEXACIÓN DE DOCUMENTOS
# ======================================

import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# 📌 Carpeta con documentos
DATA_PATH = "data"
INDEX_PATH = "faiss.index"
DOCS_PATH = "documentos.npy"

# 1️⃣ Cargar modelo de embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# 2️⃣ Leer todos los archivos .txt de la carpeta /data
documentos = []

for archivo in os.listdir(DATA_PATH):
    if archivo.endswith(".txt"):
        with open(os.path.join(DATA_PATH, archivo), "r", encoding="utf-8") as f:
            contenido = f.read()
            documentos.append(contenido)

print(f"Se cargaron {len(documentos)} documentos.")

# 3️⃣ Generar embeddings
embeddings = modelo.encode(documentos, convert_to_numpy=True)

# 4️⃣ Crear índice FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 5️⃣ Guardar índice en disco
faiss.write_index(index, INDEX_PATH)

# 6️⃣ Guardar documentos para recuperarlos luego
np.save(DOCS_PATH, np.array(documentos, dtype=object))

print("Indexación completada y guardada en disco.")
```

---

## 🔎 ¿Qué hace esta celda?

* Lee todos los `.txt` de `/data`
* Genera embeddings
* Crea índice FAISS
* Guarda:

  * `faiss.index`
  * `documentos.npy`

Es equivalente a un proceso batch nocturno en producción.

---

# ⚡ CELDA 2 — Cargar Base y Consultar

⚠️ Esta celda simula el servidor RAG que responde preguntas.

---

```python
# ======================================
# CELDA 2 - CONSULTA RAG
# ======================================

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "faiss.index"
DOCS_PATH = "documentos.npy"

# 1️⃣ Verificar que exista el índice
if not (os.path.exists(INDEX_PATH) and os.path.exists(DOCS_PATH)):
    raise Exception("No existe la base vectorial. Ejecutar primero la Celda 1.")

# 2️⃣ Cargar modelo
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# 3️⃣ Cargar índice y documentos
index = faiss.read_index(INDEX_PATH)
documentos = np.load(DOCS_PATH, allow_pickle=True)

print("Base vectorial cargada correctamente.")

# 4️⃣ Función de recuperación
def recuperar_contexto(pregunta, top_k=3):
    embedding = modelo.encode([pregunta], convert_to_numpy=True)
    D, I = index.search(embedding, top_k)
    contexto = "\n\n".join([documentos[i] for i in I[0]])
    return contexto


# 5️⃣ Loop interactivo
while True:
    pregunta = input("\nEscribe tu pregunta ('salir' para terminar): ")
    
    if pregunta.lower() == "salir":
        print("Finalizando sesión.")
        break
    
    contexto = recuperar_contexto(pregunta)
    
    print("\n--- Contexto recuperado ---")
    print(contexto)
    print("----------------------------")
```

---

# 🎓 ¿Por qué esta arquitectura es mejor?

Porque separa claramente:

| Fase       | Qué hace           | Frecuencia |
| ---------- | ------------------ | ---------- |
| Indexación | Procesa documentos | Ocasional  |
| Consulta   | Responde preguntas | Constante  |

Así funcionan:

* Sistemas corporativos
* Chatbots empresariales
* Motores de búsqueda internos

---

# 🔥 Qué estás enseñando realmente acá

Sin decirlo explícitamente, este laboratorio muestra:

* Persistencia en FAISS
* Arquitectura real de RAG
* Separación offline / online
* Base vectorial en disco
* Escalabilidad conceptual

Está varios niveles arriba de un RAG demo típico.

