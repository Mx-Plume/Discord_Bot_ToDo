import discord
import sys
from discord.ext import commands

# Add task day

class DAdd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dadd(self, ctx, arg):
        f= open("./save/day", "a")
        task = arg+ "\n"
        f.write(task)
        await ctx.send(f"__**You add a new task**:__ {task}")

def setup(bot):
    bot.add_cog(DAdd(bot))