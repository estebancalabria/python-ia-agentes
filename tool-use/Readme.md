# Tool Use (Function Calling) con LLM

Las aplicaciones que utilizan **Modelos de Lenguaje (LLM)** se vuelven mucho más poderosas cuando el modelo puede interactuar con **recursos externos**, como:

* APIs
* Bases de datos
* Servicios web
* Sistemas internos

Esta capacidad se conoce como **Tool Use** o **Function Calling**.

Gracias a Tool Use, un modelo deja de ser solamente una **interfaz conversacional** y se convierte en un **agente capaz de ejecutar acciones**, acceder a información en tiempo real y resolver problemas complejos que requieren múltiples pasos.

---

# Cómo funciona Tool Use

El proceso de uso de herramientas ocurre en **cuatro etapas principales**:

1. Se envía una solicitud al modelo junto con la definición de las herramientas.
2. El modelo decide si necesita usar una herramienta.
3. La aplicación ejecuta la herramienta solicitada.
4. El resultado se devuelve al modelo para generar la respuesta final.

A continuación se explica cada paso en detalle.

---

# 1. Solicitud inicial con definición de herramientas

Para que el modelo pueda usar herramientas, primero debemos **definirlas**.

Las herramientas se describen utilizando **JSON Schema** y se envían al modelo mediante el parámetro `tools`.

Ejemplo de solicitud con definición de herramienta:

```json
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "obtener_clima",
        "description": "Obtiene el clima actual de una ciudad",
        "parameters": {
          "type": "object",
          "properties": {
            "ubicacion": {
              "type": "string",
              "description": "Ciudad y país, por ejemplo Buenos Aires, Argentina"
            },
            "unidad": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["ubicacion"]
        }
      }
    }
  ],
  "messages": [
    {
      "role": "system",
      "content": "Eres un asistente meteorológico. Usa herramientas si es necesario para responder."
    },
    {
      "role": "user",
      "content": "¿Cómo está el clima en Buenos Aires?"
    }
  ]
}
```

Campos importantes:

* **name** → identificador de la función
* **description** → ayuda al modelo a decidir cuándo usar la herramienta
* **parameters** → parámetros de la función definidos con JSON Schema

---

# 2. El modelo solicita el uso de una herramienta

Si el modelo considera que necesita una herramienta para responder la pregunta, devolverá una solicitud estructurada llamada **tool call**.

Ejemplo de respuesta del modelo:

```json
{
  "role": "assistant",
  "tool_calls": [
    {
      "id": "call_abc123",
      "type": "function",
      "function": {
        "name": "obtener_clima",
        "arguments": "{\"ubicacion\": \"Buenos Aires, Argentina\", \"unidad\": \"celsius\"}"
      }
    }
  ]
}
```

Campos importantes:

* **id** → identificador único de la llamada
* **function.name** → nombre de la herramienta que se debe ejecutar
* **function.arguments** → argumentos en formato JSON (string)

En este punto, **el modelo no ejecuta la función**.
Solo indica **qué herramienta quiere usar y con qué parámetros**.

---

# 3. Ejecución de la herramienta

El código de la aplicación es el encargado de:

1. Leer la solicitud del modelo
2. Ejecutar la función correspondiente
3. Enviar el resultado nuevamente al modelo

Ejemplo de mensaje con el resultado de la herramienta:

```json
{
  "role": "tool",
  "tool_call_id": "call_abc123",
  "name": "obtener_clima",
  "content": "{\"temperatura\": 22, \"condicion\": \"soleado\", \"unidad\": \"celsius\"}"
}
```

Relaciones importantes:

* **tool_call_id** debe coincidir con el `id` generado por el modelo
* **content** contiene el resultado de la función

Este mensaje se agrega a la conversación antes de volver a llamar al modelo.

---

# 4. El modelo evalúa el resultado

Ahora el modelo recibe la conversación completa incluyendo el resultado de la herramienta.

Ejemplo de historial:

```json
[
  {
    "role": "user",
    "content": "¿Cómo está el clima en Buenos Aires?"
  },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "call_abc123",
        "type": "function",
        "function": {
          "name": "obtener_clima",
          "arguments": "{\"ubicacion\": \"Buenos Aires\"}"
        }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "call_abc123",
    "name": "obtener_clima",
    "content": "{\"temperatura\": 22, \"condicion\": \"soleado\"}"
  }
]
```

