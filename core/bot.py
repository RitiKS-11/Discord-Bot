import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from scraper import meme


load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv('GUILD')

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='>')


@bot.command(name="hello")
async def say_hello(ctx):
    response = 'Hey, want to see some meme'
    await ctx.send(response)

@bot.command(name="meme")
async def get_meme(ctx):
    new_meme = meme()

    embed = discord.Embed(title='BitBot',color=discord.Color.red())
    embed.title = new_meme['title']
    embed.url = new_meme['post']
    embed.set_image(url=new_meme['image'])

    await ctx.send(embed=embed)

@bot.command(name="members")
async def get_members(ctx):
    for guild in bot.guilds:
        if guild == GUILD:
            break

    members = '\n'.join([member.name for member in guild.members])
    await ctx.send(members)




if __name__ == "__main__":
    bot.run(TOKEN)

