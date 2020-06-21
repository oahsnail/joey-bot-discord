import discord
import random
from discord.ext import commands

# 724115000578539586 <- general channel id
# 724374341579702394 <- welcome channel id
# 724370556186787881 <- test channel id


client = commands.Bot(command_prefix='!')

# When bot is ready
@client.event
async def on_ready():
    print("bot is online")


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel == client.get_channel(724115000578539586):    # general
            print(str(member) + ' has joined the server')
            nameString = str(member)
            await channel.send(f"Welcome {nameString[0:len(nameString) - 5]} to JoeyCraft!")


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if channel == client.get_channel(724115000578539586):    # general
            if (member.nick):
                print(str(member.nick) + ' has left the server')
                await channel.send(f"{str(member.nick)} has escaped JoeyCraft :(")
            else:
                nameString = str(member)
                await channel.send(f"{nameString[0:len(nameString)-5]} has escaped JoeyCraft :(")
                print(nameString[0:len(nameString) - 5] +
                      ' has left the server')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


client.run('NzI0MTA3NjAwODk5MzQyNDE3.Xu-2zA.4j_jILDJmoW8J5pD-7tEKf_dozI')


# client.logout()
