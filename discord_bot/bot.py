"""
Module containing Discord bot functionality
Emil Rekola <emil.rekola@hotmail.com>
"""

# STD imports
import logging
from datetime import datetime

# 3rd-party imports
import discord

# Local imports
from discord_bot import version, github_url


class HurrDurrBot(discord.Client):
    """
    Class with bot functionality
    """

    def __init__(self, channel_id):
        super().__init__()
        self._main_channel_id = channel_id
        self.bot_name = None
        self.startup_time: datetime = datetime.now()
        self.known_commands = {
            "!help": "Print this help message",
            "!ping": "Play some Ping Pong!",
            "!version": "Get current bot version",
            "!source": "Get address for the source code of the bot",
            "!uptime": "Print current bot uptime"
        }

    async def on_ready(self):
        """
        Executed when the bot has been initialized and connection has been made to discord
        """

        # Remove the "#xxxx" appendix from the bot username
        self.bot_name = str(self.user).split("#")[0]
        logging.info("%s is online!", self.bot_name)

        # If info channel was defined
        if self._main_channel_id is not None:
            logging.debug("Sending login message")
            await self.send_message(self.get_channel(self._main_channel_id), f"{self.bot_name} is online!")

    async def on_message(self, message):
        """
        When message is sent to any of the channels, check the message and respond appropriately

        :param message: Message that was recieved from the discord server
        """

        # Ignore bot's own messages
        if message.author != self.user:
            logging.info("Message from %s at %s: %s", message.author, message.channel, message.content)

            # Tell known commands
            if message.content.lower() == "!help":
                await self.send_message(message.channel, self.get_supported_commands())

            # Play some Ping Pong with another user
            elif message.content.lower() == "!ping":
                await self.send_message(message.channel, "Pong")

            # Tell current bot version
            elif message.content.lower() == "!version":
                await self.send_message(message.channel, f"Bot version: {version}")

            # Tell address of the source code for the bot
            elif message.content.lower() == "!source":
                await self.send_message(message.channel, f"Bot source code repository: {github_url}")

            # Tell current uptime
            elif message.content.lower() == "!uptime":
                await self.send_message(message.channel, self.get_uptime())

    def get_supported_commands(self) -> str:
        """
        Create help message about supported commands

        :return: Help string
        """

        white_space = 10
        help_string = "Known commands:"

        for command, cmd_str in self.known_commands.items():
            help_string += f"\n{command.ljust(white_space)}: {cmd_str}"

        return help_string

    def get_uptime(self) -> str:
        """
        Calculate uptime based on startup time and the current time

        :return: Bot uptime
        """

        # Time difference between starting and now
        time_delta = datetime.now() - self.startup_time

        # Calculate hours, minutes and seconds
        hours = int(time_delta.seconds / 3600)
        mins = int((time_delta.seconds / 60) % 60)
        secs = int(time_delta.seconds % 60)

        uptime = f"Bot uptime: {time_delta.days} days {hours} hours {mins} minutes {secs} seconds"
        return uptime

    async def send_shutdown_msg(self):
        """
        Send a shutdown message to the info channel if it was defined
        """

        # Send shutdown message if info channel was defined
        logging.info("Shutting down")
        if self._main_channel_id is not None:
            logging.info("Sending bot logout message")
            await self.send_message(self.get_channel(self._main_channel_id), f"{self.bot_name} is going offline!")

    @staticmethod
    async def send_message(channel, message: str) -> None:
        """
        Send given message to the given channel

        :param channel: Target channel for the message
        :param message: Message to be sent to the channel
        """

        logging.debug("Sending '%s' to '%s'", message, channel)
        await channel.send(message)
