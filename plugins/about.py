import discord, datetime
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        avatar = self.bot.user.avatar_url
        embed = discord.Embed(
            colour = 0xff0000
        )

        embed.set_author(name='About Haato Bot')
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text='Made by SilentVOEZ')

        embed.add_field(name='\u200b', value="Haato Bot is a fork from QnA Bot with removed features. \nHaato Bot includes basic general tools, moderation, fun, anime image search and most of all the Haachama cooking! \n\n Source code is available [here](https://www.github.com/SilentVOEZ/haato-bot). \nInvite the bot to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=738671808139624448&permissions=486518&scope=bot).", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))