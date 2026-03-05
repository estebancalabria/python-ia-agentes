# 🧪 Laboratorio: Sistema RAG con Chunks a partir de FAQ 🚀

## 📝 Introducción

En este laboratorio vamos a construir un **sistema RAG** que:

* 📄 Carga un **FAQ como un solo texto**
* 🔖 Divide el FAQ en **chunks por preguntas**
* 🔢 Genera embeddings de cada chunk
* 🔎 Recupera los fragmentos más relevantes según la pregunta del usuario

Todo **100% en Python y consola**, sin OpenAI ni interfaces web.

---

## 📋 Requisitos

* Python 3.9+
* Pip instalado
* Conocimientos básicos de Python

---

## 🔧 Paso 1: Instalar dependencias

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

## 💡 Paso 3: Definir el FAQ como un solo texto

```python
faq_texto = """
¿Qué es Python?
Python es un lenguaje de programación de alto nivel que se utiliza en muchos ámbitos.
---
¿Cómo se utiliza Python?
Python se utiliza en desarrollo web, análisis de datos, automatización, ciencia de datos, IA, y más.
---
¿Quién es Donald Trump?
Donald Trump es un político y empresario estadounidense, expresidente de Estados Unidos.
---
¿Qué animales son domésticos?
Algunos animales domésticos son gatos, perros, conejos y aves.
---
"""
```

> 📌 Cada pregunta-respuesta está separada por `---`.

---

## 💻 Paso 4: Dividir el FAQ en chunks

```python
chunks = [c.strip() for c in faq_texto.split('---') if c.strip()]
```

> Cada chunk ahora representa un fragmento individual de FAQ que podremos buscar.

---

## 💻 Paso 5: Cargar el modelo de embeddings

```python
modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
```

---

## 🔢 Paso 6: Generar embeddings de cada chunk

```python
embeddings = modelo_embeddings.encode(chunks)
```

> Cada chunk ahora es un vector numérico que permite comparar con la pregunta del usuario.

---

## 🔍 Paso 7: Recuperar los chunks relevantes

```python
# 7.1: Preguntar al usuario
pregunta = input("Ingrese su pregunta: ")

# 7.2: Generar embedding de la pregunta
embedding_pregunta = modelo_embeddings.encode(pregunta)

# 7.3: Calcular similitud coseno
similitudes = util.cos_sim(embedding_pregunta, embeddings)[0]

# 7.4: Obtener el chunk más relevante
top_resultados = torch.topk(similitudes, 1)  # Cambiar a 2 o 3 para mostrar más

# 7.5: Construir y mostrar contexto
contexto = "\n\n".join([chunks[i] for i in top_resultados.indices])

print("-------------------------------------------")
print("Contexto más relevante encontrado:")
print(contexto)
print("-------------------------------------------")
```

---

## 💻 Paso 8: Ejemplo de ejecución

| Pregunta | Chunk seleccionado                | Explicación                                  |
| -------- | --------------------------------- | -------------------------------------------- |
| Python   | ¿Qué es Python? ...               | Relaciona la palabra con programación        |
| animales | ¿Qué animales son domésticos? ... | Relaciona con fauna doméstica                |
| Trump    | ¿Quién es Donald Trump? ...       | Relaciona con política y personajes públicos |

---

## 🎉 Conclusión

Con este laboratorio ahora tenés un **sistema RAG más fino**, que:

* ✅ Trabaja con **chunks por pregunta**
* ✅ Ideal para FAQs o documentos largos
* ✅ Totalmente local y en consola
* ✅ Puede mostrar múltiples resultados usando `torch.topk`

> 💡 Tip: Podés aumentar la granularidad dividiendo cada chunk en párrafos u oraciones para búsquedas más precisas.


