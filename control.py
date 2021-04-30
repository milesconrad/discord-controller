import discord
from discord.ext import commands
import pydirectinput as control
from pydirectinput import KEYBOARD_MAPPING as KEYS
from pynput.keyboard import Controller
from time import sleep
token = 'xxxxxxxxxxxxxxxxxxxxxxxx'
bot = commands.Bot(command_prefix='/')
keyboard = Controller()

print("Running...")

@bot.event
async def on_message(msg):
    if str(msg.channel) == 'pc-control':
        content = msg.content.lower()

        #checks if selected key is a key object
        if content in KEYS:
            control.keyDown(content)
            sleep(0.4)
            control.keyUp(content)
        
        #if selected key is not a key object, check if the key is a mouse movement
        else:
            if content == 'mup':
                control.move(0, -200)
            if content == 'mdown':
                control.move(0, 200)
            if content == 'mleft':
                control.move(-200, 0)
            if content == 'mright':
                control.move(200, 0)
            if content == 'm1':
                control.click(button = 'left')
            if content == 'm2':
                control.click(button = 'right')
            if content.startswith('say'):
                keyboard.type(content[4:])
                
        await msg.delete()

bot.run(token)
