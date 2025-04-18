import discord
from discord.ext import commands
from discord import app_commands
from email.message import EmailMessage
import smtplib
import os
import pdfkit
from jinja2 import Environment, FileSystemLoader

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

env = Environment(loader=FileSystemLoader("templates"))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(e)

@bot.tree.command(name="receipt", description="Vygeneruj účtenku")
@app_commands.describe()
async def receipt(interaction: discord.Interaction):
    await interaction.response.send_message("Tento bot používa formulár, ktorý bude pridaný čoskoro.", ephemeral=True)

bot.run(os.getenv("DISCORD_TOKEN"))