import discord
import datetime
import time
import psutil
import sys
from discord.ext import commands

start_time = time.time()

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
#    def restart_program():
#        python = sys.executable
#        os.execl(python, python, * sys.argv)

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
    @commands.command(pass_context=True)
    async def status(self, ctx):
        # Time
        current_time = time.time()
        difference = int(round(current_time - start_time))
        utime = str(datetime.timedelta(seconds=difference))

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        # PSUtil - RAM Usage
        dict(psutil.virtual_memory()._asdict())
        usedmem = psutil.virtual_memory().used/1024/1024
        # activemem = psutil.virtual_memory().active
        tmem = psutil.virtual_memory().total/1024/1024
        pmem = round((usedmem/tmem)*100)

        # PSUtil - Swap Memory Usage
        # dict(psutil.swap_memory()._asdict())
        # uswap = psutil.swap_memory().used/1024/1024
        # tswap = psutil.swap_memory().total/1024/1024
        # pswap = round((uswap/tswap)*100)

        #Bot Prefix Read
        with open (f"./prefix.txt", "r") as botprefix:
            prefix = botprefix.read()

        # PSUtil Operating System
        if psutil.LINUX:
            os = 'Linux'
        elif psutil.MACOS:
            os = 'MacOS'
        elif psutil.WINDOWS:
            os = 'Windows'
        else:
            os = 'Unknown'
        embed.set_author(name='System Monitor')
        embed.add_field(name="CPU Usage", value=f'{psutil.cpu_percent()}%', inline=True)
        embed.add_field(name="CPU Cores", value=psutil.cpu_count(), inline=True)
        embed.add_field(name="RAM Usage", value=f'{round(usedmem)}/{round(tmem)}MB ({round(pmem)}%)', inline=True)
        embed.add_field(name="Operating System", value=os, inline=True)
        # embed.add_field(name="Swap Usage", value=f'{round(uswap)}/{round(tswap)}MB ({round(pmem)}%)', inline=True)
        embed.add_field(name="Uptime", value=f'{utime}', inline=True)
        embed.add_field(name='API Latency', value=f'{round(self.bot.latency * 1000)} ms', inline=True)
        embed.add_field(name='Bot Prefix', value=f"`{prefix}`", inline=False)
        embed.set_footer(text="Bot by SilentVOEZ")
        await ctx.send(embed=embed)
        botprefix.close()

#    @commands.command()
#    @commands.is_owner()
#    async def reboot(self, ctx):
#        await ctx.send('Rebooting...')
#        restart_program()

    @commands.command()
    @commands.is_owner()
    async def e(self, ctx):
        print(f"---EMERGENCY SHUTDOWN REQUESTED BY {ctx.author}---")
        await ctx.send("**--EMERGENCY SHUTDOWN--**")
        await ctx.bot.logout()

def setup(bot):
    bot.add_cog(Utility(bot))
