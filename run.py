# shenhe_music bot by seria

from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

# load .env variables
load_dotenv()

# the bot class
class ShenheMusic(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default(),
            application_id=os.get_env("APP_ID"),
        )

    async def setup_hook(self) -> None:
        # load the music cog
        await self.load_extension("cogs.music")

    async def on_ready(self) -> None:
        # change presence
        await self.change_presence(
            discord.Activity(type=discord.ActivityType.listening, name="/music")
        )
        print(f"Logged in as {self.user}")


bot = ShenheMusic()
bot.run(os.getenv("TOKEN"))