A partir de esta información el modelo puede:

* Generar una **respuesta final**
* Solicitar **otra herramienta**
* Continuar con un **proceso multi-paso**

Ejemplo de respuesta final:

```json
{
  "role": "assistant",
  "content": "El clima en Buenos Aires es soleado con una temperatura de 22 grados."
}
```

---

# Modelos compatibles con Tool Use en Groq

Todos los modelos alojados en **Groq** soportan Tool Use.

Algunos modelos recomendados:

* `llama-3.3-70b-versatile`
* `llama-3.1-8b-instant`
* `qwen/qwen3-32b`
* `meta-llama/llama-4-scout-17b-16e-instruct`
* `openai/gpt-oss-20b`
* `openai/gpt-oss-120b`

Estos modelos soportan:

* Tool Use local
* Tool Use remoto
* JSON Mode
* Ejecución paralela de herramientas (en muchos casos)

---

# Formas de usar herramientas en Groq

Groq soporta **tres patrones principales de Tool Use**.

---

# 1. Herramientas integradas (Built-In Tools)

Groq ofrece herramientas integradas que se ejecutan directamente en su infraestructura.

Ejemplos:

* búsqueda web
* ejecución de código
* automatización de navegador

Ventajas:

* configuración mínima
* baja latencia
* ejecución completa en **una sola llamada API**

Ideal para:

* agentes simples
* aplicaciones que necesitan información en tiempo real
* prototipos rápidos

---

# 2. Tool Use remoto con MCP

El **Model Context Protocol (MCP)** es un estándar abierto que permite conectar modelos con herramientas externas.

Cada **MCP server** expone herramientas que pueden ser utilizadas por el modelo.

Groq puede:

* descubrir herramientas en el servidor MCP
* enviarlas al modelo
* ejecutar las llamadas automáticamente

Todo esto ocurre **en una sola llamada API**.

Ideal para:

* integraciones con GitHub
* bases de datos
* APIs externas
* herramientas mantenidas por terceros

---

# 3. Tool Use local (Function Calling)

En este modelo, las herramientas se ejecutan **dentro de la aplicación**.

El flujo es:

1. Definir herramientas
2. Enviarlas al modelo
3. El modelo solicita una herramienta
4. El código ejecuta la función
5. El resultado se devuelve al modelo

Esto permite integrar:

* APIs internas
* bases de datos
* lógica de negocio
* workflows personalizados

Ideal para:

* aplicaciones empresariales
* sistemas internos
* control total sobre seguridad y ejecución

---

# Comparación de enfoques

| Patrón     | Qué provee el desarrollador | Dónde se ejecuta | Orquestación  | Llamadas API |
| ---------- | --------------------------- | ---------------- | ------------- | ------------ |
| Built-In   | Lista de herramientas       | Servidores Groq  | Groq          | 1            |
| MCP Remoto | URL del servidor MCP        | Servidor MCP     | Groq          | 1            |
| Local      | Definición + implementación | Código de la app | Desarrollador | 2 o más      |

---

# Tool Use en paralelo

Algunos modelos permiten **llamar múltiples herramientas en paralelo**.

Ejemplo sin paralelismo:

```
Pregunta: clima en NYC y LA

Llamada 1 → obtener_clima(NYC)
Esperar resultado

Llamada 2 → obtener_clima(LA)
Esperar resultado
```

Ejemplo con paralelismo:

```
Pregunta: clima en NYC y LA

Llamada única:
[obtener_clima(NYC), obtener_clima(LA)]
```

Ambas herramientas se ejecutan **simultáneamente**, reduciendo la latencia.

---

# Por qué la velocidad es importante

Los agentes basados en herramientas requieren **múltiples inferencias**.

Ejemplos:

| Flujo                  | Llamadas al modelo |
| ---------------------- | ------------------ |
| 1 herramienta          | 2 inferencias      |
| múltiples herramientas | 3 a 5              |
| agentes complejos      | 10 o más           |

Con velocidades tradicionales de **10-30 tokens por segundo**, estos procesos pueden volverse lentos.

---

# Conclusión

Tool Use permite que los modelos de lenguaje:

* ejecuten acciones
* accedan a información externa
* integren APIs
* construyan sistemas multi-paso

Esto transforma a los LLM en **agentes capaces de interactuar con el mundo real**, una de las bases de la **IA moderna basada en agentes**.
