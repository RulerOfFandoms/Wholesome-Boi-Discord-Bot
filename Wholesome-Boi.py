from discord.ext import commands
TOKEN = "OTY2MzMzMzU5MzQ3MzU5Nzk0.YmAOEg.XBS1kXxbrJzWmPDhUfi8UqSqYNQ"
from ListsForWholesomeBoi import Quotes  #import the quote list
from ListsForWholesomeBoi import Gay  #import the gay list
from ListsForWholesomeBoi import Affirmation  #import the affirmations
from ListsForWholesomeBoi import BuzzBuzz  #import the bees


bot = commands.Bot(command_prefix = "<")  #prefix


@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in')  #show it's logged in



@bot.event
async def on_message(message):
    global respond
    if message.content == "<g": #gay command (sends wholesome gay stuff)
        Gay()
        respond = Gay()
        await message.channel.send(respond)
    elif message.content == "<q":  #quote command (sends quote)
        Quotes()
        respond = Quotes()
        await message.channel.send(respond)
    elif message.content == "<a":  #affirmation command (sends affirmation)
        Affirmation()
        respond = Affirmation()
        await message.channel.send(respond)
    elif message.content == "<buzz":  #posts pictures of bees
        BuzzBuzz()
        respond = BuzzBuzz()
        await message.channel.send(respond)
    elif message.content == "bee":
        await message.channel.send("Yes, Oliver likes bees lol")  #Tells us I like bees
    elif message.content == "bees":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "beez":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "BEE":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "BEEZ":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "BEES":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "Bee":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "Beez":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "Bees":
        await message.channel.send("Yes, Oliver likes bees lol")
    elif message.content == "<bonk":
        await message.channel.send("https://www.youtube.com/watch?v=IqJcXmnBIvI")
    elif message.content == "< 3":
        await message.channel.send('''
I love you and nothing will ever change that. You may not see your worth but I sure do and you are 
worthy of everything you have and everything that is coming for you. I am so proud of you and no 
matter how much you think you screw up, I will always be proud of you. You worth isn't determined by 
what you accomplish but where your heart lies.
❤🧡💛💚💙💜🖤🤍🤎''')
    elif message.content == "<sad":
        await message.channel.send("https://i.pinimg.com/236x/44/b8/3c/44b83c691eff2e0f31ef5e5a80088dd6.jpg")


bot.run(TOKEN)