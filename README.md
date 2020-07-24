# JOEY BOT

A simple discord.py bot made for my friend's discord server. So far, the only way to use this bot is to clone the repo yourself and launch bot.py, though you would have to dive into the scripts to configure some things to your own servers channel IDs. A config implementation is planned.

## Commands:

###### Information

- !github - Provides a link to the github page.
- !help - Shows a message with information on all commands.
- !info - Shows basic information about Joey Bot.
- !ping - Pong! Also provides latency in ms.
- !8ball (question) - Accurately answers any question about anything.

###### Moderation

- !purge (amount) (filter) - Purges the last 'x' amount of messages in the current channel. Has optional arguement (filter) that when entered, !purge will only deletes the messages that includes the (filter) keywords.
- !mcannounce (action) (parameter)
  - (action) options:
    - add (announcement message) - Appends a announcement message to the rotation of announcements.
    - remove (number) - Removes the (number)th announcement from the pool of announcements
    - show (number) - Shows a list of all announcements currently in rotation on the server. If (number) is entered, will only return that specific announcement.

###### Image Processing

- !grayscale (image-url) - Returns the grayscaled version of the same image.

Note: mcannounce works through utilizing the discordSRV spigot plugin to connect to the minecraft server.
