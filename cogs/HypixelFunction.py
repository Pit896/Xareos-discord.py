import discord, cogs.utils.Hypixelutils # 'hypixel' is the name of the other Python file, minus the '.py' suffix
from discord.ext import commands

class HypixelWorker(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")
   
   
    @commands.cooldown(1, 5, type=commands.BucketType.guild)
    @commands.command()
    async def hypixelevel(self, ctx, name): # The name of this function will be the name of the command. 'ctx' just provides context we can use, and all arguments after that are just arguments sent by the command
        level = cogs.utils.Hypixelutils.get_level(name) # This is a reference the function we just created in hypixel.py
        if level is None: # Remember back in hypixel.py we returned 'None' if the API couldn't find a player
            await ctx.send("Player not found! (Make sure to use their **Minecraft** username)") # This just sends a message to the channel the command was sent in from the bot
        else: # We know that we found a player now because level is not None
            await ctx.send(f"Level of Hypixel account `{name}`: **{level}**🛡") # This puts the name and level into the message


def setup(bot):
    bot.add_cog(HypixelWorker(bot)) 