# HurrDurrDiscordBot

Random discord bot with no specific functionality, functionality is added based 
on ideas that popped to mind and suggestions of friends


## Installation and usage

This package can be installed or run standalone, only difference how the bot can be started.
If the package is installed -> bot can be run anywhere, if not -> startup script must be run.

Use of a [venv](https://docs.python.org/3/tutorial/venv.html "Virtual Environments in Python")
is strongly recommended to keep the base python clean.


### Installing the package

This package can be installed to be run anywhere, installation works as follows

```
cd HurrDurrDiscordBot                           # cd into the source root
python -m pip install .                         # Install using pip
```

After installation the package can be run from anywhere as simply as:

```
python -m discord_bot.run_bot <flags>           # Start Discord bot
```


### Running the package without installing

If module installation is not preferred, you must first install required packages:

```
cd HurrDurrDiscordBot                           # cd into the source root
python -m pip install -r requirements.txt       # Install using pip
```

After which you can start the bot by running the startup script:

```
python discord_bot/run_bot.py <flags>           # Start Discord bot
```
