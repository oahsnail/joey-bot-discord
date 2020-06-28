import os
import discord
import random
from discord.ext import commands, tasks

# Using Python 3.8.2 32-bit


client = commands.Bot(command_prefix='!')

# 724115000578539586 <- general channel id
# 724374341579702394 <- welcome channel id
# 724370556186787881 <- test channel id
# 726663240997797939 <- server chat
# 726663287403577374 <- server console


announcementList = []
counter = 0

with open('announcements.txt', 'rt') as announcementFile:
    for line in announcementFile:
        announcementList.append(line)

# TASKS
# ===================================================================


@tasks.loop(seconds=90)
async def announcement():
    global counter
    channel = client.get_channel(726663287403577374)

    msg = f"say {announcementList[counter]}"
    coloredMsg = msg.replace('`', u'\u00a7')

    # print(coloredMsg)

    await channel.send(coloredMsg)
    counter += 1
    if counter >= len(announcementList):
        counter = 0


# EVENTS
# ====================================================================

# When bot is ready
@client.event
async def on_ready():
    announcement.start()
    print("bot is online")


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == 'general':    # general
            print(str(member) + ' has joined the server')
            nameString = str(member)
            await channel.send(f"Welcome **{nameString[0:len(nameString) - 5]}** to JoeyCraft!")


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == 'general':    # general
            if (member.nick):
                print(str(member.nick) + ' has left the server')
                await channel.send(f"**{str(member.nick)}** has escaped JoeyCraft :(")
            else:
                nameString = str(member)
                await channel.send(f"**{nameString[0:len(nameString)-5]}** has escaped JoeyCraft :(")
                print(nameString[0:len(nameString) - 5] +
                      ' has left the server')


# COMMANDS
# ======================================================================

@client.command(help="Shows basic information about Joey Bot")
async def info(ctx):
    info = """Joey Bot is developed and maintained by **Autolysis#2672** (Lian).
This bot has some useful features, and some... not so useful features.

To see the list of possible commands, type **!help**

The full documentation of Joey Bot is available on github. You can get there by using **!github**"""
    await ctx.send(info)


@client.command(help="Provides a link to the github page")
async def github(ctx):
    await ctx.send("https://github.com/oahsnail/joey-bot-discord")


@client.command(help="Pong! Also provides latency in ms")
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(help="Purges the last 'x' amount of messages in this channel. USE CAREFULLY")
async def purge(ctx, amount=None, *, filter=None):

    # Returns whether or now a message contains the filtered word(s)
    def match(msg):
        if filter == None:
            return True
        return str(filter).casefold() in str(msg.content).casefold()

    intAmount = 0

    if amount == None or not str(amount).isnumeric():
        # fix issue here where amount is detected as string even if it's numeric
        await ctx.send(f"*Please enter the command in the following format:*\n **!purge** **<amount>** *<filtered words>*")
        return
    intAmount = int(amount)

    deleted = await ctx.channel.purge(limit=intAmount, check=match)

    await ctx.send(f"Deleted {len(deleted)} messages.")


@client.command(name='8ball', help="Accurately answers any question about anything.")
async def _8ball(ctx, *, question=None):

    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don\'t count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']

    if question == None:
        await ctx.send(f"*Please enter a question in the following format* '**!8ball <question>**")
    else:
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


# Activate for testing
# with open("token.txt") as f:
#     TOKEN = f.read().strip()
# client.run(TOKEN)

# Activate for release
client.run(os.environ["ACCESS_TOKEN"])


# client.logout()
