from classes import startup


async def start_pomodoro():
  import configs as cfg
  cfg.pomodoro_started = True;
  return

async def startup_e():
  class_e = startup()
  class_e.start()
  return