import discord
from discord.ext import commands
import random

class Animals(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded!")


    @commands.command()
    async def dog(self, ctx):

        image = ["https://www.reddit.com/r/aww/comments/bpq14w/it_took_me_26_years_to_get_my_first_puppy_and_i/", "https://cdn.weeb.sh/images/SyeA0oENtG.jpeg", "https://cdn.weeb.sh/images/HyGYnNVKz.gif", "https://cdn.weeb.sh/images/SkVxjV4Ff.jpeg", "https://cdn.weeb.sh/images/HyWFtTCYf.jpeg","https://cdn.weeb.sh/images/HkbVMhVNKf.jpeg", "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "https://www.zooplus.co.uk/magazine/wp-content/uploads/2018/01/Female-Dogs-in-Heat-768x512.jpeg", "https://i.insider.com/5484a390eab8ea6938b17e33?width=300&format=jpeg", "https://cdn.shopify.com/s/files/1/2327/5701/articles/Omega-3-For-Dogs_1000x.jpg"]

        embed = discord.Embed(color=discord.Color.dark_blue())
        embed.set_author(name="🐶DOG🐶")
        embed.set_image(url=random.choice(image))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


    @commands.command()
    async def cat(self, ctx):

        image = ["https://cdn.mos.cms.futurecdn.net/VSy6kJDNq2pSXsCzb6cvYF-650-80.jpg", "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg", "https://ichef.bbci.co.uk/news/320/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg", "https://news.cgtn.com/news/77416a4e3145544d326b544d354d444d3355444f31457a6333566d54/img/37d598e5a04344da81c76621ba273915/37d598e5a04344da81c76621ba273915.jpg", "https://blog.ferplast.com/wp-content/uploads/2019/07/owning-a-white-cat-5b1b91a318ba9-900x600.jpg", "https://www.thesprucepets.com/thmb/V1oGzYAiUkinq94H0wZ8YM2CUsw=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Stocksy_txp33a24e10lxw100_Medium_214761-5af9d6d7875db900360440a7.jpg", "https://cdn.dnaindia.com/sites/default/files/styles/full/public/2017/11/04/622378-cat.jpg"]

        embed = discord.Embed(color=discord.Color.dark_blue())
        embed.set_author(name="🐱CAT🐱")
        embed.set_image(url=random.choice(image))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Animals(bot))  