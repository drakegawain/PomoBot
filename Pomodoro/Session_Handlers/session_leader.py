async def leader(session, message):
  #Sets session leader
  #Leader joins the session automatically 
  #Leader dont need to call pomojoin
  session.LEADER_ID=message.author.id
  session.pushleader()
  return