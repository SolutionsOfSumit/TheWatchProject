from pydantic import BaseModel

class DeadLine(BaseModel):
    hours: int = 0
    minutes: int = 0
    seconds: int = 10
