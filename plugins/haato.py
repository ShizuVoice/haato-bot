import discord, datetime
import asyncio
import random
from discord.ext import commands

class Haato(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test failed successfully!")

    @commands.command()
    async def cooking(self, ctx):
        response = ['https://www.youtube.com/watch?v=h2CfS9akvVo',
                    'https://www.youtube.com/watch?v=xBqWAQodhFg',
                    'https://www.youtube.com/watch?v=iGUzLFFKf7w',
                    'https://www.youtube.com/watch?v=HQvX9ClXsWE',
                    'https://www.youtube.com/watch?v=0y6vH-AZKMk',
                    'https://www.youtube.com/watch?v=S9OLBMG0-nY',
                    'https://www.youtube.com/watch?v=NRKsqut_FUw',
                    'https://www.youtube.com/watch?v=9zJMVHULJ0c',
                    'https://www.youtube.com/watch?v=rAEjfEd8uSk',
                    'https://www.youtube.com/watch?v=XTlDdGA5cO8',
                    'https://www.youtube.com/watch?v=cGxKncDHY_U',
                    'https://www.youtube.com/watch?v=kPBZOjh-tP4',
                    'https://www.youtube.com/watch?v=R9dLe4vOfz8',
                    'https://www.youtube.com/watch?v=D1t0NsYy4mI',
                    'https://www.youtube.com/watch?v=FAQQUMcRj_Q',
                    'https://www.youtube.com/watch?v=B5KoNaDvfmc',
                    'https://www.youtube.com/watch?v=A_DQiVAJrrc',
                    'https://www.youtube.com/watch?v=TlAi_TVzO9E',
                    'https://www.youtube.com/watch?v=IT186xDTwUU',
                    'https://www.youtube.com/watch?v=cC7y0ENWZoQ']
        await ctx.send(f'{random.choice(response)}')

    @commands.command()
    async def eat(self, ctx):
        response = ['https://tenor.com/view/haachama-akai-haato-sandwich-eating-chewing-gif-21697787',
                    'https://tenor.com/view/akai-haato-haachama-hololive-eating-2manysnacks-gif-21843490',
                    'https://pbs.twimg.com/media/Er1zgQ_UcAMahwj?format=jpg&name=large',
                    'https://i.redd.it/lkwjm5v7wha61.png']
        await ctx.send('Command is still in beta, but here you go.', delete_after=2)
        await asyncio.sleep(2)
        await ctx.send(f'{random.choice(response)}')

def setup(bot):
    bot.add_cog(Haato(bot))