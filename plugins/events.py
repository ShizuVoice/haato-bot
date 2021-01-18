import discord
import datetime
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_disconnect(self):
        consoletime = datetime.datetime.now()
        print(f"{consoletime} [WARNING] {self.bot.user.name} got disconnected! Attempting to reconnect...")

    @commands.Cog.listener()
    async def on_connect(self):
        consoletime = datetime.datetime.now()
        print(f"{consoletime} [INFO] {self.bot.user.name} successfully connected.")

    @commands.Cog.listener()
    async def on_message(self, message):
        consoletime = datetime.datetime.now()
        if message.author == self.bot.user:
            return

        message.content.lower()
        if message.content.startswith('silentvoice'):
            await message.channel.send("<@170093603530473472>")
            print(f"{consoletime} [INFO] Event triggered. 'silentvoice'.")
        elif message.content.startswith('sv'):
            await message.channel.send("<@170093603530473472>")
            print(f"{consoletime} [INFO] Event triggered. 'sv'.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to do that!")
            print(f"{consoletime} [WARNING] Admin/mod command triggered but user didn't have enough permission to use it!")
#        if isinstance(error, commands.CommandInvokeError): # This code keeps raising as an error if bot doesn't have enough permission or an error occured over bad or missing arguments.
#            await ctx.send("Command error!")
#            print(f"{consoletime} [WARNING] Bot doesn't have permission to do certain action. Check other roles that may be overriding the bot's own role permission.")
        if isinstance(error, commands.NotOwner):
            await ctx.send("You are not one of the owner of this bot!")
            print(f"{consoletime} [WARNING] Owner command triggered but user was not one of the bot owners.")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command doesn't exist. *Maybe you have typed it wrong, no?*")
            print(f"{consoletime} [INFO] User invoked the bot with non-existing command.")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))