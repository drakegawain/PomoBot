from messages import message_closed_pomodoro
from configs import pomodoro_started

def close_pomodoro(message):
  global pomodoro_started;
  pomodoro_started = False;
  message_closed_pomodoro(message)
  return