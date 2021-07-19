### Discord bot ###

# this program was created by following a tutorial from https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

import discord
import os
import requests
import json
import random
from replit import db
# from keep_alive import keep_alive #***)

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$hello"):
        await message.channel.send("Hello!")

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options += db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("new encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1].lower()
        if value in ["true", "1", "on", "hurung", "nyala"]:
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

# keep_alive() #***)
client.run(os.environ["TOKEN"]) # TOKEN is your bot token, set as environment variable


#***) Note: uncomment these line to use a web server (keep_alive.py) to keep this bot alive
# don't forget to set up uptime robot to ping the web server every five minutes
# for more information: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/