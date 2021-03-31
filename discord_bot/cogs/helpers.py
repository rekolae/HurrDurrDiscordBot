"""
Module containing more Discord bot functionality
Emil Rekola <emil.rekola@hotmail.com>
"""

# STD imports
from asyncio import sleep
from random import random

# 3rd-party imports
from discord.ext import commands

# Local imports
from discord_bot.cogs.bot_mixin import BotMixin


class Helpers(BotMixin, commands.Cog):
    """
    Helper bot actions
    """

    @commands.command(aliases=["coinToss"])
    async def flip(self, ctx):
        """
        Flip a coin
        """

        # Generate random number between 0 and 1, then round it
        rnd = round(random())

        await ctx.send("Flipping...")
        await sleep(2.5)

        if rnd:
            await ctx.send("Heads!")

        else:
            await ctx.send("Tails!")


def setup(bot):
    """
    Entry point for the 'commands.Bot.load_extension' function for loading extensions
    """

    bot.add_cog(Helpers(bot))
