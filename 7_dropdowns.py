import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.environ['GUILD_ID'])])  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

class ColourSelect(discord.ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(label='Red'),
            discord.SelectOption(label='Green'),
            discord.SelectOption(label='Blue'),
        ]
        super().__init__(placeholder='Pick a colour', options=options)

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f'You picked {self.values[0]}!')

class ColourView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.add_item(ColourSelect())

@bot.slash_command(description='Send a dropdown menu')
async def dropdown(ctx: discord.ApplicationContext) -> None:
    await ctx.respond('Here is a dropdown:', view=ColourView())

bot.run(os.getenv('DISCORD_TOKEN'))
