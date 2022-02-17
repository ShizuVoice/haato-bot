# Important Note
# This cog may use more than one API which can vary from each other and it's
# recommended to read the documentation.
#
# So far, these are the APIs that is been using:
# osu API v1
# osutrack (Soon)

import discord
import datetime
import sys
import requests
import json

from discord.ext import commands
from discord import Embed

class osu(commands.Cog):

    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    async def osu(self, ctx, user, mode = 0):
        try:
            #osu API process
            username = user
            game_mode = mode

            #API Key Read
            with open (f"./plugins/apikey/osu.txt", "r") as apikey:
                key = apikey.read()

            URL = 'https://osu.ppy.sh/api/get_user'

            parameters = {
                'k': f'{key}',
                'u': f'{username}',
                'm': f'{game_mode}'
            }

            response = requests.get(URL, params=parameters)
            data = response.json()

            osu_username = data[0]['username']
            raw_osu_pp = data[0]['pp_raw']
            osu_pp = float(raw_osu_pp)
            raw_osu_acc = data[0]['accuracy']
            osu_acc = float(raw_osu_acc)

            await ctx.send(f"**In Progress** \nUsername: {osu_username} \nPerformance Points: {round(osu_pp)} \nAccuracy: {round(osu_acc, 2)}")

            apikey.close()

        except Exception as e:
            await ctx.send('Error!')
            raise e

    @commands.command()
    async def best(self, ctx, user, mode = 0, pick = 1, limit = 10):
        try:
            #osu API process
            username = user
            game_mode = mode

            #API Key Read
            with open (f"./plugins/osu/api_key.txt", "r") as apikey:
                key = apikey.read()

            URL1 = 'https://osu.ppy.sh/api/get_user_best'

            parameters1 = {
                'k': f'{key}',
                'u': f'{username}',
                'limit': f'{limit}'
            }

            response1 = requests.get(URL1, params=parameters1)
            data1 = response1.json()

            beatmapid = data1[pick-1]['beatmap_id']
            score = data1[pick-1]['score']
            pp = data1[pick-1]['pp']
            rank = data1[pick-1]['rank']

            URL2 = 'https://osu.ppy.sh/api/get_beatmaps'

            parameters2 = {
                'k': f'{key}',
                'b': f'{beatmapid}',
                'm': f'{game_mode}'
            }

            response2 = requests.get(URL2, params=parameters2)
            data2 = response2.json()
            
            title = data2[0]['title']
            beatmapset_id = data2[0]['beatmapset_id']


            await ctx.send(f"**In Progress** \nTop play for {username} \n [{title}](<https://osu.ppy.sh/beatmapsets/{beatmapset_id}#osu/{beatmapid}>) \nScore: {score} \nPerformance Points: {pp} \nScore Rank: {rank}")

            apikey.close()

        except Exception as e:
            await ctx.send('Error!')
            raise e

    @commands.command()
    async def recent(self, ctx, user, mode = 0):
        try:
            #osu API process
            username = user
            game_mode = mode

            #API Key Read
            with open (f"./plugins/osu/api_key.txt", "r") as apikey:
                key = apikey.read()

            URL = 'https://osu.ppy.sh/api/get_user_recent'

            parameters = {
                'k': f'{key}',
                'u': f'{username}',
                'm': f'{game_mode}'
            }

            response = requests.get(URL, params=parameters)
            data = response.json()

            #JSON List
            beatmap_id = data[0]['beatmap_id']
            score = data[0]['score']
            maxcombo = data[0]['maxcombo']
            count50 = data[0]['count50']
            count100 = data[0]['count100']
            count300 = data[0]['count300']
            countmiss = data[0]['countmiss']
            countkatu = data[0]['countkatu']
            countgeki = data[0]['countgeki']
            perfect = int(data[0]['perfect'])
            enabled_mods = data[0]['enabled_mods']
            user_id = data[0]['user_id']
            date = data[0]['date']
            rank = data[0]['rank']

            await ctx.send(f"**In progress** \nBeatmap: https://osu.ppy.sh/b/{beatmap_id} \nScore: {score} \nPerfect?: {(perfect > 0)}")

        except Exception as e:
            await ctx.send('Error!')
            raise e


    @osu.error
    async def osu_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please enter a username!')


def setup(bot):
    bot.add_cog(osu(bot))