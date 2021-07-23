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

class reichslaender(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def reichstal(self, ctx):
        embed = discord.Embed(title="Informationen über Reichstal")
        embed.add_field(name="Hauptstadt", value="Reichstal")
        embed.add_field(name="Stadtoberhaupt", value="Klaas tom Brok")
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
        embed.add_field(name="Hauptstadt", value="Tuusdorf")
        embed.add_field(name="Landesoberhaupt", value="Königin Beatrice I.")
        embed.add_field(name="Regierungschef", value="Stephan Nörden")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def rem(self, ctx):
        embed = discord.Embed(title="Informationen über das Königreich Rem")
        embed.add_field(name="Hauptstadt", value="Montjoie")
        embed.add_field(name="Landesoberhaupt", value="König Paul-Guillaume III.")
        embed.add_field(name="Regierungschef", value="Marius de Waldeck-Leon")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def stauffen(self, ctx):
        embed = discord.Embed(title="Informationen über das Königreich Stauffen")
        embed.add_field(name="Hauptstadt", value="Hohenstauffen")
        embed.add_field(name="Landesoberhaupt", value="Xaver von Dunkelstein-Hohenstauffen (Reichskommissar)")
        embed.add_field(name="Regierungschef", value="Loris von Tanningen")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def hohenburglohe(self, ctx):
        embed = discord.Embed(title="Informationen über das Großherzogtum Hohenburg-Lohe")
        embed.add_field(name="Hauptstadt", value="Amalien")
        embed.add_field(name="Landesoberhaupt", value="Friedrich Wilhelm")
        embed.add_field(name="Regierungschef", value="Nikolaus von Berg")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def bazen(self, ctx):
        embed = discord.Embed(title="Informationen über das Großherzogtum Bazen")
        embed.add_field(name="Hauptstadt", value="Ludwigsruh")
        embed.add_field(name="Landesoberhaupt", value="Georg III. Rufus (der Unartige)")
        embed.add_field(name="Regierungschef", value="Elisabeth von Barnim")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def cranach(self, ctx):
        embed = discord.Embed(title="Informationen über das Churfürstenthum Cranach")
        embed.add_field(name="Hauptstadt", value="Leibach")
        embed.add_field(name="Landesoberhaupt", value="Constantin I.")
        embed.add_field(name="Regierungschef", value="Elisabeth Despencer")
        await ctx.send(embed=embed)
        return

    @commands.command()
    async def geldern(self, ctx):
        embed = discord.Embed(title="Informationen über das Erzherzogtum Geldern-Veldoril")
        embed.add_field(name="Hauptstadt", value="Vengard")
        embed.add_field(name="Landesoberhaupt", value="Ludwig I.")
        embed.add_field(name="Regierungschef", value="Hagen von Gotha")
        await ctx.send(embed=embed)
        return

class sonstige(commands.Cog):
    def __init__(self,mdnbot):
        self.bot = mdnbot

    @commands.command()
    async def reichstag(self, ctx):
        embed = discord.Embed(title="Sitzverteilung in der LXII. Sitzungsperiode des Reichstags")
        embed.set_image(url="https://forum.dreibuergen.van-mauritz.de/index.php?image-proxy/&key=f1208fc6485581a02b86fa878337bbe24078bdbe0d4c1ec3ba06f38eb1e9c5dc-aHR0cHM6Ly9iaWxkZXIuZGVyLm1pa3JvbmF0aW9uZW4uZGUvdXBsb2Fkcy8yMDIxLzA2L2kxMTk5M2JpZXdnYy5wbmc%3D")#
        embed.add_field(name="Fraktion der Partei der Arbeit Dreibürgens (PDADB)", value="62 Sitze")
        embed.add_field(name="Fortschrittliche Volkspartei (FVP)", value="124 Sitze")
        embed.add_field(name="Fraktion der Nationalliberalen Partei (NLP)", value="144 Sitze")
        embed.add_field(name="Fraktion der Christlich-Sozialen Volkspartei (CSVP)", value="81 Sitze")
        embed.add_field(name="Kaisertreue Union des Konservativen Gedankenguts (KUdeKG)", value="185 Sitze")
        embed.add_field(name="Fraktion des Mouvement impérialiste pour la Restauration de l'Absolutisme/Kaisertreue Bewegung für die Wiederherstellung des Absolutismus (MIRA/BdK)", value="124 Sitze")
        embed.add_field(name="Fraktion des Dreibürgischen Nationalkonservativen Zentrums (DNZ", value="124 Sitze")
        await ctx.send(embed=embed)
        return

def setup(bot):
    bot.add_cog(funcommands(bot))
    bot.add_cog(reichslaender(bot))
    bot.add_cog(sonstige(bot))