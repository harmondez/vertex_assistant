import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def preguntar_ia(prompt):
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "Eres Vertex, un asistente personal polímata y servicial. Ayudas en cualquier rama (tecnología, psicología, etc.) de forma brillante."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            top_p=0.9
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("--- 🤖 Vertex Online (Escribe 'salir'/ 'exit' / 'quit' para finalizar) ---")
    
    # Bucle infinito
    while True:
        user_input = input("\nTú: ")
        
        # Condición de salida
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Vertex: ¡Hasta pronto! Un placer ayudarte.")
            break
            
        resultado = preguntar_ia(user_input)
        print(f"\nVertex: {resultado}")