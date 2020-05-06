from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if "Glad" in message.content.lower():
            print(message.channel.id)
            if message.channel.id == 586645529778454530:
                await message.channel.send("TEST")
 

def setup(bot):
    bot.add_cog(BoostPlugin(bot))