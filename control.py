import discord
from discord.ext import commands
import pydirectinput as con
from pydirectinput import KEYBOARD_MAPPING
from pynput.keyboard import Controller
from time import sleep as s
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bot = commands.Bot(command_prefix='/')
k = Controller()

print("Running...")

@bot.event
async def on_message(msg):
    if str(msg.channel) == 'pc-control':
        st = msg.content.lower()
        if st in KEYBOARD_MAPPING:
            con.keyDown(st)
            s(0.4)
            con.keyUp(st)
        else:
            if st == 'mup':
                con.move(0, -200)
            if st == 'mdown':
                con.move(0, 200)
            if st == 'mleft':
                con.move(-200, 0)
            if st == 'mright':
                con.move(200, 0)
            if st == 'm1':
                con.click(button = 'left')
            if st == 'm2':
                con.click(button = 'right')
            if st.startswith('say'):
                k.type(st[4:])
        await msg.delete()

bot.run(token)
