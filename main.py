import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to FATTY_SMP {member.name}!!!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "seb is not a fatty" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} don't use that sentence. Seb is a FATTY. REMEMBER RULE ONE NEVER SAY seb is not a fatty!!!")

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)