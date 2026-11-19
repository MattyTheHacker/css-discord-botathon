import os

import discord
import dotenv

dotenv.load_dotenv()

bot = discord.Bot(debug_guilds=[int(os.environ['GUILD_ID'])])  # type: ignore[no-untyped-call]

@bot.event
async def on_ready() -> None:
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.slash_command(description='Send an embed')
async def embed(ctx: discord.ApplicationContext) -> None:
    my_embed = discord.Embed(title='My embed', description='This is the description', colour=discord.Colour.blurple())
    my_embed.add_field(name='Field 1', value='This field is inline', inline=True)
    my_embed.add_field(name='Field 2', value='So is this one', inline=True)
    my_embed.set_image(url=ctx.author.display_avatar.url)
    my_embed.set_footer(text='This is the footer')
    await ctx.respond(embed=my_embed)

bot.run(os.getenv('DISCORD_TOKEN'))
