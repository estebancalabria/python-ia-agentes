# Laboratorio: Sistema RAG con LLM y Gradio 🤖

## Introducción 📝

En este laboratorio aprenderemos a crear un **sistema RAG (Retrieval-Augmented Generation)** que:

* Cargue documentos
* Genere embeddings
* Recupere información relevante
* Utilice un **LLM para generar la respuesta final**
* Permita ingresar la **API Key desde la interfaz**

El flujo será:

```
Pregunta del usuario
      ↓
Generar embedding
      ↓
Buscar documentos relevantes
      ↓
Enviar contexto + pregunta al LLM
      ↓
Generar respuesta final
```

Usaremos:

* **Sentence Transformers** → embeddings
* **Groq + Llama 3** → generación de respuesta
* **Gradio** → interfaz web

---

# Paso 1: Configurar el Entorno 🔧

```python
!pip install gradio
!pip install sentence-transformers
!pip install groq
```

---

# Paso 2: Importar Bibliotecas 📚

```python
import gradio as gr
from sentence_transformers import SentenceTransformer, util
from groq import Groq
```

---

# Paso 3: Configurar el Modelo de Embeddings 💡

```python
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

---

# Paso 4: Cargar Documentos 📄

```python
documentos = [
    "Python es un lenguaje de programación de alto nivel.",
    "Donald Trump ataca a Bolivia y se hace con el control de Sudamérica.",
    "Los animales son buenos y forman parte de la naturaleza."
]

embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)
```

---

# Paso 5: Función de Recuperación de Contexto 🔍

```python
def recuperar_contexto(pregunta, top_k=2):

    embedding_pregunta = modelo_embeddings.encode(
        pregunta,
        convert_to_tensor=True
    )

    resultados = util.cos_sim(
        embedding_pregunta,
        embeddings_docs
    )[0]

    top_indices = resultados.topk(top_k).indices

    contexto = "\n".join(
        [documentos[i] for i in top_indices]
    )

    return contexto
```

---

# Paso 6: Generar Respuesta con el LLM 🧠

```python
def generar_respuesta_llm(contexto, pregunta, api_key):

    cliente = Groq(api_key=api_key)

    prompt = f"""
Usa el siguiente contexto para responder la pregunta.

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta:
"""

    respuesta = cliente.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return respuesta.choices[0].message.content
```

---

# Paso 7: Función Principal del RAG 🚀

```python
def consulta_rag(api_key, pregunta):

    contexto = recuperar_contexto(pregunta)

    respuesta_llm = generar_respuesta_llm(
        contexto,
        pregunta,
        api_key
    )

    return f"""
Contexto recuperado:

{contexto}

Respuesta del modelo:

{respuesta_llm}
"""
```

---

# Paso 8: Crear Interfaz con Gradio 🌐

Aquí agregamos un **input para la API Key**.

```python
interfaz = gr.Interface(
    fn=consulta_rag,
    inputs=[
        gr.Textbox(
            label="Groq API Key",
            type="password"
        ),
        gr.Textbox(
            label="Pregunta"
        )
    ],
    outputs="text",
    title="Sistema RAG con LLM",
    description="Introduce tu API Key de Groq y una pregunta. El sistema buscará información relevante y generará una respuesta usando un LLM."
)
```

---

# Paso 9: Lanzar la Interfaz 🚀

```python
interfaz.launch()
```

---

# Paso 7: Ejemplo de ejecución

Usando los documentos definidos, se podrían hacer estas consultas:

| Pregunta   | Documento seleccionado                                              | Explicación                                              |
| ---------- | ------------------------------------------------------------------- | -------------------------------------------------------- |
| software   | Python es un lenguaje de programación de alto nivel                 | "software" se relaciona con programación y Python        |
| politica   | Donald Trump ataca a Bolivia y se hace con el control de Sudamérica | "politica" está asociada a gobierno y control de países  |
| naturaleza | Los animales son buenos                                             | "naturaleza" se relaciona con animales y entorno natural |

El sistema:

1️⃣ Busca documentos relevantes usando **embeddings**
2️⃣ Envía esos documentos como **contexto al LLM**
3️⃣ El LLM genera una **respuesta basada en ese contexto**

---

# Código Completo 🧩

```python
!pip install gradio
!pip install sentence-transformers
!pip install groq

import gradio as gr
from sentence_transformers import SentenceTransformer, util
from groq import Groq

modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')

documentos = [
    "Python es un lenguaje de programación de alto nivel.",
    "Donald Trump ataca a Bolivia y se hace con el control de Sudamérica.",
    "Los animales son buenos y forman parte de la naturaleza."
]

embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)


def recuperar_contexto(pregunta, top_k=2):

    embedding_pregunta = modelo_embeddings.encode(
        pregunta,
        convert_to_tensor=True
    )

    resultados = util.cos_sim(
        embedding_pregunta,
        embeddings_docs
    )[0]

    top_indices = resultados.topk(top_k).indices

    contexto = "\n".join(
        [documentos[i] for i in top_indices]
    )

    return contexto


def generar_respuesta_llm(contexto, pregunta, api_key):

    cliente = Groq(api_key=api_key)

    prompt = f"""
Usa el siguiente contexto para responder la pregunta.

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta:
"""

    respuesta = cliente.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return respuesta.choices[0].message.content


def consulta_rag(api_key, pregunta):

    contexto = recuperar_contexto(pregunta)

    respuesta_llm = generar_respuesta_llm(
        contexto,
        pregunta,
        api_key
    )

    return f"""
Contexto recuperado:

{contexto}

Respuesta del modelo:

{respuesta_llm}
"""


interfaz = gr.Interface(
    fn=consulta_rag,
    inputs=[
        gr.Textbox(label="Groq API Key", type="password"),
        gr.Textbox(label="Pregunta")
    ],
    outputs="text",
    title="Sistema RAG con LLM",
    description="Introduce tu API Key de Groq y una pregunta."
)

interfaz.launch()
```

---

## Conclusión 🎉

¡Ahora tienes un **RAG completo con LLM**!

Este laboratorio permite:

* experimentar con **embeddings**
* entender **cómo funciona RAG**
* integrar **LLMs reales**
* usar **Gradio para crear una interfaz**

Y además cada usuario puede **ingresar su propia API Key desde la interfaz**, ideal para laboratorios en clase. 🚀

