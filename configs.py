#----------------Discord Configuration-----------
import discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
activity = discord.Game(name=".help \nin {} guilds" .format(str(len(client.guilds))))
client = discord.Client(intents=intents, activity=activity)
#------------------------------------------------
#---------------Global Variables-----------------
from classes import class_mute_all
from when_class import when
c = 0; #counter
pomodoro_started = False;
ids_get = [];
joined = 0;
ids = set();
study_time_global = 0;
rest_time_global = 0;
status_class = class_mute_all('none')
close = when() #starts a when class, see in when_class
#------------------------------------------------