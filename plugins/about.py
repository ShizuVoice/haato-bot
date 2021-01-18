import discord, datetime
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        avatar = self.bot.user.avatar_url
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='About Haato Bot')
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text='Made by SilentVOEZ')

        embed.add_field(name='\u200b', value="Haato Bot was a fork from QnA Bot with removed features. \nHaato Bot is a basic bot that includes general tools, moderation, fun, anime image search and most of all the Haachama cooking!", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))