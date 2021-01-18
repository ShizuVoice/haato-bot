import discord
import datetime
import time
import os
import sys
import psutil

import asyncio
from discord.ext import commands

start_time = time.time()

TOKEN = open("./token.txt","r").read()
PREFIX = open("./prefix.txt","r").read()

ID = open ("./author.txt", "r").read()
ID_list = ID.split()
map_object = map(int, ID_list)
list_IDs = list(map_object)

bot = commands.Bot(command_prefix=PREFIX, owner_ids=list_IDs)
bot.remove_command('help')

@bot.event
async def on_ready():
    prefix = open('./prefix.txt','r').read()
    print(f'--------------------------')
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'--------------------------')
    print(f'Ensure that the bot has adequate permission to prevent errors while in use.')
    print(f'--------------------------')
    activity = discord.Game(name=f"{prefix}help | Early version", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

# Extension commands
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    consoletime = datetime.datetime.now()
    try:
        bot.load_extension(f'plugins.{extension}')
        embed = discord.Embed(colour = 0xdfe30b)
        embed.set_author(name='Haato Bot Notice')
        embed.add_field(name='Status', value='Bot loading an extension', inline=False)
        embed.add_field(name='Extension Name', value=f'{extension}.py', inline=False)
        embed.add_field(name='Result', value='Loaded successfully', inline=False)
        
        await ctx.send(embed=embed)
        print(f'{consoletime} [INFO] {extension} loaded')
    except Exception as e:
        embed = discord.Embed(colour = 0xd90b0b)
        embed.set_author(name='Haato Bot Notice')
        embed.add_field(name='Status', value='Bot loading an extension', inline=False)
        embed.add_field(name='Extension Name', value=f'{extension}.py', inline=False)
        embed.add_field(name='Result', value='Bot failed to load', inline=False)
        embed.set_footer(text="Check the extension's code or extension does not exist.")
        
        await ctx.send(embed=embed)
        print(f"{consoletime} [WARNING] Failed to load {extension}. Please check the extension's code or extension does not exist.")
        raise e

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    consoletime = datetime.datetime.now()
    try:
        bot.unload_extension(f'plugins.{extension}')
        embed = discord.Embed(colour = 0xdfe30b)
        embed.set_author(name='Haato Bot Notice')
        embed.add_field(name='Status', value='Bot unloading an extension', inline=False)
        embed.add_field(name='Extension Name', value=f'{extension}.py', inline=False)
        embed.add_field(name='Result', value='Unloaded successfully', inline=False)
        
        await ctx.send(embed=embed)
        print(f'{consoletime} [INFO] {extension} unloaded')
    except Exception as e:
        embed = discord.Embed(colour = 0xd90b0b)
        embed.set_author(name='Haato Bot Notice')
        embed.add_field(name='Status', value='Bot unloading an extension', inline=False)
        embed.add_field(name='Extension Name', value=f'{extension}.py', inline=False)
        embed.add_field(name='Result', value='Bot failed to unload', inline=False)
        embed.set_footer(text="Extension does not exist or it's been already unloaded.")
        
        await ctx.send(embed=embed)
        print(f"{consoletime} [WARNING] Failed to unload {extension}. Extension does not exist or it's been already unloaded.")
        raise e
    
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    consoletime = datetime.datetime.now()
    try:
        bot.unload_extension(f'plugins.{extension}')
        bot.load_extension(f'plugins.{extension}')
        embed = discord.Embed(colour = 0xdfe30b)
        embed.set_author(name='Haato Bot Notice')
        embed.add_field(name='Status', value='Bot reloading an extension', inline=False)
        embed.add_field(name='Extension Name', value=f'{extension}.py', inline=False)
        embed.add_field(name='Result', value='Reloaded successfully', inline=False)
        
        await ctx.send(embed=embed)
        print(f'{consoletime} [INFO] {extension} reloaded')
    except Exception as e:
        embed = discord.Embed(colour = 0xd90b0b)
        embed.set_author(name='Haato Bot Notice')
        embed.add_field(name='Status', value='Bot reloading an extension', inline=False)
        embed.add_field(name='Extension Name', value=f'{extension}.py', inline=False)
        embed.add_field(name='Result', value='Bot failed to reload', inline=False)
        embed.set_footer(text="Check the extension's code or you were trying to reloading an unloaded extension or non-existing extension.")
        
        await ctx.send(embed=embed)
        print(f"{consoletime} [WARNING] Failed to reload {extension}. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
        raise e

@bot.command()
@commands.is_owner()
async def loadall(ctx):
    for filename in os.listdir('./plugins'):
        consoletime = datetime.datetime.now()
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'plugins.{filename[:-3]}')
                await asyncio.sleep(3)
                await ctx.send(f"**{filename}** extensions loaded.")
                print(f'{consoletime} [INFO] {filename} loaded')
            except Exception as e:
                await ctx.send(f"Failed to reload **{filename}**. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
                print(f"{consoletime} [WARNING] Failed to load {filename}. Please check the extension's code or extension does not exist.")
                raise e

@bot.command()
@commands.is_owner()
async def unloadall(ctx):
    for filename in os.listdir('./plugins'):
        consoletime = datetime.datetime.now()
        if filename.endswith('.py'):
            bot.unload_extension(f'plugins.{filename[:-3]}')
            await asyncio.sleep(3)
            await ctx.send(f"**{filename}** unloaded")
            print(f'{consoletime} [INFO] {filename} extension unloaded.')

@bot.command()
@commands.is_owner()
async def shutdown(ctx, *, reason = None):
    consoletime = datetime.datetime.now()
    embed = discord.Embed(colour = discord.Colour.red())
    
    current_time = time.time()
    difference = int(round(current_time - start_time))
    utime = str(datetime.timedelta(seconds=difference))
    
    embed.set_author(name='Haato Bot Notice')
    embed.set_thumbnail(url='https://i.imgur.com/YyIPdSf.png')
    embed.add_field(name='Status', value='Bot is shutting down', inline=False)
    embed.add_field(name='Reason', value=f'{reason}', inline=False)
    embed.add_field(name='Uptime', value=f'{utime}', inline=False)
    embed.set_footer(text=f'All requests at this moment will be done and proceeds to shutdown.')
    await ctx.send(embed=embed)
    print(f'{consoletime} [WARNING] Bot is shutting down.')
    await asyncio.sleep(10)
    
    await ctx.bot.logout()
    print(f"Bot closed at {consoletime}")

for filename in os.listdir('./plugins'):
    consoletime = datetime.datetime.now()
    if filename.endswith('.py'):
        bot.load_extension(f'plugins.{filename[:-3]}')
        print(f'{consoletime} [INFO] {filename} loaded')

bot.run(TOKEN)