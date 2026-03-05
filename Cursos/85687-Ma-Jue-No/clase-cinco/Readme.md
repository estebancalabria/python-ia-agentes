# Clase Cinco - 5 de Marzo del 2026

# Repaso

* RAG
  * Conceptos
    * Embedings: https://projector.tensorflow.org/
  * python
      * sentence-transformer
          * util ----> cos_sin
      * toch (una librerias para manejos de vectores que se usa para implementar redes neuronales)
  * Bases de Datos Vectoriales
      * Faiss
      * ChromaDB
      * Postgres
          * Supabase
      * Azure : Cognitive Search

# Colab de la clase

> https://colab.research.google.com/drive/1gz8lk-7xrB5GgSval1IhLm2T5f4C2bq1?usp=sharing

# Uso de API

* Temperatura : Valor que se le puede pasar al llm para controlar cuan creativo (Probabilidad)
  * 0 : Practicamente deterministico, siempre responde igual
     * Generalmente para chatbots enterprise si quiero previsibilidad en la respuestas se usan temperaturas bajas 0.1
  * 2 : Super creativo
* TopP : Determina la cantidad de palabras posibles a elegir (Cantidad de palabras posibles)
  * 0 : Elije 1 sola palabria posible siguiente
  * 1 : Muchas proximas paalabras posible

# Links Utiles

* https://gallantlab.org/viewer-huth-2016/

---

# Rag

## Buenas Practicas

* A la hora de armar un RAG es muy comun tener un documento con FAQ de respuestas conocidas, esperadas, deseables de como respode el agente
* Hay que estudiar como dividir un documento grade en chunks que tengan sentidos
   * Como referencia que cada chunk tenga alrededor de 500 palabras
   * Cada chunk en lo posible tiene que ser autocontenido y tener sentido
   * IDEA: Por ejemplo usando la IA para generar los chunks
* Preprocesar el documento para ordenarlo y eliminar, caraceres especiales, html residual, salto de linea invalidos

## Chunks

El siguiente ejemplo maneja Chunks

```python
from sentence_transformers import SentenceTransformer, util
import torch

faq_texto = """
¿Que es Python?
Python es un lenguaje de programación de alto nivel
---
¿Donde se utilizar Python?
Python se utiliza en una amplia variedad de aplicaciones
---
¿A quien ataco Trump?
Donald Trump ataca a Bolivia y se hace con el control de Suamerica
---
¿Que animales son domesticos?
Los animales son buenos y los domesticos son perros, gatos, aves y conejos
"""

chunks = [chunk.strip() for chunk in faq_texto.strip().split('---')]
print(chunks)

print("---------------------------------------------")

modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = modelo_embeddings.encode(chunks)

pregunta = input("Ingrese su pregunta:")

embedding_pregunta = modelo_embeddings.encode(pregunta)

similitudes = util.cos_sim(embedding_pregunta, embeddings)[0]
top_resultados = torch.topk(similitudes, 1)
contexto = "\n".join([chunks[i] for i in top_resultados.indices])

print("-------------------------------------------")
print(contexto)


#print(embeddings);
#print(embedding_pregunta)
```

## Ejemplo con gradio donde Claude se lucio y se mando alto codigo...

