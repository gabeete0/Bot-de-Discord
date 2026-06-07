import discord
import requests
import json

# 1. Función para obtener el meme de internet
def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme')
        json_data = json.loads(response.text)
        return json_data['url']
    except Exception as e:
        return "No pude cargar el meme en este momento, intenta de nuevo."

# 2. Clase del cliente de Discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # Importante: Evita que el bot se responda a sí mismo
        if message.author == self.user:
            return

        # Comando de prueba 1
        if message.content.startswith('$hello'):
            await message.channel.send('¡Hola! El bot funciona perfectamente. status: ok')

        # Comando de prueba 2
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# 3. Configuración de permisos de lectura de mensajes
intents = discord.Intents.default()
intents.message_content = True

# 4. Encender el bot
client = MyClient(intents=intents)
client.run('MTUxMzI2MDYwMjA1MzYyNzk2NA.GA7Ea5.2WbWRCqWFzrNRqucYYS0XfO2uu2jMdExk33I7I') 