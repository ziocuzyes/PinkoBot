import os
 
import discord
from discord.ext import commands
 
# --- settings you should edit ---
TOKEN = os.environ["DISCORD_TOKEN"]  # set this in Railway's "Variables" tab, never hardcode it
CHANNEL_NAME = "general"  # the text channel the bot will post hello/goodbye in
# ---------------------------------
 
intents = discord.Intents.default()
intents.members = True  # required for on_member_join / on_member_remove to fire
 
bot = commands.Bot(command_prefix="!", intents=intents)
 
 
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id: {bot.user.id})")
 
 
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name=CHANNEL_NAME)
    if channel:
        await channel.send(f"hello {member.mention}, welcome to the server!")
 
 
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name=CHANNEL_NAME)
    if channel:
        await channel.send(f"{member.name} just left. goodbye!")
 
 
bot.run(TOKEN)
