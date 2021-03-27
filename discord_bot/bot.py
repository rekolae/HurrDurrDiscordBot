"""
Module containing Discord bot base actions
Emil Rekola <emil.rekola@hotmail.com>
"""

# STD imports
import logging
from datetime import datetime

# 3rd-party imports
from discord.ext import commands


class HurrDurrBot(commands.Bot):
    """
    Bot implementation
    """

    def __init__(self, channel_id: int, prefix: str):
        super().__init__(command_prefix=prefix)
        self._main_channel_id = channel_id
        self.bot_name = None
        self.startup_time: datetime = datetime.now()

    async def on_ready(self):
        """
        Executed when the bot has been initialized and connection has been made to discord
        """

        self.load_extension("discord_bot.cogs.actions")

        # Remove the "#xxxx" appendix from the bot username
        self.bot_name = str(self.user).split("#")[0]
        logging.info("%s is online!", self.bot_name)

        # If info channel was defined
        if self._main_channel_id is not None:
            logging.debug("Sending login message")
            await self.send_message(self.get_channel(self._main_channel_id), f"{self.bot_name} is online!")
            cmds = ""
            for command in self.commands:
                cmds += f"{command}\n"
            await self.send_message(self.get_channel(self._main_channel_id), f"Commands: {cmds}")

    @staticmethod
    async def send_message(channel, message: str) -> None:
        """
        Send given message to the given channel

        :param channel: Target channel for the message
        :param message: Message to be sent to the channel
        """

        logging.debug("Sending '%s' to '%s'", message, channel)
        await channel.send(message)

    async def send_shutdown_msg(self):
        """
        Send a shutdown message to the info channel if it was defined
        """

        # Send shutdown message if info channel was defined
        logging.info("Shutting down")
        if self._main_channel_id is not None:
            logging.info("Sending bot logout message")
            await self.send_message(self.get_channel(self._main_channel_id), f"{self.bot_name} is going offline!")

    async def close(self):
        """
        Overwrite close class method that is called when the Discord client is shutting down
        """

        # Send shutdown message
        await self.send_shutdown_msg()

        # Execute the original "close" function
        await super().close()
