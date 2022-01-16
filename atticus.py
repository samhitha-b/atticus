import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('-ttcs1'):
    myembed=discord.Embed(title="Timetable for CSE/CSY batch 1", color=discord.Color.yellow())
    myembed.set_image(url="https://media.discordapp.net/attachments/920029895273381939/928909309948071966/timetable.png")
    await msg.channel.send(embed=myembed)

  if msg.content.startswith('-ttcs2'):
    myembed=discord.Embed(title="Timetable for CSE/CSY batch 2", color=discord.Color.yellow())
    myembed.set_image(url="https://media.discordapp.net/attachments/920029895273381939/928908186591850496/unknown.png")
    await msg.channel.send(embed=myembed)

  if msg.content.startswith('-ttec1'):
    myembed=discord.Embed(title="Timetable for ECE batch 1", color=discord.Color.yellow())
    myembed.set_image(url="https://media.discordapp.net/attachments/920029895273381939/928909310170365992/timetable_ece.png")
    await msg.channel.send(embed=myembed)

  if msg.content.startswith('-ttec2'):
    myembed=discord.Embed(title="Timetable for ECE batch 2", color=discord.Color.yellow())
    myembed.set_image(url="https://media.discordapp.net/attachments/920029895273381939/928907990726213692/unknown.png")
    await msg.channel.send(embed=myembed)

client.run(os.getenv("TOKEN"))