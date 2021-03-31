"""
Module containing more Discord bot functionality
Emil Rekola <emil.rekola@hotmail.com>
"""

# STD imports
from asyncio import sleep
from random import random, choice

# 3rd-party imports
from discord import Embed, Color
from discord.ext import commands

# Local imports
from discord_bot.cogs.bot_mixin import BotMixin
from discord_bot.utils import jokes


class Helpers(BotMixin, commands.Cog):
    """
    Helper bot actions
    """

    seppuku_img_url = "https://i.pinimg.com/originals/b0/7b/70/b07b702182e46735c5925429db1a4492.jpg"
    joke_categories = f"Supported categories: {jokes.get_categories()}"
    i_choose_you = "https://media1.tenor.com/images/84c5b716f0f747acc57a8176e3e6affd/tenor.gif"
    bamboozel = "https://media.makeameme.org/created/bamboozled.jpg"

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

    @commands.command(aliases=["commitSeppuku"])
    @commands.cooldown(rate=1, per=15.0, type=commands.BucketType.user)
    async def seppuku(self, ctx):
        """
        Shamefur dispray
        """

        await ctx.send(self.seppuku_img_url)

    @commands.command(
        brief="Tell a random joke",
        description="Tell a random joke from a category if specified",
        help=joke_categories
    )
    async def joke(self, ctx, *, category=None):
        """
        Tell a random joke
        """

        # Try to remove double/single quotes from the given category
        if category is not None:
            category = category.replace("'", "").replace('"', "")

        await ctx.send(jokes.get_random_joke_from_category(category))

    @commands.command(aliases=["randomChoice", "pickOne"])
    async def choose(self, ctx, *args):
        """
        Make a random choice from given items
        """

        # Bamboozeled with nothing to choose from
        if len(args) == 0:
            embed_msg = Embed(
                title="Much bamboozel, such confuse",
                description="Stoopid hooman, you have to give me something to choose from!",
                color=Color.dark_gold()
            )

            embed_msg.set_image(url=self.bamboozel)

            await ctx.send(embed=embed_msg)

        # Many choice, such decision
        elif len(args) == 1:
            await ctx.send(f"Such a hard choice, I choose '{args[0]}'")

        # Take a random pick
        else:
            await ctx.send(f"{len(args)} items given to choose from...\nHmmm...")
            await sleep(2)

            embed_msg = Embed(
                title=f"I choose '{choice(args)}'!",
                color=Color.random()
            )

            embed_msg.set_image(url=self.i_choose_you)

            await ctx.send(embed=embed_msg)


def setup(bot):
    """
    Entry point for the 'commands.Bot.load_extension' function for loading extensions
    """

    bot.add_cog(Helpers(bot))
