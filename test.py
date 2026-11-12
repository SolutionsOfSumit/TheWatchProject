import keyboard 
import time

tik = 10
is_paused = False

def count_down(count_down):
    while count_down >= 0:

        if keyboard.is_pressed('p') and is_paused == False:
            tik = tik
            is_paused = True

        print(count_down)
        count_down -= 1
        time.sleep(1)

while tik >= 0 and is_paused == False:
    count_down(tik)

    if keyboard.is_pressed('p') and is_paused == False:
        tik = tik
        is_paused = True

    if keyboard.is_pressed('p') and is_paused == True:
        count_down(tik)

    if keyboard.is_pressed('s'):
        print(f"You stopped the countdown at {tik}")
        break