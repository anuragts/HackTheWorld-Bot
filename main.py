import discord
import os
import requests
import json

client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle,activity=discord.Game('Language up'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('fuck'):
    quote = "you have be warned"
    await message.channel.send(quote)
    

client.run("ODczMzA1OTk4NTk1NjEyNzQy.YQ2flw.jDbBEIaVVfjPRxosR-IjGm52CjQ") 