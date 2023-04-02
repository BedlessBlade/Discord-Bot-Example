#Import the required libraries/modules
#The only dependency is discord.py, to install it run "pip install discord.py" in your terminal
import discord
from discord.ext import commands, tasks
import random
import time
from itertools import cycle
#To change the command prefix edit the current "!" below
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#Change the sentences/words in the cycle to change the status
#You can also change it to one string instead of the cycle
bot_status = cycle(["!help for help!", "!gpt coming soon!", "Try !8ball!", "A rubik's cube"])
@client.event
async def on_ready():
    print("Success: Bot is connected to discord")
    change_status.start()
@client.command(aliases=["Ping", "PING"])
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Pong! {latency} ms")
@client.command(aliases=["Pong", "PONG"])
async def pong(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Ping! {latency} ms")
@client.command(aliases=["Roll", "ROLL", "dice", "die", "gamble"])
async def roll(ctx):
    await ctx.send(random.randint(1, 6))
@client.command(aliases=["Hello, World", "Hello World", "hello, world", "hello world"])
async def helloworld(ctx):
    await ctx.send("In Python 3, you would use print() for printing characters. Specify the characters inside qoutes. Put this charector in qoutes inside of the () It will print the string.")
@client.command(aliases=["botheryoself", "annoying", "dmtest"])
async def annoyurself(ctx):
    await ctx.author.send("bro you must be so annoyed rn") 
@client.command()
async def sus(ctx):
    await ctx.send("https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif")
@client.command()
async def megasus(ctx):
    await ctx.send("https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif")
    await ctx.send("https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif")
    await ctx.send("https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif")
    await ctx.send("https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif")
    await ctx.send("https://media.tenor.com/GBdIH5sL4XQAAAAM/the-rock-rock.gif")
@client.command()
async def memes(ctx):
    await ctx.send("https://tenor.com/")
#Remove down to the 8ball if you don't want to have this absolutely terrible command
@client.command()
async def megaping(ctx):
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    time.sleep(10)
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
    await ctx.send("@everyone")
#8ball command, responses pulled from wikipedia (I know this is a terrible way to do this you don't have to tell me
#but i wanted everything in one file
@client.command(aliases=["8ball", "magicball", "eightball"])
async def magic_eightball(ctx, *, question):
    n = random.randint(1, 20)
    print("Chosen response number", n)
    if n == int(1):
        await ctx.send("It is certain.")
    if n == int(2):
        await ctx.send("It is decidedly so.")
    if n == int(3):
        await ctx.send("Without a doubt.")
    if n == int(4):
        await ctx.send("Yes definitely.")
    if n == int(5):
        await ctx.send("You may rely on it.")
    if n == int(6):
        await ctx.send("As I see it, yes.")
    if n == int(7):
        await ctx.send("Most likely.")
    if n == int(8):
        await ctx.send("Outlook good.")
    if n == int(9):
        await ctx.send("Yes.")
    if n == int(10):
        await ctx.send("Signs point to yes.")
    if n == int(11):
        await ctx.send("Reply hazy, try again.")
    if n == int(12):
        await ctx.send("Ask again later.")
    if n == int(13):
        await ctx.send("Better not tell you now.")
    if n == int(14):
        await ctx.send("Cannot predict now.")
    if n == int(15):
        await ctx.send("Concentrate and ask again.")
    if n == int(16):
        await ctx.send("Don't count on it.")
    if n == int(17):
        await ctx.send("My reply is no.")
    if n == int(18):
        await ctx.send("My sources say no.")
    if n == int(19):
        await ctx.send("Outlook not so good.")
    if n == int(20):
        await ctx.send("Very doubtful.")
@tasks.loop(seconds=5)
async def change_status():
    #Changes bot status to the cycle at the beginning of the program
    await client.change_presence(activity=discord.Game(next(bot_status)))
#Put your discord bot token in the area labeled "HERE"
client.run("HERE")
