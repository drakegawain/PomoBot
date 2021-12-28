
async def handle_study_time(study_time):
  study_time = study_time * 60;
  return study_time

async def handle_rest_time(rest_time):
  rest_time = rest_time * 60;
  return rest_time;

async def study_time(message):
  pomodoro = message.content;
  time_study = ''
  for char in pomodoro[9:12:1]:
    time_study = time_study + char;
  return int(time_study);

async def rest_time(message):
  pomodoro = message.content;
  rest_time = ''
  for char in pomodoro[12:15:1]:
    rest_time = rest_time + char;
  return int(rest_time)

  