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
#This class handles the information of the current sessions
#------------------------------------------------