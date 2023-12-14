import discord
import random
import topic
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

questions = topic.questions


@bot.event
async def on_ready():
    print(f"we're live as {bot.user}")

@bot.command()
async def topic(ctx):
    embed=discord.Embed(title=f"{random.choice(questions)}", description= "Categorie: jzegu", color = discord.Color.pink())
    await ctx.send(embed=embed)

with open("bottoken.txt", "r") as file: TOKEN = file.read()
bot.run(TOKEN)