# Laboratorio: Sistema RAG con LLM 

## Introducción

En este laboratorio aprenderemos a crear un **sistema RAG (Retrieval-Augmented Generation)** que:

* Cargue documentos
* Genere embeddings
* Recupere información relevante
* Utilice un **LLM para generar la respuesta final**
* Permita ingresar la **API Key por consola**

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
* **input()/print()** → interfaz por consola

---

## Paso 1: Instalar dependencias

```
pip install sentence-transformers groq
```

---

## Paso 2: Importar bibliotecas

```python
from sentence_transformers import SentenceTransformer, util
from groq import Groq
```

---

## Paso 3: Configurar el modelo de embeddings

```python
modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

---

## Paso 4: Cargar documentos

```python
documentos = [
    "Python es un lenguaje de programación de alto nivel.",
    "Donald Trump ataca a Bolivia y se hace con el control de Sudamérica.",
    "Los animales son buenos y forman parte de la naturaleza."
]

embeddings_docs = modelo_embeddings.encode(documentos, convert_to_tensor=True)
```

---

## Paso 5: Función de recuperación de contexto

```python
def recuperar_contexto(pregunta, top_k=2):
    embedding_pregunta = modelo_embeddings.encode(pregunta, convert_to_tensor=True)
    resultados = util.cos_sim(embedding_pregunta, embeddings_docs)[0]
    top_indices = resultados.topk(top_k).indices
    return "\n".join([documentos[i] for i in top_indices])
```

---

## Paso 6: Generar respuesta con el LLM

```python
from openai import OpenAI
import os

def generar_respuesta_llm(contexto, pregunta, api_key):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    prompt = f"""
Usa el siguiente contexto para responder la pregunta.

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta:
""".strip()

    response = client.responses.create(
        model="llama3-8b-8192",
        input=prompt,
    )

    return response.output_text
```

---

## Paso 7: Función principal del RAG

```python
def consulta_rag(api_key, pregunta):
    contexto = recuperar_contexto(pregunta)
    respuesta_llm = generar_respuesta_llm(contexto, pregunta, api_key)
    return contexto, respuesta_llm
```

---

## Paso 8: Loop de interacción por consola

```python
def main():
    print("=== Sistema RAG con LLM (Groq) ===\n")
    api_key = input("Ingresá tu Groq API Key: ").strip()

    while True:
        pregunta = input("\nPregunta (o 'salir' para terminar): ").strip()
        if pregunta.lower() == "salir":
            print("Chau!")
            break

        contexto, respuesta = consulta_rag(api_key, pregunta)

        print("\n--- Contexto recuperado ---")
        print(contexto)
        print("\n--- Respuesta del modelo ---")
        print(respuesta)


if __name__ == "__main__":
    main()
```

---

## Ejemplo de ejecución

Usando los documentos definidos, se podrían hacer estas consultas:

| Pregunta   | Documento seleccionado                                               | Explicación                                                |
| ---------- | ---------------------------------------------------------------------| ----------------------------------------------------------|
| software   | Python es un lenguaje de programación de alto nivel                  | "software" se relaciona con programación y Python          |
| politica   | Donald Trump ataca a Bolivia y se hace con el control de Sudamérica  | "politica" está asociada a gobierno y control de países    |
| naturaleza | Los animales son buenos                                              | "naturaleza" se relaciona con animales y entorno natural   |

El sistema:

1. Busca documentos relevantes usando **embeddings**
2. Envía esos documentos como **contexto al LLM**
3. El LLM genera una **respuesta basada en ese contexto**

---

## Código completo

```python
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
    embedding_pregunta = modelo_embeddings.encode(pregunta, convert_to_tensor=True)
    resultados = util.cos_sim(embedding_pregunta, embeddings_docs)[0]
    top_indices = resultados.topk(top_k).indices
    return "\n".join([documentos[i] for i in top_indices])


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
        messages=[{"role": "user", "content": prompt}]
    )

    return respuesta.choices[0].message.content


def consulta_rag(api_key, pregunta):
    contexto = recuperar_contexto(pregunta)
    respuesta_llm = generar_respuesta_llm(contexto, pregunta, api_key)
    return contexto, respuesta_llm


def main():
    print("=== Sistema RAG con LLM (Groq) ===\n")
    api_key = input("Ingresá tu Groq API Key: ").strip()

    while True:
        pregunta = input("\nPregunta (o 'salir' para terminar): ").strip()
        if pregunta.lower() == "salir":
            print("Chau!")
            break

        contexto, respuesta = consulta_rag(api_key, pregunta)

        print("\n--- Contexto recuperado ---")
        print(contexto)
        print("\n--- Respuesta del modelo ---")
        print(respuesta)


if __name__ == "__main__":
    main()
```

---

## Conclusión

Ahora tenés un **RAG completo con LLM** funcionando por consola, sin dependencias de interfaz gráfica. Este laboratorio permite:

* experimentar con **embeddings**
* entender **cómo funciona RAG**
* integrar **LLMs reales**
* practicar el patrón **input/print** para probar lógica antes de meterla en cualquier interfaz
