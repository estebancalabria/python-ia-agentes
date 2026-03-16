# Laboratorio: Agente de Reservas con Tool Use y Groq

En este laboratorio construirás un **asistente de reservas** utilizando **Tool Use con Groq**.

El asistente podrá:

* Consultar disponibilidad de turnos
* Reservar un turno
* Consultar la fecha y hora actual

La disponibilidad se almacenará en una **matriz en memoria que representa los horarios disponibles para la semana próxima**.

El modelo utilizado será:

**Llama 3.3 70B Versatile**

Llama 3.3 70B Versatile

---

# Objetivos del laboratorio

Al finalizar este laboratorio el estudiante comprenderá:

* Cómo usar **múltiples tools**
* Cómo implementar **un loop de tool execution**
* Cómo mantener **estado en memoria**
* Cómo construir un **agente simple**

---

# Requisitos

* Cuenta en Groq
* API Key de Groq
* Cuenta de Google Colab

---

# Paso 1: Instalar dependencias

En una celda de Colab:

```python
!pip install openai
```

---

# Paso 2: Importar librerías

```python
from openai import OpenAI
import json
import datetime
```

---

# Paso 3: System Prompt

Definimos el comportamiento del asistente.

```python
system_prompt = """
Eres un asistente que gestiona reservas de turnos.

Puedes:
- consultar disponibilidad
- reservar turnos
- consultar la fecha actual

Siempre debes usar las herramientas disponibles para obtener información.
"""
```

---

# Paso 4: Crear la matriz de disponibilidad

Simularemos turnos para **la semana próxima**.

Cada día tendrá horarios:

```
9
10
11
14
15
16
```

```python
disponibilidad = {
    "lunes":   [9,10,11,14,15,16],
    "martes":  [9,10,11,14,15,16],
    "miercoles":[9,10,11,14,15,16],
    "jueves":  [9,10,11,14,15,16],
    "viernes": [9,10,11,14,15,16]
}
```

---

# Paso 5: Crear las funciones (Tools)

## Tool 1 — Fecha actual

```python
def obtener_fecha_actual():
    ahora = datetime.datetime.now()

    return {
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M")
    }
```

---

## Tool 2 — Consultar disponibilidad

```python
def consultar_disponibilidad(dia):

    if dia.lower() not in disponibilidad:
        return {"error":"día inválido"}

    return {
        "dia": dia,
        "horarios_disponibles": disponibilidad[dia.lower()]
    }
```

---

## Tool 3 — Reservar turno

```python
def reservar_turno(dia, hora):

    dia = dia.lower()

    if dia not in disponibilidad:
        return {"error":"día inválido"}

    if hora not in disponibilidad[dia]:
        return {"error":"horario no disponible"}

    disponibilidad[dia].remove(hora)

    return {
        "estado":"reservado",
        "dia":dia,
        "hora":hora
    }
```

---

# Paso 6: Definir las Tools

```python
tools = [

{
"type":"function",
"function":{
"name":"obtener_fecha_actual",
"description":"Devuelve la fecha y hora actual",
"parameters":{
"type":"object",
"properties":{}
}
}
},

{
"type":"function",
"function":{
"name":"consultar_disponibilidad",
"description":"Consulta horarios disponibles para un día",
"parameters":{
"type":"object",
"properties":{
"dia":{
"type":"string",
"description":"día de la semana"
}
},
"required":["dia"]
}
}
},

{
"type":"function",
"function":{
"name":"reservar_turno",
"description":"Reserva un turno en un día y horario",
"parameters":{
"type":"object",
"properties":{
"dia":{"type":"string"},
"hora":{"type":"integer"}
},
"required":["dia","hora"]
}
}
}

]
```

---

# Paso 7: Crear cliente Groq

```python
api_key = input("Ingrese API Key: ")
pregunta = input("¿Qué desea hacer?: ")

cliente = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
```

---

# Paso 8: Historial de conversación

```python
messages = [
{"role":"system","content":system_prompt},
{"role":"user","content":pregunta}
]
```

---

# Paso 9: Loop del agente

Este es el **patrón real de agentes**.

```python
while True:

    respuesta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    mensaje = respuesta.choices[0].message

    if not mensaje.tool_calls:
        print(mensaje.content)
        break

    messages.append(mensaje)

    for tool_call in mensaje.tool_calls:

        nombre = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        if nombre == "obtener_fecha_actual":
            resultado = obtener_fecha_actual()

        elif nombre == "consultar_disponibilidad":
            resultado = consultar_disponibilidad(**args)

        elif nombre == "reservar_turno":
            resultado = reservar_turno(**args)

        messages.append({
            "role":"tool",
            "tool_call_id":tool_call.id,
            "content":json.dumps(resultado)
        })
```

---

# Ejemplos para probar

## Ejemplo 1

Prompt:

```
¿Qué horarios hay disponibles el martes?
```

Respuesta esperada:

```
Los horarios disponibles el martes son: 9, 10, 11, 14, 15 y 16.
```

---

## Ejemplo 2

Prompt:

```
Reservá un turno el martes a las 10
```

Respuesta esperada:

```
Tu turno fue reservado para el martes a las 10.
```

---

## Ejemplo 3

Prompt:

```
¿Quedan horarios el martes?
```

Respuesta esperada:

```
Los horarios disponibles son: 9, 11, 14, 15 y 16.
```

(el turno de las 10 ya no aparece)

---

## Ejemplo 4

Prompt:

```
¿Qué día es hoy?
```

Respuesta esperada:

```
Hoy es 2026-03-16.
```

---

# Qué aprendiste en este laboratorio

Este laboratorio introduce conceptos fundamentales de **agentes con LLM**:

* múltiples tools
* estado compartido
* ejecución iterativa
* tool selection automática

\
