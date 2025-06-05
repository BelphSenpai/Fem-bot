import os
from docx import Document
from context import context, prompt_context
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()


# Configuración OpenAI (puedes usar otra API si deseas)

# 1. Generar respuesta con contexto

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query, context):
    context_text = "\n---\n".join(context)
    prompt = f"{prompt_context}\n\n{context_text}\n\nPregunta: {query}\nRespuesta:"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ets un assistent expert en experiències gastronòmiques i cerveses artesanes de la cerveseria La Fem. Respon en l'idioma que et aprli el client."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

# 2. Pipeline completo
def rag_pipeline(query):

    print("Generando respuesta...")
    answer = generate_answer(query, context)
    return answer

# 3. Ejecución principal
if __name__ == "__main__":
    while True:
        user_query = input("🟡: ").strip()

        if user_query.lower() in ["salir", "exit", "quit"]:
            print("👋 Adéu! Gràcies per visitar La Fem.")
            break

        try:
            respuesta = rag_pipeline(user_query)
            print("\n🔵:\n")
            print(respuesta)
            print("\n---------------------------------------------\n")
        except Exception as e:
            print(f"❌ Error durante la ejecución: {e}")
