# Helyx Assistant 🤖

![Helyx Banner](https://i.imgur.com/6srNuej.png) 


**Helyx** es un asistente personal polímata diseñado para adaptarse dinámicamente a cualquier necesidad del usuario. Desde resolución de problemas técnicos complejos hasta apoyo consultivo en diversas áreas del conocimiento.

---

## 🪵 Registro de Evolución (Changelog)

En esta sección se detallan las actualizaciones y mejoras críticas de **Helyx**.

| Versión | Hito | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **v1.0** | **The Core** | Versión fundacional: Conexión base con GPT-4o-mini, identidad de Vertex establecida y bucle de chat infinito. | ✅ Estable |
| **coming soon** | **RAG Engine** | Implementación de ingesta de documentos locales y base de datos vectorial para consultas contextuales. | 🛠️ En desarrollo |
| **coming soon** | **Memory Pro** | Persistencia de memoria a corto plazo y gestión de contexto avanzado. | 🛠️ En desarrollo |

---

### 🔍 Detalle de la Versión Actual: v1.0 (The Core)
*Es el motor primario sobre el que se construye Vertex.*
- **Personalidad:** Configuración de identidad "Vertex" vía System Prompt.
- **Seguridad:** Aislamiento de API Keys mediante `.env`.
- **Control Técnico:** Optimización de respuesta con `temperature=0.7` y `top_p=0.9`.
- **Interactividad:** Interfaz de línea de comandos (CLI) con normalización de salida.

## 🛠️ Stack Tecnológico
* **Language:** Python 3.x
* **AI Engine:** OpenAI API (GPT-4o-mini)
* **Environment:** Virtualenv & Dotenv

## 📋 Instalación Rápida

Sigue estos pasos para desplegar tu propia instancia de **Helyx** en local:

1. **Clonar el repositorio:**
   
    git clone [https://github.com/harmondez/helyx_assistant.git](https://github.com/harmondez/helyx_assistant.git)
    
    cd vertex_assistant

2. **Instalar dependencias:**
    pip install -r requirements.txt

3. **Configuración de credenciales:**
    -Localiza el archivo .env.example en la raíz del proyecto.

    -Renómbralo a .env

    -Abre el archivo y sustituye TU_API_KEY_AQUI por tu clave de OpenAI (requerida para este asistente).

4. **DISFRUTA DE TU ASISTENTE!💪🤓**


---

## 👨‍💻 Sobre el Autor

> **Hernán** | *Prompt Engineer*
> 
> Vertex Assistant es mi primer proyecto enfocado en la arquitectura **RAG** (Retrieval-Augmented Generation). Este repositorio nace de la búsqueda por crear una herramienta polímata, funcional y escalable, aplicando las mejores prácticas de ingeniería de prompts y desarrollo de agentes de IA.