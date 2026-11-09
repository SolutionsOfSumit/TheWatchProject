import time

deadline = int(input(
    "Set up your best time for the work in seconds"
))

while deadline >= 0:
    print(f"{deadline}seconds left")
    deadline -= 1
    time.sleep(1)