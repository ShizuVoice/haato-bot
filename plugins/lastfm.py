import discord
import sys
import requests
import json
import asyncio
import datetime as dt

from datetime import datetime
from discord.ext import commands

class lastfm(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lfmuser(self, ctx, *, arg):
        consoletime = dt.datetime.now()
        async with ctx.typing():
            try:
                with open (f"./plugins/apikey/lastfm.txt", "r") as apikey:
                    key = apikey.read()

                #Process
                URL = 'http://ws.audioscrobbler.com/2.0/'

                parameters = {
                    'method': 'user.getinfo',
                    'user': f'{arg}',
                    'api_key': f'{key}',
                    'format': 'json'
                }

                response = requests.get(URL, params=parameters)
                data = response.json()

                parameters2 = {
                    'method': 'user.getRecentTracks',
                    'user': f'{arg}',
                    'limit': '10',
                    'api_key': f'{key}',
                    'format': 'json'
                }

                response2 = requests.get(URL, params=parameters2)
                data2 = response2.json()

                #Variables
                username = (data['user']['name'])
                url = (data['user']['url'])
                country = (data['user']['country'])
                profile_pic = (data['user']['image'][3]['#text'])
                unixtime = int(data['user']['registered']['unixtime'])
                utctime = (datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S'))
                playcount = (data['user']['playcount'])

                #Recent Tracks
                track0artist = (data2['recenttracks']['track'][0]['artist']['#text'])
                track0title = (data2['recenttracks']['track'][0]['name'])
                track1artist = (data2['recenttracks']['track'][1]['artist']['#text'])
                track1title = (data2['recenttracks']['track'][1]['name'])
                track2artist = (data2['recenttracks']['track'][2]['artist']['#text'])
                track2title = (data2['recenttracks']['track'][2]['name'])
                track3artist = (data2['recenttracks']['track'][3]['artist']['#text'])
                track3title = (data2['recenttracks']['track'][3]['name'])
                track4artist = (data2['recenttracks']['track'][4]['artist']['#text'])
                track4title = (data2['recenttracks']['track'][4]['name'])
                track5artist = (data2['recenttracks']['track'][5]['artist']['#text'])
                track5title = (data2['recenttracks']['track'][5]['name'])
                track6artist = (data2['recenttracks']['track'][6]['artist']['#text'])
                track6title = (data2['recenttracks']['track'][6]['name'])
                track7artist = (data2['recenttracks']['track'][7]['artist']['#text'])
                track7title = (data2['recenttracks']['track'][7]['name'])
                track8artist = (data2['recenttracks']['track'][8]['artist']['#text'])
                track8title = (data2['recenttracks']['track'][8]['name'])
                track9artist = (data2['recenttracks']['track'][9]['artist']['#text'])
                track9title = (data2['recenttracks']['track'][9]['name'])

                embed = discord.Embed(title=f"Last.fm - {username}", colour=0xba0000, url=url)
                embed.set_thumbnail(url=profile_pic)
                embed.add_field(name='Username', value=f'{username}', inline=True)
                embed.add_field(name='Country', value=f'{country}',inline=True)
                embed.add_field(name='Total Scrobbles', value=f'{playcount}', inline=True)
                embed.add_field(name='Created at', value=f'{utctime} UTC \n', inline=True)
                try:
                    now_playing = (data2['recenttracks']['track'][0]['@attr']['nowplaying'])
                    if "true" in now_playing:
                        embed.add_field(name='Now Playing', value=f'{track0artist} - {track0title}', inline=False)
                except:
                    pass

                embed.add_field(name='Recent Tracks', value=f'{track0artist} - {track0title} \n {track1artist} - {track1title} \n {track2artist} - {track2title} \n {track3artist} - {track3title} \n {track4artist} - {track4title} \n {track5artist} - {track5title} \n {track6artist} - {track6title} \n {track7artist} - {track7title} \n {track8artist} - {track8title} \n {track9artist} - {track9title}', inline=False)
        
            except Exception as e:
                await ctx.send('Error! - User not found')
                apikey.close()
                raise e

        await ctx.send(embed = embed)
        print(f"{consoletime} [INFO] lfmuser triggered. User {ctx.author} requested an info for last.fm user {arg}")
        apikey.close()

    @commands.command()
    async def lfmnp(self, ctx, *, arg):
        consoletime = dt.datetime.now()
        with open (f"./plugins/apikey/lastfm.txt", "r") as apikey:
            key = apikey.read()

        URL = 'http://ws.audioscrobbler.com/2.0/'

        #Process 1 (Fetch basic user info)
        parameters1 = {
            'method': 'user.getinfo',
            'user': f'{arg}',
            'api_key': f'{key}',
            'format': 'json'
        }

        response1 = requests.get(URL, params=parameters1)
        data1 = response1.json()
        data1if = json.dumps(data1)

        if "user" in data1if:
        #try:
            async with ctx.typing():
                #Process 2 (Fetch currently playing track)
                parameters2 = {
                    'method': 'user.getRecentTracks',
                    'user': f'{arg}',
                    'limit': '5',
                    'api_key': f'{key}',
                    'format': 'json'
                }

                response2 = requests.get(URL, params=parameters2)
                data2 = response2.json()

                #Variables
                user = (data2['recenttracks']['@attr']['user'])
                title = (data2['recenttracks']['track'][0]['name'])
                artist = (data2['recenttracks']['track'][0]['artist']['#text'])
                album = (data2['recenttracks']['track'][0]['album']['#text'])
                art = (data2['recenttracks']['track'][0]['image'][3]['#text'])
                titleurl = (data2['recenttracks']['track'][0]['url'])
                artisturl = artist.replace(" ", "%20")
                playcount = (data2['recenttracks']['@attr']['total'])
                profile_pic = (data1['user']['image'][0]['#text'])

                #Process 3 (Fetch total scrobble for current playing track)
                parameters3 = {
                    'method': 'track.getInfo',
                    'artist': f'{artist}',
                    'track': f'{title}',
                    'user': f'{arg}',
                    'api_key': f'{key}',
                    'format': 'json'
                }

                response3 = requests.get(URL, params=parameters3)
                data3 = response3.json()


                try:
                    now_playing = (data2['recenttracks']['track'][0]['@attr']['nowplaying'])
                    if "true" in now_playing:
                        scrobbletrack = (data3['track']['userplaycount'])
                        if not scrobbletrack:
                            scrobbletrack = 0

                except Exception as e:
                    await ctx.send(f'{user} is not playing anything at this moment.')
                    apikey.close()
                    raise e
            
            embed = discord.Embed(title=f'Last.fm - {user} is Now Playing', colour=0xba0000, url=f'https://www.last.fm/user/{user}')
            embed.set_image(url=art)
            embed.add_field(name=f'{album}', value=f'[{artist}](https://www.last.fm/music/{artisturl}) - [{title}]({titleurl})', inline=False)
            embed.set_footer(text=f"{user}'s scrobble data \n{scrobbletrack} time(s) for this track. {playcount} time(s) in total.", icon_url=profile_pic)

            await ctx.send(embed = embed)
            print(f"{consoletime} [INFO] lfmnp triggered. User {ctx.author} requested an activity for last.fm user {arg}")
            apikey.close()

        else:
        #except Exception as f:
            await ctx.send('Error! - User not found')
            apikey.close()
            #raise f

def setup(bot):
    bot.add_cog(lastfm(bot))