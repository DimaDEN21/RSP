import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
list=[":rock:", ":roll_of_paper:", ":scissors:"]
#reply (нужен для ответа пользователю на сообщение)
#await ctx.send("пон")



@bot.event


async def on_message(message):
    if message.content.startswith("Rules"):
        print("I","You can use :rock: :roll_of_paper: :scissors:","\nTipe one of this emoji")

        await message.channel.send("You can use :rock: :roll_of_paper: :scissors:")
        await message.channel.send("Copy one of this emoji or write    \n:/rock:     :/roll_of_paper:     :/scissors:    (but without /)")



    elif message.content.startswith("🪨"):
        randuns = random.choice(list)
        print("I",randuns,"Player :rock:")
        await message.channel.send(randuns)

        if randuns == ":scissors:":
            await message.channel.send("You Win")
            print("I","You Win")

        elif randuns == ":roll_of_paper:":
            await message.channel.send("I Win")
            print("I","I Win")

        elif randuns == ":rock:":
            await message.channel.send("A Draw")
            print("I","A Draw")


    elif message.content.startswith("🧻"):
        randuns = random.choice(list)
        print("I", randuns, "Player :roll_of_paper:")
        await message.channel.send(randuns)

        if randuns == ":scissors:":
            await message.channel.send("I Win")
            print("I","I Win")

        elif randuns == ":roll_of_paper:":
            await message.channel.send("A Draw")
            print("I","A Draw")

        elif randuns == ":rock:":
            await message.channel.send("You Win")
            print("I","You Win")




    elif message.content.startswith("✂"):
        randuns = random.choice(list)
        print("I", randuns, "Player :scissors:")
        await message.channel.send(randuns)

        if randuns==":scissors:":
            await message.channel.send("A Draw")
            print("I","A Draw")

        elif randuns==":roll_of_paper:":
            await message.channel.send("You Win")
            print("I","You Win")

        elif randuns==":rock:":
            await message.channel.send("I Win")
            print("I","I Win")


    elif message.content.startswith("Boobs"):
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif message.content.startswith("Nah"):
        await message.channel.send(file=discord.File('When The New Friend Fights an Iron Golem.mp4'))



bot.run('MTIwNTE3NzEyMzE1NzgzNTg1Ng.GBxcVy.m72-O2bnxuFjcUY7AlOoIySO7kZVH7ILh1zdHo')


