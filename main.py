import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
list=[":rock:", ":roll_of_paper:", ":scissors:"]
#reply (нужен для ответа пользователю на сообщение)
#await ctx.send("пон")



@bot.event



async def on_message(message):
    if message.content.startswith("🪨"):
        randuns = random.choice(list)
        print("Я",randuns,"Игрок :rock:")
        await message.channel.send(randuns)

        if randuns == ":scissors:":
            await message.channel.send("Вы выиграли")

        elif randuns == ":roll_of_paper:":
            await message.channel.send("Я выиграл")

        elif randuns == ":rock:":
            await message.channel.send("Ничья")



    elif message.content.startswith("🧻"):
        randuns = random.choice(list)
        print("Я", randuns, "Игрок :roll_of_paper:")
        await message.channel.send(randuns)

        if randuns == ":scissors:":
            await message.channel.send("Я выиграл")
            print("Я",":scissors:","Я выиграл")

        elif randuns == ":roll_of_paper:":
            await message.channel.send("Ничья")
            print("Я",":roll_of_paper:","Ничья")

        elif randuns == ":rock:":
            await message.channel.send("Вы выиграли")
            print("Я",":rock:","Вы выиграли")




    elif message.content.startswith("✂"):
        randuns = random.choice(list)
        print("Я", randuns, "Игрок :scissors:")
        await message.channel.send(randuns)

        if randuns==":scissors:":
            await message.channel.send("Ничья")

        elif randuns==":roll_of_paper:":
            await message.channel.send("Вы выиграли")

        elif randuns==":rock:":
            await message.channel.send("Я выиграл")


    elif message.content.startswith("💀"):
        await message.channel.send("https://tenor.com/view/skull-skull-emoji-sus-smile-gif-25113334")
    elif message.content.startswith("база"):
        await message.channel.send("https://www.youtube.com/watch?v=mLVws70GYtg&ab_channel=DiscardPixelhttps://www.youtube.com/watch?v=mLVws70GYtg&ab_channel=DiscardPixel")
    elif message.content.startswith("мега база"):
        await message.channel.send("https://www.youtube.com/watch?v=ptgj9rrZokQ&ab_channel=Chinozo")
    elif message.content.startswith("F"):
        await message.channel.send(file=discord.File('Yoriichi.mp4'))





bot.run('MTA3MDQzNDUxOTU2MTI3NzYzMQ.GO2-UU.yBG1lgVHkOlrSeTLIlB3_GQSOhp2LCXGXfn9rA')


