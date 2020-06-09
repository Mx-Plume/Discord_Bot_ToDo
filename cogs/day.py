import discord
from discord.ext import commands
from datetime import datetime

#print task day

class Day(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def day(self, ctx):
        now = datetime.strftime(datetime.now(), '%A, %d %B %Y')
        await ctx.send(f"__**{now} task list**__\n\n")
        f= open("./save/day", "r")
        if f.mode == 'r':
            task = f.read()
            await ctx.send(task)

def setup(bot):
    bot.add_cog(Day(bot))