```python
from sentence_transformers import SentenceTransformer, util
import torch
import gradio as gr

# ─── Base de conocimiento FAQ ────────────────────────────────────────────────
faq_texto = """
¿Que es Python?
Python es un lenguaje de programación de alto nivel
---
¿Donde se utilizar Python?
Python se utiliza en una amplia variedad de aplicaciones
---
¿A quien ataco Trump?
Donald Trump ataca a Bolivia y se hace con el control de Suamerica
---
¿Que animales son domesticos?
Los animales son buenos y los domesticos son perros, gatos, aves y conejos
"""

# ─── Pre-procesamiento y embeddings ─────────────────────────────────────────
chunks = [chunk.strip() for chunk in faq_texto.strip().split("---")]

print("Cargando modelo de embeddings...")
modelo = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings_base = modelo.encode(chunks, convert_to_tensor=True)
print("Modelo cargado. Chunks indexados:", len(chunks))


# ─── Lógica de búsqueda ───────────────────────────────────────────────────────
def buscar_respuesta(pregunta: str, top_k: int = 1):
    if not pregunta.strip():
        return "⚠️ Por favor ingresá una pregunta.", "", 0.0

    embedding_pregunta = modelo.encode(pregunta, convert_to_tensor=True)
    similitudes = util.cos_sim(embedding_pregunta, embeddings_base)[0]
    top_resultado = torch.topk(similitudes, k=min(top_k, len(chunks)))

    score = float(top_resultado.values[0])
    idx = int(top_resultado.indices[0])
    contexto = chunks[idx]

    # Formatear resultado
    lineas = contexto.split("\n")
    if len(lineas) >= 2:
        pregunta_faq = lineas[0].strip()
        respuesta_faq = "\n".join(lineas[1:]).strip()
    else:
        pregunta_faq = "Resultado encontrado"
        respuesta_faq = contexto

    score_pct = round(score * 100, 1)

    # Construir resultado HTML enriquecido
    color = "#22c55e" if score > 0.6 else "#f59e0b" if score > 0.35 else "#ef4444"
    label = "Alta" if score > 0.6 else "Media" if score > 0.35 else "Baja"

    resultado_html = f"""
    <div style="
        font-family: 'Georgia', serif;
        background: #1a1a2e;
        border: 1px solid #2d2d4e;
        border-radius: 12px;
        padding: 24px;
        margin-top: 8px;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <span style="color: #a78bfa; font-size: 13px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;">
                📚 Resultado encontrado
            </span>
            <span style="
                background: {color}22;
                color: {color};
                border: 1px solid {color}55;
                padding: 3px 10px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 700;
            ">
                Similitud {label}: {score_pct}%
            </span>
        </div>
        <div style="
            color: #c4b5fd;
            font-size: 15px;
            font-style: italic;
            margin-bottom: 12px;
            padding-bottom: 12px;
            border-bottom: 1px solid #2d2d4e;
        ">
            {pregunta_faq}
        </div>
        <div style="
            color: #e2e8f0;
            font-size: 15px;
            line-height: 1.7;
        ">
            {respuesta_faq}
        </div>
    </div>
    """

    return resultado_html, contexto, score_pct


def interfaz_principal(pregunta):
    resultado_html, contexto_raw, score = buscar_respuesta(pregunta)
    return resultado_html


def listar_chunks():
    items = ""
    for i, c in enumerate(chunks):
        lineas = c.split("\n")
        titulo = lineas[0].strip() if lineas else f"Chunk {i+1}"
        items += f"<div style='padding: 8px 12px; border-left: 3px solid #7c3aed; margin-bottom: 8px; color: #a78bfa; font-size: 13px;'>{i+1}. {titulo}</div>"
    return f"""
    <div style='background:#1a1a2e; border-radius:10px; padding:16px; font-family:Georgia,serif;'>
        <p style='color:#64748b; font-size:12px; margin-bottom:12px;'>BASE DE CONOCIMIENTO — {len(chunks)} entradas indexadas</p>
        {items}
    </div>
    """


# ─── Interfaz Gradio ──────────────────────────────────────────────────────────
css = """
body, .gradio-container {
    background: #0f0f1a !important;
    font-family: 'Georgia', serif !important;
}
.gradio-container {
    max-width: 860px !important;
    margin: 0 auto !important;
}
#titulo {
    text-align: center;
    padding: 32px 0 8px;
}
#titulo h1 {
    font-size: 2.4rem;
    background: linear-gradient(135deg, #a78bfa, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
}
#titulo p {
    color: #64748b;
    font-size: 14px;
    font-style: italic;
}
.label {
    color: #a78bfa !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}
textarea, input[type="text"] {
    background: #1a1a2e !important;
    border: 1px solid #2d2d4e !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
    font-family: 'Georgia', serif !important;
    font-size: 15px !important;
}
textarea:focus, input[type="text"]:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 2px #7c3aed33 !important;
}
button.primary {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    border: none !important;
    border-radius: 10px !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 12px 24px !important;
    transition: opacity 0.2s !important;
}
button.primary:hover {
    opacity: 0.88 !important;
}
.tabs button {
    color: #64748b !important;
}
.tabs button.selected {
    color: #a78bfa !important;
    border-bottom-color: #7c3aed !important;
}
"""

with gr.Blocks(css=css, title="FAQ Semántico") as demo:

    gr.HTML("""
    <div id="titulo">
        <h1>🔍 FAQ Semántico</h1>
        <p>Búsqueda por similitud usando sentence-transformers · all-MiniLM-L6-v2</p>
    </div>
    """)

    with gr.Tabs():
        with gr.Tab("💬 Consultar"):
            with gr.Row():
                with gr.Column(scale=4):
                    pregunta_input = gr.Textbox(
                        placeholder="Ej: ¿Para qué sirve Python?",
                        label="Tu pregunta",
                        lines=2,
                        elem_id="input-pregunta"
                    )
                with gr.Column(scale=1, min_width=120):
                    buscar_btn = gr.Button("Buscar →", variant="primary")

            resultado_output = gr.HTML(label="Resultado")

            gr.Examples(
                examples=[
                    ["¿Qué es Python?"],
                    ["¿Qué mascotas puedo tener?"],
                    ["¿Dónde se usa Python?"],
                    ["¿Qué hizo Trump?"],
                ],
                inputs=pregunta_input,
                label="Ejemplos rápidos",
            )

        with gr.Tab("📚 Base de conocimiento"):
            base_html = gr.HTML(value=listar_chunks())

    buscar_btn.click(
        fn=interfaz_principal,
        inputs=pregunta_input,
        outputs=resultado_output
    )
    pregunta_input.submit(
        fn=interfaz_principal,
        inputs=pregunta_input,
        outputs=resultado_output
    )

if __name__ == "__main__":
    demo.launch()
```

