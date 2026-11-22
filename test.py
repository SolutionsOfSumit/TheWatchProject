import time
import keyboard
import datetime as dt
from pydantic import BaseModel, ValidationError, AfterValidator
from typing import Annotated

# Schema functions

def is_hour(value: int):
    if not 0 <= value <= 23:
        raise ValueError("Value is not an valid")
    return value

def is_min(value: int):

    if not 0 <= value <= 59:
        raise ValueError("Value is not an valid")
    return value

# Schemas

class DeadLine(BaseModel):
    hour : Annotated[int, AfterValidator(is_hour)]  = time.localtime().tm_hour
    minute : Annotated[int, AfterValidator(is_min)]  = time.localtime().tm_min
    second : Annotated[int, AfterValidator(is_min)]  = time.localtime().tm_sec

    

# Functions 

def get_deadline(hour, minutes, seconds):
    user_data = {
        "hour" : hour,
        "minute" : minutes,
        "second" : seconds 
    }
    try:
        deadline = DeadLine(**user_data).model_dump()
        return deadline
    except ValueError as e :
        print(e)
        

print(get_deadline(21,21,50))
