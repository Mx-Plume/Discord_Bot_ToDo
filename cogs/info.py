import discord
from discord.ext import commands

# Print Info

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.send("<:info:718551227809660948> **Info** <:info:718551227809660948>\n\n__**Commands list :**__\n\t**&info :** Show commands list\n\t**&day : **Show today\'s tasks\n\t**&dadd : **Add today's task\n\t**&dclean :** Clean today\'s tasks\n\n*version : 1.0.1*")

def setup(bot):
    bot.add_cog(Info(bot))