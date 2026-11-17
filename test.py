import keyboard
import time

tik = 10
restart = tik

is_paused = False
is_quit = False
restart_want = False
is_stopped = False

print("Press P to pause/resume and S to stop")

while is_quit == False:

    if restart_want== True and is_stopped == False:
        keyboard.wait('r', trigger_on_release=True)
        restart_want = not restart_want
        is_stopped = False

    if is_quit == True:
        keyboard.wait('q', trigger_on_release=True)
        break

    while tik >= 0:

        if keyboard.is_pressed('q'):
            print(f"program quit")
            is_quit = True
            break

        if keyboard.is_pressed('s'):
            print(f"Countdown stopped at {tik}")
            is_stopped = True
            break

        if keyboard.is_pressed('r'):
            print("Restarting the countdown")
            tik = restart
            is_paused = False
            restart_want = True
            break
        

        if keyboard.is_pressed('p'):
            is_paused = not is_paused

            if is_paused:
                print("Paused")
            else:
                print("Resumed")

            keyboard.wait('p')  

        if not is_paused:
            print(tik)
            tik -= 1
            time.sleep(1)

print("Countdown finished")