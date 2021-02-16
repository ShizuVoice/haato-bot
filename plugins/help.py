import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.send("Please enable direct messaging if you turned it off. I can't send you this 3 love le- I MEAN THE DOCS. *Baka~*")
#        await ctx.send("Please enable direct messaging if you turned it off. I can't send you the help guide for this bot.")
        await asyncio.sleep(2)
        author = ctx.message.author

        embed = discord.Embed(
            colour = 0xff0000
        )

        embed.set_author(name='General Help')
        embed.add_field(name='hello', value='Respond with "Hello!" when bot is online.', inline=False)
        embed.add_field(name='ping', value='Respond with "Pong!" and latency time.', inline=False)
        embed.add_field(name='say', value='Make the bot say with your response.', inline=False)
        embed.add_field(name='userinfo', value='Shows info of a mentioned user or yourself.', inline=False)
        embed.add_field(name='avatar', value="Shows you the full size of the user's profile picture.", inline=False)
        embed.add_field(name='status', value="Shows the status of the computer where the bot is running on", inline=False)
        embed.add_field(name='version', value='Shows the bot version.', inline=False)
        embed.add_field(name='about', value='Shows the about dialog of the bot.', inline=False)

        await author.send(embed=embed)
        await asyncio.sleep(2)

        embed = discord.Embed(
            colour = 0xff0000
        )

        embed.set_author(name='Fun and Others')
        embed.add_field(name='rps', value='Play rock, paper, scissor!', inline=False)
        embed.add_field(name='eightball', value='Ask the eightball for question.', inline=False)
        embed.add_field(name='eightballfil', value='Magtanong kay eightball ng isang katanungan.', inline=False)
        embed.add_field(name='bonk', value='Bonks a user for being too horny.')
        embed.add_field(name='cooking', value='Have some cooking tips from Akai Haato.', inline=False)
        embed.add_field(name='yandere', value="Fetches images with the tag. Can't guarantee that it filters out NSFW images.", inline=False)
        embed.add_field(name='moebooru', value="Fetches images with the tag. Can't guarantee that it filters out NSFW images.", inline=False)
        embed.add_field(name='danbooru', value="Fetches images with the tag. Can't guarantee that it filters out NSFW images.", inline=False)

        await author.send(embed=embed)
        await asyncio.sleep(2)

        embed = discord.Embed(
            colour = 0xff0000
        )

        embed.set_author(name='Moderation (Administrator)')
        embed.add_field(name='pas', value='Make a public address within that channel you were on.', inline=False)
        embed.add_field(name='warn', value='Warns a member on the server.', inline=False)
        embed.add_field(name='kick', value='Kicks a member on the server.', inline=False)
        embed.add_field(name='ban', value='Bans a member on the server.', inline=False)
        embed.add_field(name='purge', value='Clears messages with a certain amount.', inline=False)
        embed.add_field(name='uhelp', value='Sends a DM about owner-only command.', inline=False)

        await author.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.is_owner()
    @commands.has_permissions(kick_members=True)
    async def uhelp(self,ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = 0xff0000
        )

        embed.set_author(name='Utility Help (Owner only)')
        embed.add_field(name='load', value='Loads the cog inside the `plugins` folder', inline=False)
        embed.add_field(name='unload', value='Unloads the cog inside the `plugins` folder', inline=False)
        embed.add_field(name='reload', value='Reloads the cog inside the `plugins` folder.', inline=False)
        embed.add_field(name='loadall', value='Loads all the cogs inside the `plugins` folder.', inline=False)
        embed.add_field(name='unloadall', value='Unloads all the cogs inside the `plugins` folder.', inline=False)
        embed.add_field(name='shutdown', value='Shuts down the bot outside the terminal.', inline=False)

        await author.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))