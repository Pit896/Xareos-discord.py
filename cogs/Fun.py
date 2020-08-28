import discord
from discord.ext import commands
import random
import asyncio
import praw
            
            
class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.command(aliases=['echo'])
    async def send(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)


    @commands.command()
    async def roll(self, ctx):
        cards = ["1","2","3","4", "5", "6"]
        await ctx.send(f"You choose number **{random.choice(cards)}**🎲!")  


    @commands.command()
    async def howlove(self, ctx, user1: discord.Member, user2: discord.Member):
        love = random.randint(0, 100)
        await asyncio.sleep(1.5)
        await ctx.send(f"✨{user1.mention} ❤{love}%❤ {user2.mention}✨")    


    @commands.cooldown(1, 5, type=commands.BucketType.guild)
    @commands.command()
    async def flip(self, ctx):
        coin_sides = ['Heads!', 'Tails!']
        result = random.choice(coin_sides)
        await ctx.send('Flipping a coin...')
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send(result)


    @commands.command()
    async def meme(self, ctx):

        image = random.randint(1,500)

        embed = discord.Embed(color=discord.Color.dark_blue())
        embed.set_author(name="😂MEME😂")
        embed.set_image(url=f"https://ctk-api.herokuapp.com/meme/{image}")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


    @commands.cooldown(1, 5, type=commands.BucketType.guild)
    @commands.command()
    async def eightball(self, ctx, question: str = None):
        responses = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it."
        ]
        if question is None:
            await ctx.send("Please ask me a question.")
            return
        result = random.choice(responses)
        await ctx.send('Let me see...')
        await ctx.trigger_typing()
        await asyncio.sleep(2)
        await ctx.send(f"Answer: {result}")    



    @send.error
    async def send_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X send [world]")
            await ctx.send(embed=embed)      

        raise error

    @howlove.error
    async def howlove_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X howlove [user 1] [user 2]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):   
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X howlove [user 1] [user 2]")
            await ctx.send(embed=embed)                      

        raise error        


def setup(bot):
    bot.add_cog(Fun(bot))   