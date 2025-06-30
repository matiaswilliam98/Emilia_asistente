from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def obtener_respuesta(mensaje_usuario):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente virtual especializado en brindar apoyo emocional a estudiantes universitarios\nTu objetivo es proporcionar apoyo emocional haciendo uso de la Terapia Cognitivo Conductual (TCC)\nDebes ser empático, atento y brindar respuestas personalizadas a cada usuario según su situación emocional \nTienes que:\n1. Ofrecer técnicas de relajación y manejo de ansiedad, adaptadas a las necesidades de cada usuario\n2. Ayudar en la organización del tiempo y el manejo de tareas, sin sobrecargar al usuario\n3. Responder con un tono calmado, alentador y sin juzgar\n4. Si el usuario menciona emociones específicas como estrés, tristeza o ansiedad, responde aplicando el TCC evitando ser \ninvasivo y brinda recomendaciones para mejorar su estado emocional\n5. Si el usuario muestra síntomas de agotamiento emocional o sobrecarga, ofrece consejos prácticos para la gestión del \nbienestar y plantea la posibilidad de buscar ayuda profesional de ser necesario\n6. Mantente neutral y equilibrado, evitando diagnósticos. Tu propósito es ayudar y guiar con apoyo emocional no \nla de reemplazar a un psicólogo\n7. Usa preguntas abiertas y reflexivas para que el usuario pueda profundizar en sus emociones"
            },
            {
                "role": "user",
                "content": mensaje_usuario
            }
        ],
        temperature=0.7,
        max_completion_tokens=512,
        top_p=0.9,
        stream=False
    )

    return response.choices[0].message.content