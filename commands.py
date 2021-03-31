import discord
from discord.ext import commands


class funcommands(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def watschenwald(self, ctx):
        embed = discord.Embed(title="Watschenwald")
        embed.add_field(name="Delta läuft...", value="...voller Freude, Elan und Enthusiasmus durch den Watschenwald..")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def kaiser(self, ctx):
        embed = discord.Embed(title="Wichtige Ankündigung")
        embed.add_field(name="Oh höret alle den Ruf...", value="...lang lebe der Kaiser!")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(funcommands(bot))