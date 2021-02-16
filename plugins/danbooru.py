import discord
import datetime
import sys
import requests
import json
import random
import asyncio

from discord.ext import commands

class Danbooru(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def danbooru(self, ctx, *, tag):
        consoletime = datetime.datetime.now()
        try:
            #danbooru API process
            tags = tag
            limit = 100

            URL = 'https://danbooru.donmai.us/posts.json'

            parameters = {
                'tags': f'{tags}',
                'limit': int(limit)
            }

            response = requests.get(URL, params=parameters)

            data = response.json()

            choice = random.randint(0, limit)

            embed_pic_url = (data[choice]['file_url'])
            source_link = (data[choice]['source'])
            rating = (data[choice]['rating'])

            if not source_link:
                embed_source_url = "None"
            else:
                embed_source_url = (data[choice]['source'])

            if "s" in rating:
                embed_rating = "Safe"
            elif "q" in rating:
                embed_rating = "Questionable"
            elif "e" in rating:
                embed_rating = "Explicit"
            else:
                embed_rating = "Unknown"

            #footer responses
            footer_responses = ["Some source links from Pixiv does not work because of the link directing to the file rather the post. This is a problem from the Pixiv's API, not the bot. Don't blame me for that.",
                                "Using this command may fetch some questionable or explicit content from danbooru. Be careful while using this command.",
                                "Search tags may not be accurate as it can search other pictures with the same tag.",
                                "Test failed successfully.",
                                "There are some instances where the picture embed doesn't show up.",
                                "The command `yandere` and `moebooru` almost share the same code and API with `danbooru`."]
            
            footer_responses_buffer = random.choice(footer_responses)

            embed = discord.Embed(title='Danbooru',colour = 0x098ae6)
            embed.set_image(url=embed_pic_url)
            embed.add_field(name='Source', value=f'[Link]({embed_source_url})', inline=False)
            embed.add_field(name='Rating', value=embed_rating, inline=False)
            embed.set_footer(text=footer_responses_buffer)
        
            print('--------------------------------')
            print(f"{consoletime} [INFO] Danbooru triggered. \nTag: {tag} \nImage link: {embed_pic_url} \nSource link: {embed_source_url}")
            await ctx.send(embed=embed)
           
        except Exception as e:
            await ctx.send('No results!')
            print(f"{consoletime} [WARNING] Danbooru triggered. Request returned none!")
            raise e

    @danbooru.error
    async def danbooru_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('Chill down!', delete_after=5)

def setup(bot):
    bot.add_cog(Danbooru(bot))