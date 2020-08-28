import discord
from discord.ext import commands
import datetime

class ServerTool(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.command(aliases=['info'])
    async def member(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Info of the user {member}", icon_url=member.avatar_url)

        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Name:", value=member.display_name, inline=False)
        embed.add_field(name="Joined in server at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"Role({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False) 
        embed.add_field(name="Top role:", value=member.top_role.mention)

        await ctx.send(embed=embed) 


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False) 
        await ctx.send("Channel locked🔒!")


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True) 
        await ctx.send("Channel unlocked🔓!") 


    @commands.has_permissions(manage_channels=True)
    @commands.command(aliases=['nchannel'])
    async def newchannel(self, ctx, channel_name='text channel'):
        '''
        Creates new text channel.
        Usage: !nchannel [username (optional)]
        '''
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f"Creating a new channel called {channel_name}.")
            await guild.create_text_channel(channel_name) 


    @commands.command()
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to **{seconds}** seconds!")        


    @member.error
    async def member_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X member @[membername]")
            await ctx.send(embed=embed)               

        raise error  

    @slowmode.error
    async def slowmode_error(self, ctx, error): 
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X slowmode [seconds]")
            await ctx.send(embed=embed)  
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")  

        raise error   

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!") 

        raise error 


    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!") 

        raise error  

    @newchannel.error
    async def NewChannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!") 
        
        raise error          



def setup(bot):
    bot.add_cog(ServerTool(bot))       