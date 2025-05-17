from redbot.core import commands

class WPReports(commands.Cog):
    """Test Cog"""

    @commands.command()
    async def wprtest(self, ctx):
        """Test command for WPReports."""
        await ctx.send("WPReports is loaded!")
