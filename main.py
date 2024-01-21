import webbrowser as wb
import time
from subprocess import Popen

sites = ["https://chat.openai.com/" , "https://twitter.com/" , "https://discord.com/channels/@me" , "https://web.whatsapp.com/"]
apps = [r'"C:\Users\Public\Desktop\Google Chrome.lnk"' , r"C:\Users\windows\OneDrive\Desktop\Notion.lnk"]

def open_tabs(urls):
    for url in urls:
        wb.open_new(url)
        time.sleep(3)

def open_apps(paths):
    for path in paths:
        Popen(path , shell = True)

open_tabs(sites)
open_apps(apps)