import os
import subprocess
import time

import psutil
import schedule

MAA1 = r"D:\Auto\lnk\MAA1.lnk"
MAA2 = r"D:\Auto\lnk\MAA2.lnk"


def maadetection():
    for prcs in psutil.process_iter():
        if prcs.name().lower() == "meoasstgui.exe":
            return True


def bsdetection():
    for prcs in psutil.process_iter():
        if prcs.name().lower() == "hd-player.exe":
            return True


def kill():
    for prcs in psutil.process_iter():
        if prcs.name().lower() == "meoasstgui.exe":
            subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % prcs.pid, shell=True)
        if prcs.name().lower() == "hd-player.exe":
            subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % prcs.pid, shell=True)


def start(x):
    os.system(x)


def detection(x):
    if maadetection():
        if bsdetection():
            pass
        else:
            kill()
            start(x)
    else:
        start(x)


schedule.every().day.at("20:00:00").do(start, x=MAA1)
schedule.every().day.at("20:00:20").do(detection, x=MAA1)
schedule.every().day.at("20:02:00").do(detection, x=MAA1)
schedule.every().day.at("20:55:00").do(kill)
schedule.every().day.at("20:55:20").do(start, x=MAA2)
schedule.every().day.at("20:55:40").do(detection, x=MAA2)
schedule.every().day.at("20:57:00").do(detection, x=MAA2)
while True:
    schedule.run_pending()
    time.sleep(1)
