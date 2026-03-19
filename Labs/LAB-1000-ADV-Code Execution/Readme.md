# Laboratorio: Code Execution con Groq y Google Colab (Calculadora de Estadísticas)

Este laboratorio muestra cómo implementar **Code Execution** usando la API de Groq desde Google Colab.
El asistente será capaz de **generar y ejecutar código Python automáticamente** para realizar cálculos estadísticos sobre un conjunto de números que proporcione el usuario.

Se utilizará el modelo:

**Llama 3.3 70B Versatile**

Ver documentación del modelo:
[https://console.groq.com/docs/model/llama-3.3-70b-versatile](https://console.groq.com/docs/model/llama-3.3-70b-versatile)

Este modelo es un LLM de **70 mil millones de parámetros optimizado para conversación, razonamiento y ejecución de código**.

---

# Requisitos previos

* Tener una cuenta en **Groq**
* Tener una **API Key**
* Tener una cuenta de **Google**
* Acceso a **Google Colab**

---

# Paso 1: Obtener la API Key de Groq

1. Ir a [https://console.groq.com/](https://console.groq.com/)
2. Iniciar sesión
3. Ir a **API Keys**
4. Hacer clic en **Create API Key**
5. Copiar la clave generada

Ejemplo:

```python
gsk_xxxxxxxxxxxxxxxxx
```

---

# Paso 2: Crear un Notebook en Google Colab

1. Ir a [https://colab.google/](https://colab.google/)
2. Crear un **Nuevo Notebook**

---

# Paso 3: Instalar dependencias

Crear una celda y ejecutar:

```python
!pip install openai
```

---

# Paso 4: Definir el System Prompt

El comportamiento del asistente se controla con un **system prompt**.
El asistente solo generará **código Python para cálculos estadísticos** y devolverá los resultados.

```python
system_prompt = """
Eres un asistente que puede generar y ejecutar código Python para cálculos estadísticos. 
Solo puedes responder generando código Python que defina una variable 'resultado'.
No escribas texto explicativo, solo el código Python listo para ejecutar.
"""
```

---

# Paso 5: Crear función de ejecución segura de código

Esta función ejecuta código Python generado por el modelo y devuelve la variable `resultado`.

```python
def ejecutar_codigo(codigo):
    """
    Ejecuta código Python seguro en un entorno controlado y devuelve el resultado.
    """
    resultado = None
    try:
        entorno = {}
        exec(codigo, {}, entorno)
        resultado = entorno.get("resultado", "No se definió variable 'resultado'")
    except Exception as e:
        resultado = f"Error en ejecución: {e}"
    return resultado
```

---

# Paso 6: Crear cliente de Groq

```python
from openai import OpenAI

api_key = input("Ingrese su API key: ")
prompt_usuario = input("Ingrese la tarea de cálculo o estadística que desea: ")

cliente = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
```

---

# Paso 7: Solicitar al modelo que genere código Python

```python
respuesta = cliente.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt_usuario}
    ]
)

codigo_generado = respuesta.choices[0].message.content
print("Código generado por el modelo:\n", codigo_generado)
```

---

# Paso 8: Ejecutar el código generado

```python
resultado = ejecutar_codigo(codigo_generado)
print("\nResultado de la ejecución:", resultado)
```

---

# Paso 9: Ejemplo de uso

**Prompt de usuario sugerido:**

```text
Calcular la media, mediana y desviación estándar del conjunto de números [5, 12, 7, 9, 15, 20]
```

**Código que podría generar el modelo:**

```python
import statistics

numeros = [5, 12, 7, 9, 15, 20]

resultado = {
    "media": statistics.mean(numeros),
    "mediana": statistics.median(numeros),
    "desviacion_estandar": statistics.stdev(numeros)
}
```

**Resultado de la ejecución:**

```json
{
    "media": 11.333333333333334,
    "mediana": 10.5,
    "desviacion_estandar": 5.335
}
```

---

# Paso 10: Otros prompts de ejemplo

1. **Suma y producto de una lista de números:**

   ```text
   Calcular la suma y el producto de [2, 3, 5, 7]
   ```

2. **Valores mínimo, máximo y rango de una lista:**

   ```text
   Determinar el valor mínimo, máximo y el rango del conjunto [10, 4, 7, 2, 9]
   ```

3. **Conteo de números mayores a un valor:**

   ```text
   Contar cuántos números son mayores a 10 en [8, 15, 3, 12, 9, 20]
   ```

---

# 💡 Nota didáctica

* Este laboratorio demuestra un **agente con Code Execution**, donde el LLM genera código Python y este se ejecuta automáticamente en Colab.
* No se usan tool calls externas; el LLM decide la lógica y la ejecuta.
* Es un paso intermedio hacia agentes más avanzados que combinan **RAG + Tool Use + Code Execution**, como lo hace Claude.

