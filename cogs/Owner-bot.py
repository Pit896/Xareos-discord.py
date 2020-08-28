import discord
from discord.ext import commands

class Owner_bot(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")

    @commands.command(aliases=['disconnect'])
    @commands.is_owner()
    async def logout(self, ctx):
       await ctx.send(f"Hey **{ctx.author.name}**, I see that you are allowed to use this command, so in a while I will disconnect as requested👍")
       await self.bot.logout()


    @commands.is_owner()
    @commands.command(name="setstatus")
    async def setstatus(self, ctx, status: str = None):
        '''
        Changes the status message of the bot.
        Usage: !setstatus [status]
        '''
        if status is None:
            await ctx.send("No status was recevied. Status is unchanged.")
            return
        await self.bot.change_presence(
            status=discord.Status.online,
            activity=discord.Game(status)
        )
        await ctx.send("Bot status has been changed!")


    @setstatus.error
    async def setstatus_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You don't have permission to do that!")

    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You don't have permission to do that!")

        raise error     





def setup(bot):
    bot.add_cog(Owner_bot(bot))        