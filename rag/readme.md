# RAG y Embeddings: Guía Profesional para Python y Agentes 🤖📚

Este documento es parte del curso de Python y agentes, y tiene como objetivo ofrecer una **guía clara y práctica sobre RAG (Retrieval-Augmented Generation) y embeddings**, incluyendo:

- Qué es RAG y cómo funciona.  
- Conceptos clave de embeddings y su relación con LLMs como ChatGPT.  
- Diferencias entre embeddings locales y remotos.  
- Decisiones arquitecturales y bases de datos vectoriales.  
- Casos de uso, limitaciones y riesgos.  

> Nota: Este documento es **teórico**. Los ejemplos prácticos y laboratorios se desarrollarán en secciones posteriores del curso.

---

## 1️⃣ Qué es RAG

**RAG (Retrieval-Augmented Generation)** es un enfoque que combina **recuperación de información** y **generación de texto**.  

En lugar de que un modelo de lenguaje genere respuestas solo con su conocimiento entrenado, RAG le permite **consultar información externa** (documentos, bases de datos, sitios web) para producir respuestas más precisas y actualizadas.  

### 🔹 Cómo funciona a grandes rasgos:

1. El usuario hace una pregunta o prompt.  
2. El sistema **recupera documentos relevantes** usando embeddings.  
3. Un LLM (como ChatGPT) genera la respuesta **basándose en esos documentos recuperados**.  

> Ejemplo conceptual:  
> - Pregunta: “¿Cuáles son los beneficios del lenguaje Python?”  
> - RAG recupera fragmentos de documentación y artículos.  
> - El LLM genera una respuesta completa integrando la información recuperada.  

RAG es especialmente útil para:
- Sistemas de soporte o atención al cliente.  
- Buscadores internos en empresas.  
- Resúmenes automáticos de grandes volúmenes de información.  

---

## 2️⃣ Qué es un Embedding

Un **embedding** es una representación numérica de un texto (palabra, frase o documento) en un **vector de números** en un espacio de alta dimensión.  

### 🔹 Concepto clave
- Palabras o textos **semánticamente cercanos** tienen vectores **cercanos**.  
- Esto permite medir similitud entre textos usando métricas como **distancia euclidiana** o **coseno de similitud**.

### 🔹 Ejemplo conceptual
- “Perro” y “Gato” → vectores cercanos  
- “Perro” y “Avión” → vectores más lejanos  

### 🔹 Para qué sirven los embeddings
- Comparar textos y encontrar similitudes.  
- Recuperar información relevante en RAG.  
- Agrupar documentos por significado.  
- Alimentar modelos de ML o LLMs para mejorar precisión de respuestas.  

> 💡 Nota: Los embeddings **no son texto**, son vectores matemáticos que los modelos pueden usar para medir significado y contexto.

---

## 3️⃣ Relación Embeddings y LLMs (tipo ChatGPT)

Los embeddings y los **LLMs (Large Language Models)** trabajan juntos en un sistema RAG para producir respuestas más precisas y actualizadas.  

### 🔹 Cómo se relacionan
1. **Embeddings**: transforman los documentos y la pregunta del usuario en vectores numéricos.  
2. **Búsqueda semántica**: se comparan los vectores de la pregunta con los vectores de los documentos para **encontrar información relevante**.  
3. **LLM (ChatGPT, GPT-4, etc.)**: recibe los documentos recuperados como contexto y genera la respuesta final.  

### 🔹 Flujo conceptual de RAG

```
Usuario → Pregunta
↓
Embeddings → Búsqueda de documentos relevantes
↓
LLM → Genera respuesta usando contexto recuperado
```

### 🔹 Beneficio de esta combinación
- Un LLM por sí solo responde según su entrenamiento y datos hasta cierta fecha.  
- Con embeddings y recuperación de documentos, el LLM puede **usar información actualizada** y específica del dominio.  
- Mejora la precisión, la relevancia y la confiabilidad de las respuestas.

