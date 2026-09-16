# LLM APIs: Direct SDK vs LangChain

Ejemplo práctico de integración con modelos de lenguaje utilizando directamente las APIs de los proveedores y utilizando **LangChain** como capa de abstracción.

El objetivo es mostrar la diferencia entre ambos enfoques y entender qué aporta LangChain sobre una integración directa.

## Estructura

```text
.
├── direct/
│   ├── openai.py
│   └── groq.py
├── langchain/
│   ├── openai.py
│   └── groq.py
├── requirements.txt
└── README.md
```

## 1. OpenAI directamente

La integración directa utiliza el SDK oficial de OpenAI:

```python
from openai import OpenAI

client = OpenAI(api_key="...")

response = client.responses.create(
    model="gpt-5",
    input="Explicame qué es RAG"
)

print(response.output_text)
```

En este enfoque la aplicación trabaja directamente con la API del proveedor.

---

## 2. Groq directamente

Groq ofrece una API compatible con el SDK de OpenAI, por lo que podemos utilizar el cliente de OpenAI apuntando al endpoint de Groq:

```python
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explicame qué es RAG"
        }
    ]
)

print(response.choices[0].message.content)
```

La estructura de la llamada es similar a la utilizada con OpenAI porque Groq implementa una API compatible.

---

# 3. OpenAI utilizando LangChain

LangChain proporciona una abstracción común para interactuar con diferentes proveedores:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-5",
    api_key="..."
)

response = llm.invoke(
    "Explicame qué es RAG"
)

print(response.content)
```

La aplicación deja de trabajar directamente con el SDK de OpenAI y utiliza la interfaz de LangChain.

---

# 4. Groq utilizando LangChain

Para Groq podemos utilizar la integración correspondiente de LangChain:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="..."
)

response = llm.invoke(
    "Explicame qué es RAG"
)

print(response.content)
```

La llamada desde la aplicación mantiene una interfaz muy similar a la utilizada con otros modelos compatibles con LangChain.

---

# Comparación

## Sin LangChain

```text
                    ┌──────────────┐
                    │ Aplicación   │
                    └──────┬───────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
        OpenAI SDK              OpenAI SDK
                │                     │
                ▼                     ▼
          OpenAI API              Groq API
```

La aplicación conoce directamente la implementación del proveedor.

## Con LangChain

```text
                    ┌──────────────┐
                    │ Aplicación   │
                    └──────┬───────┘
                           │
                           ▼
                     ┌───────────┐
                     │ LangChain │
                     └─────┬─────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
           ChatOpenAI            ChatGroq
                 │                   │
                 ▼                   ▼
            OpenAI API            Groq API
```

LangChain proporciona una interfaz común y permite reutilizar componentes de la aplicación independientemente del proveedor concreto.

# ¿Qué aporta LangChain?

LangChain resulta especialmente útil cuando la aplicación necesita algo más que una llamada aislada a un modelo.

Por ejemplo:

* Prompt templates
* Structured output
* Tool calling
* RAG
* Retrievers
* Chains
* Agents
* Memory/state
* Integración con diferentes proveedores
* Integración con vector stores
* Observabilidad y trazabilidad mediante el ecosistema de LangChain

Para una aplicación sencilla como:

```text
Prompt → LLM → Response
```

una llamada directa a la API puede ser suficiente.

Para una arquitectura más compleja:

```text
User
 ↓
Router
 ↓
Retriever
 ↓
LLM
 ↓
Tool
 ↓
LLM
 ↓
Response
```

una capa de abstracción y orquestación puede resultar más conveniente.

# Filosofía del ejemplo

Este proyecto no plantea que LangChain sea necesariamente mejor que utilizar las APIs directamente.

Son dos enfoques diferentes:

**Direct API**

* Mayor control sobre la API del proveedor.
* Menos abstracciones.
* Dependencia directa del SDK/API utilizado.
* Adecuado cuando se necesita controlar explícitamente cada interacción.

**LangChain**

* Abstracción común entre proveedores.
* Componentes reutilizables para aplicaciones LLM.
* Facilita arquitecturas más complejas.
* Introduce una capa adicional sobre las APIs subyacentes.

La elección depende de la arquitectura y de las necesidades de la aplicación.

# Instalación

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

# Variables de entorno

Crear un archivo `.env`:

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
```

No incluir claves reales en el repositorio.

Agregar `.env` a `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
```

# Objetivo educativo

Este repositorio forma parte de una exploración práctica de **AI Engineering**, enfocada en comprender qué ocurre debajo de las abstracciones utilizadas por los frameworks de desarrollo con LLMs.

La intención es poder pasar de:

```text
Aplicación
    ↓
Framework
    ↓
LLM
```

a comprender también:

```text
Aplicación
    ↓
Framework / SDK
    ↓
HTTP API
    ↓
Modelo
```

Comprender ambas capas permite tomar decisiones arquitectónicas con mayor criterio y evitar depender de una abstracción sin conocer la tecnología que existe debajo.
