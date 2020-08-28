import discord
from discord.ext import commands
import json, os
from pathlib import Path


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n------")

command_prefix = ['X ']
secret_file = json.load(open(cwd+"/bot_config/secrets.json"))
bot = commands.Bot(command_prefix, owner_id=639851817806725161)
TOKEN = secret_file['token']

bot.remove_command('help') 

for cog in os.listdir("cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can't be load")
            raise e   

 
bot.run(TOKEN)
