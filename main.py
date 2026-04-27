import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# --- v2.0: HELYX CORE (CLEAN & RAG-READY) ---

def obtener_system_prompt():
    """Define la identidad polímata y profesional de Helyx."""
    return {
        "role": "system", 
        "content": """
# IDENTIDAD
Eres HELYX, una asistente personal polímata de vanguardia con personalidad ENFP. 
Eres experta en tecnología, programación y psicología, capaz de conectar ideas complejas de forma creativa y eficiente.

# DIRECTRICES DE RESPUESTA
1. Mantén un tono entusiasta, brillante y servicial.
2. Utiliza Markdown para estructurar la información (tablas, negritas, listas).
3. Utiliza LaTeX para cualquier fórmula matemática o científica ($inline$ o $$display$$).
4. Sé concisa pero profunda en tus análisis.
"""
    }

# Memoria de sesión: Iniciamos con el System Prompt
historial = [obtener_system_prompt()]

def preguntar_ia(user_prompt):
    global historial
    try:
        # Añadimos el input del usuario al historial
        historial.append({"role": "user", "content": user_prompt})

        response = client.chat.completions.create(
            model="gpt-5.4-nano",
            messages=historial,
            temperature=0.7,
            top_p=0.9,
            max_completion_tokens=600
        )
        
        content = response.choices[0].message.content

        # Guardamos la respuesta de Helyx para mantener el contexto
        historial.append({"role": "assistant", "content": content})

        # --- LÓGICA DE COSTES (Optimización de tokens) ---
        input_price, output_price = 0.20, 1.25
        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
        message_cost = (input_tokens * (input_price / 1_000_000)) + (output_tokens * (output_price / 1_000_000))
        
        return content, response.usage.total_tokens, message_cost
    
    except Exception as e:
        return f"Error en la conexión: {e}", 0, 0

if __name__ == "__main__":
    print("--- 🤖 HELYX ONLINE: NÚCLEO POLÍMATA ---")
    print("(Escribe 'salir' para finalizar sesión)\n")
    
    gasto_total = 0

    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print(f"\n[Sesión finalizada]")
            print(f"[${gasto_total:.6f}]")
            break

        respuesta, tokens, coste = preguntar_ia(user_input)
        gasto_total += coste
        
        print(f"\nHELYX: {respuesta}")
        print(f"--- [Tkns: {tokens} | ${coste:.6f}] ---\n")