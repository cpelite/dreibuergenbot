from discord.ext import commands
import discord

class gifs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def delta(self, ctx):
        embed = discord.Embed(title="Delta halt...")
        embed.set_image(url="https://media1.tenor.com/images/dc3821d4cb8f871034d39983484c3e18/tenor.gif?itemid=16606549")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def kolonien(self, ctx):
        embed = discord.Embed(title="Kolonien!")
        embed.set_image(url="https://media1.tenor.com/images/e710cf539e44682cdd427372ae3e5da4/tenor.gif?itemid=19541838")
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
        embed.set_image(url="https://media1.tenor.com/images/940fab33108e1f6bd61cad3c768f6ca1/tenor.gif?itemid=20974358")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(gifs(bot))