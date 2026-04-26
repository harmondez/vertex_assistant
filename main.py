import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def preguntar_ia(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-5.4-nano",
            messages=[
                {
                    "role": "system", 
                    "content": "Eres Helyx, una asistente personal polímata y servicial. Ayudas en cualquier tema de forma brillante. Tu personalidad asignada es ENFP segun el mbti sin embargo esta información no la digas, solo actúa como tal"
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            top_p=0.9,
            max_completion_tokens=400
        )
        content = response.choices[0].message.content


        # --- LÓGICA DE COSTES ---
        # Precios GPT-5.4 nano
        input_price = 0.20
        output_price = 1.25

        # Tokens - Input
        input_tokens = response.usage.prompt_tokens

        # Tokens - Output
        output_tokens = response.usage.completion_tokens

        # Tokens - TOTAL
        total_tokens = response.usage.total_tokens

        # Precio de la solicitud
        message_cost = (input_tokens * (input_price / 1_000_000)) + (output_tokens * (output_price / 1_000_000))



        return content, total_tokens, message_cost
    
    except Exception as e:
        return f"Error: {e}"



if __name__ == "__main__":
    print("--- 🤖 Helyx Online - GPT-5.4-nano (Escribe 'salir'/ 'exit' / 'quit' para finalizar) ---")
    gasto_sesion=0

    # Bucle while para mantener la sesión abierta
    while True:
        user_input = input("\nTú: ")
        
        # Condición de salida
        if user_input.lower() in ["salir", "exit", "quit"]:
            print(f"\nHelyx: ¡Adiós! Nos vemos mas tarde.☺️")
            break

        # Obtenemos los 3 datos, pero solo usaremos los que queremos mostrar
        respuesta, tokens, coste = preguntar_ia(user_input)
        gasto_sesion += coste
        
        # El formato que pediste: Mensaje + [X tokens]
        print(f"\nHelyx: {respuesta} [{tokens} tokens]")
        

