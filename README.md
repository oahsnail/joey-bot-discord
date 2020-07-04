# JOEY BOT

A simple discord.py bot made for my friend's discord server.

Commands:

- !github - Provides a link to the github page.
- !help - Shows a message with information on all commands.
- !info - Shows basic information about Joey Bot.
- !ping - Pong! Also provides latency in ms.
- !8ball (question) - Accurately answers any question about anything.
- !purge (amount) (filter) - Purges the last 'x' amount of messages in the current channel. Has optional arguement (filter) that when entered, !purge will only deletes the messages that includes the (filter) keywords.
- !mcannounce (action) (parameter)
  - (action) options:
    - add (announcement message) - Appends a announcement message to the rotation of announcements.
    - remove (number) - Removes the (number)th announcement from the pool of announcements
    - show (number) - Shows a list of all announcements currently in rotation on the server. If (number) is entered, will only return that specific announcement.

Note: mcannounce works through utilizing the discordSRV spigot plugin to connect to the minecraft server.