> 💡 Ejemplo conceptual:  
> - Pregunta: “¿Qué novedades tiene Python 3.12?”  
> - LLM sin RAG → respuesta basada en conocimiento previo (hasta fecha de entrenamiento).  
> - LLM con RAG → busca en documentación reciente y genera respuesta actualizada y precisa.

---

## 4️⃣ Componentes de un sistema de Embeddings

Un sistema de embeddings (y por extensión un sistema RAG) tiene varios componentes clave que trabajan juntos para **recuperar información y generar respuestas precisas**.

### 🔹 1. Motor de embeddings
- Modelo que transforma texto en vectores numéricos.  
- Ejemplos: `Sentence-Transformers`, `OpenAI text-embedding-ada-002`.  
- Determina la calidad de la similitud semántica.

### 🔹 2. Almacenamiento / índice
- Contiene los embeddings de los documentos.  
- Puede ser:
  - **En memoria**: simple pero limitado en escala.  
  - **Base de datos vectorial**: escalable y eficiente (FAISS, Pinecone, Weaviate).  
- Permite búsquedas rápidas de los documentos más relevantes.

### 🔹 3. Mecanismo de búsqueda
- Calcula la **similitud entre la pregunta y los documentos** usando los embeddings.  
- Métricas comunes: coseno de similitud, distancia euclidiana.  
- Devuelve los `top-k` documentos más relevantes.

### 🔹 4. LLM o generador de texto
- Recibe los documentos recuperados como **contexto**.  
- Genera la respuesta final basada en la información más relevante.  

### 🔹 5. Integración con la aplicación
- Interfaz web (Gradio, Streamlit, FastAPI) o chatbot.  
- Permite que el usuario interactúe con el sistema RAG de forma fácil y directa.

> 💡 Nota: Cada componente se puede reemplazar o mejorar según la escala, privacidad y recursos disponibles.

---

## 5️⃣ Embeddings locales vs remotos

Al implementar RAG, los embeddings pueden generarse **localmente** o mediante un **servicio remoto**. Cada enfoque tiene ventajas y desventajas según la escala, privacidad y costos.

### 🔹 Embeddings locales
- Se ejecutan en tu propio hardware usando modelos descargados.  
- Ejemplos: `Sentence-Transformers`, `Hugging Face Transformers`.  
- **Ventajas**:
  - Total control sobre los datos y la privacidad.  
  - Sin costos por API externa.  
  - Respuestas rápidas para volúmenes pequeños o medianos.  
- **Desventajas**:
  - Limitado por la memoria y capacidad de cómputo.  
  - Dificultad para manejar millones de documentos.

### 🔹 Embeddings remotos
- Se generan mediante un **servicio en la nube** (API).  
- Ejemplos: OpenAI (`text-embedding-ada-002`), Cohere, Anthropic.  
- **Ventajas**:
  - Escalable a grandes volúmenes de datos.  
  - Modelos actualizados y optimizados por el proveedor.  
- **Desventajas**:
  - Costo por uso de API.  
  - Latencia dependiente de la red.  
  - Datos sensibles deben enviarse a terceros (considerar privacidad).

> 💡 Tip: Para proyectos educativos o prototipos, lo local suele ser suficiente. Para producción con gran cantidad de documentos, los embeddings remotos son más prácticos.

---

## 6️⃣ Librerías de embeddings locales

Las librerías locales permiten generar embeddings sin depender de servicios externos, usando tu propio hardware. Son ideales para **proyectos educativos, prototipos o sistemas que requieren privacidad**.

### 🔹 1. Sentence-Transformers
- **Descripción**:  
  Basada en Hugging Face Transformers, la librería `Sentence-Transformers` facilita la generación de embeddings de alta calidad para frases, oraciones o documentos. Permite buscar similitudes semánticas, agrupar textos y construir sistemas RAG locales.
- **Instalación**:  
  pip install sentence-transformers
- **Uso en Python**:  
  from sentence_transformers import SentenceTransformer
  modelo_embeddings = SentenceTransformer('all-MiniLM-L6-v2')
  embeddings = modelo_embeddings.encode(["Texto de ejemplo"], convert_to_tensor=True)
