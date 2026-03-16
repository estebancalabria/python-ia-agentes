# Streamlit: Crear Interfaces Web para Aplicaciones de Python

**Streamlit** es una librería de Python que permite crear **interfaces web interactivas de forma rápida y sencilla**, especialmente para aplicaciones de **data science, machine learning e inteligencia artificial**.

Con Streamlit podés convertir un script de Python en una aplicación web **sin necesidad de saber HTML, CSS o JavaScript**.

---

# Instalación

Primero instalamos la librería:

```bash
pip install streamlit
````

---

# Primer Programa con Streamlit

Creamos un archivo llamado:

```bash
app.py
```

Contenido:

```python
import streamlit as st

st.title("Mi primera app con Streamlit")

st.write("Hola mundo 👋")

nombre = st.text_input("¿Cómo te llamás?")

if nombre:
    st.write(f"Hola {nombre}, bienvenido a Streamlit!")
```

---

# Ejecutar la aplicación

Para ejecutar la aplicación usamos:

```bash
streamlit run app.py
```

Streamlit iniciará un servidor local y abrirá automáticamente el navegador.

Normalmente la app se ejecuta en:

```
http://localhost:8501
```

---

# Componentes Básicos

Streamlit tiene muchos componentes interactivos.

## Texto

```python
st.title("Título")
st.header("Header")
st.subheader("Subheader")
st.text("Texto simple")
st.markdown("**Markdown** soportado")
```

---

## Inputs

### Campo de texto

```python
nombre = st.text_input("Tu nombre")
```

### Slider

```python
edad = st.slider("Edad", 0, 100)
```

### Selectbox

```python
lenguaje = st.selectbox(
    "Lenguaje favorito",
    ["Python", "JavaScript", "Java", "C#"]
)
```

---

# Botones

```python
if st.button("Saludar"):
    st.write("Hola!")
```

---

# Mostrar Datos

## Mostrar listas o diccionarios

```python
datos = {
    "nombre": "Ana",
    "edad": 28
}

st.write(datos)
```

---

## Mostrar DataFrames

```python
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "Pedro"],
    "Edad": [28, 34, 45]
})

st.dataframe(df)
```

---

# Subir archivos

```python
archivo = st.file_uploader("Subí un archivo")

if archivo:
    st.write("Archivo cargado:", archivo.name)
```

---

# Mostrar imágenes

```python
st.image("imagen.png", caption="Imagen de ejemplo")
```

---

# Ejemplo Completo

```python
import streamlit as st

st.title("Calculadora simple")

a = st.number_input("Número A")
b = st.number_input("Número B")

if st.button("Sumar"):
    resultado = a + b
    st.write("Resultado:", resultado)
```

---

# Ventajas de Streamlit

* Muy fácil de usar
* Ideal para prototipos rápidos
* Perfecto para demos de IA y machine learning
* No requiere frontend

---

# Casos de Uso

Streamlit se utiliza comúnmente para:

* Dashboards de datos
* Interfaces para modelos de machine learning
* Aplicaciones de inteligencia artificial
* Herramientas internas para análisis de datos
* Prototipos de aplicaciones web

---

# Recursos

Documentación oficial:

[https://docs.streamlit.io](https://docs.streamlit.io)

```
```
