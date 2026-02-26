# Tutorial Completo de Gradio: De Cero a Aplicaciones Interactivas 🚀

## ¿Qué es Gradio?

Gradio es una librería de Python que permite crear aplicaciones web interactivas de forma simple y rápida.

Su objetivo es transformar funciones de Python en interfaces web sin necesidad de conocimientos en:

* HTML
* CSS
* JavaScript

Con Gradio puedes:

* Crear demos interactivas
* Construir formularios web
* Desarrollar chatbots
* Probar modelos de Machine Learning
* Compartir aplicaciones desde Google Colab

---

# 1️⃣ Instalación

En Google Colab o entorno local:

```python
!pip install -q gradio
```

---

# 2️⃣ Concepto Fundamental

Gradio conecta tres elementos:

**Función Python → Componentes de Entrada → Componentes de Salida**

La interfaz es simplemente una forma visual de ejecutar una función.

---

# 3️⃣ Interfaz Básica con Interface

`Interface` es la forma más simple de usar Gradio.

## Paso 1: Importar

```python
import gradio as gr
```

---

## Paso 2: Crear una función

```python
def saludar(nombre):
    return f"Hola {nombre}, bienvenido a Gradio."
```

---

## Paso 3: Crear la interfaz

```python
demo = gr.Interface(
    fn=saludar,
    inputs="text",
    outputs="text",
    title="Saludo Simple",
    description="Escribe tu nombre y recibirás un saludo."
)
```

---

## Paso 4: Lanzar la aplicación

```python
demo.launch()
```

---

## ¿Qué está ocurriendo?

* `fn` → Función backend
* `inputs` → Tipo de entrada
* `outputs` → Tipo de salida
* `.launch()` → Inicia el servidor web

---

# 4️⃣ Tipos de Componentes

Gradio incluye múltiples componentes.

## Entrada de texto

```python
gr.Textbox()
```

## Número

```python
gr.Number()
```

## Slider

```python
gr.Slider(minimum=0, maximum=100)
```

## Checkbox

```python
gr.Checkbox()
```

## Imagen

```python
gr.Image()
```

---

# 5️⃣ Ejemplo con Múltiples Entradas

```python
import gradio as gr

def calcular_area(base, altura):
    return base * altura

demo = gr.Interface(
    fn=calcular_area,
    inputs=[
        gr.Number(label="Base"),
        gr.Number(label="Altura")
    ],
    outputs="number",
    title="Calculadora de Área"
)

demo.launch()
```

---

# 6️⃣ Personalización Visual

```python
demo = gr.Interface(
    fn=saludar,
    inputs=gr.Textbox(placeholder="Escribe tu nombre aquí"),
    outputs=gr.Textbox(),
    title="Aplicación Personalizada",
    description="Ejemplo con personalización",
    theme="soft"
)

demo.launch()
```

---

# 7️⃣ Introducción a Blocks

`Blocks` permite crear interfaces más complejas y personalizadas.

Diferencias principales:

| Interface            | Blocks                |
| -------------------- | --------------------- |
| Simple               | Flexible              |
| Una función          | Multiples componentes |
| Configuración rápida | Layout personalizado  |

---

# 8️⃣ Estructura de Blocks

```python
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Mi Aplicación")
    entrada = gr.Textbox()
    salida = gr.Textbox()
    boton = gr.Button("Ejecutar")

    def procesar(texto):
        return texto.upper()

    boton.click(procesar, inputs=entrada, outputs=salida)

demo.launch()
```

---

## Conceptos Nuevos

* `with gr.Blocks()` → Contenedor principal
* Componentes asignados a variables
* Eventos como `.click()`

---

# 9️⃣ Layout con Row y Column

```python
with gr.Blocks() as demo:
    gr.Markdown("# Layout Demo")
    
    with gr.Row():
        gr.Textbox(label="Campo 1")
        gr.Textbox(label="Campo 2")

    with gr.Column():
        gr.Button("Botón 1")
        gr.Button("Botón 2")

demo.launch()
```

---

# 🔟 Manejo de Estado

Gradio permite almacenar información durante la sesión.

```python
import gradio as gr

def contador(valor, estado):
    if estado is None:
        estado = 0
    estado += 1
    return f"Clicks: {estado}", estado

with gr.Blocks() as demo:
    estado = gr.State(0)
    texto = gr.Textbox()
    boton = gr.Button("Contar")
    
    boton.click(contador, inputs=[texto, estado], outputs=[texto, estado])

demo.launch()
```

---

# 1️⃣1️⃣ Construcción de un Chatbot

```python
import gradio as gr

def responder(mensaje, historial):
    if historial is None:
        historial = []
    
    respuesta = f"🤖 Dijiste: {mensaje}"
    historial.append((mensaje, respuesta))
    
    return "", historial

with gr.Blocks(title="Chatbot Demo") as demo:
    
    gr.Markdown("# 🤖 Chatbot con Gradio")
    
    chatbot = gr.Chatbot(height=400)
    
    with gr.Row():
        mensaje = gr.Textbox(
            placeholder="Escribí tu mensaje...",
            show_label=False,
            scale=8
        )
        boton = gr.Button("Enviar", variant="primary", scale=1)

    estado = gr.State([])

    mensaje.submit(
        responder,
        inputs=[mensaje, estado],
        outputs=[mensaje, chatbot]
    )

    boton.click(
        responder,
        inputs=[mensaje, estado],
        outputs=[mensaje, chatbot]
    )

demo.launch()
```

---

# 1️⃣2️⃣ Flujo Interno de Gradio

1. Usuario interactúa con un componente.
2. Se dispara un evento (`click`, `submit`, etc.).
3. Se ejecuta una función Python.
4. Se actualizan componentes de salida.
5. La interfaz se re-renderiza automáticamente.

Gradio utiliza un modelo reactivo basado en eventos.

---

# 1️⃣3️⃣ Ejecutar en Google Colab

Pasos esenciales:

1. Instalar Gradio.
2. Ejecutar todas las celdas.
3. Ejecutar `.launch()`.
4. Abrir el enlace generado.

---

# 1️⃣4️⃣ Resumen Conceptual

Gradio se basa en:

* Funciones puras de Python
* Componentes visuales
* Eventos
* Estado
* Renderizado reactivo automático

No es necesario frontend tradicional.

Permite iterar rápido, experimentar y compartir aplicaciones web interactivas en minutos.