- **Modelos populares disponibles**:  
  - all-MiniLM-L6-v2 → rápido y liviano  
  - all-MPNet-base-v2 → muy buena calidad semántica  
  - paraphrase-MiniLM-L6-v2 → ideal para detectar similitudes de frases  
  - paraphrase-mpnet-base-v2 → alta precisión en similitud  
  - multi-qa-MiniLM-L6-cos-v1 → optimizado para preguntas y respuestas  

> 💡 Tip: Sentence-Transformers combina facilidad de uso con rendimiento, y es la librería más usada para prototipos de RAG locales.

### 🔹 2. Hugging Face Transformers
- **Descripción**:  
  Librería oficial de Hugging Face, que incluye modelos de lenguaje preentrenados como BERT, RoBERTa, DistilBERT o MPNet. Permite generar embeddings, ajustar modelos y realizar tareas de NLP avanzadas.
- **Instalación**:  
  pip install transformers
- **Uso en Python (ejemplo básico)**:  
  from transformers import AutoTokenizer, AutoModel
  tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
  model = AutoModel.from_pretrained('distilbert-base-uncased')
  inputs = tokenizer("Texto de ejemplo", return_tensors="pt")
  outputs = model(**inputs)
  embeddings = outputs.last_hidden_state.mean(dim=1)

### 🔹 3. spaCy
- **Descripción**:  
  Librería de NLP ligera y rápida. Algunos modelos permiten generar vectores de palabras, frases o documentos. Ideal para prototipos o sistemas donde no se requiere máxima precisión semántica.
- **Instalación**:  
  pip install spacy
  python -m spacy download en_core_web_md
- **Uso en Python**:  
  import spacy
  nlp = spacy.load("en_core_web_md")
  doc = nlp("Texto de ejemplo")
  embeddings = doc.vector

> 💡 Nota: spaCy es rápido y sencillo, pero menos potente que Sentence-Transformers para búsquedas semánticas profundas.

---

## 7️⃣ Librerías de embeddings remotos

Los embeddings remotos se generan mediante **servicios en la nube**, lo que permite escalar a grandes volúmenes de documentos y acceder a modelos optimizados, aunque con un costo y dependencia de conexión.  

### 🔹 1. [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- **Descripción**:  
  OpenAI ofrece modelos de embeddings de alta calidad, como `text-embedding-ada-002`. Permite generar vectores semánticos para frases, documentos o preguntas, y es ampliamente usado en RAG y sistemas de búsqueda inteligente.  
- **Instalación**:  
  pip install openai
- **Uso en Python**:  
  import openai  
  openai.api_key = "TU_API_KEY"  
  response = openai.Embedding.create(  
      model="text-embedding-ada-002",  
      input="Texto de ejemplo"  
  )  
  embedding = response['data'][0]['embedding']  
- **Modelos populares**:  
  - text-embedding-ada-002 → recomendado para la mayoría de casos  
  - text-embedding-3-large → mayor precisión y dimensionalidad  
  - text-embedding-3-small → rápido y económico  

### 🔹 2. [Cohere Embeddings](https://cohere.ai/docs/embed)
- **Descripción**:  
  Cohere ofrece modelos de embeddings para similitud semántica, búsqueda y clasificación. Se usa mediante API remota y permite integración rápida en Python.  
- **Instalación**:  
  pip install cohere
- **Uso en Python**:  
  import cohere  
  co = cohere.Client("TU_API_KEY")  
  response = co.embed(texts=["Texto de ejemplo"], model="small")  
  embedding = response.embeddings[0]  
- **Modelos populares**:  
  - small → rápido y eficiente  
  - medium → balance entre velocidad y precisión  
  - large → máxima precisión, mayor costo

### 🔹 3. [Anthropic / Claude Embeddings](https://www.anthropic.com/index/embeddings)
- **Descripción**:  
  Anthropic ofrece embeddings vía su API, orientados a sistemas de RAG y agentes inteligentes.  
