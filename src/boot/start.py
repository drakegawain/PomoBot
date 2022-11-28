import datetime
import tracemalloc
import gc
import logging
import mysql.connector
import itertools
import threading
import time
import sys
import asyncio
from ..Configs import configs as cfg
from ..Configs.configs import db, cursor, cursor2, extract, t1
from mysql.connector import RefreshOption
from ..cli.ppadron import prntpdr
from ..Configs.setup import setup
from ..Configs.events import events
from ..Configs.slash import slash

async def start():
  prntpdr(cfg.black, "collecting garbage")
  tracemalloc.start()
  assert truncateStatus(db, cursor, "botstatus") == True, "Fail to truncate botstatus"
  #sch = cursor.execute("select status from botstatus")
  #print(extract(sch))
  #time.sleep(10)
  gc.collect(0)
  gc.collect(1)
  gc.collect(2)
  prntpdr(cfg.green, "collected")
  prntpdr(cfg.black, "loading files")
  def worker(loop:asyncio.AbstractEventLoop, db:mysql.connector.CMySQLConnection, cursor:mysql.connector.connection.CursorBase):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(isReady(db, cursor))
    loop.close()
  loop = asyncio.new_event_loop()
  t1 = threading.Thread(target=worker, args=[loop, db, cursor2])
  t1.start()
  #isReady(db, cursor2)
  #assert await loadGuilds(db, cursor, cfg.session_guilds) == True, "Fail to load guilds"
  setup()
  SM = logging.getLogger("SecurityMessage")
  logger = logging.getLogger("Event")
  grsrc = logging.getLogger("GuildRsrc")
  await events(grsrc)
  await slash(logger, SM)
  #time.sleep(10)
  #sch = cursor.execute("select status from botstatus")
  #print(extract(sch))
  return True

async def loadGuilds(db:mysql.connector.CMySQLConnection, cursor:mysql.connector.connection.CursorBase, guilds:list):
  table = "Guilds"
  search = cursor.execute("select {guildName} from {table}".format(guildName = "Name", table = table))
  search = cfg.extract(search)
  srchName = [infos[0] for gld in search for infos in gld]
  try:
    for guild in guilds:
      if guild.name not in srchName:
        cursor.execute("insert into {table} (Name, id) values ({guildName}, {id})".format(table = table, guildName = guild.name, id = guild.id))
    db.commit()
    return True
  except:
    raise Exception

async def isReady(db:mysql.connector.CMySQLConnection, cursor:mysql.connector.connection.CursorBase):
    time.sleep(0.5)
    #it seems to work
    state = "status"
    for c in itertools.cycle(['.', '/', '-', '\\']):
        search = cursor.execute("select {state} from botstatus".format(state = state))
        search = cursor.fetchone()
        #search = extract(search)
        if search != None and search != []:
          if search[0] == 'Online':
            t = threading.main_thread()
            sys.stdout.write("{aesthetic}[ OK ]{commonAesthetic}\n".format(aesthetic = cfg.green, commonAesthetic = cfg.cli_date))
            prntpdr(cfg.green, "{}".format(search[0]))
            t.join()
            pass
        sys.stdout.write('\r[{time}][{aesthetic}loading{commonAesthetic}'.format(time = datetime.datetime.now(), aesthetic = cfg.black, commonAesthetic = cfg.cli_date) + c + ']')
        sys.stdout.flush()
        cursor.reset(True)
        time.sleep(0.1)
        

def truncateStatus(db:mysql.connector.CMySQLConnection, cursor:mysql.connector.connection.CursorBase, table:str):
  cursor.execute("truncate table {table}".format(table = table))
  db.commit()
  return True