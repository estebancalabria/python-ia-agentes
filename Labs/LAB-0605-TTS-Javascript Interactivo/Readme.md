
Idea pedagógica de este laboratorio:

```
Usuario habla
     ↓
Speech-to-Text
     ↓
Prompt
     ↓
LLM (API)
     ↓
Respuesta
     ↓
Text-to-Speech
```

Esto es básicamente un **Voice AI Agent simple**.

---

# 🧪 Laboratorio: Crear un Agente de Voz con JavaScript 🤖🎤

## 📝 Introducción

En este laboratorio construiremos un **agente conversacional por voz** que:

* 🎤 Escucha al usuario (Speech-to-Text)
* 🧠 Envía la pregunta a un **LLM**
* 💬 Obtiene una respuesta
* 🔊 La responde con voz (Text-to-Speech)

Todo esto usando:

* HTML
* JavaScript
* APIs nativas del navegador
* Un endpoint de LLM

---

# 🧠 Arquitectura del Agente

El flujo será:

```
Usuario habla
     ↓
SpeechRecognition
     ↓
Texto reconocido
     ↓
LLM API
     ↓
Respuesta del modelo
     ↓
SpeechSynthesis
     ↓
Respuesta hablada
```

---

# 📋 Requisitos

* Navegador Chrome
* Micrófono
* Una API de LLM (OpenAI, Groq, etc.)

Para este laboratorio dejaremos un **endpoint simulado** para simplificar.

---

# 📄 Paso 1: Crear el archivo

Crear:

```
voice-agent.html
```

---

# 🧩 Paso 2: Crear interfaz básica

```html
<!DOCTYPE html>
<html>

<body>

<h2>Agente de Voz</h2>

<button id="start">Hablar</button>

<p><b>Usuario:</b> <span id="user"></span></p>
<p><b>Agente:</b> <span id="agent"></span></p>

</body>

</html>
```

---

# 🎤 Paso 3: Inicializar Speech-to-Text

```javascript
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang = "es-ES";
recognition.continuous = false;
recognition.interimResults = false;
```

---

# 🎧 Paso 4: Capturar lo que dice el usuario

```javascript
recognition.onresult = async (event) => {

    const textoUsuario = event.results[0][0].transcript;

    document.getElementById("user").innerText = textoUsuario;

    const respuesta = await consultarLLM(textoUsuario);

    document.getElementById("agent").innerText = respuesta;

    hablar(respuesta);
};
```

---

# 🧠 Paso 5: Simular consulta a un LLM

Para simplificar el laboratorio, crearemos una función que **simula un modelo**.

```javascript
async function consultarLLM(pregunta) {

    if (pregunta.toLowerCase().includes("hora")) {
        return "No tengo reloj, pero puedes mirar tu celular.";
    }

    if (pregunta.toLowerCase().includes("nombre")) {
        return "Soy un agente de voz creado en JavaScript.";
    }

    return "Interesante pregunta. Aún estoy aprendiendo.";
}
```

> 💡 En un laboratorio avanzado esto podría conectarse a **OpenAI, Groq o cualquier API de LLM**.

---

# 🔊 Paso 6: Crear la función de Text-to-Speech

```javascript
function hablar(texto) {

    const utterance = new SpeechSynthesisUtterance(texto);

    utterance.lang = "es-ES";
    utterance.pitch = 1;
    utterance.rate = 1;

    speechSynthesis.speak(utterance);
}
```

---

# ▶️ Paso 7: Activar el reconocimiento

```javascript
document.getElementById("start").onclick = () => {
    recognition.start();
};
```

---

# 💻 Código Completo

```html
<!DOCTYPE html>
<html>

<body>

<h2>Agente de Voz</h2>

<button id="start">Hablar</button>

<p><b>Usuario:</b> <span id="user"></span></p>
<p><b>Agente:</b> <span id="agent"></span></p>

<script>

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang = "es-ES";
recognition.continuous = false;
recognition.interimResults = false;

recognition.onresult = async (event) => {

    const textoUsuario = event.results[0][0].transcript;

    document.getElementById("user").innerText = textoUsuario;

    const respuesta = await consultarLLM(textoUsuario);

    document.getElementById("agent").innerText = respuesta;

    hablar(respuesta);
};

async function consultarLLM(pregunta) {

    if (pregunta.toLowerCase().includes("hora")) {
        return "No tengo reloj, pero puedes mirar tu celular.";
    }

    if (pregunta.toLowerCase().includes("nombre")) {
        return "Soy un agente de voz creado en JavaScript.";
    }

    return "Interesante pregunta. Aún estoy aprendiendo.";
}

function hablar(texto) {

    const utterance = new SpeechSynthesisUtterance(texto);

    utterance.lang = "es-ES";
    utterance.pitch = 1;
    utterance.rate = 1;

    speechSynthesis.speak(utterance);
}

document.getElementById("start").onclick = () => {
    recognition.start();
};

</script>

</body>

</html>
```

---

# 🧪 Ejemplo de interacción

Usuario dice:

```
¿Cómo te llamas?
```

Flujo:

```
Speech-to-Text
↓
"como te llamas"
↓
LLM
↓
"Soy un agente de voz creado en JavaScript"
↓
Text-to-Speech
```

El navegador **habla la respuesta**.

---

# 🚀 Ejercicio para los alumnos

Modificar el agente para que:

1️⃣ Consulte una **API real de LLM**
2️⃣ Mantenga **historial de conversación**
3️⃣ Permita conversación continua

Flujo final:

```
Usuario
  ↓
Speech-to-Text
  ↓
LLM
  ↓
Memoria de conversación
  ↓
Text-to-Speech
```

---

# 🎉 Conclusión

Este laboratorio muestra cómo construir un **Voice AI Agent simple en el navegador** usando:

* 🎤 Speech Recognition
* 🧠 LLM
* 🔊 Speech Synthesis

Conceptos aprendidos:

* Conversión voz → texto
* Integración con modelos de IA
* Conversión texto → voz

**Un ChatGPT por voz en JavaScript usando la API de OpenAI o Groq (30 líneas de código)**.
A los alumnos literalmente **les vuela la cabeza cuando lo ven.**
