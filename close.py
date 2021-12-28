from messages import message_closed_pomodoro
import configs as cfg

def close_pomodoro(message):
  cfg.pomodoro_started = False;
  message_closed_pomodoro(message)
  return