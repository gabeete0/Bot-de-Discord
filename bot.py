import discord
import requests
import json
import os  # Permite interactuar con el sistema operativo
from dotenv import load_dotenv  # Carga las variables desde tu archivo .env

# 1. Cargar las variables ocultas del archivo .env
load_dotenv()

# 2. Función que consulta la API y obtiene el meme de Reddit
def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        return json_data['url']
    except Exception as e:
        print(f"Error al obtener el meme: {e}")
        return "No pude cargar el meme en este momento, intenta de nuevo."

# 3. Clase principal para controlar los eventos del Bot
class MyClient(discord.Client):
    # Evento: Se ejecuta cuando el bot logra iniciar sesión con éxito
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # Evento: Se ejecuta cada vez que alguien escribe en un canal
    async def on_message(self, message):
        # Evita que el bot se responda a sí mismo en un bucle infinito
        if message.author == self.user:
            return

        # Comando de saludo sencillo
        if message.content.startswith('$hello'):
            await message.channel.send('¡Hola! El bot está online y escuchando perfectamente. 🤖')

        # Comando para enviar el meme aleatorio
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# 4. Configurar los Intents (Permisos de lectura del bot)
intents = discord.Intents.default()
intents.message_content = True

# 5. Inicializar el cliente pasándole los permisos configurados
client = MyClient(intents=intents)

# 6. Arrancar el bot llamando de forma segura al token guardado en el .env
client.run(os.getenv('DISCORD_TOKEN'))