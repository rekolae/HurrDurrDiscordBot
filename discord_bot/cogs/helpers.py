"""
Module containing more Discord bot functionality
Emil Rekola <emil.rekola@hotmail.com>
"""

# STD imports
from asyncio import sleep
from random import random, choice
from itertools import zip_longest

# 3rd-party imports
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

    @commands.command(aliases=["makeTeams"])
    async def team(self, ctx, even_teams: bool, *people):
        """
        Create teams, first arg signifies if teams should be even
        """

        if len(people) == 0:
            await ctx.send("No people to choose from!")

        elif len(people) == 1:
            await ctx.send(f"'{people[0]}' has no friends and has to play alone \U0001F625")

        # Decide teams when there is not even amount of people and even teams were requested
        elif even_teams and (len(people) % 2 != 0):
            removed_person = choice(people)
            await ctx.send(f"Teams are not be even, so somebody has to be left out and that one is '{removed_person}'")

            people_left = [p for p in people if p != removed_person]

            team1 = []
            team2 = []

            # Pick one person, remove from list and add to one of the teams
            for x in range(len(people_left)):
                p = choice(people_left)
                people_left.remove(p)
                if x % 2 == 0:
                    team1.append(p)

                else:
                    team2.append(p)

            teams = "Teams have been decided:"
            teams += f"\n{'Team1:'.ljust(20)}Team2:"
            for x, y in zip(team1, team2):
                teams += f"\n{x.ljust(20)} {y}"

            await ctx.send(teams)

        # Randomize teams without caring about balance
        else:
            team1 = []
            team2 = []

            people_list = [p for p in people]

            # Pick one person, remove from list and add to one of the teams
            for x in range(len(people)):
                p = choice(people_list)
                people_list.remove(p)
                if x % 2 == 0:
                    team1.append(p)

                else:
                    team2.append(p)

            teams = "Teams have been decided:"
            teams += f"\n{'Team1:'.ljust(20)}Team2:"
            for x, y in zip_longest(team1, team2, fillvalue=""):
                teams += f"\n{x.ljust(20)} {y}"

            await ctx.send(teams)


def setup(bot):
    """
    Entry point for the 'commands.Bot.load_extension' function for loading extensions
    """

    bot.add_cog(Helpers(bot))
