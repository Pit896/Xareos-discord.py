import discord
from discord.ext import commands
import praw
import random

class Reddit(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    reddit = praw.Reddit(client_id='2-mUsKQdNK9G-g',
                        client_secret='yMk-rhdaVstDKS2y3P16uRImhaA',
                        user_agent='Python automatic Xareosbot v2.0 (by /u/Snoo-84278)')        


    @commands.command()
    async def reddit(self, ctx, message):
        reddit = praw.Reddit(client_id='2-mUsKQdNK9G-g',
                        client_secret='yMk-rhdaVstDKS2y3P16uRImhaA',
                        user_agent='Python automatic Xareosbot v2.0 (by /u/Snoo-84278)')  

        submissions = reddit.subreddit(message).hot()
        post_to_pick = 1
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

            await ctx.send(submission.url)


    @reddit.error
    async def reddit_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Reddit channel doesn't exist!")    



def setup(bot):
    bot.add_cog(Reddit(bot))     