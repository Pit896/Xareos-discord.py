import discord
from discord.ext import commands

class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.command(pass_context=True)
    async def help(self, ctx):    
        embed = discord.Embed(color=discord.Colour.teal(), timesetamp=ctx.message.created_at)
        embed.set_author(name="Help", icon_url="https://pbs.twimg.com/profile_images/1042080943241089025/3od9_ciI.jpg")
        embed.set_footer(text=f"Requested by | {ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="🎉About", value="`stats`, `ping`, `hi`, `help`", inline=False)
        embed.add_field(name="⚔Moderation", value="`kick`, `ban`, `purge`, `mute`, `unmute`", inline=False)
        embed.add_field(name="🛑Owner bot", value="`logout`, `setstatus`", inline=False)
        embed.add_field(name="🔧Server Toolbox", value="`member`, `lock`, `unlock`, `newchannel`, `slowmode`", inline=False)  
        embed.add_field(name="😂Fun", value="`send`, `roll`, `howlove`, `flip`, `meme`, `eightball`", inline=False)
        embed.add_field(name="🛡Admin", value="`setup`", inline=False)
        embed.add_field(name="🎟Plugins", value="`reddit`, `hypixelevel`", inline=False)
        embed.add_field(name="🐶Animals", value="`dog`, `cat`", inline=False)

        await ctx.send(embed=embed)  


def setup(bot):
    bot.add_cog(Help(bot)) 