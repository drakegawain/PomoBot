from replit import db
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg
import logging

class SecurityMessage:
  def __init__(self, command:str, ctx:str, userid:int):
    self.command=command
    self.message=''
    self.ctx=ctx
    self.reason=''
    self.user=userid
    self.logger=logging.getLogger("SecurityMessage")
    self.error=None
  async def send(self, error:int):
    try:
      self.search_reason(error)
    except TypeError:
      print('error in send search_reason')
    try:
      self.set_message()
    except:
      print('error in send set_message')
    try:
      message=self.ctx
      await message.channel.send(self.message)
      self.logger.error("{}  :  {}".format(self.error, self.command))
    except:
      self.logger.error("Error in third block SecurityMessage_send")
      
  def set_message(self):
    self.message=("\n>>> <@{user}> \nUnfourtunally PomoBot could'nt call ``{command}`` **because**: *{reason}*".format(user=self.user, command=self.command, reason=self.reason))
  def set_reason(
    self, command:str, bad_access:str # raise an error number
    , reason:str
  ):
    db["{command}_{bad_access}".format(command=command, bad_acess=bad_access)] = "{reason}".format(reason=reason)
  def search_reason(self, error:int):
    self.error = error
    #implemented errors
    #pomostop_101 - User outside the session
    #pomostop_121 - No session running
    #pomostop_141 - User outside Voice_Channel
    #pomodoro_201 - User already in another session
    #pomodoro_221 - Inputs must be a integer
    #pomodoro_251 - Must have two inputs
    #pomodoro_271 - Only one session per voice_channel at the same time
    #pomojoin_301 - No session running
    for key in db.keys():
      if str(error) in key:
        value=db[key]
        self.reason=value
        prntpdr(cfg.red, value)
        return 
    return

    