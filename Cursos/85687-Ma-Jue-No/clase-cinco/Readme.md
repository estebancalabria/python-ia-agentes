# Clase Cinco - 5 de Marzo del 2026

# Repaso

* RAG
  * Conceptos
    * Embedings: https://projector.tensorflow.org/
  * python
      * sentence-transformer
          * util ----> cos_sin
      * toch (una librerias para manejos de vectores que se usa para implementar redes neuronales)
  * Bases de Datos Vectoriales
      * Faiss
      * ChromaDB
      * Postgres
          * Supabase
      * Azure : Cognitive Search

# Uso de API

* Temperatura : Valor que se le puede pasar al llm para controlar cuan creativo (Probabilidad)
  * 0 : Practicamente deterministico, siempre responde igual
     * Generalmente para chatbots enterprise si quiero previsibilidad en la respuestas se usan temperaturas bajas 0.1
  * 2 : Super creativo
* TopP : Determina la cantidad de palabras posibles a elegir (Cantidad de palabras posibles)
  * 0 : Elije 1 sola palabria posible siguiente
  * 1 : Muchas proximas paalabras posible

# Links Utiles

* https://gallantlab.org/viewer-huth-2016/

---

# Rag

## Buenas Practicas

* A la hora de armar un RAG es muy comun tener un documento con FAQ de respuestas conocidas, esperadas, deseables de como respode el agente
* Hay que estudiar como dividir un documento grade en chunks que tengan sentidos
   * Como referencia que cada chunk tenga alrededor de 500 palabras
   * Cada chunk en lo posible tiene que ser autocontenido y tener sentido
   * IDEA: Por ejemplo usando la IA para generar los chunks
* Preprocesar el documento para ordenarlo y eliminar, caraceres especiales, html residual, salto de linea invalidos

## Chunks

## Base de Datos Vectoriales



