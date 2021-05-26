from discord.ext import commands
import discord

class gifs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def delta(self, ctx):
        embed = discord.Embed(title="Delta halt...")
        embed.set_image(url="https://media.tenor.com/images/b9f7f39603388b34441f199d1b543533/tenor.gif")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def kolonien(self, ctx):
        embed = discord.Embed(title="Kolonien!")
        embed.set_image(url="https://media.tenor.com/images/9b381e87f3e793f8c5fdb1ce49f77b02/tenor.gif")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def laughing(self, ctx):
        embed = discord.Embed(title="Der Kaiser findet Ihren Beitrag zur Debatte erheiternd.")
        embed.set_image(url="https://media1.tenor.com/images/e6d3043a6ee5a4ec30b5ca23b70baf28/tenor.gif?itemid=18896357")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def einmarsch(self, ctx):
        embed = discord.Embed(title="Wenn Dreibürgen wieder mal wo einmarschiert...")
        embed.set_image(url="https://media.tenor.com/images/2907a8fcbd38e8eef3cb609ccd783e3a/tenor.gif")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(gifs(bot))