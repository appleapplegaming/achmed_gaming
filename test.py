import discord
import random
import topic
from discord.ext import commands
sender = None
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

questions = topic.questions


@bot.event
async def on_ready():
    print(f"we're live as {bot.user}")

@bot.command()
async def turkey(ctx):
  await ctx.reply(
      "‼️🔥🥱🥱🐺🐺‼️🇹🇷🇹🇷🇹🇷🔥‼️🇹🇷🥱🥱🐺🔥 TÜRKIYE MENTIONED 🥱🥱🐺🔥🔥‼️🥱🇹🇷🇹🇷‼️🐺‼️🐺🔥‼️🐺‼️🥱🥱 WHAT THE FUCK IS ECONOMY 🇹🇷🇹🇷🇹🇷🥱🔥🥱🔥🐺🐺‼️🔥‼️🇹🇷🥱🇹🇷‼️🇹🇷🇹🇷‼️‼️🇹🇷🥱🐺🐺🔥🥱AWOOOOOO 🐺🐺‼️‼️‼️🔥🔥🥱🇹🇷🇹🇷🥱🥱🐺🔥🇹🇷🇹🇷🇹🇷🇹🇷"
  )

@bot.command()
async def topic(ctx):
    embed=discord.Embed(title=f"{random.choice(questions)}", description= "Categorie: jzegu", color = discord.Color.pink())
    await ctx.reply(embed=embed)

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#            return 
#     await bot.process_commands(message)
    

@bot.command()
async def yay(ctx):
      await ctx.reply(file=discord.File(r'yay.ogg'))
@bot.command()
async def jzegu(ctx):
    msg = await ctx.fetch_message(ctx.message.reference.message_id)
    await ctx.message.delete()
    await msg.reply(f"je ziet er goed uit")

@bot.command()
async def mashallah(ctx):
        embed=discord.Embed(title=f"google.com wat betekent mashallah", description="Mashallah (Arabisch: ما شاء الله), ook geschreven als Maşallah of Ma Shaa Allah, is een Arabische term en betekent 'wat God heeft gewild'. Masallah wordt vaak gebruikt om waardering, vreugde, lof of dankbaarheid uit te drukken voor een bepaalde gebeurtenis of een bepaalde persoon.", color=discord.Color.green())
        await ctx.reply(embed=embed)

@bot.command()
async def inshallah(ctx):
        embed=discord.Embed(title=f"google.com wat betekent inshallah", description="Hoewel een gelovige in hart en nieren inderdaad “Inshallah” gebruikt om te zeggen “ja, met de wil van God,” wordt de uitdrukking ook veelvuldig gebruikt als synoniem voor “misschien,” “we zien nog wel,” “hopelijk” of “nooit van m'n leven,” aan de goede verstaander de keuze.", color=discord.Color.green())
        await ctx.reply(embed=embed)
with open("bottoken.txt", "r") as file: TOKEN = file.read()
bot.run(TOKEN)
