import discord
import datetime
import time
import sys
from discord.ext import commands
from discord import Embed

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        consoletime = datetime.datetime.now()
#        print(f'{consoletime} [INFO] Pinging at `{round(self.bot.latency * 1000)} ms`')
#        await ctx.send(f'Pong! Responded for `{round(self.bot.latency * 1000)} ms`')
        before = time.monotonic()

        embed1 = Embed(title='Pong!', description=f':globe_with_meridians: End-to-End Delay: 0ms\n\n :book: API Latency: 0ms', colour = discord.Colour.green())
 
        msg = await ctx.send(embed=embed1)

        ping = (time.monotonic() - before) * 1000
        embed2 = Embed(title='Pong!', description=f':globe_with_meridians: End-to-End Delay: {int(ping)}ms\n\n :book: API Latency: {round(self.bot.latency * 1000)}ms', colour = discord.Colour.green())

        await msg.edit(embed=embed2)
        print(f'{consoletime} [INFO] Pinging with an End-to-End Delay of {int(ping)}ms and API Latency of {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")
    
    @commands.command()
    async def version(self, ctx):
        # Change the bot's version on this part
        BotV = '0.4 Beta Version'
        DpyV = discord.__version__
        PyVMaj = sys.version_info.major
        PyVMin = sys.version_info.minor
        PyVMic = sys.version_info.micro

        avatar = self.bot.user.avatar_url
        embed = discord.Embed(
            colour = 0xff0000
        )

        embed.set_author(name='Haato Bot')
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text='Bot by SilentVOEZ')

        embed.add_field(name='Version', value=BotV, inline=False)
        embed.add_field(name='Discord.py Version', value=DpyV, inline=False)
        embed.add_field(name='Python Version', value=(f'{PyVMaj}.{PyVMin}.{PyVMic}'), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        consoletime = datetime.datetime.now()
        await ctx.send(message)
        print(f"{consoletime} [INFO] Say triggered by '{ctx.author}'. User said: '{message}'")
        await ctx.message.delete()

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'ID: {member.id}')

        embed.add_field(name='Server nickname:', value=member.display_name)

        embed.add_field(name='Created at:', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name='Top role:', value=member.top_role.mention)

        embed.add_field(name='Bot?', value=member.bot)

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
            member = ctx.author if not member else member

            embed = discord.Embed(
                colour = member.color
            )

            embed.add_field(name=f'{member}', value=f'[Link]({member.avatar_url})', inline=False)
            embed.set_image(url=member.avatar_url)

            await ctx.send(embed=embed)

# Dedicated error handling for this command
    @say.error
    async def say_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        with open (f"./prefix.txt", "r") as botprefix:
            prefix = botprefix.read()

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"What should I say? `{prefix}say <your response>`")
            print(f'{consoletime} [INFO] Say triggered, but no arguments found.')
            botprefix.close()

def setup(bot):
    bot.add_cog(General(bot))