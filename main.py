import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))
ENABLE_VOICE = os.getenv("ENABLE_VOICE", "false").lower() == "true"

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=GUILD_ID)
    print(f"✅ Logged in as {client.user} (ID: {client.user.id})")
    print(f"✅ Slash commands synced to guild {GUILD_ID.id}")
    if ENABLE_VOICE:
        print("🔊 Voice mode ENABLED")
    else:
        print("🔇 Voice mode DISABLED")

@tree.command(name="ping", description="Check if the bot is online", guild=GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! Bot is connected and responding.")

# Placeholder for voice feature if enabled
if ENABLE_VOICE:
    try:
        import audioop
        from discord import VoiceChannel, FFmpegPCMAudio
        print("Voice features loaded.")
        # Add voice-related functions here as needed
    except ImportError:
        print("⚠️ Voice modules could not be loaded. Check server compatibility.")

client.run(DISCORD_TOKEN)
