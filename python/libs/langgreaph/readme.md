# LangGraph — Asistente de soporte técnico con RAG

Ejemplo práctico de un **workflow agentic con LangGraph y un LLM**.

El escenario es un asistente de soporte técnico para una aplicación empresarial. El usuario realiza una consulta y el sistema:

1. Analiza la consulta con un LLM.
2. Decide si necesita consultar documentación.
3. Busca información en una base de conocimiento.
4. Genera la respuesta final utilizando el contexto recuperado.

## Arquitectura

```text
                         Usuario
                            │
                            ▼
                    ┌───────────────┐
                    │    Analizar   │
                    │    consulta   │
                    │      LLM      │
                    └───────┬───────┘
                            │
                     ¿Necesita RAG?
                       /          \
                     Sí            No
                     │              │
                     ▼              │
              ┌──────────────┐      │
              │    Buscar    │      │
              │ documentación│      │
              └──────┬───────┘      │
                     │              │
                     └──────┬───────┘
                            ▼
                    ┌───────────────┐
                    │    Generar    │
                    │    respuesta  │
                    │      LLM      │
                    └───────┬───────┘
                            │
                            ▼
                          Usuario
```

La parte importante es que **el flujo no es completamente lineal**.

El LLM puede decidir que una pregunta requiere información externa y enviar la ejecución hacia el nodo de búsqueda.

---

# Ejemplo

El usuario pregunta:

> ¿Cómo puedo restablecer la contraseña de un usuario en Azure?

El sistema podría ejecutar:

```text
Usuario
   ↓
Analizar consulta
   ↓
¿Necesita documentación?
   ↓
   Sí
   ↓
Buscar documentación
   ↓
Generar respuesta
   ↓
Usuario
```

Para una pregunta como:

> ¿Qué es Azure?

podría ejecutar:

```text
Usuario
   ↓
Analizar consulta
   ↓
¿Necesita documentación?
   ↓
   No
   ↓
Generar respuesta
   ↓
Usuario
```

Esto es lo que empieza a diferenciar un workflow agentic de una simple cadena.

---

# Implementación

## Dependencias

```bash
pip install langgraph langchain-openai
```

Definir la variable de entorno:

```bash
OPENAI_API_KEY=your_api_key
```

---

## Código

```python
from typing import Literal, TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    pregunta: str
    necesita_documentacion: bool
    contexto: str
    respuesta: str


llm = ChatOpenAI(
    model="gpt-5",
    temperature=0
)


def analizar_consulta(state: State):
    """
    El LLM determina si la pregunta requiere
    información de la documentación interna.
    """

    prompt = f"""
Analiza esta consulta de soporte técnico:

{state["pregunta"]}

Determina si para responder correctamente
es necesario consultar documentación interna.

Responde solamente:
SI
o
NO
"""

    response = llm.invoke(prompt)

    necesita_documentacion = response.content.strip().upper() == "SI"

    return {
        "necesita_documentacion": necesita_documentacion
    }


def decidir_siguiente_paso(
    state: State
) -> Literal["buscar_documentacion", "generar_respuesta"]:

    if state["necesita_documentacion"]:
        return "buscar_documentacion"

    return "generar_respuesta"


def buscar_documentacion(state: State):
    """
    Simulación de una búsqueda en una base de conocimiento.

    En una aplicación real este nodo podría consultar:
    - Azure AI Search
    - PostgreSQL + pgvector
    - Elasticsearch
    - Pinecone
    - otro vector store
    """

    pregunta = state["pregunta"]

    # Simulación de resultados recuperados.
    contexto = f"""
Documentación interna relacionada con:

{pregunta}

La documentación indica que los procedimientos
de administración deben realizarse desde el portal
correspondiente y respetando las políticas de
seguridad y permisos de la organización.
"""

    return {
        "contexto": contexto
    }


def generar_respuesta(state: State):
    """
    El LLM genera la respuesta final.
    """

    prompt = f"""
Eres un asistente de soporte técnico.

Responde la siguiente consulta:

{state["pregunta"]}

Utiliza el contexto disponible cuando exista:

{state["contexto"]}

Si el contexto no contiene información específica,
responde utilizando tus conocimientos generales.

Sé claro y conciso.
"""

    response = llm.invoke(prompt)

    return {
        "respuesta": response.content
    }


# --------------------------------------------------
# Construcción del grafo
# --------------------------------------------------

builder = StateGraph(State)

builder.add_node(
    "analizar_consulta",
    analizar_consulta
)

builder.add_node(
    "buscar_documentacion",
    buscar_documentacion
)

builder.add_node(
    "generar_respuesta",
    generar_respuesta
)


builder.add_edge(
    START,
    "analizar_consulta"
)

builder.add_conditional_edges(
    "analizar_consulta",
    decidir_siguiente_paso
)

builder.add_edge(
    "buscar_documentacion",
    "generar_respuesta"
)

builder.add_edge(
    "generar_respuesta",
    END
)


graph = builder.compile()


# --------------------------------------------------
# Ejecución
# --------------------------------------------------

resultado = graph.invoke({
    "pregunta": "¿Cómo restablezco la contraseña de un usuario?",
    "necesita_documentacion": False,
    "contexto": "",
    "respuesta": ""
})


print("\n--- RESPUESTA ---")
print(resultado["respuesta"])
```

# ¿Qué está haciendo LangGraph?

El punto importante está acá:

```python
builder.add_conditional_edges(
    "analizar_consulta",
    decidir_siguiente_paso
)
```

El workflow puede tomar diferentes caminos.

```text
                  analizar_consulta
                         │
                  ┌──────┴──────┐
                  │             │
                 Sí             No
                  │             │
                  ▼             │
          buscar_documentacion  │
                  │             │
                  └──────┬──────┘
                         ▼
                  generar_respuesta
```

El LLM participa en la decisión, pero **LangGraph controla la ejecución del workflow**.

---

# ¿Por qué no hacerlo simplemente con Python?

Podríamos escribir:

```python
if necesita_documentacion:
    contexto = buscar_documentacion()

respuesta = generar_respuesta()
```

Y para un flujo pequeño probablemente sería suficiente.

La ventaja de LangGraph aparece cuando el workflow empieza a crecer:

```text
                     ┌─────────────┐
                     │    Router   │
                     └──────┬──────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
             RAG          Tool          SQL
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                           LLM
                            │
                     ¿Necesita otra
                        acción?
                       /       \
                     Sí         No
                     │           │
                     └──→ Tool   ▼
                              Response
```

Ahí LangGraph permite representar explícitamente:

* **State**
* **Nodes**
* **Conditional routing**
* **Loops**
* **Tool execution**
* **Human-in-the-loop**
* **Persistencia/checkpoints**

## Concepto clave

LangGraph no es el LLM.

El LLM realiza tareas como:

```text
analizar
razonar
clasificar
generar
```

LangGraph se ocupa de **orquestar qué ocurre antes, después y según el resultado de esas operaciones**.

La diferencia conceptual es:

```text
LLM:
"¿Qué debería hacer?"

LangGraph:
"¿Qué nodo ejecuto ahora y hacia dónde continúa el workflow?"
```

Ese es el motivo por el que LangGraph resulta especialmente útil para construir aplicaciones **agentic** más complejas que una simple llamada a una API de LLM.
