import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

# Set up bot
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=GUILD_ID)
    print(f"✅ Logged in as {client.user} (ID: {client.user.id})")
    print(f"✅ Slash commands synced for guild: {GUILD_ID.id}")

@tree.command(name="ping", description="Check if the bot is online", guild=GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! Bot is connected and responding.")

client.run(DISCORD_TOKEN)
