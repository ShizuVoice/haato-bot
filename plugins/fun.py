import discord, datetime
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, *, draw):
        consoletime = datetime.datetime.now()
        responses = ["rock!",
                    "paper!",
                    "scissor!"]

        responsebuffer = random.choice(responses)

        await ctx.send("It's a " + f'{responsebuffer}')
        print(f"{consoletime} [INFO] RPS triggered. '{ctx.author}' drawed {draw}. Bot drawed {responsebuffer}")

    @commands.command()
    async def eightball(self, ctx, *, question):
        consoletime = datetime.datetime.now()
        responses = ["It is certain.",
                    "It is decidedly so.",
 #                   "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
#                    "Better not tell you now.",
#                    "Cannot predict now.",
#                    "Concentrate and ask again.",
#                    "Don't count on it.",
                    "My reply is no.",
                    "No",
                    "My sources say no.",
                    "Outlook not so good."]
#                    "Very doubtful."]

        responsebuffer = random.choice(responses)

        await ctx.send(f'{responsebuffer}')
        print(f"{consoletime} [INFO] Eightball triggered. Question: '{question}' Answer: '{responsebuffer}'")

    @commands.command()
    async def eightballfil(self, ctx, *, question):
        consoletime = datetime.datetime.now()
        responses = ["Panigurado.",
#                    "Napagpasyahan ito.",
#                    "Walang duda.",
                    "Oo - sigurado.",
                    "Maaari kang umasa dito.",
                    "Sa nakikita ko, oo.",
                    "Maaaring totoo.",
                    "Oo.",
                    "Nakikita ko na oo.",
                    "Medyo malabo yung sagot, subukan mo ulit.",
                    "Magtanong ka mamaya.",
#                    "Mas mabuti na hindi sabihin sa iyo ngayon.",
#                    "Hindi mahuhulaan ngayon.",
#                    "Pagtuon at magtanong muli.",
                    "Sa nakikita ko, hindi.",
                    "Ang sagot ko hindi.",
                    "Hindi.",
                    "Medyo hindi maganda."]
#                    "Napaka duda."]

        responsebuffer = random.choice(responses)

        await ctx.send(f'{responsebuffer}')
        print(f"{consoletime} [INFO] Eightballfil triggered. Question: '{question}' Answer: '{responsebuffer}'")

    @commands.command()
    async def cooking(self, ctx):
        responses = ['https://www.youtube.com/watch?v=h2CfS9akvVo',
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
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def choose(self, ctx, choice1: commands.clean_content, choice2: commands.clean_content):
        consoletime = datetime.datetime.now()
        choice = [f'{choice1}',
                f'{choice2}']
            
        choicebuffer = random.choice(choice)
        
        response = [f'I would choose **{choicebuffer}**.',
                    f'**{choicebuffer}** would be my best bet.',
                    f'If I were you, I will choose **{choicebuffer}**.',
                    f'**{choicebuffer}**, no more question.',
                    f'**{choicebuffer}** is much better.']
        
        responsebuffer = random.choice(response)
            
        print(f"{consoletime} [INFO] Choose triggered. {ctx.author} questioned: '{choice1} or {choice2}' Answer: '{choicebuffer}'")
        await ctx.send(f'{responsebuffer}')
        
def setup(bot):
    bot.add_cog(Fun(bot))
