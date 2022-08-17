import discord
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

client = discord.Client()
intents = nextcord.Intents.default()

intents.members = True

client2 = commands.Bot(command_prefix='!', intents=intents)
server_identity = '969594307860385843'

@client.event # loads an event specifically for this client
async def on_ready():

    print('Logging in as {0.user}'.format(client))
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('Hello Elon!'):
        await message.channel.send('Hello %s!'%(message.author))

    if message.content.endswith('Ni What?'):
        await message.channel.send('Elon Recognises BenaWaMalines!')

@client2.event
async def on_ready():

    print('Also Logging in as {0.user}'.format(client2))

@client2.slash_command(name='Niaje', description='Inajibu na Hello', guild_ids=server_identity)
async def Niaje(interaction: Interaction):
    await interaction.response.send_message('Niaje')


client.run('MTAwNzI5MzU3OTY1NzQ5MDQ4Mw.GwL4rB.BUoSNHKT7agz_oYiS8EHrhrtjRufiXGxI7mcw0')
