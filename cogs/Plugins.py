import discord
from discord.ext import commands

class Plugins(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


def setup(bot):
    bot.add_cog(Plugins(bot))         