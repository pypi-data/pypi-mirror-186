# Roleplay Cog
This package is a cog edition of [my roleplay bot repository](https://github.com/mariohero24/Roleplay-Bot)
## Installation
```cs
pip install roleplaycog
```
## Setup examples
If you want normal slash commands:
```py
discord.ext.commands.Bot.load_extension(".roleplay", package="roleplaycog")
```
Elif you want all the commands to be in a slash command group:
```py
discord.ext.commands.Bot.load_extension(".roleplaygrouped", package="roleplaycog")
```
Elif you want all the commands to be bridge commands:
```py
discord.ext.bridge.Bot.load_extension(".roleplaybridged", package="roleplaycog")
```