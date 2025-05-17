from .zerolivesleft import ZeroLivesLeft
from .wp_reports import WPReports

async def setup(bot):
    await bot.add_cog(ZeroLivesLeft(bot))
    await bot.add_cog(WPReports(bot))
