import os
import discord
from discord.ext import commands, tasks
import requests 
import asyncio

token = os.getenv('token')

#Made by theaxes


prefix = input("Input prefix:")
#Embed Settings
title = input("Input Embed Title:")
fieldname = input("Input A Name For embed field:")
fieldvalue = input("enter a message for field description:")

#non embed settings

message = input("Input message for mass dm:")
os.system('clear')
print('''
███╗░░░███╗░█████╗░░██████╗░██████╗
████╗░████║██╔══██╗██╔════╝██╔════╝
██╔████╔██║███████║╚█████╗░╚█████╗░
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░

██████╗░███╗░░░███╗
██╔══██╗████╗░████║
██║░░██║██╔████╔██║
██║░░██║██║╚██╔╝██║
██████╔╝██║░╚═╝░██║
╚═════╝░╚═╝░░░░░╚═╝
Made By TheAxes
''')

intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
   await client.change_presence(activity=discord.Game(name="Axe Are On Top"))
   print('Logged In As ' + client.user.name)
 
embed=discord.Embed(title=title)
embed.add_field(name=fieldname, value=fieldvalue, inline=False)
embed.set_thumbnail(url="https://media.discordapp.net/attachments/859319182495973386/1000328591474700378/QA-Monogram.png")
embed.set_footer(text="Made By reaper.exe")

 
#embeded
@client.command(pass_context=True)
async def embedmassdm(ctx):
	await ctx.send(" MASS DM STARTED\n> Made By reaper.exe", mention_author=True)
	members = ctx.guild.members
	for member in members:
		try:
			await member.send(embed=embed)
			print("Embeded Mass Dm Sent To " +  member.name)
		except:
			print("Unable To Dm " + member.name + " Reason = dms off")
			



        
@client.command(pass_context=True)
async def help(ctx):
	embed=discord.Embed(title="Mass Dm Bot", description="Made By TheAxes")
	embed.add_field(name="Help ", value="Help Command Of Axe Mass Dm Bot", inline=False)
	embed.add_field(name=prefix + "embedmassdm", value="Send Users A embeded messsge that looks Cool", inline=True)
	embed.add_field(name=prefix + "massdm", value="Send Users a Normal Mass Dm Message", inline=True)
	embed.set_footer(text="Made By TheAxes ")
	await ctx.send(embed=embed)
	
	
	
	
@client.command()
async def massdm(ctx):
	await ctx.send("MASS DM STARTED\n> Made By TheAxes", mention_author=True)
	members = ctx.guild.members
	for member in members:
		try:
			await member.send(message)
			print("Normal Mass Dm Sent To " + member.name)
		except:
			print("Unable To Dm " + member.name + " reason = Dms Off")
			



client.run(token, bot=True)

        
        
        
        
        

#madebytheaxes
