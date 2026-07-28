import time
import keyboard
import pynput
from KeyCodes import *


running = False
start_time = 0
count_duration = 15.0 # 1 = 1 second
phase_countdown = 15

# Countdown before starting
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

print("Script is running in the background.")
print("Press NUMPAD 5 to toggle")
print("Press NUMPAD 0 to releace keys from being held")
print("Press Shift+Backspace to quit.")



def game_acctions():
    # HoldAndReleaseMouse(10)
    # releces w and e keys from being held
    ReleaseKey(W)
    ReleaseKey(E)

    # start of restart menu sequence
    HoldAndReleaseKey(ESC, 1.5)
    time.sleep(1)
    HoldAndReleaseKey(S, .1)
    time.sleep(1)
    HoldAndReleaseKey(S, .1)
    time.sleep(1)
    HoldAndReleaseKey(ENTER, .5)
    time.sleep(2)
    HoldAndReleaseKey(W, .5)
    time.sleep(1)
    HoldAndReleaseKey(ENTER, .5)
    time.sleep(2)
    # end of restart sequence


def counter():

    for count in range(phase_countdown, 0, -1):
        print(count)
        count -= 1
        time.sleep(1)




while True:
    # Toggle with num pad 5
    if keyboard.is_pressed("num 5"):
        running = not running


        if running:
            start_time = time.time()
            print("Started holding Acceleration and Yaw Right (W + E) ")
            HoldKey(W)
            HoldKey(E)
            last_printed = None
            # MouseMove(10,  0.01)
            # print(phase_countdown)
            # if timmer == 0:
                
            #     game_acctions()
            #     phase_countdown = 15
        else:
            print("Stopped holding Acceleration and Yaw Right (W + E) ")
            ReleaseKey(W)
            ReleaseKey(E)
            last_printed = None

        # Wait until the key is released so it only toggles once
        while keyboard.is_pressed("num 5"):
            time.sleep(0.01)

    if running:
        elapsed = time.time() - start_time
        remaining = int(count_duration - elapsed)

        # Print each new countdown value
        if remaining > 0 and remaining != last_printed:
            print(remaining)
            last_printed = remaining

            # When the phase ends, run actions and reset the timer
        if remaining <= 0:
            print("Phase complete — running game actions!")
            game_acctions()
            HoldKey(W)                    
            HoldKey(E) 
            start_time = time.time()       # restart countdown
            last_printed = None
            
        
    # Exit the script
    if keyboard.is_pressed("shift+backspace"):
        break

    if keyboard.is_pressed("num 0"):
        print("releasing W + E ")
        ReleaseKey(W)
        ReleaseKey(E)
    

    time.sleep(0.01)


# Makes sure keys are released before exiting the program
ReleaseKey(W)
ReleaseKey(E)
print("Exited the program")


