"""
Module containing Discord bot functionality
Emil Rekola <emil.rekola@hotmail.com>
"""

# STD imports
from datetime import datetime

# 3rd-party imports
from discord.ext import commands

# Local imports
from discord_bot import VERSION, GITHUB_URL
from discord_bot.cogs.bot_mixin import BotMixin


class Actions(BotMixin, commands.Cog):
    """
    Bot actions
    """

    @commands.command()
    async def ping(self, ctx):
        """
        Ping Pong!!!
        """

        await ctx.send("Pong!")

    @commands.command()
    async def version(self, ctx):
        """
        Display bot version
        """

        await ctx.send(f"Bot version: {VERSION}")

    @commands.command()
    async def source(self, ctx):
        """
        Github address of the source code repository
        """

        await ctx.send(f"Bot source code repository: {GITHUB_URL}")

    @commands.command()
    async def uptime(self, ctx):
        """
        Display bot uptime
        """

        # Time difference between starting and now
        time_delta = datetime.now() - self.bot.startup_time

        # Calculate hours, minutes and seconds
        hours = int(time_delta.seconds / 3600)
        mins = int((time_delta.seconds / 60) % 60)
        secs = int(time_delta.seconds % 60)

        uptime = f"Bot uptime: {time_delta.days} days {hours} hours {mins} minutes {secs} seconds"
        await ctx.send(uptime)


def setup(bot):
    """
    Entry point for the 'commands.Bot.load_extension' function for loading extensions
    """

    bot.add_cog(Actions(bot))
