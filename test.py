import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)



@bot.event
async def on_ready():
    print(f"we're live as {bot.user}")

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

with open("bottoken.txt", "r") as file: TOKEN = file.read()
bot.run(TOKEN)