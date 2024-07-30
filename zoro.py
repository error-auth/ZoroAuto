# telethon : @corpsealone
import asyncio
from telethon import TelegramClient, events
import random
from telethon.errors import MessageIdInvalidError

api_id = 4608923
api_hash = '0fc54e6096c9cd77cd1e1954b899676d'

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    print('''
          Zoro Bot Fishing Auto  
          On it!!
                                 ~ paradox  ''') 
   


    @client.on(events.NewMessage(from_users=5284997893))
    async def _(event):
        if "Are you ready?" in event.raw_text:
            try:
                await asyncio.sleep(1.2)
                await event.click(0)  # click the first button
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
        
    @client.on(events.MessageEdited(from_users=5284997893))
    async def _(event):
        if "You caught" in event.raw_text:
            try:
                await asyncio.sleep(1.5)
                await client.send_message(5284997893, '/fish')  # send /fish message
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.NewMessage(from_users=5284997893))
    async def _(event):
        if "Your rod is broken!" in event.raw_text:
            try:
                print('Rod is broken, waiting to regenerate \n ....')
                await asyncio.sleep(180)  # Wait for 60 seconds
                print('\n Rod has regenerated, preparing to fish again')
                await client.send_message(5284997893, '/fish')  # send /fish message
                print('\n Sent /fish message')
            except Exception as e:
                print(f'An error occurred: {e}')

    @client.on(events.NewMessage(from_users=6810396528))
    async def _(event):
        if "paradox" in event.raw_text:
            try:
                await asyncio.sleep(1.0)
                await client.send_message(6810396528, 'Zoro Bot Fishing Auto is working !') 
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

#   await send_fish_message()
    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())