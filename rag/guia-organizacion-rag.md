# Guía práctica para preparar documentos para RAG

Esta guía resume las **buenas prácticas y recomendaciones** para generar y organizar documentos listos para un sistema RAG (Retrieval-Augmented Generation).  

---

## 1️⃣ Tamaño y granularidad de los documentos
- Dividir el contenido en **chunks o fragmentos pequeños**, entre **100 y 500 palabras** (aprox. 500–1000 tokens).  
- Cada chunk debe ser **autocontenido**, con sentido completo sin depender de otros fragmentos.  
- Evitar fragmentos demasiado grandes o demasiado pequeños para mantener relevancia y contexto.

---

## 2️⃣ Limpieza y normalización
- Quitar elementos irrelevantes: menús, headers, footers, publicidad, boilerplate.  
- Normalizar texto: eliminar saltos de línea innecesarios, caracteres especiales o HTML residual.  
- Mantener formato semántico cuando sea útil: párrafos, listas, títulos.

---

## 3️⃣ Estructuración y metadatos
- Incluir **información adicional útil** en cada chunk:
  - Fuente o URL del documento.  
  - Fecha de publicación o versión.  
  - Sección o categoría temática.  
- Los metadatos facilitan mostrar el origen de la información y mejorar el ranking de resultados.

---

## 4️⃣ Organización temática
- Categorizar o etiquetar documentos por tema.  
- Facilita filtrado antes de la búsqueda y evita que el modelo mezcle contextos distintos.

---

## 5️⃣ Optimización para embeddings
- Antes de generar embeddings:  
  - Eliminar redundancias.  
  - Evitar frases ambiguas o fuera de contexto.  
  - Usar oraciones claras y completas para que la semántica se capture mejor.

---

## 6️⃣ Actualización y mantenimiento
- Reindexar únicamente los documentos modificados.  
- Evitar reindexar todo por cambios menores.  
- Mantener sincronía entre contenido y embeddings para asegurar precisión.

---

## 7️⃣ Separación de chunks
- **Por longitud:** dividir cada N palabras o tokens.  
- **Por separador:** usar un carácter o secuencia como "----" para separar secciones naturalmente.  
  - Ejemplo de documento con separadores:

----
Introducción al software
El software es un conjunto de instrucciones...
----
Historia del software
Desde los años 50...
----
Tipos de software
Existen aplicaciones, sistemas operativos...
----

- Consideraciones al usar separadores:  
  - Evitar que el separador aparezca dentro del texto normal.  
  - Si un chunk es muy largo, se puede dividir en sub-chunks para optimizar embeddings.  
  - Limpiar los separadores antes de generar embeddings.

---

## 8️⃣ Buenas prácticas finales
- Fragmentar PDFs, artículos largos o documentación técnica para que cada chunk sea autocontenido.  
- Representar correctamente tablas o código, considerando cómo los interpretará el LLM.  
- Para FAQs, separar cada pregunta-respuesta en chunks individuales para mejorar precisión.  
- Mantener consistencia y claridad en cada chunk para facilitar la búsqueda y la generación de respuestas.

---

**Resumen:** un buen documento RAG es **pequeño, limpio, autocontenido, con metadatos, organizado temáticamente y optimizado para embeddings**, listo para generar respuestas precisas y contextuales con un LLM.