- **Instalación**:  
  pip install anthropic
- **Uso en Python (ejemplo conceptual)**:  
  import anthropic  
  client = anthropic.Client("TU_API_KEY")  
  response = client.embeddings.create(model="claude-embedding-1", input="Texto de ejemplo")  
  embedding = response['embedding']  

> 💡 Nota: Los embeddings remotos son **mantenidos y actualizados por el proveedor**, ideales para proyectos con grandes volúmenes de información y necesidades de precisión.  

---

## 8️⃣ Decisiones arquitecturales al hacer un agente que usa embeddings

Al diseñar un agente o sistema RAG, es importante tomar decisiones estratégicas sobre **dónde y cómo almacenar los embeddings** y cómo integrarlos con el LLM. Estas decisiones impactan en **velocidad, escalabilidad, costo y privacidad**.

### 🔹 1. Memoria vs base de datos vectorial
- **En memoria**:
  - Ideal para pocos documentos o prototipos.  
  - Búsqueda rápida, simple de implementar con `Sentence-Transformers` y listas en Python.  
  - Limitado por memoria RAM y cantidad de documentos.  
- **Base de datos vectorial**:
  - Escalable a millones de documentos.  
  - Permite búsquedas aproximadas (ANN) eficientes y rápidas.  
  - Ejemplos: [FAISS](https://github.com/facebookresearch/faiss), [Pinecone](https://www.pinecone.io/), [Weaviate](https://weaviate.io/), [Qdrant](https://qdrant.tech/).

### 🔹 2. Frecuencia de actualización de embeddings
- Documentos estáticos → embeddings generados una vez.  
- Documentos dinámicos → se deben actualizar embeddings regularmente para reflejar nueva información.

### 🔹 3. Elección del modelo de embeddings
- Modelos livianos (MiniLM) → rápidos, menos recursos, suficiente para prototipos.  
- Modelos grandes (MPNet, OpenAI embeddings) → más precisos, mayor costo y consumo de recursos.

### 🔹 4. Privacidad y seguridad de datos
- Embeddings locales → control total de la información.  
- Embeddings remotos → cuidado con enviar datos sensibles a servicios de terceros.  
- Considerar **encriptación y anonimización** cuando sea necesario.

### 🔹 5. Integración con LLM
- Definir cómo el agente pasará el **contexto recuperado** al LLM:  
  - Número de documentos (top-k)  
  - Longitud máxima de tokens  
  - Formato del prompt para generar la respuesta

> 💡 Tip: Las decisiones arquitecturales dependen de **escala, presupuesto, privacidad y objetivos de tu proyecto**. Para prototipos educativos, memoria + Sentence-Transformers suele ser suficiente. Para producción, conviene usar DB vectorial y embeddings remotos escalables.

---

## 9️⃣ Bases de datos de embeddings

Las bases de datos vectoriales permiten **almacenar y buscar embeddings** de manera eficiente. Dependiendo de tus necesidades, pueden ser **locales gratuitas**, **remotas de pago**, o incluso **bases de datos tradicionales con soporte de vectores**.

### 🔹 1. FAISS (Facebook AI Similarity Search)  
- [Repositorio oficial](https://github.com/facebookresearch/faiss)  
- Open source y local, funciona offline.  
- Muy rápido para búsquedas aproximadas en millones de vectores.  
- Ideal para prototipos y proyectos donde controlas el hardware.  

### 🔹 2. Annoy (Approximate Nearest Neighbors Oh Yeah)  
- [Repositorio oficial](https://github.com/spotify/annoy)  
- Open source, local y liviano.  
- Optimizado para memoria y velocidad en búsquedas aproximadas.  
- Bueno para prototipos y sistemas medianos.  

### 🔹 3. HNSWLib  
- [Repositorio oficial](https://github.com/nmslib/hnswlib)  
- Open source, local, basado en grafos HNSW para búsquedas rápidas.  
- Excelente performance incluso en grandes colecciones de vectores.  

### 🔹 4. Qdrant  
- [Sitio oficial](https://qdrant.tech/)  
- Puede instalarse localmente **gratis** o usar versión cloud de pago.  
- Optimizado para búsquedas semánticas y escalable a millones de vectores.  

### 🔹 5. Pinecone  
- [Sitio oficial](https://www.pinecone.io/)  
- Vector DB remota, totalmente administrada y escalable.  
- Plan gratuito limitado; producción paga según almacenamiento y consultas.  

### 🔹 6. Weaviate  
- [Sitio oficial](https://weaviate.io/)  
- Disponible como versión cloud de pago o open source local.  
- Permite búsquedas vectoriales y combinación con NLP / LLMs.  

### 🔹 7. PostgreSQL + pgvector  
- [Repositorio pgvector](https://github.com/pgvector/pgvector)  
- Extensión para PostgreSQL que permite almacenar embeddings y realizar búsquedas de similitud.  
- Ideal si ya usas PostgreSQL y quieres integrar vectores sin instalar otra base de datos.  
- Limitaciones: rendimiento menor para millones de vectores comparado con FAISS o Pinecone.  
- Ejemplo conceptual de búsqueda:  
  SELECT *  
  FROM documentos  
  ORDER BY embedding <-> '[vector del query]'::vector  
  LIMIT 5;

### 🔹 Resumen y recomendaciones
- **Local / Gratuito**: FAISS, Annoy, HNSWLib, Qdrant local → prototipos, laboratorios, control total de datos.  
- **Remoto / Pago**: Pinecone, Weaviate Cloud, Qdrant Cloud → producción, escalabilidad masiva, mantenimiento mínimo.  
- **Integración con DB tradicional**: PostgreSQL + pgvector → proyectos medianos, fácil integración si ya usas Postgres.

> 💡 Tip: La elección depende de **escala, presupuesto, privacidad y objetivos del proyecto**.

---

## 1️⃣0️⃣ 🔹 Embeddings en la nube y servicios administrados

Además de usar librerías locales o bases de datos vectoriales, muchas plataformas en la nube ofrecen **servicios de embeddings y búsqueda vectorial** listos para producción. Esto permite escalar rápidamente y aprovechar modelos optimizados sin preocuparse por mantenimiento.

### 1️⃣ Azure Cognitive Search + Azure OpenAI
- [Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)  
- Permite **almacenar documentos y buscar embeddings vectoriales**.  
- Integración con [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) para generar embeddings y texto con LLMs como GPT-4.  
- Ventajas:
  - Indexación automática de documentos.  
  - Búsqueda vectorial combinada con filtros semánticos.  
  - Escalable y seguro, ideal para empresas que ya usan Azure.  
- Ejemplo conceptual:
  - Subir documentos → generar embeddings con OpenAI → almacenar en Cognitive Search → búsqueda semántica para RAG.

### 2️⃣ AWS (Amazon Kendra / Bedrock)
- [Amazon Kendra](https://aws.amazon.com/kendra/) → servicio de búsqueda empresarial con soporte vectorial.  
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) → permite usar LLMs y generar embeddings sin gestionar infraestructura.  
- Ventajas:
  - Escalable y administrado por AWS.  
  - Integración con otras bases de datos y S3 para documentos.  
  - Permite pipelines de RAG completamente en la nube.  

### 3️⃣ Google Cloud (Vertex AI / Generative AI)
- [Vertex AI](https://cloud.google.com/vertex-ai) y [Generative AI Studio](https://cloud.google.com/vertex-ai/docs/generative-ai/overview)  
- Permite generar embeddings y hacer búsqueda vectorial sobre documentos.  
- Integración directa con otros servicios de Google Cloud (BigQuery, Storage).  
- Ventajas:
  - Modelos de última generación optimizados por Google.  
  - Fácil escalado y seguridad empresarial.  

### 🔹 Resumen
- Estos servicios son **de pago**, pero eliminan la necesidad de instalar y mantener infraestructura propia.  
- Recomendado si:
  - Quieres producción escalable y segura.  
  - Necesitas integración rápida con LLMs y otras herramientas de la nube.  
- Puedes combinar estos servicios con bases de datos vectoriales locales para prototipos o pruebas.

> 💡 Tip: Si ya trabajás con Azure, AWS o Google Cloud, usar sus servicios administrados de embeddings y búsqueda vectorial **acelera la implementación de sistemas RAG** sin preocuparte por optimización de índices o mantenimiento.

---

## 1️⃣1️⃣ Casos de uso, limitaciones y riesgos

### 🔹 Casos de uso de RAG y embeddings

1. **Sistemas de soporte al cliente**  
   - Chatbots que buscan respuestas precisas en documentación interna.  
   - Ejemplo: atención automatizada en portales de ayuda.

2. **Búsqueda semántica en documentos**  
   - Recuperar información relevante en grandes repositorios de texto.  
   - Ejemplo: consultas legales, artículos científicos, manuales técnicos.

3. **Agentes inteligentes / asistentes personales**  
   - Integración de LLMs con documentos propios para generar respuestas personalizadas.  
   - Ejemplo: asistentes corporativos que responden según políticas internas.

4. **Resumen de información y análisis de contenido**  
   - Generación de resúmenes a partir de múltiples fuentes relevantes.  
   - Ejemplo: informes ejecutivos automáticos, análisis de noticias.

---

### 🔹 Limitaciones

- **Dependencia del LLM**: la calidad de la respuesta depende del modelo que uses.  
- **Cobertura de documentos**: si la base de embeddings no incluye información relevante, la respuesta puede ser incompleta o incorrecta.  
- **Tamaño del contexto**: los LLMs tienen límite de tokens; si recuperas demasiados documentos, es necesario resumir o priorizar.  
- **Costo**: embeddings remotos y bases de datos vectoriales en la nube pueden generar gastos significativos en producción.

---

### 🔹 Riesgos

- **Privacidad y seguridad de datos**: enviar información sensible a servicios remotos puede ser riesgoso.  
- **Sesgo y confiabilidad**: los LLMs pueden generar respuestas sesgadas o incorrectas incluso con contexto relevante.  
- **Mantenimiento y actualización**: los documentos cambian con el tiempo; si los embeddings no se actualizan, la información queda obsoleta.

> 💡 Tip: Mitigar riesgos requiere combinar buenas prácticas de **seguridad de datos**, **curación de documentos** y **pruebas periódicas de las respuestas del agente**.

---

## 1️⃣2️⃣ Conclusiones

- **RAG (Retrieval-Augmented Generation)** permite que los LLMs generen respuestas precisas usando información externa y actualizada.  
- Los **embeddings** son la base para medir similitud semántica y recuperar documentos relevantes.  
- Existen **librerías locales** (Sentence-Transformers, Hugging Face, spaCy) y **servicios remotos** (OpenAI, Cohere, Anthropic), cada uno con ventajas según privacidad, escala y costos.  
- La **elección de la base de datos** (FAISS, PostgreSQL, Pinecone, Weaviate, etc.) depende de volumen de datos, necesidades de búsqueda, escalabilidad y presupuesto.  
- Los **servicios en la nube** (Azure, AWS, Google Cloud) permiten integración rápida y escalable, ideal para producción.  
- Antes de implementar RAG, es importante considerar **casos de uso, limitaciones y riesgos**, incluyendo privacidad, sesgo y mantenimiento de datos.

> 💡 Recomendación final:  
> Para prototipos y laboratorios educativos, **embeddings locales + memoria o PostgreSQL** suelen ser suficientes.  
> Para sistemas de producción con grandes volúmenes y necesidades de escalabilidad, conviene usar **bases de datos vectoriales administradas y servicios de embeddings en la nube**.

Este documento sirve como **guía completa para entender RAG y embeddings**, y sienta las bases para los laboratorios prácticos de Python y agentes que siguen en el curso.
