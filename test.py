import keyboard
import time

tik = 10
restart = tik

is_paused = False

print("Press P to pause/resume and S to stop")

while tik >= 0:

    if keyboard.is_pressed('s'):
        print(f"Countdown stopped at {tik}")
        break
    if keyboard.is_pressed('r'):
        print("Restarting the countdown")
        tik = restart

    if keyboard.is_pressed('p'):
        is_paused = not is_paused

        if is_paused:
            print("Paused")
        else:
            print("Resumed")

        keyboard.wait('p')  # Wait until P is released

    if not is_paused:
        print(tik)
        tik -= 1
        time.sleep(1)


print("Countdown finished")