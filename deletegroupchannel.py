import pyfiglet
import webbrowser
import colorama
from tqdm import tqdm
from time import sleep
from colorama import Back, Style, Fore
from telethon.sync import TelegramClient
from telethon.tl.types import Channel, Chat
from telethon.tl.functions.channels import LeaveChannelRequest
print(Fore.GREEN + pyfiglet.figlet_format(" Alpha Cyber ", font="hollywood"))

data_loader = list(range(1000))

for i, j in enumerate(tqdm(data_loader)):
    sleep(0.01)	
    

print(Fore.CYAN+ " ♤ Nothing hack just i help you for exit your all groups and chanel telegram ♤")

webbrowser.open("https://www.instagram.com/yassindeveloper?igsh=ZzFjNXlnMTVxcG5p")

api_id = int(input(Fore.GREEN + " Enter your api_id: "))
api_hash = input("Enter your api_hash: ")
phone = input("Enter your phone number with country code (e.g., +9647830528876): ")

client = TelegramClient('session_name', api_id, api_hash)

async def leave_all():
    await client.connect()
    
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input("Enter the code you received: ")
        await client.sign_in(phone, code)

    print("Fetching dialogs...")

    async for dialog in client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):  
            try:
                print(f"Leaving channel/group: {dialog.name}")
                await client(LeaveChannelRequest(entity))
            except Exception as e:
                print(f"Error while leaving {dialog.name}: {e}")
        elif isinstance(entity, Chat):  
            try:
                print(f"Leaving group: {dialog.name}")
                await client.delete_dialog(dialog.id)
            except Exception as e:
                print(f"Error while leaving {dialog.name}: {e}")

    await client.disconnect()
    print("Finished leaving all channels and groups.")

import asyncio
asyncio.run(leave_all())
