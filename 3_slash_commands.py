import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.environ['GUILD_ID'])])  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.slash_command(description='Say hello to someone')
async def hello(ctx: discord.ApplicationContext, name: str) -> None:
    await ctx.respond(f'Hello, {name}!')

@bot.slash_command(description='Send a message only you can see')
async def secret(ctx: discord.ApplicationContext) -> None:
    await ctx.respond('Only you can see this!', ephemeral=True)

bot.run(os.getenv('DISCORD_TOKEN'))
