#----------------Discord Configuration-----------
import discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#------------------------------------------------

#---------------Global Variables-----------------
from classes import class_mute_all
from classes_handle_variables import when
c = 0; #counter
pomodoro_started = False;
ids_get = [];
joined = 0;
ids = set();
study_time_global = 0;
rest_time_global = 0;
status_class = class_mute_all('none')
close = when(None)
#------------------------------------------------
