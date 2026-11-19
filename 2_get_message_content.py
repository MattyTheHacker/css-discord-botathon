import os

import discord
import dotenv

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message: discord.Message) -> None:
    print(f'{message.author.name}: {message.content}')

bot.run(os.getenv('DISCORD_TOKEN'))
