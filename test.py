import discord

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)



@bot.event
async def on_ready():
    print(f"we're live as {bot.user}")



with open("bottoken.txt", "r") as file: TOKEN = file.read()

bot.run(TOKEN)