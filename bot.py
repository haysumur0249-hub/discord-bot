import discord
from discord.ext import tasks

TOKEN = 'MTQ4NTkyMjM1MzMzMzUzODg1Ng.G8mkxU.B6Uy0eD08lXa4cb5-Nk90pP9VgHqMvCulLWBUI'
CHANNEL_ID = 1455257168562356408

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_message(content):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(content)

@tasks.loop(seconds=30)
async def msg_30s():
    await send_message("OH")

@tasks.loop(minutes=5)
async def msg_5m():
    await send_message("O PRAY")

@tasks.loop(hours=24)
async def msg_24h():
    await send_message("O DAILY")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    msg_30s.start()
    msg_5m.start()
    msg_24h.start()

client.run(TOKEN)


