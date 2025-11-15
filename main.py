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

bot = commands.Bot(command_prefix=".", intents=intents)

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

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, {0.author.mention}!".format(ctx))

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"{ctx.author.mention} You said {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message!")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question, color=discord.Color.dark_purple())
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("✅")
    await poll_message.add_reaction("❌")

@bot.command()
async def seb_mug(ctx):
    # Load the local file
    file = discord.File("seb_mugshot.jpg", filename="seb_mugshot.jpg")

    # Create the embed
    embed = discord.Embed(
        title="Seb Mugshot",
        description="Here it is 😭💔🥀\n\n(Why does he look like that…) ",
        color=discord.Color.green()
    )

    # Attach the image INSIDE the embed
    embed.set_image(url="attachment://seb_mugshot.jpg")

    # Send embed + file
    await ctx.send(embed=embed, file=file)

@bot.command()
async def erika(ctx):
    # 1. Load audio file
    audio_file = discord.File("audio/erika.mp3", filename="audio/erika.mp3")

    # 2. Load image
    image_file = discord.File("images/erika.png", filename="images/erika.png")

    # 3. Build embed
    embed = discord.Embed(
        title="Erika – Song",
        description="aarav favourite song...",
        color=discord.Color.red()
    )

    # 4. Add image INSIDE embed
    embed.set_image(url="attachment://erika.png")

    # 5. Add lyrics text underneath image
    embed.add_field(
        name="Lyrics",
        value=(
            """1. Auf der Heide blüht ein kleines Blümelein (xxx)
und das heißt (xxx) Erika. (xxx)
Heiß von hunderttausend kleinen Bienelein (xxx)
wird umschwärmt (xxx) Erika. (xxx)
Denn ihr Herz ist voller Süßigkeit, (xxx)
zarter Duft entströmt dem Blütenkleid. (xxx)
Auf der Heide blüht ein kleines Blümelein (xxx)
und das heißt (xxx) Erika. (xxx)
(xxx) as before

2. In der Heimat wohnt ein kleines Mägdelein
und das heißt Erika.
Dieses Mädel ist mein treues Schätzelein
und mein Glück, Erika.
Wenn das Heidekraut rot-lila blüht,
singe ich zum Gruß ihr dieses Lied.
Auf der Heide blüht ein kleines Blümelein
und das heißt: Erika.

3. In mein'm Kämmerlein blüht auch ein Blümelein
und das heißt Erika.
Schon beim Morgengrau'n sowie beim Dämmerschein
schaut's mich an, Erika.
Und dann ist es mir, als spräch' es laut:
"Denkst du auch an deine kleine Braut?"
In der Heimat weint um dich ein Mägdelein
und das heißt Erika."""
        ),
        inline=False
    )

    # 6. Send everything
    await ctx.send(
        embed=embed,
        files=[audio_file, image_file]
    )

bot.run(token, log_handler=handler, log_level=logging.DEBUG)