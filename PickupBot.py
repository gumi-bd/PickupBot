import os
import discord
import requests
import json
import random

#Uncomment the code below, enter your token and uncomment the last line if you want to use the bot
#token = 'PLACEHOLDER'

client = discord.Client()

sad_words = ["sad", "unhappy", "miserable", "angry", "miserable", "break up"]

starter_encoragements = [
  "Hang in there my friend!",
  "Things will get better",
  "You are a cutie pie don't worry"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_line():
  response = requests.get("https://getpickuplines.herokuapp.com/lines/random")
  json_data = json.loads(response.text)
  pickup = json_data['line']
  return(pickup)
    
  
@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$pickup'):
    pickup = get_line()
    await message.channel.send(pickup)
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encoragements)) 
      
#client.run(token)