"""
Read config file, env vars and command line args
Emil Rekola <emil.rekola@hotmail.com>
"""

# Local imports
import logging
from pathlib import Path

# 3rd-party imports
from configargparse import ArgParser, Namespace


def add_args(parser: ArgParser) -> None:
    """
    Add known arguments for parsing
    """

    parser.add_argument(
        "-c",
        "--config",
        help="Config file path",
        type=Path,
        is_config_file=True
    )

    parser.add_argument(
        "-v",
        "--verbosity",
        help="Application verbosity",
        type=str.upper,
        choices=["ERROR", "INFO", "DEBUG"],
        default="INFO"
    )

    parser.add_argument(
        "-t",
        "--bot-token",
        help="Discord bot token, must be present for the bot to work",
        type=str,
        env_var="DISCORD_BOT_TOKEN",
        required=True
    )

    parser.add_argument(
        "-i",
        "--info-channel-id",
        help="Main channel ID, used for notifications when bot comes online or going offline",
        type=int,
        env_var="DISCORD_MAIN_CHANNEL_ID"
    )

    parser.add_argument(
        "-p",
        "--prefix",
        help="Prefix for bot commands e.g. '.<command>'",
        type=str,
        default="."
    )


def config_logging(args: Namespace) -> None:
    """
    Configure logging based on the configured verbosity level
    """

    logging_level = getattr(logging, args.verbosity)
    logging.basicConfig(level=logging_level)


def get_config() -> Namespace:
    """
    Parse config and return the parsed args

    :return: ConfigArgParse Namespace object holding parsed args
    """

    parser = ArgParser()
    add_args(parser)
    args = parser.parse_args()

    return args
