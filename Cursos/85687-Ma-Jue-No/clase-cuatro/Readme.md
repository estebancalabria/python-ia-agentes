# Clase Cuatro - 3 de Marzo del 2026

# Repaso

* Estuvimos programando!
* Iterfaz de Gradio
    * Integramos con un LLM
    * La integramos con un buen System Prompt
* Kaggle
* Usar modelos de Hugging Face
  * El boton "Use in colab"
    * Usamos el GPT2

# RAG (Retival Augmented Generation)

> https://www.instagram.com/p/DVcBRoGFS8a/?img_index=1

Ejemplo de RAG:

```
D1: (perro)  -> [1,1,1,1,1]
D2: (can)    -> [1,1,1,1,0.999]
D3: (el perro de mi abuela es muy grande y se llama Alberto)  ->  [1,1,2,3,4]
D4: (juan es un cabron) -> [5,5,5,5,5]

PROMPT ORIGINAL: (Cual es el major amigo del hombre?) -> [1,1,1,1,0.7]

(Busco documentos relacionados)

PROMTP MODIFICADO :La pregunta es "Cual es el major amigo del hombre?" , los documentos relacionados a la pregunt son {D1,D2,D3} <<< NUEVO PROMP

Respuesta : El mejor amigo del hombre es el perro, como el perro de tu abuela que se llama Alberto
```

* Tenemos
   * RAG (Retrival Augmented Generation)
      * Desventajas : Para cada consulta tenes que calcularle el embeding si usas modelos remotos
         * Le pagas x2 : El calculo de embeding y las consultas
   * Optimizaciones
      * CAG (Context Augmented Generation)
         * OJO, si todos los documentos de tu charbot ENTRAN en la ventana de contexto, no lo gusardes en una base vectorial, metelos como parte del system prompt
      * CAG (Cache Augmented Generation)
         * Cachea las respuestas generadas

* NotebookLM tiene una arquitectura asi por Dentro

```python
from sentence_transformers import SentenceTransformer, util
import torch

documentos = [
    "Python es un lenguaje de programación de alto nivel",
    "Python se utiliza en una amplia variedad de aplicaciones",
    "Donald Trump ataca a Bolivia y se hace con el control de Suamerica",
    "Los animales son buenos"
]

modelo_embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = modelo_embeddings.encode(documentos)

pregunta = input("Ingrese su pregunta:")
embedding_pregunta = modelo_embeddings.encode(pregunta)

similitudes = util.cos_sim(embedding_pregunta, embeddings)[0]
top_resultados = torch.topk(similitudes, 1)
contexto = "\n".join([documentos[i] for i in top_resultados.indices])

print(contexto)
```
  
# Fine Tunning

* Bueno si quiero puedo evitar usar RAG y hacer FINE TUNNING
* ES costosisimo!
* Ver canal
   * https://www.youtube.com/@machinelearnear
      * https://www.youtube.com/watch?v=bIZMgHK8Y-8


# System prompts

Hay repos con Leaks de System Prompts como este:
> https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-in-chrome.md

# Despliegue de Agentes

* Se despliegan como una app cualquiera en un hosting que soporte python
* https://www.instagram.com/p/DOKQgB3jpFQ/?img_index=1
