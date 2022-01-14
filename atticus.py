import discord
import os
import io
import aiohttp

client = discord.Client()

@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('-ttcs1'):
    async with aiohttp.ClientSession() as session:
      async with session.get("https://media.discordapp.net/attachments/920029895273381939/928909309948071966/timetable.png") as resp:
          if resp.status != 200:
              return await msg.channel.send('Could not download file...')
          data = io.BytesIO(await resp.read())
          await msg.channel.send(file=discord.File(data, 'ttcs1.png'))

  if msg.content.startswith('-ttec1'):
    async with aiohttp.ClientSession() as session:
      async with session.get("https://media.discordapp.net/attachments/920029895273381939/928909310170365992/timetable_ece.png") as resp:
          if resp.status != 200:
              return await msg.channel.send('Could not download file...')
          data = io.BytesIO(await resp.read())
          await msg.channel.send(file=discord.File(data, 'ttec1.png'))
  if msg.content.startswith('-ttcs2'):
      async with aiohttp.ClientSession() as session:
        async with session.get("https://media.discordapp.net/attachments/920029895273381939/928908186591850496/unknown.png") as resp:
            if resp.status != 200:
                return await msg.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await msg.channel.send(file=discord.File(data, 'ttcs2.png'))

  if msg.content.startswith('-ttec2'):
    async with aiohttp.ClientSession() as session:
      async with session.get("https://media.discordapp.net/attachments/920029895273381939/928907990726213692/unknown.png") as resp:
          if resp.status != 200:
              return await msg.channel.send('Could not download file...')
          data = io.BytesIO(await resp.read())
          await msg.channel.send(file=discord.File(data, 'ttec2.png'))

client.run(os.getenv("TOKEN"))