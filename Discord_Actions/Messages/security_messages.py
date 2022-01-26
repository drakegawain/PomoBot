#--------This-file-storage-security-messages-------
from replit import db

class SecurityMessage:
  def __init__(self, command:str, ctxmessage:str, userid:int):
    self.command=command
    self.message=''
    self.ctx=ctxmessage
    self.reason=''
    self.user=userid
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
    except:
      print('Error in third block SecurityMessage_send')
  def set_message(self):
    self.message=("<@{user}> \nUnfourtunally PomoBot could'nt call ``{command}`` because: ``{reason}``".format(user=self.user, command=self.command, reason=self.reason))
  def set_reason(
    self, command:str, bad_access:str # raise an error number
    , reason:str
  ):
    db["{command}_{bad_access}".format(command=command, bad_acess=bad_access)] = "{reason}".format(reason=reason)
  def search_reason(self, error:int):
    #implemented errors
    #pomostop_101 - User outside the session
    #pomostop_121 - No session running
    #pomodoro_201 - User already in another session
    #pomodoro_271 - Only one session per voice_channel at the same time
    #pomojoin_301 - No session running
    for key in db.keys():
      if str(error) in key:
        value=db[key]
        self.reason=value
        print(value)
        return 
    return