# 🚀 Laboratorio: Crear una App Web con Streamlit en Google Colab

---

## 🎯 Objetivo

Construir una aplicación web interactiva usando:

* 🐍 Python
* 🚀 Streamlit
* 🌐 ngrok (para exponer la app en internet)

---

# 📋 Requisitos

1. Cuenta de Google
2. Acceso a Google Colab
   👉 [https://colab.research.google.com](https://colab.research.google.com)
3. Cuenta gratuita en ngrok
   👉 [https://dashboard.ngrok.com/signup](https://dashboard.ngrok.com/signup)

⚠️ IMPORTANTE: verificar el email en ngrok.

---

# 🔧 PASO 1 — Instalar dependencias

Ejecutar en una celda:

```python
!pip install streamlit pyngrok
```

---

# 🔐 PASO 2 — Configurar tu Authtoken de ngrok

1️⃣ Ir a:
[https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)

2️⃣ Copiar tu token

3️⃣ Ejecutar en una celda (reemplazar TU_TOKEN):

```python
from pyngrok import ngrok

# Limpiar procesos anteriores
ngrok.kill()

# Configurar token
ngrok.set_auth_token("TU_TOKEN_AQUI")
```

Si tu cuenta está verificada, no dará error.

---

# 📝 PASO 3 — Crear la aplicación Streamlit

Ejecutar en una nueva celda:

```python
with open("app.py", "w") as f:
    f.write("""
import streamlit as st

st.set_page_config(page_title="Laboratorio Streamlit", page_icon="🚀")

st.title("🚀 Mi Primera App con Streamlit")

st.write("Este laboratorio convierte texto a MAYÚSCULAS.")

texto = st.text_input("Escribe algo:")

if texto:
    st.success(texto.upper())

st.divider()

st.subheader("Extra 🚀")

numero = st.slider("Elegí un número", 0, 100, 10)
st.write("El número al cuadrado es:", numero**2)
""")
```

---

# ▶️ PASO 4 — Ejecutar Streamlit

Ejecutar en una nueva celda:

```python
import subprocess
import time
from pyngrok import ngrok

# Cerrar posibles procesos anteriores
!pkill streamlit

# Iniciar Streamlit
process = subprocess.Popen(["streamlit", "run", "app.py"])

# Esperar que inicie
time.sleep(5)

# Crear túnel público
public_url = ngrok.connect(8501)

print("🚀 Aplicación disponible en:")
print(public_url)
```

---

# 🌐 PASO 5 — Abrir la aplicación

1. Hacer clic en el enlace que aparece
2. Aceptar advertencia de seguridad de ngrok
3. ¡Listo! 🎉

---

# 🧠 ¿Qué se aprende en este laboratorio?

* Crear una app web con Python
* Generar archivo dinámicamente
* Exponer servidor local a internet
* Componentes Streamlit:

  * `text_input`
  * `slider`
  * `button`
  * `st.success`
* Manejo básico cliente-servidor

