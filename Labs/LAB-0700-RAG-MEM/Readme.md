# 🧪 Laboratorio: Sistema RAG Básico en Memoria 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema RAG (Retrieval-Augmented Generation) básico** que:

* 📄 Carga documentos
* 🔢 Genera embeddings
* 🔎 Recupera los fragmentos más relevantes según una pregunta del usuario

Todo esto usando únicamente:

* Python
* Hugging Face
* SentenceTransformers

⚠️ Sin OpenAI ni interfaces web, solo consola.

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

## 💡 Paso 3: Definir documentos de ejemplo

Estos son los textos que nuestro sistema podrá consultar:

```python
documentos = [
    "Python es un lenguaje de programación de alto nivel",
    "Python se utiliza en una amplia variedad de aplicaciones",
    "Donald Trump ataca a Bolivia y se hace con el control de Suamerica",
    "Los animales son buenos"
]
```

---

## 💻 Paso 4: Cargar el modelo de embeddings

El modelo `all-MiniLM-L6-v2` convierte cada texto en un vector numérico que podemos comparar matemáticamente:

```python
modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
```

---

## 🔢 Paso 5: Generar embeddings de los documentos

```python
embeddings = modelo_embeddings.encode(documentos)
```

> ⚡ Cada documento ahora es un **vector numérico**. Esto nos permite medir qué tan similares son los documentos entre sí o respecto a una pregunta.

---

## 🔍 Paso 6: Recuperación de documentos relevantes

Dividimos este proceso en **subpasos** para mayor claridad:

### 6.1: Pedir la pregunta al usuario

```python
pregunta = input("Ingrese su pregunta: ")
```

### 6.2: Convertir la pregunta en embedding

```python
embedding_pregunta = modelo_embeddings.encode(pregunta)
```

> 🧠 Ahora tenemos un vector que representa la semántica de la pregunta.

### 6.3: Calcular similitud coseno

```python
similitudes = util.cos_sim(embedding_pregunta, embeddings)[0]
```

> 📊 La similitud coseno mide cuán parecida es la pregunta a cada documento. Va de -1 (totalmente diferente) a 1 (idéntico).

### 6.4: Obtener el documento más relevante

```python
top_resultados = torch.topk(similitudes, 1)
```

> 🏆 `torch.topk` nos devuelve el índice del documento con mayor similitud.

### 6.5: Construir y mostrar el contexto

```python
contexto = "\n".join([documentos[i] for i in top_resultados.indices])

print("-------------------------------------------")
print("Contexto más relevante encontrado:")
print(contexto)
print("-------------------------------------------")
```

> ✅ Ahora vemos en consola el fragmento más relevante para nuestra pregunta.

---

## 💻 Paso 7: Ejemplo de ejecución

Usando los documentos definidos, se podrían hacer estas consultas:

| Pregunta   | Documento seleccionado                                             | Explicación                                                |
| ---------- | ------------------------------------------------------------------ | ---------------------------------------------------------- |
| software   | Python es un lenguaje de programación de alto nivel                | `"software"` se relaciona con programación y Python        |
| politica   | Donald Trump ataca a Bolivia y se hace con el control de Suamerica | `"politica"` está asociada a gobierno y control de países  |
| naturaleza | Los animales son buenos                                            | `"naturaleza"` se relaciona con animales y entorno natural |

---

## 🧩 Código Completo Actualizado

```python
from sentence_transformers import SentenceTransformer, util
import torch

# Documentos
documentos = [
    "Python es un lenguaje de programación de alto nivel",
    "Python se utiliza en una amplia variedad de aplicaciones",
    "Donald Trump ataca a Bolivia y se hace con el control de Suamerica",
    "Los animales son buenos"
]

# Cargar modelo de embeddings
modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generar embeddings de los documentos
embeddings = modelo_embeddings.encode(documentos)

# Paso 6: Recuperación de documentos relevantes
pregunta = input("Ingrese su pregunta:")

# 6.2 Generar embedding de la pregunta
embedding_pregunta = modelo_embeddings.encode(pregunta)

# 6.3 Calcular similitud coseno
similitudes = util.cos_sim(embedding_pregunta, embeddings)[0]

# 6.4 Obtener el documento más relevante
top_resultados = torch.topk(similitudes, 1)

# 6.5 Construir y mostrar contexto
contexto = "\n".join([documentos[i] for i in top_resultados.indices])

print("-------------------------------------------")
print("Contexto más relevante encontrado:")
print(contexto)
print("-------------------------------------------")
```

---

## 🎉 Conclusión

Con este laboratorio ahora tienes un **sistema RAG básico en consola**:

* ✅ Local y simple
* ✅ 100% en Python
* ✅ Sin OpenAI ni interfaz web
* ✅ Didáctico paso a paso

> 💡 Tip: Puedes aumentar `top_k` si quieres mostrar más de un documento relevante. Por ejemplo, `torch.topk(similitudes, 2)` mostrará los dos más relevantes.
