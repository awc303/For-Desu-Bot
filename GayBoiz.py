import discord
from discord.ext import commands
import praw
class GayBoiz:
    """My custom cog that does stuff!"""
    
    def __init__(self, bot):
        self.bot = bot

        
    @commands.command()
    async def mycom(self):
        """This does stuff!"""
        #Debug
        #Your code will go here
        await self.bot.say("Tyrus is gay!")

    @commands.command()
    async def gibdoggo(self, saveme : int=1):
        image=False
        while(image!=True):
        
            debug=False
            if(saveme!=1):
                debug=True
            if(debug):
                await self.bot.say("Start")
            reddit = praw.Reddit(client_id='DAsQaf9Ek2m3yA',
                client_secret='l6Vd3bpngUeTdCDAD1WQ9ia0olA',
                password='spooperz',
                user_agent='testscript',
                username='WoofWoofBork')
            sub=reddit.subreddit('doggos')
            posts=sub.random()
            if(posts.url.find("imgur")!=-1):
                image=True
            elif(posts.url.find("reddituploads")!=-1):
                image=True
            if(debug):
                await self.bot.say("looping")
        if(debug):
            await self.bot.say("You didnt fuck up")
        await self.bot.say(posts.url)

    @commands.command()
    async def rando(self, sreddit):
        reddit = praw.Reddit(client_id='DAsQaf9Ek2m3yA',
            client_secret='l6Vd3bpngUeTdCDAD1WQ9ia0olA',
            password='spooperz',
            user_agent='testscript',
            username='WoofWoofBork')
        sub=reddit.subreddit(sreddit)
        posts=sub.random()
        await self.bot.say(posts.url)

    @commands.command()
    async def lowqualitymeme(self):
        reddit = praw.Reddit(client_id='DAsQaf9Ek2m3yA',
            client_secret='l6Vd3bpngUeTdCDAD1WQ9ia0olA',
            password='spooperz',
            user_agent='testscript',
            username='WoofWoofBork')
        sub=reddit.subreddit("memes")
        posts=sub.random()
        await self.bot.say(posts.url)

    @commands.command()
    async def topdoggo(self, specific):
        reddit = praw.Reddit(client_id='DAsQaf9Ek2m3yA',
            client_secret='l6Vd3bpngUeTdCDAD1WQ9ia0olA',
            password='spooperz',
            user_agent='testscript',
            username='WoofWoofBork')
        sub=reddit.subreddit(specific)
        listgen=sub.top('hour').next()
        await self.bot.say(listgen.url)
        
def setup(bot):
    bot.add_cog(GayBoiz(bot))
