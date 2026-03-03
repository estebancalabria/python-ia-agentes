# 🧪 Laboratorio: Sistema RAG Básico en Consola (sin Gradio) 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema RAG (Retrieval-Augmented Generation) básico** que:

* 📄 Carga documentos
* 🔢 Genera embeddings
* 🔎 Recupera los fragmentos más relevantes según una pregunta

Todo esto usando únicamente:

* Python
* Hugging Face
* SentenceTransformers

⚠️ No usamos OpenAI ni interfaces web. Solo consola.

---

## 📋 Requisitos

* Python 3.9+
* Pip instalado
* Conocimientos básicos de Python

---

## 🔧 Paso 1: Instalar dependencias

Desde la terminal:

```bash
pip install sentence-transformers
```

---

## 📚 Paso 2: Importar bibliotecas

```python
from sentence_transformers import SentenceTransformer, util
import torch
```

---

## 💡 Paso 3: Cargar modelo de embeddings

Usaremos el modelo:

```python
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

Este modelo convierte texto en vectores numéricos (embeddings).

---

## 📄 Paso 4: Definir documentos de ejemplo

```python
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "SentenceTransformers permite generar embeddings fácilmente.",
    "Los sistemas RAG combinan recuperación de información con generación de texto."
]
```

### Generamos los embeddings:

```python
embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)
```

🔎 Aquí estamos transformando cada documento en un vector matemático.

---

## 🔍 Paso 5: Función de recuperación de contexto

Esta función:

1. Genera el embedding de la pregunta
2. Calcula similitud coseno
3. Devuelve los documentos más relevantes

```python
def recuperar_contexto(pregunta, top_k=2):
    
    # 1️⃣ Generar embedding de la pregunta
    embedding_pregunta = modelo_embeddings.encode(pregunta, convert_to_tensor=True)
    
    # 2️⃣ Calcular similitud coseno
    similitudes = util.cos_sim(embedding_pregunta, embeddings_docs)[0]
    
    # 3️⃣ Obtener los índices más similares
    top_resultados = torch.topk(similitudes, k=top_k)
    
    # 4️⃣ Construir contexto
    contexto = "\n".join([documentos[i] for i in top_resultados.indices])
    
    return contexto
```

---

## 🧠 Paso 6: Loop interactivo con input() y print()

En vez de interfaz web, creamos un bucle en consola:

```python
def iniciar_rag():
    print("====================================")
    print(" Sistema RAG Básico en Consola ")
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

## 🚀 Paso 7: Ejecutar el sistema

```python
if __name__ == "__main__":
    iniciar_rag()
```

---

# 🧩 Código Completo

```python
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util
import torch

# 1️⃣ Cargar modelo
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')

# 2️⃣ Documentos de ejemplo
documentos = [
    "Python es un lenguaje de programación muy popular.",
    "SentenceTransformers permite generar embeddings fácilmente.",
    "Los sistemas RAG combinan recuperación de información con generación de texto."
]

# 3️⃣ Generar embeddings
embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)

# 4️⃣ Función de recuperación
def recuperar_contexto(pregunta, top_k=2):
    
    embedding_pregunta = modelo_embeddings.encode(pregunta, convert_to_tensor=True)
    similitudes = util.cos_sim(embedding_pregunta, embeddings_docs)[0]
    top_resultados = torch.topk(similitudes, k=top_k)
    
    contexto = "\n".join([documentos[i] for i in top_resultados.indices])
    
    return contexto

# 5️⃣ Loop principal
def iniciar_rag():
    print("====================================")
    print(" Sistema RAG Básico en Consola ")
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

# 6️⃣ Ejecutar
if __name__ == "__main__":
    iniciar_rag()
```

---

# 🎉 Conclusión

Ahora tienes un:

✅ Sistema RAG básico
✅ 100% local
✅ Sin OpenAI
✅ Sin interfaz web
✅ Ejecutable desde terminal

Este laboratorio es ideal para entender claramente la arquitectura RAG:

1. Documentos
2. Embeddings
3. Similaridad
4. Recuperación

