import discord
import datetime
import sys
import requests
import json
import random
import asyncio

from discord.ext import commands

class Yandere(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def yandere(self, ctx, tag, post = '-1'):
        consoletime = datetime.datetime.now()
        try:
            async with ctx.typing():
                #yande.re API process
                tags = tag
                include_tag = 1
                limit = 100
                number = int(post)

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

                if "-1" in post:
                    embed_pic_url = (data['posts'][choice]['file_url'])
                    source_link = (data['posts'][choice]['source'])
                    rating = (data['posts'][choice]['rating'])
                    footer_roll = choice
                    if not source_link:
                        embed_source_text = "No Post Source"
                        embed_source_url = "None"
                    else:
                        embed_source_text = "Post"
                        embed_source_url = (data['posts'][choice]['source'])
                else:
                    embed_pic_url = (data['posts'][number]['file_url'])
                    source_link = (data['posts'][number]['source'])
                    rating = (data['posts'][number]['rating'])
                    footer_roll = number
                    if not source_link:
                        embed_source_text = "No Post Source"
                        embed_source_url = "None"
                    else:
                        embed_source_text = "Post"
                        embed_source_url = (data['posts'][number]['source'])

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
                                    "Using this command may fetch some questionable or explicit content from yandere. Be careful while using this command.",
                                    "Search tags may not be accurate as it can search other pictures with the same tag.",
                                    "Test failed successfully.",
                                    "There are some instances where the picture embed doesn't show up.",
                                    "The command `moebooru` and `danbooru` almost share the same code and API with `yandere`."]

                footer_responses_buffer = random.choice(footer_responses)

                embed = discord.Embed(title='Yande.re',colour = 0xd66d6d)
                embed.set_image(url=embed_pic_url)
                embed.add_field(name='Source', value=f'[{embed_source_text}]({embed_source_url}) | [Direct Link]({embed_pic_url})', inline=False)
                embed.add_field(name='Rating', value=embed_rating, inline=False)
                embed.set_footer(text=f"{footer_responses_buffer} \n--- \nImage roll: {footer_roll} \nTags: {tags}")

                print('--------------------------------')
                print(f"{consoletime} [INFO] Yandere triggered. \nTag: {tag} \nRandom number roll: {choice} \nUser roll: {number} \nImage link: {embed_pic_url} \nSource link: {embed_source_url}")
                await ctx.send(embed=embed)
           
        except Exception as e:
            await ctx.send('No results!')
            print(f"{consoletime} [WARNING] Yandere triggered. Request returned none!")
            raise e

    @yandere.error
    async def yandere_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('Chill down!', delete_after=5)

def setup(bot):
    bot.add_cog(Yandere(bot))