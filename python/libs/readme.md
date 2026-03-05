# 📚 Librerías de Python para el Curso de Agentes de IA

Este repositorio contiene información sobre las principales librerías de Python que utilizaremos en el curso de **Agentes de Inteligencia Artificial**. Incluye instalación, autor y funciones útiles para cada una.

---

## 1. PyTorch (torch)

- **Autor / Mantenedor:** Facebook AI Research (FAIR)  
- **Descripción:** Librería para redes neuronales y deep learning. Permite crear y entrenar modelos de manera flexible.  
- **Instalación:** pip install torch torchvision torchaudio  
- **Funciones útiles:**
  - torch.tensor() – Crea tensores.  
  - torch.nn.Module – Clase base para crear modelos.  
  - torch.optim – Optimizadores como Adam, SGD.  
  - torch.load() / torch.save() – Guardar y cargar modelos.  
  - Operaciones matemáticas: torch.matmul(), torch.mean(), torch.sum().  

---

## 2. Sentence Transformers (sentence-transformers)

- **Autor / Mantenedor:** Hugging Face  
- **Descripción:** Extensión de transformers especializada en generar embeddings para frases, oraciones y documentos.  
- **Instalación:** pip install sentence-transformers  
- **Funciones útiles:**
  - SentenceTransformer('model_name') – Carga un modelo para embeddings.  
  - model.encode(texts) – Convierte texto a vectores.  
  - Compatible con tareas de semantic search y clustering.  

---

## 3. Transformers (transformers)

- **Autor / Mantenedor:** Hugging Face  
- **Descripción:** Librería para usar modelos de lenguaje preentrenados (GPT, BERT, T5, etc.) y tareas de NLP.  
- **Instalación:** pip install transformers  
- **Funciones útiles:**
  - from transformers import AutoModel, AutoTokenizer – Cargar modelos y tokenizadores.  
  - tokenizer(text) – Tokeniza texto.  
  - model.generate(input_ids) – Genera texto a partir de un prompt.  
  - model.forward(inputs) – Obtener salidas del modelo.  

---

## 4. Gradio (gradio)

- **Autor / Mantenedor:** Gradio / Hugging Face  
- **Descripción:** Librería para crear interfaces web interactivas de manera rápida para probar modelos de IA.  
- **Instalación:** pip install gradio  
- **Funciones útiles:**
  - gr.Interface() – Crea interfaces de entrada y salida.  
  - launch() – Ejecuta la app en un servidor local o en la nube.  
  - Soporta inputs como texto, imagen, audio y outputs múltiples.  

---

## 5. Streamlit (streamlit)

- **Autor / Mantenedor:** Streamlit Inc.  
- **Descripción:** Framework para construir aplicaciones web interactivas orientadas a datos y modelos de IA.  
- **Instalación:** pip install streamlit  
- **Funciones útiles:**
  - st.title(), st.header(), st.subheader() – Para títulos y encabezados.  
  - st.text_input(), st.slider() – Inputs del usuario.  
  - st.button() – Botones de acción.  
  - st.write(), st.dataframe() – Mostrar resultados y datos.  
  - st.image(), st.audio(), st.video() – Multimedia.  

---

## 6. LangChain (langchain)

- **Autor / Mantenedor:** LangChain Inc.  
- **Descripción:** Framework para construir agentes, pipelines de prompts y cadenas de herramientas para IA.  
- **Instalación:** pip install langchain  
- **Funciones útiles:**
  - LLMChain – Crea cadenas de prompts con modelos de lenguaje.  
  - Agents – Configura agentes con herramientas externas.  
  - Memory – Permite mantener contexto entre interacciones.  
  - Prompts – Plantillas dinámicas para prompts.  

---

## 7. Numpy (numpy)

- **Autor / Mantenedor:** Comunidad de código abierto  
- **Descripción:** Librería para manejo de arrays, álgebra lineal y operaciones matemáticas.  
- **Instalación:** pip install numpy  
- **Funciones útiles:**
  - np.array() – Crear arrays.  
  - np.dot(), np.matmul() – Producto punto y matrices.  
  - np.mean(), np.sum(), np.std() – Estadísticas básicas.  
  - np.random – Generar números aleatorios.  

---

## 8. Pandas (pandas)

- **Autor / Mantenedor:** Comunidad de código abierto  
- **Descripción:** Librería para manipulación y análisis de datos estructurados (tablas).  
- **Instalación:** pip install pandas  
- **Funciones útiles:**
  - pd.DataFrame() – Crear dataframes.  
  - df.head(), df.tail() – Visualizar filas.  
  - df.describe() – Estadísticas descriptivas.  
  - df.merge(), df.join() – Combinar datasets.  
  - df.groupby() – Agrupar y resumir datos.  

---

Con estas librerías, podrás desarrollar agentes de IA completos, desde la creación y entrenamiento de modelos, hasta la construcción de interfaces y agentes inteligentes interactivos.
