#----------------Discord Configuration-----------
import discord
intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name=".pomohelp")
client = discord.Client(intents=intents, activity=activity)
from Classes.session import Session
#------------------------------------------------
#---------------Global Variables-----------------
class SessionGuild():
  def __init__(self, guild_name, index):
    self.guild_name=guild_name
    self.session={
      'Main':Session()
    }
    self.index=index
  def get_index(self):
    return self.index
  def get_session(self):
    return self.session
  def get_guild_name(self):
    return self.guild_name
#session={
  #'Main':NEW_SESSION
#}
session_guilds=None
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
def create_sessions():
  session_guild=["None"]
  indexX=0
  for guild in client.guilds:
    if indexX == 0:
      session_guild.insert(indexX, SessionGuild(guild.name, indexX))
    else:
      session_guild.append(SessionGuild(guild.name, indexX))
    indexX=indexX+1
  session_guild.remove("None")
  print(session_guild)
  return session_guild
#-------------------------------------------------