import discord
from discord.ext import commands
import asyncio

            
class About(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.command(aliases=['hello'], pass_context=True)
    async def hi(self, ctx):
        """
        A simple command which send hi to author
        """
        message = await ctx.send(f"Hi {ctx.author.mention}, have you an idea to use this bot today? For help send `Xhelp`:tada:")
        await asyncio.sleep(5)
        await message.edit(content="Or contact **𒆜𝕎𝕃𝔽| ༺Leͥgeͣnͫd༻ᴳᵒᵈ** for add new commands! Enjoy fun!")

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        """
        Ping command
        """
        embed = discord.Embed(color=discord.Color.teal())
        embed.set_author(name="Pinging...")    

        message = await ctx.send(embed=embed)
        await asyncio.sleep(3)

        new_message = discord.Embed(color=discord.Color.teal())
        latency = round(self.bot.latency*1000)
        new_message.set_author(name=f"{latency} ms") 

        await message.edit(embed=new_message)



    @commands.command(aliases=['stat'])
    async def stats(self, ctx):

        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        embed = discord.Embed(title="Xareos stats", color=discord.Colour.dark_grey(), timestamp=ctx.message.created_at)
        embed.set_author(name="Version bot: ALPHA")
        embed.set_image(url="https://pbs.twimg.com/profile_images/1042080943241089025/3od9_ciI.jpg")
        embed.set_footer(icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRT3mDhKQv_r7cwKROqwbliCoeFET3MBfPoaA&usqp=CAU.jpeg")
        embed.add_field(name="Discord.py Version:", value=dpyVersion)
        embed.add_field(name="Server Counter:", value=serverCount)
        embed.add_field(name="Member Counter:", value=memberCount)

        await ctx.send(embed=embed)         


def setup(bot):
    bot.add_cog(About(bot))     