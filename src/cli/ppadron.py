import src.Configs.configs as cfg
import datetime

def now_time():
  now=datetime.datetime.now()
  return now
def prntpdr(aesthetic:str, string:str):
  now=now_time()
  print("[{date_aesthetic}{now}][{aesthetic}{string_content}{common_aesthetic}]".format(date_aesthetic=cfg.cli_date,aesthetic=aesthetic, now=now, string_content=string, common_aesthetic=cfg.cli_date))
  return