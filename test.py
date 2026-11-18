import keyboard
import time

tik = 10
restart = tik

paused = False
stopped = False
running = True
quit = False

print("Press P to pause/resume and S to stop")

while True:

    if quit == True:
            print("Program quit")
            break

    if paused == True:
        if keyboard.is_pressed('q'):
            quit = True
            break

        if keyboard.is_pressed('s'):
            paused = False
            stopped = True
            print("stopped")
            keyboard.wait('s', trigger_on_release=True)
        
        if keyboard.is_pressed('p'):
            paused = False
            running = True
            print("program resumed")
            keyboard.wait('p', trigger_on_release=True)

    if stopped == True: 
        if keyboard.is_pressed('q'):
            quit = True
            break

        if keyboard.is_pressed('r'):
            stopped = False
            running = True
            tik = restart
            print("Countdown Restarted")
            keyboard.wait('r', trigger_on_release=True)

    if running == True:
        while tik > 0:
            if keyboard.is_pressed('p'):
                tik = tik
                paused = True
                running = False
                print("Countdown paused")
                keyboard.wait('p', trigger_on_release=True)
                break

            if keyboard.is_pressed('q'):
                quit = True
                break

            if keyboard.is_pressed('s'):
                running= False
                stopped = True
                tik = restart
                print("stopped")
                keyboard.wait('s', trigger_on_release=True)
                break

            if keyboard.is_pressed('r'):
                tik = restart
                keyboard.wait('r', trigger_on_release=True)
                continue
            
            print(tik)
            tik -= 1
            time.sleep(1)

    if tik == 0:
        print("Countdown finished")

        Further_instructions = int(input("What you want to do 1 for quit and 2 for restart"))

        if Further_instructions == 2:
            tik = restart
            continue

        if Further_instructions == 1:
            break

    