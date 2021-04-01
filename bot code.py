#importing libraries (don't change)
from keep_alive import keep_alive
import random
import discord
from discord.ext import commands
import os
#database import (don't change)
from replit import db


#prefix (don't change)
client = commands.Bot(command_prefix="--")



@client.command(name="start")
async def id_(ctx):
    v = ctx.author.id
    db[str(v)] = 5000
    value = (db[str(v)])    
    await ctx.send("you start with " + str(value) + " credits")
    v = ""

#get balance command
@client.command(name="bal")
async def bal_(ctx):
  value = db[str(ctx.author.id)]
  await ctx.send("you have " + str(value) + " credits")  
  value = ""


#search command
@client.command(name="search")
async def search_(ctx):
  if (db[str(ctx.author.id)]) < 100:
   money = random.randint(1, 100)
   db[str(ctx.author.id)] = (db[str(ctx.author.id)]) + money
   mp = db[str(ctx.author.id)]
   await ctx.send("you now have " + str(mp) + " credits")
  else:
    await ctx.send("you can only search if you have less then 100 credits")
    mp = ""


@client.command(name="higherlower")
async def higherlower_(ctx, bal : int, hl : str):
  if (db[str(ctx.author.id)]) >= bal:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    if hl == "higher":
     if a < b:
      db[str(ctx.author.id)] = (db[str(ctx.author.id)]) + (bal * 2)  
      await ctx.send("now you have " + str(db[str(ctx.author.id)]) + " credits")
      await ctx.send("a was " + str(a) + " and b was " + str(b))
     else:
      db[str(ctx.author.id)] = db[str(ctx.author.id)] - bal
      await ctx.send("you lost you now only have " + str(db[str(ctx.author.id)]) + " credits")
      await ctx.send("a was " + str(a) + " and b was " + str(b))
    elif hl == "lower":
     if a > b:
      db[str(ctx.author.id)] = (db[str(ctx.author.id)]) + (bal * 2)  
      await ctx.send("now you have " + str(db[str(ctx.author.id)]) + " credits")
      await ctx.send("a was " + str(a) + " and b was " + str(b))
     else:
      db[str(ctx.author.id)] = db[str(ctx.author.id)] - bal
      await ctx.send("you lost you now only have " + str(db[str(ctx.author.id)]) + " credits")
      await ctx.send("a was " + str(a) + " and b was " + str(b))
  else:
    await ctx.send("you don't have enough credits to do that right now")

player1 = ""
player2 = ""

@client.command(name="cointoss")
async def cointoss_(ctx,  p1: discord.Member, p2: discord.Member, bal : int):
  global player1
  global player2
  if bal <= int(db[str(player1.id)]):
   if bal <= int(db[str(player2.id)]):
     num = random.randint(1, 2)
     if num == 1:
      db[str(player1.id)] = int(db[str(player1.id)]) + bal 
      (db[str(player2.id)]) = int(db[str(player2.id)]) - bal 
      await ctx.send("player 1 gained " + str(bal) + " credits, while player 2 lost " + str(bal) + " credits")
      await ctx.send("player 1's now has " + str(db[str(player1.id)]) + " credits, while player 2 now has " + str(db[str(player2.id)]) + " credits")
     else:
      db[str(player2.id)] = int(db[str(player2.id)]) + bal 
      (db[str(player1.id)]) = int(db[str(player1.id)]) - bal 
      await ctx.send("player 2 gained " + str(bal) + " credits, while player 1 lost " + str(bal) + " credits")
      await ctx.send("player 1's now has " + str(db[str(player1.id)]) + " credits, while player 2 now has " + str(db[str(player2.id)]) + " credits")
   else:
      await ctx.send("player 2 doesn't have enough credits for this")
  else:
    await ctx.send("player 1 doesn't have enough credits for this") 

@client.command(name="rtd")
async def rtd_(ctx, bal : int, dice : int):
  if bal >= int(db[str(ctx.author.id)]):
    await ctx.send("you don't have enough credits for this")
  else:
    rtd = random.randint(1,6)
    if rtd == dice:
      db[str(ctx.author.id)] = db[str(ctx.author.id)] + (bal * 3)
      await ctx.send("you guessed the diceroll right you now have " + str(db[str(ctx.author.id)]) + " credits")
    else:
      db[str(ctx.author.id)] = db[str(ctx.author.id)] - bal
      await ctx.send("you didn't guess the diceroll correctly now you have " + str(db[str(ctx.author.id)]) + " credits")

player3 = ""
@client.command(name="give")
async def give_(ctx, bal : int, p3 : discord.Member):
  global player3
  player3 = p3
  if bal > db[str(ctx.author.id)]:
    await ctx.send("you don't have enough credits for that")
  else:
    db[str(ctx.author.id)] = db[str(ctx.author.id)] - bal
    db[str(player3.id)] = db[str(player3.id)] + bal
    await ctx.send("you have given them " + str(bal) + " credits")

@client.command(name="gethelp")
async def gethelp_(ctx):
  await ctx.send("--start to start")
  await ctx.send("--search to search for credits")
  await ctx.send("--bal to check your balance")
  await ctx.send("--higherlower (amount) (higher or lower) to have a random chance to win double your input back")
  await ctx.send("--rtd (input) (number between 1 and 6) to win 3 times your input back")
  await ctx.send(" --cointoss (@ player1) (@ player 2) (input) cointoss with someone else ")

#how it connects to bot (don't change)
keep_alive()
client.run(os.getenv('TOKEN'))

