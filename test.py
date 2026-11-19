import time
import keyboard
import datetime as dt
from pydantic import BaseModel

# Schemas

class DeadLine(BaseModel):
    year : int = time.localtime().tm_year,
    month : int = time.localtime().tm_mon,
    day : int = time.localtime().tm_mday,
    hour : int = time.localtime().tm_hour,
    minute : int = time.localtime().tm_min,
    second : int = time.localtime().tm_sec,

# Functions 

def get_deadline(hour, minutes, seconds):
    user_data = {
        "hour" : hour,
        "minute" : minutes,
        "second" : seconds 
    }

    deadline = DeadLine(**user_data)

    print(deadline.model_dump())


get_deadline(5,10,15)
