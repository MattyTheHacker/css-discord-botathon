import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.environ['GUILD_ID'])])  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

class Greetings(discord.Cog):
    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print('Greetings cog is ready')

    @discord.slash_command(description='Say hello from a cog')
    async def hello(self, ctx: discord.ApplicationContext) -> None:
        await ctx.respond('Hello from the Greetings cog!')

bot.add_cog(Greetings())

bot.run(os.getenv('DISCORD_TOKEN'))
