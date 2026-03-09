# 🧪 Laboratorio: Agente de Voz con Groq LLM 🎤🤖🔊

## 📝 Introducción

En este laboratorio vamos a construir un **agente de voz** que funciona directamente en el navegador y se conecta a **Groq LLM** usando tu propia API Key. El agente podrá:

* 🎤 Escuchar la voz del usuario y convertirla en texto (Speech-to-Text)
* 🧠 Consultar Groq LLM con el modelo `openai/gpt-oss-20b`
* 🔊 Responder con voz usando Text-to-Speech

Este laboratorio está pensado **paso a paso** para que sea didáctico y fácil de seguir.

---

## 📋 Requisitos

* Navegador moderno (Chrome recomendado)
* Micrófono
* Una **API Key válida de Groq**
* Conocimientos básicos de HTML y JavaScript

---

## 🔧 Paso 1: Crear la interfaz básica

Primero crearemos un archivo HTML y agregaremos:

* Un input para ingresar la API Key
* Un botón para iniciar la escucha
* Párrafos para mostrar la frase que dice el usuario y la respuesta del agente

```html
<label>API Key de Groq: <input type="password" id="apiKey" placeholder="Ingresa tu API Key"></label><br><br>
<button id="start">Hablar</button>

<p><b>Usuario:</b> <span id="user"></span></p>
<p><b>Agente:</b> <span id="agent"></span></p>
```

---

## 💡 Paso 2: Crear la función de Text-to-Speech

La función `hablar` tomará un texto y lo reproducirá en voz usando `SpeechSynthesisUtterance`:

```javascript
function hablar(texto) {
    const utterance = new SpeechSynthesisUtterance(texto);
    utterance.lang = "es-ES";  // idioma español
    utterance.pitch = 1;        // tono
    utterance.rate = 1;         // velocidad
    speechSynthesis.speak(utterance);
}
```

> ⚡ Esta función se encargará de “darle voz” a cualquier respuesta del agente.

---

## 🧠 Paso 3: Crear la función para consultar Groq LLM

Esta función enviará la pregunta del usuario al **modelo `openai/gpt-oss-20b`** usando **fetch** a la API de Groq:

```javascript
async function consultarLLM(pregunta) {
    const apiKey = document.getElementById("apiKey").value.trim();
    if (!apiKey) return "Por favor ingresa tu API Key de Groq.";

    const body = {
        model: "openai/gpt-oss-20b",
        messages: [
            { role: "system", content: "Eres un asistente útil y amable." },
            { role: "user", content: pregunta }
        ]
    };

    try {
        const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify(body)
        });

        const data = await response.json();

        const respuesta = data.choices?.[0]?.message?.content;
        return respuesta || "No recibí respuesta del modelo.";

    } catch (error) {
        console.error(error);
        return "Error al conectarse con Groq LLM.";
    }
}
```

> 💡 Aquí se muestra cómo enviar un prompt al LLM y recibir la respuesta.

---

## 🎤 Paso 4: Inicializar Speech-to-Text

Creamos el objeto de reconocimiento de voz del navegador:

```javascript
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = "es-ES";       // idioma español
recognition.continuous = false;   // solo captura una frase
recognition.interimResults = false; // resultados finales
```

> ⚡ `webkitSpeechRecognition` se usa para compatibilidad con Chrome.

---

## 🎧 Paso 5: Manejar el resultado de la voz

Cuando el usuario hable, capturamos el texto, lo mostramos y enviamos la pregunta al LLM:

```javascript
recognition.onresult = async (event) => {
    const textoUsuario = event.results[0][0].transcript;
    document.getElementById("user").innerText = textoUsuario;

    const respuesta = await consultarLLM(textoUsuario);

    document.getElementById("agent").innerText = respuesta;
    hablar(respuesta);
};
```

> 🧠 Aquí se conecta la entrada de voz con la función de LLM y la salida de voz.

---

## ▶️ Paso 6: Iniciar la escucha al hacer clic

Vinculamos el botón con el inicio del reconocimiento de voz:

```javascript
document.getElementById("start").onclick = () => {
    recognition.start();
};
```

---

## 💻 Código Completo del Laboratorio

```html
<!DOCTYPE html>
<html lang="es">

<head>
<meta charset="UTF-8">
<title>Laboratorio: Agente de Voz con Groq LLM</title>
</head>

<body>

<h2>🧪 Laboratorio: Agente de Voz con Groq LLM</h2>

<label>API Key de Groq: <input type="password" id="apiKey" placeholder="Ingresa tu API Key"></label><br><br>
<button id="start">Hablar</button>

<p><b>Usuario:</b> <span id="user"></span></p>
<p><b>Agente:</b> <span id="agent"></span></p>

<script>

// Función Text-to-Speech
function hablar(texto) {
    const utterance = new SpeechSynthesisUtterance(texto);
    utterance.lang = "es-ES";
    utterance.pitch = 1;
    utterance.rate = 1;
    speechSynthesis.speak(utterance);
}

// Función para consultar Groq LLM
async function consultarLLM(pregunta) {
    const apiKey = document.getElementById("apiKey").value.trim();
    if (!apiKey) return "Por favor ingresa tu API Key de Groq.";

    const body = {
        model: "openai/gpt-oss-20b",
        messages: [
            { role: "system", content: "Eres un asistente útil y amable." },
            { role: "user", content: pregunta }
        ]
    };

    try {
        const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify(body)
        });

        const data = await response.json();
        const respuesta = data.choices?.[0]?.message?.content;
        return respuesta || "No recibí respuesta del modelo.";

    } catch (error) {
        console.error(error);
        return "Error al conectarse con Groq LLM.";
    }
}

// Inicializar Speech-to-Text
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = "es-ES";
recognition.continuous = false;
recognition.interimResults = false;

// Manejar resultado de voz
recognition.onresult = async (event) => {
    const textoUsuario = event.results[0][0].transcript;
    document.getElementById("user").innerText = textoUsuario;

    const respuesta = await consultarLLM(textoUsuario);

    document.getElementById("agent").innerText = respuesta;
    hablar(respuesta);
};

// Iniciar escucha al click
document.getElementById("start").onclick = () => {
    recognition.start();
};

</script>

</body>
</html>
```

---

## ✅ Conclusión

Con este laboratorio aprendiste a:

* Capturar la voz del usuario usando **SpeechRecognition**
* Enviar preguntas a **Groq LLM** usando la API Key ingresada
* Convertir la respuesta en voz con **SpeechSynthesis**
* Integrar todo en un **agente de voz real** que funciona completamente en el navegador

> 💡 Tip: Puedes ampliar este laboratorio añadiendo historial de conversación, prompts más complejos, o soporte para múltiples idiomas.
