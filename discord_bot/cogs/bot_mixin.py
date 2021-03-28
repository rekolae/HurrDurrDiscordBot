"""
Module defining mixin class
Emil Rekola <emil.rekola@hotmail.com>
"""

from discord_bot.bot import HurrDurrBot


class BotMixin:
    """
    Define mixing class base
    """

    def __init__(self, bot: HurrDurrBot):
        self.bot = bot
