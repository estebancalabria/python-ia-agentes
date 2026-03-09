# 🧪 Laboratorio: Speech-to-Text y Text-to-Speech con JavaScript 🎤🔊

## 📝 Introducción

En este laboratorio vamos a construir una pequeña aplicación web que permite:

* 🎤 **Convertir voz a texto** (Speech-to-Text)
* 🔊 **Convertir texto a voz** (Text-to-Speech)

Todo esto usando únicamente:

* **HTML**
* **JavaScript**
* **APIs nativas del navegador**

⚠️ No usamos librerías externas ni APIs de terceros.

---

# 📋 Requisitos

* Navegador moderno (Chrome recomendado)
* Conocimientos básicos de HTML y JavaScript
* Un micrófono

---

# 🧠 ¿Qué APIs vamos a usar?

El navegador incluye dos APIs muy útiles:

| API                   | Función                |
| --------------------- | ---------------------- |
| **SpeechRecognition** | Convierte voz en texto |
| **SpeechSynthesis**   | Convierte texto en voz |

Estas APIs forman parte de:

**Web Speech API**

---

# 🎤 Parte 1: Speech-to-Text (Voz → Texto)

---

# 📄 Paso 1: Crear archivo HTML

Crear un archivo:

```
speech-to-text.html
```

---

# 🧩 Paso 2: Crear la interfaz básica

```html
<!DOCTYPE html>
<html>

<body>

<h2>Speech to Text</h2>

<button id="start">Hablar</button>

<p id="output"></p>

</body>

</html>
```

---

# ⚙️ Paso 3: Crear el objeto de reconocimiento de voz

Ahora agregamos JavaScript para usar la API de reconocimiento.

```javascript
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
```

> ⚠️ `webkitSpeechRecognition` se usa para compatibilidad con Chrome.

---

# 🌎 Paso 4: Configurar idioma y comportamiento

```javascript
recognition.lang = "es-ES";
recognition.continuous = false;
recognition.interimResults = false;
```

### Significado

| Configuración  | Descripción              |
| -------------- | ------------------------ |
| lang           | idioma de reconocimiento |
| continuous     | si sigue escuchando      |
| interimResults | resultados parciales     |

---

# 🎧 Paso 5: Capturar el resultado de voz

Cuando el usuario habla, el navegador devuelve el texto detectado.

```javascript
recognition.onresult = (event) => {
    const texto = event.results[0][0].transcript;
    document.getElementById("output").innerText = texto;
};
```

---

# ▶️ Paso 6: Iniciar el reconocimiento

Cuando el usuario hace clic en el botón:

```javascript
document.getElementById("start").onclick = () => {
    recognition.start();
};
```

---

# 💻 Código Completo Speech-to-Text

```html
<!DOCTYPE html>
<html>

<body>

<h2>Speech to Text</h2>

<button id="start">Hablar</button>

<p id="output"></p>

<script>

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang = "es-ES";
recognition.continuous = false;
recognition.interimResults = false;

recognition.onresult = (event) => {
    const texto = event.results[0][0].transcript;
    document.getElementById("output").innerText = texto;
};

document.getElementById("start").onclick = () => {
    recognition.start();
};

</script>

</body>
</html>
```

---

# 🔊 Parte 2: Text-to-Speech (Texto → Voz)

---

# 📄 Paso 1: Crear archivo

Crear un archivo:

```
text-to-speech.html
```

---

# 🧩 Paso 2: Crear botón para hablar

```html
<button onclick="hablar()">Hablar</button>
```

---

# 🗣️ Paso 3: Crear función de voz

```javascript
function hablar() {
    const texto = "Hola Esteban, este es un ejemplo de text to speech en JavaScript";
}
```

---

# 🔊 Paso 4: Crear objeto de voz

La API utiliza el objeto:

**SpeechSynthesisUtterance**

```javascript
const utterance = new SpeechSynthesisUtterance(texto);
```

---

# 🌎 Paso 5: Configurar idioma y voz

```javascript
utterance.lang = "es-ES";
utterance.pitch = 1;
utterance.rate = 1;
```

| Propiedad | Significado |
| --------- | ----------- |
| lang      | idioma      |
| pitch     | tono        |
| rate      | velocidad   |

---

# ▶️ Paso 6: Reproducir voz

```javascript
speechSynthesis.speak(utterance);
```

---

# 💻 Código Completo Text-to-Speech

```html
<!DOCTYPE html>
<html>

<body>

<h2>Text to Speech</h2>

<button onclick="hablar()">Hablar</button>

<script>

function hablar() {

    const texto = "Hola Esteban, este es un ejemplo de text to speech en JavaScript";

    const utterance = new SpeechSynthesisUtterance(texto);

    utterance.lang = "es-ES";
    utterance.pitch = 1;
    utterance.rate = 1;

    speechSynthesis.speak(utterance);
}

</script>

</body>

</html>
```

---

# 🧪 Ejemplo de Uso

### Speech-to-Text

1️⃣ Click en **Hablar**
2️⃣ Decir algo como:

```
Hola esto es una prueba de reconocimiento de voz
```

3️⃣ El texto aparece en pantalla.

---

### Text-to-Speech

1️⃣ Click en **Hablar**
2️⃣ El navegador dirá:

```
Hola Esteban, este es un ejemplo de text to speech en JavaScript
```

---

# 🚀 Desafío (Ejercicio para el alumno)

Modificar el laboratorio para crear un **asistente simple** que:

1️⃣ Escuche al usuario
2️⃣ Convierta la voz a texto
3️⃣ Repita lo que dijo usando voz

Flujo:

```
Usuario habla
      ↓
Speech to Text
      ↓
Texto
      ↓
Text to Speech
      ↓
El sistema lo repite
```

---

# 🎉 Conclusión

En este laboratorio aprendiste a usar **las APIs nativas del navegador para voz**:

### 🎤 Speech-to-Text

Convierte voz en texto usando **SpeechRecognition**

### 🔊 Text-to-Speech

Convierte texto en voz usando **SpeechSynthesis**

Ventajas:

✅ No requiere librerías
✅ No requiere backend
✅ Funciona directamente en el navegador

