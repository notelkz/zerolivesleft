from redbot.core import commands

class ZeroLivesLeft(commands.Cog):
    """Cog for ZeroLivesLeft."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def zlltest(self, ctx):
        """Test command for ZeroLivesLeft."""
        await ctx.send("ZeroLivesLeft is loaded!")
