import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot()  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    print(f"Bot has access to: {', '.join([guild.name for guild in bot.guilds])}")
    print('------')

bot.run(os.getenv('DISCORD_TOKEN'))
