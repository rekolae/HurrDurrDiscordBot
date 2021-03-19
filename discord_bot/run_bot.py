"""
Main file that start the discord bot
Emil Rekola <emil.rekola@hotmail.com>
"""

# Local imports
from discord_bot import config
from discord_bot.bot import HurrDurrBot


def run():
    """
    Start the discord bot
    """

    # Parse args and config logging
    args = config.get_config()
    config.config_logging(args)

    # Initialize bot and start it up
    bot = HurrDurrBot(args.info_channel_id)
    bot.run(args.bot_token)


if __name__ == '__main__':
    run()
