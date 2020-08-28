import discord
from discord.ext import commands


class Admin(commands.Cog):
    '''
    Administrative tools for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.has_permissions(administrator=True)
    @commands.command(name="setup")
    async def setup(self, ctx):
        '''
        This command must be used for best functionality of the bot. Failure to
        do so will result in bugs.
        Usage: !setup
        '''
        await ctx.send("Setting up server for best possible functionality...")
        print("Performing setup for the server...")
        # Setup the Muted role for mute and unmute commands
        print("Setting up Muted role...")
        role_name = "Muted"
        if not discord.utils.get(ctx.guild.roles, name=role_name):
            # Muted role does not exist, create it
            perm = discord.Permissions(    # defaults to no permissions allowed
                read_message_history=True
            )
            await ctx.guild.create_role(
                name=role_name,
                permissions=perm,
                reason="There was no 'Muted' role previously to mute members."
            )
            print("Created Muted role...")
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        # Set permissions for the muted role in each text channel
        print("Setting text channel permissions for Muted role...")
        for channel in ctx.guild.text_channels:
            await channel.set_permissions(role, send_messages=False)
        await ctx.send("Setup is now complete.")
        print("Setup is complete.")

    @setup.error
    async def setup_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")

        raise error


def setup(bot):
    bot.add_cog(Admin(bot))
