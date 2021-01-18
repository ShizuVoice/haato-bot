import discord
import datetime
import sys
import requests
import json
import random

from discord.ext import commands

class Yandere(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def yandere(self, ctx, *, tag):
        consoletime = datetime.datetime.now()
        try:
            #yande.re API process
            tags = tag
            include_tag = 1
            limit = 50

            URL = 'https://yande.re/post.json'

            parameters = {
                'rating': 's',
                'api_version': '2',
                'tags': f'{tags}',
                'include_tags': int(include_tag),
                'limit': int(limit)
            }
        
            response = requests.get(URL, params=parameters)

            data = response.json()

            choice = random.randint(0, limit)

            embed_pic_url = (data['posts'][choice]['file_url'])
            embed_source_url = (data['posts'][choice]['source'])
            embed_rating = (data['posts'][choice]['rating'])
            
            #footer responses
            footer_responses = ["Some source links from Pixiv does not work because of the link directing to the file rather the post. This is a problem from the Pixiv's API rather than the bot. Don't blame me for that.",
                                "Using this command may fetch some questionable (q) or explicit content (e) from yandere. Be careful while using this command.",
                                "Search tags may not be accurate as it can search other pictures with the same tag.",
                                "Test failed successfully.",
                                "There are some instances where the picture embed doesn't show up."]
            
            footer_responses_buffer = random.choice(footer_responses)

            embed = discord.Embed(title='Yande.re',colour = 0xd66d6d)
            embed.set_image(url=embed_pic_url)
            embed.add_field(name='Source', value=embed_source_url, inline=False)
            embed.add_field(name='Rating', value=embed_rating, inline=False)
            embed.set_footer(text=footer_responses_buffer)
        
            print(f"{consoletime} [INFO] Yandere triggered. Tag: {tag} Image link: {embed_pic_url}")
            await ctx.send(embed=embed)
           
        except Exception:
            await ctx.send('No results!')
            print(f"{consoletime} [WARNING] Yandere triggered. Request returned none!")
            pass

    @yandere.error
    async def yandere_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('Chill down!', delete_after=5)

def setup(bot):
    bot.add_cog(Yandere(bot))