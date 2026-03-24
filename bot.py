import discord
from discord.ext import tasks

TOKEN = 'MTQ4NTkyMjM1MzMzMzUzODg1Ng.G70gjC.PGjZX9E3T5cfTo6oHzybu6HlWqM0dG-_Dzmshw'
CHANNEL_ID = 1455257168562356408

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_message(content):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(content)
    else:
        print("চ্যানেল পাওয়া যায়নি")

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
