import os
import discord
from wazirx_sapi_client.rest import Client
import asyncio
from db import data_entry
from db import dat_query
from db import create_table


wazir = Client()
T = {'adausdt':'3.5','enjusdt':'4.69','manausdt':'6.0'}


def wazirT(crypto):
  data = wazir.send("ticker",
             {"symbol": crypto})
  datadic = data[1]
  return datadic['lastPrice']
  
z = wazirT("btcinr")
print(z)
async def sendMessage(message):
    await discord.utils.get(discordclient.get_all_channels(),
                            name='general').send(message)

async def detectforalert():
  try:  
    for crypto in T:
          create_table()
          l_p = float(wazirT(crypto))
          t_p = float(T[crypto]) 
          if l_p > t_p : 
            await sendMessage(
            f'!!!!Hey {crypto}  passed {t_p} USD. The current price is: {l_p} USD.!!!!')
            data_entry(crypto,l_p)
            print(dat_query())
          else:
            print(dat_query())
            await sendMessage(
            f'The price of {crypto} has not passed {t_p} USD. The current price is: {l_p} USD.')
               
  except Exception as e:
    print("an exception occurred - {}".format(e)) 
  await asyncio.sleep(1000)
    # https://tutorials.botsfloor.com/a-discord-bot-with-asyncio-359a2c99e256  that runs detectPriceAlert every 5 seconds
 # Timer(500, await detectforalert()).start()
 #print("--Finished--")          


discordclient = discord.Client()
@discordclient.event
async def on_ready():
    print(f'You have logged in as {discordclient}')
    channel = discord.utils.get(discordclient.get_all_channels(), name='general')

    await discordclient.get_channel(channel.id).send('bot is now online!')
    

# called whether there is a message in the chat
@discordclient.event
async def on_message(message):
    if message.author == discordclient.user:
        return
    if message.content.startswith('$start'):
        await message.channel.send(
            "starting detecting price alert")
        while True:
            await detectforalert()

             # second        
      
my_secret = os.environ['Token']
discordclient.run(my_secret)

