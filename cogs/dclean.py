import discord
from discord.ext import commands

#clean task day

class DClean(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dclean(self, ctx):
        f= open("./save/day", "w")
        task = "\n"
        f.write(task)
        await ctx.send(f"__**You have deleted your tasks**__")

def setup(bot):
    bot.add_cog(DClean(bot))