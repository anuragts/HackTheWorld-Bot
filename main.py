import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle,activity=discord.Game('!helpme'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    a = message.content.startswith('hello455')
    print(a)
  if message.content.startswith('fuck'):
    quote = "you have been warned "
    await message.channel.send(quote)
  if message.content.startswith('!site'):
    quote = "HackTheWorld live site - https://hacktheworld.online/"
    await message.channel.send(quote)
  if message.content.startswith('!devpost'):
    quote = "HackTheWorld Devpost - https://hacktheworld-online.devpost.com/?ref_feature=challenge&ref_medium=discover "
    await message.channel.send(quote)
  if message.content.startswith('!twitch'):
    quote = "HackTheWorld Twitch - https://www.twitch.tv/00mb1 "
    await message.channel.send(quote)  
  if message.content.startswith('!linkedin'):
    quote = "HackTheWorld LinkedIn - https://www.linkedin.com/company/neuralworks/ "
    await message.channel.send(quote)
  if message.content.startswith('!neuralworks'):
    quote = "NeuralWorks live site - https://neuralworks.group/"
    await message.channel.send(quote)
  if message.content.startswith('!helpme'):
    quote = "All commands \n !helpme \n !site - HackTheWorld Live site \n !devpost - HackTheWorld Devpost \n !twitch - HackHackTheWorld Twitch \n !linkedin - HackTheWorld LinkedIn \n !neuralworks - Neural Works Site"
    await message.channel.send(quote)


client.run("TOKEN") 