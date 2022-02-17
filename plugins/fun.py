import discord, datetime
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, *, draw):
        consoletime = datetime.datetime.now()
        responses = ["rock",
                    "paper",
                    "scissor"]

        responsebuffer = random.choice(responses)
        if draw == "rock" and responsebuffer == "paper":
            winmessage = "**Paper** wins!"
        elif draw == "rock" and responsebuffer == "scissor":
            winmessage = "**Rock** wins!"
        elif draw == "paper" and responsebuffer == "rock":
            winmessage = "**Paper** wins!"
        elif draw == "paper" and responsebuffer == "scissor":
            winmessage = "**Scissor** wins!"
        elif draw == "scissor" and responsebuffer == "rock":
            winmessage = "**Rock** wins!"
        elif draw == "scissor" and responsebuffer == "paper":
            winmessage = "**Scissor** wins!"
        elif draw == "rock" and responsebuffer == "rock":
            winmessage = "It's a draw!"
        elif draw == "paper" and responsebuffer == "paper":
            winmessage = "It's a draw!"
        elif draw == "scissor" and responsebuffer == "scissor":
            winmessage = "It's a draw!"
        else:
            winmessage = "Error, invalid value."

        await ctx.send(f"You choose **{draw}**. I choose **{responsebuffer}**. \n{winmessage}")
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
                    "Oo - sigurado.",
                    "Maaari kang umasa dito.",
                    "Sa nakikita ko, oo.",
                    "Maaaring totoo.",
                    "Oo.",
                    "Nakikita ko na oo.",
                    "Medyo malabo yung sagot, subukan mo ulit.",
                    "Magtanong ka mamaya.",
#                    "Mas mabuti na hindi sabihin sa iyo ngayon.",
                    "Sa nakikita ko, hindi.",
                    "Ang sagot ko hindi.",
                    "Hindi.",
                    "Medyo hindi maganda."]
#                    "Napaka duda."]

        responsebuffer = random.choice(responses)

        await ctx.send(f'{responsebuffer}')
        print(f"{consoletime} [INFO] Eightballfil triggered. Question: '{question}' Answer: '{responsebuffer}'")

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
    
    @commands.command()
    async def roll(self, ctx, value = 100):
        consoletime = datetime.datetime.now()
        if value == 100:
            rolls = random.randint(0, 100)
        else:
            offset = [10,
                      15,
                      20,
                      25,
                      40,
                      50]
                      
            offres = random.choice(offset)
                      
            trolls = random.randint(0, value)
            
            if (trolls % 2) == 0:
                finalvalue = value + offres
                rolls = random.randint(0, finalvalue)
            else:
                finalvalue = value - offres
                rolls = random.randint(0, finalvalue)
            
        print(f"{consoletime} [INFO] Roll triggered. {ctx.author} rolled {value} and it came out {rolls}")
        if rolls == 69:
            await ctx.send(f'{rolls} ||*nice*||')
        if rolls == 727:
            await ctx.send(f'{rolls} **WYSI**')
        else:
            await ctx.send(rolls)

    @commands.command()
    async def bonk(self, ctx, member: discord.Member, *, limit = None):
        consoletime = datetime.datetime.now()

        if member == ctx.author:
            await ctx.send("Why are you going to bonk yourself?")
        else:
            if not limit:
                await ctx.send(f"{member.mention}, you got bonked by {ctx.author.mention} for being too horny.")
                print(f"{consoletime} [INFO] Bonk triggered. {ctx.author} bonked {member}.")
            else:
                try:
                    limit = int(limit)
                    await ctx.send(f"{member.mention}, you got bonked by {ctx.author.mention} {limit} times for being too horny.")
                    print(f"{consoletime} [INFO] Bonk triggered. {ctx.author} bonked {member} {limit} times.")
                except:
                    await ctx.send("Sorry, I only read numbers.")

    @commands.command()
    async def loli(self, ctx):
        consoletime = datetime.datetime.now()
        response = ["Moshi moshi FBI desu.",
                    "Don't ever try it.",
                    "This man right here officer.",
                    f"Officer, this user {ctx.author.mention} is into lolis again.",
                    "Suspicious.",
                    "*stares*",
                    ":police_officer:",
                    ":oncoming_police_car:",
                    "FBI OPEN UP!!!",
                    "You are under arrest!",
                    "https://tenor.com/view/fbi-open-up-fbi-open-up-breaking-in-gif-15644236"]

        responsebuffer = random.choice(response)

        await ctx.send(f"{responsebuffer}")
        print(f"{consoletime} [INFO] Loli triggered by {ctx.author}")

    @bonk.error
    async def bonk_error(self, ctx, error):

        #Bot Prefix Read
        with open (f"./prefix.txt", "r") as botprefix:
            prefix = botprefix.read()

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Which user you are going to bonk? \n Usage: `{prefix}bonk @user <# of times (optional)>`")

        botprefix.close()


def setup(bot):
    bot.add_cog(Fun(bot))
