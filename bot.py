import os
import discord
import random
import opencv
from discord.ext import commands, tasks

# Using Python 3.8.2 32-bit


client = commands.Bot(command_prefix='!')

# 724115000578539586 <- general channel id
# 724374341579702394 <- welcome channel id
testChannelID = 724370556186787881
mcChatChannelID = 726663240997797939
mcConsoleChannelID = 726663287403577374


# TASKS
# ===================================================================

counter = 0


@tasks.loop(minutes=10)
async def announcement():
    global counter
    global mcConsoleChannelID
    channel = client.get_channel(mcConsoleChannelID)  # Server Console
    announcementList = []

    with open('announcements.txt', 'r+') as announcementFile:
        for line in announcementFile:
            announcementList.append(line)
        announcementFile.close()
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
                await channel.send(f"**{str(member.nick)}** has left JoeyCraft :(")
            else:
                nameString = str(member)
                await channel.send(f"**{nameString[0:len(nameString)-5]}** has escaped JoeyCraft :(")
                print(nameString[0:len(nameString) - 5] +
                      ' has left the server')


# COMMANDS
# ======================================================================
cringeCheck = False


@client.command()
async def mcannounce(ctx, operation="", *, arg2="", help="Modify the pool of announcements currently in circulation on JoeyCraft"):
    announcementFile = open("announcements.txt", 'r')
    lines = announcementFile.readlines()
    announcementFile.close()
    global cringeCheck
    if operation == 'add':
        if arg2 == "":
            await ctx.send("*Please enter the command in the following format:*\n **!mcannounce** **add** *<announcement message>*")
            return
        with open('announcements.txt', 'a') as file:
            file.write(arg2 + '\n')
            file.close()
        await ctx.send("**Announcement successfully added**")
        return

    if operation == 'remove':
        if not arg2.isnumeric():
            await ctx.send("*Please enter the command in the following format:*\n **!mcannounce** **remove** *<number>*")
            return
        if cringeCheck == False:
            await ctx.send('Are you sure? This action cannot be reversed. Enter the command again to confirm')
            cringeCheck = True
            return
        delete_line('announcements.txt', int(arg2) - 1)
        cringeCheck = False
        await ctx.send("**Announcement successfully removed**")
        return

    if operation == 'show':
        if arg2 != "":
            if arg2.isnumeric():
                await ctx.send('Showing announcement #' + arg2)
                await ctx.send('```' + lines[int(arg2) - 1] + '```')
                return
            else:
                await ctx.send("*Please enter the command in the following format:*\n **!mcannounce** **show** *<number>*")
        i = 1
        await ctx.send("**Showing all announcements in rotation**")
        for line in lines:
            await ctx.send('```' + str(i) + ". " + line + '```')
            i += 1
        await ctx.send("**Finished**")
        return
    await ctx.send("*Please enter a valid mcannounce operation: 'add', 'remove', or 'show'")


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


@client.command(help='Provides a link to the dynmap')
async def dynmap(ctx):
    await ctx.send('http://149.56.85.85:8123/')


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


@client.command(name='grayscale', help="Takes a given image URL and returns the same image, but grayscaled")
async def grayscale(ctx, imageUrl):
    try:
        filepath = opencv.download_img(imageUrl)
    except Exception as e:
        await ctx.send('Please provide a valid url')
        return
    opencv.grayscale(filepath)
    if os.path.exists(filepath):
        await ctx.send(file=discord.File(filepath))
    opencv.delete_file(filepath)


@client.command(name='facedetect', help="Takes image url and returns the same image with faces marked")
async def facedetect(ctx, imageUrl):
    try:
        filepath = opencv.download_img(imageUrl)
    except Exception as e:
        await ctx.send('Please provide a valid url')
        return
    opencv.face_detect(filepath)
    if os.path.exists(filepath):
        await ctx.send(file=discord.File(filepath))
    opencv.clean_temp()

# HELPERS
# =========================================================================


def delete_line(original_file, line_number):
    """ Delete a line from a file at the given line number """
    is_skipped = False
    current_index = 0
    dummy_file = original_file + '.bak'
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Line by line copy data from original file to dummy file
        for line in read_obj:
            # If current line number matches the given line number then skip copying
            if current_index != line_number:
                write_obj.write(line)
            else:
                is_skipped = True
            current_index += 1
    # If any line is skipped then rename dummy file as original file
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)


# Activate for testing
with open("token.txt") as f:
    TOKEN = f.read().strip()
client.run(TOKEN)

# Activate for release
# client.run(os.environ["ACCESS_TOKEN"])
