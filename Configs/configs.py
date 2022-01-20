#----------------Discord Configuration-----------
import discord
intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name=".pomohelp")
client = discord.Client(intents=intents, activity=activity)
from Classes.classes import class_mute_all
from Classes.when_class import when
from Classes.session import Session
#------------------------------------------------
#---------------Global Variables-----------------
c = 0; #counter
pomodoro_started = False;
ids_get = [];
joined = 0;
ids = set();
study_time_global = 0;
rest_time_global = 0;
status_class = class_mute_all(None) #This class mute's all
close = when() #Starts a when class, see in when_class
vc = None; #This is a voice variable, its used in play_audio
class_e=None #This variables are classes
class_i=None #they control the future of the classes e_w_with_args, and exec
session=Session() #This class handles the information of the current sessions
#------------------------------------------------