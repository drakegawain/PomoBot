#----------------Discord Configuration-----------
import discord
intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name=".pomohelp")
client = discord.Client(intents=intents, activity=activity)
from Classes.classes import class_mute_all
from Classes.when_class import when
#------------------------------------------------
#---------------Global Variables-----------------
c = 0; #counter
pomodoro_started = False;
ids_get = [];
joined = 0;
ids = set();
study_time_global = 0;
rest_time_global = 0;
status_class = class_mute_all('none')
close = when() #starts a when class, see in when_class
vc = None;
class_e=None
class_i=None
#------------------------------------------------