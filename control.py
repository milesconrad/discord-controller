import discord
from discord.ext import commands

import pydirectinput as control
from pydirectinput import KEYBOARD_MAPPING as KEYS

from pynput.keyboard import Controller
from time import sleep

bot = commands.Bot(command_prefix='/')
keyboard = Controller()

print("Running...")

@bot.event
async def on_message(message):
    if str(message.channel) == 'pc-control':
        message.content = message.content.lower()

        if message.content in KEYS:
            control.keyDown(message.content)
            sleep(0.4)
            control.keyUp(message.content)
        
        else:
            if message.content == 'mup':
                control.move(0, -200)
            if message.content == 'mdown':
                control.move(0, 200)
            if message.content == 'mleft':
                control.move(-200, 0)
            if message.content == 'mright':
                control.move(200, 0)
            if message.content == 'm1':
                control.click(button = 'left')
            if message.content == 'm2':
                control.click(button = 'right')
            if message.content.startswith('say'):
                keyboard.type(message.content[4:])
                
        await message.delete()

bot.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
