import discord
import asyncio
from discord.ext import commands
from discord import Embed

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = Embed(title='Haato Bot Commands',
            description="**General Commands**\n `hello` `ping` `say` `userinfo` `avatar` `status` `version` `invite` `about`\n\n **Fun Commands**\n `rps` `roll` `eightball` `eighballfil` `choose` `bonk` `loli`\n\n **Haato Things**\n `cooking` `eat`\n\n **Booru Commands - 50/50 NSFW**\n `yandere` `moebooru` `danbooru`\n\n **last.fm Commands**\n `lfmuser` `lfmnp`\n\n **Moderation Commands (Beta)**\n `changeprefix` `pas` `warn` `kick` `ban` `purge` `uhelp`\n\n *For the complete guide of the commands, visit the GitHub page [here](https://www.github.com/SilentVOEZ/haato-bot).*\n\n **Note:** *DMs does not work with the bot.*", colour = 0xff0000)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.is_owner()
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
        embed.add_field(name='reboot', value='Reboots the bot outside the terminal.', inline=False)
        embed.add_field(name='sudohalt', value='Shuts down the system where the bot runs on.', inline=False)
        embed.add_field(name='sudoreboot', value='Reboots the system where the bot runs on.', inline=False)

        await author.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))