## Base de Datos Vectoriales

Instalando librerias
```python
!pip install faiss-cpu
```

Utilizando Indice Vectorial
```python
from sentence_transformers import SentenceTransformer, util
import torch
import faiss

faq_texto = """
¿Que es Python?
Python es un lenguaje de programación de alto nivel
---
¿Donde se utilizar Python?
Python se utiliza en una amplia variedad de aplicaciones
---
¿A quien ataco Trump?
Donald Trump ataca a Bolivia y se hace con el control de Suamerica
---
¿Que animales son domesticos?
Los animales son buenos y los domesticos son perros, gatos, aves y conejos
"""

chunks = [chunk.strip() for chunk in faq_texto.strip().split('---')]

modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = modelo_embeddings.encode(chunks)

dimension_embedding = embeddings.shape[1];
tabla_embeddings = faiss.IndexFlatL2(dimension_embedding)
tabla_embeddings.add(embeddings)

pregunta = input("Escriba su pregunta:")
embedding_pregunta = modelo_embeddings.encode([pregunta]);

distancia, indice = tabla_embeddings.search(embedding_pregunta,1)
#print(indice)

print("Documento recuperado")
print(chunks[indice[0][0]])
print("Distancia a la pregunta:");
print(distancia);

```

## Persistiendo la base de datos

* Celda 1 : Los documentos en memoria (en realidad van en disco pero los hacemos en memoria para simplificar)
```python
# Para tener los documentos en memoria
from sentence_transformers import SentenceTransformer, util
import torch
import faiss

faq_texto = """
¿Que es Python?
Python es un lenguaje de programación de alto nivel
---
¿Donde se utilizar Python?
Python se utiliza en una amplia variedad de aplicaciones
---
¿A quien ataco Trump?
Donald Trump ataca a Bolivia y se hace con el control de Suamerica
---
¿Que animales son domesticos?
Los animales son buenos y los domesticos son perros, gatos, aves y conejos
"""

chunks = [chunk.strip() for chunk in faq_texto.strip().split('---')]
```

* Celda 2 : Creo el archivo fisico persistente
```python
#PAra generar la tabla de embedings persistente
modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = modelo_embeddings.encode(chunks)

dimension_embedding = embeddings.shape[1];
tabla_embeddings = faiss.IndexFlatL2(dimension_embedding)
tabla_embeddings.add(embeddings)

faiss.write_index(tabla_embeddings, "tabla_embeddings.index")
```

* Celda 3 : Levanto el indice de disco
```python
indice_recuperado = faiss.read_index("tabla_embeddings.index")

pregunta = input("Escriba su pregunta:")
embedding_pregunta = modelo_embeddings.encode([pregunta]);

distancia, indice = indice_recuperado.search(embedding_pregunta,1)
#print(indice)

print("Documento recuperado")
print(chunks[indice[0][0]])
print("Distancia a la pregunta:");
print(distancia);
```
