import dotenv
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", )

MODERATOR_ROLES = ["The Grubber", "Mods", "Cool People"]
TOKEN = dotenv.get_key('.env', "BOT_KEY")


bot.run(TOKEN)