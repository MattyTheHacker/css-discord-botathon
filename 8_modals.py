import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.environ['GUILD_ID'])])  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

class NameModal(discord.ui.Modal):
    def __init__(self) -> None:
        super().__init__(title='Introduce yourself')
        self.add_item(discord.ui.InputText(label='What is your name?'))

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f'Hello, {self.children[0].value}!')

@bot.slash_command(description='Open a form')
async def modal(ctx: discord.ApplicationContext) -> None:
    await ctx.send_modal(NameModal())

bot.run(os.getenv('DISCORD_TOKEN'))
