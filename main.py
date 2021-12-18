import dotenv

from discord.ext import commands
import discord
from discord_funcs import *
from database_funcs import *

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

MODERATOR_ROLES = ["The Grubber", "Mods", "Cool People"]
VOTE_EMOTES = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven", ":eight:", ":nine:", ":ten:"]
TOKEN = dotenv.get_key('.env', "BOT_KEY")

@bot.event
async def on_ready():
    print("Signed in as", bot.user)

@commands.has_any_role(*MODERATOR_ROLES)
@bot.command()
async def start_game(ctx, vote_time):
    text = "The community will be playing with the white pieces. What should the first move be? "
    message = await ctx.send(text)
    poll_message = discord.utils.get(id=message.id)

    await poll_message.add_reaction()

bot.run(TOKEN)