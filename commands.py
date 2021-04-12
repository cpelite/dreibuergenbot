import discord
from discord.ext import commands

class funcommands(commands.Cog):
    def __init__(self,dbbot):
        self.bot = dbbot

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

class reichsländer:
    def __init(self, mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def reichstal(self, ctx):
        embed = discord.Embed(title="Informationen über Reichstal")
        embed.add_field(name="Hauptstadt", value="Reichstal")
        embed.add_field(name="Stadtoberhaupt", value="Klaas tom Brok (Schultheiß)")
        embed.add_field(name="Regierungschef", value="vakant")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def werthen(self, ctx):
        embed = discord.Embed(title="Informationen über das Königreich Werthen")
        embed.add_field(name="Hauptstadt", value="Greifenburg")
        embed.add_field(name="Landesoberhaupt" ,value="König Karl-Josef von Werthen")
        embed.add_field(name="Regierungschef" ,value="Sophia Schamm")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def haxagon(self, ctx):
        embed = discord.Embed(title="Informationen über das Königreich Haxagon")
        embed.add_field(title="Hauptstadt", value="Tuusdorf")
        embed.add_field(title="Landesoberhaupt", value="Königin Beatrice I.")
        embed.add_field(title="Regierungschef", value="Stephan Nörden")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def rem(self, ctx):
        embed = discord.Embed(title="Informationen über das Königreich Rem")
        embed.add_field(title="Hauptstadt", value="Montjoie")
        embed.add_field(title="Landesoberhaupt", value="König Paul-Guillaume III.")
        embed.add_field(title="Regierungschef", value="Marius de Waldeck-Leon")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def stauffen(self, ctx):
        embed = discord.Embed(title="Informationen über das Königreich Stauffen")
        embed.add_field(title="Hauptstadt", value="Hohenstauffen")
        embed.add_field(title="Landesoberhaupt", value="Xaver von Dunkelstein-Hohenstauffen (Reichskommissar)")
        embed.add_field(title="Regierungschef", value="Loris von Tanningen")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def hohenburglohe(self, ctx):
        embed = discord.Embed(title="Informationen über das Großherzogtum Hohenburg-Lohe")
        embed.add_field(title="Hauptstadt", value="Amalien")
        embed.add_field(title="Landesoberhaupt", value="Friedrich Wilhelm")
        embed.add_field(title="Regierungschef", value="Nikolaus von Berg")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def bazen(self, ctx):
        embed = discord.Embed(title="Informationen über das Großherzogtum Bazen")
        embed.add_field(title="Hauptstadt", value="Ludwigsruh")
        embed.add_field(title="Landesoberhaupt", value="Georg III. Rufus (der Unartige)")
        embed.add_field(title="Regierungschef", value="Elisabeth von Barnim")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def cranach(self, ctx):
        embed = discord.Embed(title="Informationen über das Churfürstenthum Cranach")
        embed.add_field(title="Hauptstadt", value="Leibach")
        embed.add_field(title="Landesoberhaupt", value="Constantin I.")
        embed.add_field(title="Regierungschef", value="Elisabeth Despencer")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def geldern(self, ctx):
        embed = discord.Embed(title="Informationen über das Erzherzogtum Geldern-Veldoril")
        embed.add_field(title="Hauptstadt", value="Vengard")
        embed.add_field(title="Landesoberhaupt", value="Ludwig I.")
        embed.add_field(title="Regierungschef", value="Hagen von Gotha")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(funcommands(bot))
    bot.add_cog(reichsländer(bot))