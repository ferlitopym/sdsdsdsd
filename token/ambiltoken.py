#بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِ
#GUNAKAN DENGAN BIJAK KAWAN....EDIT SESUKA KALIAN...
#HARGAI TANGAN CREATOR..!!!!!
#[KIBAZ TEAM BOT]:
from linepy  import *
#from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
#from akad.ttypes import Message
#from akad.ttypes import ContentType as Type
#from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from Naked.toolshed.shell import execute_js
#import subprocess, youtube_dl, humanize, traceback
#import subprocess as cmd
import platform
import requests, json
#import time, random, sys, json, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
eric = LINE("akunytdijual@gmail.com","ferbot2212")
eric.log("Auth Token : " + str(eric.authToken))
waitOpen = codecs.open("eric/wait.json","r","utf-8")
settingsOpen = codecs.open("eric/temp.json","r","utf-8")
ericProfile = eric.getProfile()
ericSettings = eric.getSettings()
ericPoll = OEPoll(eric)
ericStart = time.time()
ericMID = eric.getProfile().mid
loop = asyncio.get_event_loop()
admin =[""]
botStart = time.time()
kuciyose = {}
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
mulai = time.time()


def run():
    while True:
        try:
            ops = ericPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(ericBot(op))
                   ericPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)

if __name__ == "__main__":
    run()
