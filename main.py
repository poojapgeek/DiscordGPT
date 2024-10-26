import discord
import os
import google.generativeai as genai

genai.configure(api_key=os.environ['Gemini_API'])

token = os.environ['Secrer_key']


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if self.user != message.author:
            if self.user in message.mentions:

                channel = message.channel
                model = genai.GenerativeModel("gemini-1.5-flash")

                user = message.content
                response = model.generate_content(user)

                #messageTosend=response.choices[0].text
                await channel.send(response.text)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
#publickey:829b2bd8a16058b39c634847cd2d4a21ef952c591fca1d3ace0d13df91e72791
#appid:1298589165830799412
