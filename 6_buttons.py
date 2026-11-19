import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.environ['GUILD_ID'])])  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

class ButtonView(discord.ui.View):
    @discord.ui.button(label='Click me!', style=discord.ButtonStyle.primary)
    async def click(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('You clicked the button!')

@bot.slash_command(description='Send a button')
async def button(ctx: discord.ApplicationContext) -> None:
    await ctx.respond('Here is a button:', view=ButtonView())

bot.run(os.getenv('DISCORD_TOKEN'))
