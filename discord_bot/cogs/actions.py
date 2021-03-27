"""
Module containing Discord bot functionality
Emil Rekola <emil.rekola@hotmail.com>
"""

from datetime import datetime

from discord.ext import commands

from discord_bot import VERSION, GITHUB_URL
from discord_bot.utils import jokes
from discord_bot.cogs.bot_mixin import BotMixin


class Actions(BotMixin, commands.Cog):
    """

    """

    seppuku_img_url = "https://i.pinimg.com/originals/b0/7b/70/b07b702182e46735c5925429db1a4492.jpg"
    joke_categories = f"Supported categories: {jokes.get_categories()}"

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

    @commands.command(aliases=["commitSeppuku"])
    @commands.cooldown(rate=1, per=15.0, type=commands.BucketType.user)
    async def seppuku(self, ctx):
        """
        Shamefur dispray
        """

        await ctx.send(self.seppuku_img_url)

    @commands.command(brief='Tell a joke', description=joke_categories)
    async def joke(self, ctx, category):
        """
        Tell a random joke from a category if specified
        """

        await ctx.send(jokes.get_random_joke_from_category(category))


def setup(bot):
    bot.add_cog(Actions(bot))
