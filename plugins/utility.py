import discord
import os
import asyncio
import datetime
import time
import psutil
import sys
import platform
from discord.ext import commands

start_time = time.time()
consoletime = datetime.datetime.now()

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

# Status Cycle
    @commands.command()
    @commands.is_owner()
    async def online(self, ctx, *, cactivity = ""):
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{cactivity}', type=3))

    @commands.command()
    @commands.is_owner()
    async def idle(self, ctx, *, cactivity = ""):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'{cactivity}', type=3))

    @commands.command()
    @commands.is_owner()
    async def dnd(self, ctx, *, cactivity = ""):
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=f'{cactivity}', type=3))

# Utility
    @commands.command()
    @commands.is_owner()
    async def sysinfo(self, ctx):
        
        #Platform call
        osname = platform.system()
        osrelease = platform.release()
        machine = platform.machine()
        platformv = platform.platform()
        sysname = platform.node()

        embed = discord.Embed(
            colour = 0xB8650C
        )

        embed.set_author(name='System Info')
        embed.add_field(name="Operating System", value=osname, inline=True)
        embed.add_field(name="Version", value=osrelease, inline=True)
        embed.add_field(name="Architecture Type", value=machine, inline=False)
        embed.add_field(name="Full Platform Name", value=platformv, inline=False)
        embed.add_field(name="System Name", value=sysname, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def owner(self, ctx):
        try:
            await ctx.send("You are part of the \"Owner\" group.")
        except:
            pass

    @commands.command()
    @commands.is_owner()
    async def e(self, ctx):
        print(f"---EMERGENCY SHUTDOWN REQUESTED BY {ctx.author}---")
        await ctx.send("**--EMERGENCY SHUTDOWN--**")
        await ctx.bot.close()

    @commands.command()
    @commands.is_owner()
    async def sudoreboot(self, ctx, *, reason = None):
        embed = discord.Embed(colour = discord.Colour.red())
    
        current_time = time.time()
        difference = int(round(current_time - start_time))
        utime = str(datetime.timedelta(seconds=difference))
    
        embed.set_author(name='Haato Bot Notice')
        embed.set_thumbnail(url='https://i.imgur.com/YyIPdSf.png')
        embed.add_field(name='Status', value='System is rebooting.', inline=False)
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        embed.add_field(name='Uptime', value=f'{utime}', inline=False)
        embed.set_footer(text=f'All requests at this moment will be done and system will restart. Bot owner needs to manually start the bot after system restart.')
        await ctx.send(embed=embed)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print('--------------------------------')
        print(f'{consoletime} [WARNING] SYSTEM IS REBOOTING. NEED MANUAL START AFTER THIS ACTION.')
        print('--------------------------------')

        await asyncio.sleep(10)

        if psutil.WINDOWS:
            os.system('shutdown -r -f -t 0')
        else:
            os.system('sudo shutdown -r now')

    @commands.command()
    @commands.is_owner()
    async def sudohalt(self, ctx, *, reason = None):
        embed = discord.Embed(colour = discord.Colour.red())
    
        current_time = time.time()
        difference = int(round(current_time - start_time))
        utime = str(datetime.timedelta(seconds=difference))
    
        embed.set_author(name='Haato Bot Notice')
        embed.set_thumbnail(url='https://i.imgur.com/YyIPdSf.png')
        embed.add_field(name='Status', value='System is shutting down.', inline=False)
        embed.add_field(name='Reason', value=f'{reason}', inline=False)
        embed.add_field(name='Uptime', value=f'{utime}', inline=False)
        embed.set_footer(text=f'All requests at this moment will be done and system will restart.')
        await ctx.send(embed=embed)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print('--------------------------------')
        print(f'{consoletime} [WARNING] SYSTEM IS SHUTTING DOWN.')
        print('--------------------------------')

        await asyncio.sleep(10)

        if psutil.WINDOWS:
            os.system('shutdown -r -f -t 0')
        else:
            os.system('sudo shutdown -r now')

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        consoletime = datetime.datetime.now()
        await ctx.send('Bot is rebooting...')
        print('--------------------------------')
        print(f'{consoletime} [WARNING] Bot is rebooting...')
        print('--------------------------------')
        await asyncio.sleep(5)

        args = sys.argv[:]  # get shallow copy of running script args
        args.insert(0, sys.executable)  # give it the executable
        os.execv(sys.executable, args)  # execute the script with current args, effectively relaunching it, can modify args above to change how it relaunches

def setup(bot):
    bot.add_cog(Utility(bot))
