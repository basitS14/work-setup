import webbrowser as wb
import time
from subprocess import Popen

sites = ["https://www.example.com/"]
apps = [r'"C:\path\to\app name"' ]

def open_tabs(urls):
    for url in urls:
        wb.open_new(url)
        time.sleep(3)

def open_apps(paths):
    for path in paths:
        Popen(path , shell = True)

open_tabs(sites)
open_apps(apps)
