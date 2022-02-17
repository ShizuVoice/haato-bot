# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="No reason"):
        consoletime = datetime.datetime.now()

        embed = discord.Embed(description=f"***{member.mention} has been warned! || {reason}***", colour=0xff7700)

        await ctx.message.delete()
        await ctx.send(embed=embed)
        print(f"{consoletime} [INFO] User '{member.mention}' got warned by {ctx.author.mention} with the reason of '{reason}'.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        consoletime = datetime.datetime.now()
        await member.send(f"You were kicked from the server by {ctx.author.mention}.\n Reason: {reason}")
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.\n Reason: {reason}")
        print(f"{consoletime} [INFO] User '{member.mention}' got kicked by '{ctx.author.mention}' with the reason of '{reason}'.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        consoletime = datetime.datetime.now()
        await member.send(f"You were banned from the server by {ctx.author.mention}.\n [{reason}]")
        await member.ban(reason=reason)
        await ctx.message.delete()
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.\n Reason: {reason}")
        print(f"{consoletime} [INFO] User '{member.mention}' got banned by '{ctx.author.mention}' with the reason of '{reason}'.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit = None, member: discord.Member = None):
        consoletime = datetime.datetime.now()
        await ctx.message.delete()
        msg = []
        try:
            limit = int(limit)
        except:
            return await ctx.send("Please add a number!")
        if not member:
            await ctx.channel.purge(limit=limit)
            return await ctx.send(f"Purged {limit} messages", delete_after=5)
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == member:
                msg.append(m)
        await ctx.channel.delete_messages(msg)
        await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=5)
        print(f'{consoletime} [INFO] Purged {limit} messages on a channel or from a member.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def pas(self, ctx, *, arg):
        consoletime = datetime.datetime.now()
        embed = discord.Embed(colour = discord.Colour.darker_grey())
        
        embed.add_field(name='Public Address System', value=(f'{arg}'))

        await ctx.send(embed=embed)
        await ctx.message.delete()
        print(f"{consoletime} [INFO] PAS triggered! It's said: '{arg}'")


# Dedicated error handling for this commands

    @kick.error
    async def kick_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage is: `q!kick <User/ID> <Reason>`")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to do that!")
            print(f"{consoletime} [WARNING] Admin/mod command triggered but user didn't have enough permission to use it!")
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to kick a member. Check other roles that may be overriding the bot's own role permission.")
        
        raise error

    @ban.error
    async def ban_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage is: `q!ban <User/ID> <Reason>`")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to do that!")
            print(f"{consoletime} [WARNING] Admin/mod command triggered but user didn't have enough permission to use it!")
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to ban a member. Check other roles that may be overriding the bot's own role permission.")

        raise error

#    @purge.error
#    async def purge_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            await ctx.send("Usage is: `q!purge <amount>`")
#        if isinstance(error, commands.BadArgument):
#            await ctx.send("Not a number!")
#        if isinstance(error, commands.CommandInvokeError):
#            await ctx.send("Bot doesn't have permission to delete a message. Check other roles that may be overriding the bot's own role permission.")
#
#        raise error

def setup(bot):
    bot.add_cog(Mod(bot))