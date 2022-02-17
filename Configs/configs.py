#----------------Discord Configuration-----------
import discord
intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name=".pomohelp")
client = discord.Client(intents=intents, activity=activity)
from Classes.session import Session
#------------------------------------------------
#---------------Global Variables-----------------
NEW_SESSION=Session()
session={
  'Main':NEW_SESSION
}
#------------------------------------------------
#----------------AESTHETIC-CONFIGs---------------
green="\033[0;32;40m"
black="\033[0;30;47m"
blue="\033[1;36;40m"
#------------------------------------------------
#------------------Guilds------------------------
def guilds_connected():
  for guild in client.guilds:
    print(guild.name)
  return
def total_guilds():
  total=client.guilds
  return len(total)
#-------------------------------------------------