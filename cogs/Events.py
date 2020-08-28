import discord
from discord.ext import commands

class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as: {self.bot.user.name}\n-------")
        serverCount = len(self.bot.guilds)
        await self.bot.change_presence(activity=discord.Game(name=f"Xareos🎉: X help [ALPHA] | In {serverCount} Server💜"))        


def setup(bot):
    bot.add_cog(Help(bot)) 