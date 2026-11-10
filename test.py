import time
import datetime as dt

# Setting up deadline 


# hours = int(input("Numbers of hours to setup: "))
# minuts = int(input("Numbers of Minuts to setup: "))
# seconds = int(input("Number of Seconds to setup: "))

hours = 11
minutes = 12
seconds = 12


def print_deadline(hours, minutes, seconds):
    deadline = dt.datetime(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,hours,minutes,seconds).timetuple()
    set_deadline = time.strftime('%H:%M:%S', deadline)
    return set_deadline


while True: 
    if seconds == 0:
        print_deadline(hours, minutes, seconds)
        minutes -= 1
        seconds = 59
        time.sleep(1)

    if minutes == 0:
        print_deadline(hours, minutes, seconds)
        hours -= 1
        minutes = 59
        time.sleep(1)

    if hours == 0 and minutes == 0 and seconds == 0:
        print("Time is up")
        break

    else:
        print_deadline(hours, minutes, seconds)
        seconds -= 1
        time.sleep(1)