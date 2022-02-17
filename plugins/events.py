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
    async def on_command_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to do that!")
            print(f"{consoletime} [ERROR] Admin/mod command triggered but user didn't have enough permission to use it!")
        if isinstance(error, commands.NotOwner):
            await ctx.send("Sorry, you are not part of the \"Owner\" group.")
            print(f"{consoletime} [ERROR] Owner command triggered but user was not one of the bot owners.")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command doesn't exist. *Maybe you have typed it wrong, no?*")
            print(f"{consoletime} [INFO] User invoked the bot with non-existing command.")

        raise error

    @commands.Cog.listener()
    async def on_message(self, message):
        consoletime = datetime.datetime.now()
        if message.author == self.bot.user:
            return

        if message.content.startswith("sus"):
            await message.channel.send("amogus")
            print(f"{consoletime} [INFO] {message.author} said 'sus', bot said 'amogus'.")
        elif message.content.startswith("amogus"):
            await message.channel.send("sus")
            print(f"{consoletime} [INFO] {message.author} said 'amogus', bot said 'sus'.")
        elif message.content.startswith("erosena"):
            await message.channel.send("`Onii-chan pierce my **** with your huge hot ****! Pump me full of your **** milk!`")
            print(f"{consoletime} [INFO] {message.author} said 'erosena', bot said the ero lines of Kashiwazaki Sena.")

def setup(bot):
    bot.add_cog(Events(bot))
