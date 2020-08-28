import discord
from discord.ext import commands

class Error(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): 
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found, for help use **X help**")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Command **on Cooldown**! Try again later")         

        raise error 



def setup(bot):
    bot.add_cog(Error(bot)) 