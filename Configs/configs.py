#----------------Discord Configuration-----------
import nextcord
#intents.members = True
intents = nextcord.Intents(guilds=True, voice_states=True)
activity = nextcord.Game(name="/pomohelp")
client = nextcord.Client(activity=activity, intents=intents)
from Classes.session import Session
from Cli_Commands.Print_Padronization.ppadron import prntpdr
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

session_guilds=None
#------------------------------------------------
#----------------AESTHETIC-CONFIGs---------------
green="\033[38;5;40m"
black="\033[38;5;230m"
normal="\033[38;5;246m"
blue="\033[38;5;27m"
yellow="\033[38;5;190m"
red="\033[38;5;196m"
cli_date="\033[38;5;15m"
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
  index=0
  for guild in client.guilds:
    if index == 0:
      session_guild.insert(index, SessionGuild(guild.name, index))
    else:
      session_guild.append(SessionGuild(guild.name, index))
    prntpdr(normal, "index:{} guild:{}".format(index, guild.name))
    index=index+1
  session_guild.remove("None")
  return session_guild
#-------------------------------------------------
