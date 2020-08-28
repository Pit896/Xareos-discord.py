import discord
from discord.ext import commands
import asyncio
            
class Moderation(commands.Cog):
    """Commands used to moderate your guild"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")

            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):

       await member.ban(reason=reason)
       await ctx.send(f"{member} has been banned from the server👍, \nReason: {reason}")
       message = await ctx.send(f"Receiving data from {member} in 3")
       await asyncio.sleep(0.5)
       await message.edit(content=f"Receiving data from {member} in 2")
       await asyncio.sleep(0.5)
       await message.edit(content=f"Receiving data from {member} in 1")
       await asyncio.sleep(0.5)
       await message.edit(content=f"Receiving data from {member} done")       
       embed = discord.Embed(color=discord.Color.default(), timestamp=ctx.message.created_at)       
       embed.set_author(name=f"Kicked User info - {member}")
       embed.set_thumbnail(url=member.avatar_url)
       embed.add_field(name="User ID:", value=member.id, inline=False)
       embed.add_field(name="Reason:", value=reason, inline=False)
       embed.add_field(name="Guild name:", value=member.display_name, inline=False)        
       embed.add_field(name="Bot?", value=member.bot, inline=False)    

       await ctx.send(embed=embed) 


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):

       await member.kick(reason=reason)
       await ctx.send(f"{member} has been kicked from the server👍, \nReason: {reason}")
       message = await ctx.send(f"Receiving data from {member} -")
       await asyncio.sleep(0.5)
       await message.edit(content=f"Receiving data from {member} /")
       await asyncio.sleep(0.5)
       await message.edit(content=f"Receiving data from {member} |")
       await asyncio.sleep(0.5)
       await message.edit(content=f"Receiving data from {member} Done")  
       embed = discord.Embed(color=discord.Color.default(), timestamp=ctx.message.created_at)     
       embed.set_author(name=f"Kicked User info - {member}")
       embed.set_thumbnail(url=member.avatar_url)
       embed.add_field(name="User ID:", value=member.id, inline=False)
       embed.add_field(name="Reason:", value=reason, inline=False)
       embed.add_field(name="Guild name:", value=member.display_name, inline=False)        
       embed.add_field(name="Bot?", value=member.bot, inline=False)    

       await ctx.send(embed=embed) 

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(color=discord.Color.blue())
        embed.set_author(name="Purge Command")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Clear command requested by {ctx.author}")
        embed.add_field(name="Cleared message amount:", value=amount, inline=False)

        await ctx.send(embed=embed)
        await asyncio.sleep(2.3)
        await ctx.channel.purge(limit=1)


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        '''
        Mutes a user from text channels.
        Usage: !mute [username]
        '''
        role_name = "Muted"
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        # Assign muted role to user
        await member.add_roles(role)
        await ctx.send(f"{member.name} has been muted.") 


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        '''
        Unmutes a user from text channels.
        Usage: !unmute [username]
        '''
        role_name = "Muted"
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not discord.utils.get(member.roles, name=role_name):
            # Member doesn't have Muted role6
            await ctx.send(f"{member.name} is already unmuted.")
        else:
            # Unmute user
            await member.remove_roles(role)
            await ctx.send(f"{member.name} has been unmuted.")


    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X purge [intiger]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X purge [intiger]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!") 

        raise error


    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X mute [member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X mute [member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!") 

        raise error


    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X unmute [member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X unmute [member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!") 

        raise error                    


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X kick @[member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X kick @[member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")             

        raise error

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X ban @[member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(color=discord.Color.dark_red())
            embed.set_author(name="Invalid use!")
            embed.add_field(name="Example for the correct use:", value="X ban @[member]")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")             

        raise error      
        
def setup(bot):
    bot.add_cog(Moderation(bot))
       
