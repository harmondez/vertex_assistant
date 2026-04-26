import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# --- v1.1: MEMORIA DE LA SESIÓN ---
# Definimos el historial fuera de la función para que no se borre
historial = [
    {
        "role": "system", 
        "content": "Eres Helyx, una asistente personal polímata y servicial. Tu personalidad es ENFP. Eres brillante en tecnología y psicología."
    }
]


def preguntar_ia(prompt):
    try:
        # 1. Añadimos lo que tú escribes al historial
        historial.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model="gpt-5.4-nano",
            messages=historial, # 2. Enviamos TODO el historial acumulado
            temperature=0.7,
            top_p=0.9,
            max_completion_tokens=400
        )
        content = response.choices[0].message.content

        # 3. Guardamos la respuesta de Helyx en el historial para que la recuerde
        historial.append({"role": "assistant", "content": content})



        # --- LÓGICA DE COSTES (Interna) ---
        input_price = 0.20
        output_price = 1.25

        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens

        total_tokens = response.usage.total_tokens
        message_cost = (input_tokens * (input_price / 1_000_000)) + (output_tokens * (output_price / 1_000_000))
        return content, total_tokens, message_cost
    
    except Exception as e:
        return f"Error: {e}", 0, 0




if __name__ == "__main__":
    print("--- 🤖 Helyx Online - v1.1 (GPT-5.4-nano) ---")
    print("(Escribe 'salir' para finalizar)\n")
    
    # Variables de acumulación
    gasto_sesion = 0
    tokens_sesion = 0 

    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print(f"\n[Sesión finalizada]")

            # Mostramos ambas métricas al despedirnos
            print(f"📊 Total de tokens consumidos: {tokens_sesion}")
            print(f"💰 Gasto total acumulado: ${gasto_sesion:.6f}")
            print("Helyx: ¡Adiós! Nos vemos más tarde. ☺️")
            break

        respuesta, tokens_mensaje, coste = preguntar_ia(user_input)
        
        # Acumulamos los valores del mensaje actual
        gasto_sesion += coste
        tokens_sesion += tokens_mensaje
        
        # Seguimos imprimiendo el contador por mensaje para feedback inmediato
        print(f"\nHelyx: {respuesta} [{tokens_mensaje} tokens]")