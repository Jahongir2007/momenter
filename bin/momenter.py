'''
    Author: Jahongir Sobirov
    Momenter python library
    Version: 1.0.1
    License: MIT
    All rights reserved (c) 2021
'''

import datetime
import calendar
from time import time, ctime, strftime

def format(value):
    if value == "YYYY MM DD HH MM SS":
        x = datetime.datetime.now()
        print(x.strftime("%Y"), x.strftime("%m"), x.strftime("%A"), x.strftime("%H"), x.strftime("%M"), x.strftime("%S"))
    elif value == "YYYY MM DD HH MM":
        x = datetime.datetime.now()
        print(x.strftime("%Y"), x.strftime("%m"), x.strftime("%A"), x.strftime("%H"), x.strftime("%M"))
    elif value == "YYYY MM DD HH":
        x = datetime.datetime.now()
        print(x.strftime("%Y"), x.strftime("%m"), x.strftime("%A"), x.strftime("%H"))
    elif value == "YYYY MM DD":
        x = datetime.datetime.now()
        print(x.strftime("%Y"), x.strftime("%m"), x.strftime("%A"))
    elif value == "YYYY MM":
        x = datetime.datetime.now()
        print(x.strftime("%Y"), x.strftime("%m"))
    elif value == "YYYY":
        x = datetime.datetime.now()
        print(x.strftime("%Y"))
    elif value == "MM":
        x = datetime.datetime.now()
        print(x.strftime("%m"))
    elif value == "DD":
        x = datetime.datetime.now()
        print(x.strftime("%A"))
    elif value == "HH":
        x = datetime.datetime.now()
        print(x.strftime("%H"))
    elif value == "MM":
        x = datetime.datetime.now()
        print(x.strftime("%M"))
    elif value == "SS":
        x = datetime.datetime.now()
        print(x.strftime("%S"))
    elif value == "h:m":
        x = datetime.datetime.now()
        print(x.strftime("%H"),":",x.strftime("%M"))
    elif value == "h:m:s":
        x = datetime.datetime.now()
        print(x.strftime("%H"),":",x.strftime("%M"),":",x.strftime("%S"))
    elif value == "m/d/y":
        x = datetime.datetime.now()
        print(x.strftime("%x"))
    else:
        print("Error code!")

def calendar():
    x = datetime.datetime.now()
    print(x.strftime("%c"))

def moment():
    x = datetime.datetime.now()
    print(x.strftime("%H"),":",x.strftime("%M"),":",x.strftime("%S"))

def between(firtime, sectime, type):
    if type == "YYYY":
        if sectime-firtime == 1:
            print(sectime-firtime, "year")
        else:
            print(sectime-firtime, "years")
        print(sectime-firtime, "years")
    elif type == "MM":
        if sectime-firtime == 1:
            print(sectime-firtime, "month")
        else:
            print(sectime-firtime, "months")       
        print(sectime-firtime, "months")
    elif type == "DD":
        if sectime-firtime == 1:
            print(sectime-firtime, "day")
        else:
            print(sectime-firtime, "days")
    elif type == "HH":
        if sectime-firtime == 1:
            print(sectime-firtime, "hour")
        else:
            print(sectime-firtime, "hours")
    elif type == "mm":
        if sectime-firtime == 1:
            print(sectime-firtime, "minute")
        else:
            print(sectime-firtime, "minutes")
    elif type == "SS":
        if sectime-firtime == 1:
            print(sectime-firtime, "second")
        else:
            print(sectime-firtime, "seconds")
def times(time):
    print(time)
def mydate(year, day, month):
    if day == "false":
        print(year,".",month)
    else:
        print(year,".",day,".",month)
def nowyear():
        x = datetime.datetime.now()
        print(x.strftime("%Y"))
def nowmonth():
        x = datetime.datetime.now()
        print(x.strftime("%m"))
def nowday():
        x = datetime.datetime.now()
        print(x.strftime("%A"))
