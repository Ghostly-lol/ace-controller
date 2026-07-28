import time
import keyboard
import pynput
from KeyCodes import *


running = False


# Countdown before starting
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

print("Script is running in the background.")
print("Press NUMPAD 5 to toggle")
print("Press Shift+Backspace to quit.")



while True:
    # Toggle with Numpad 5
    if keyboard.is_pressed("num 5"):
        running = not running

        if running:
            print("Started holding W + E and moveing MOUSE to the right")
            HoldKey(W)
            HoldKey(E)
            #MouseMove(10,  0.01)
        else:
            print("Stopped holding W + E and moveing MOUSE to the right")
            ReleaseKey(W)
            ReleaseKey(E)
            

        # Wait until the key is released so it only toggles once
        while keyboard.is_pressed("num 5"):
            time.sleep(0.01)

    # Exit the script
    if keyboard.is_pressed("shift+backspace"):
        break

    time.sleep(0.01)

# Make sure keys are released before exiting
ReleaseKey(W)
ReleaseKey(E)
print("Exited.")
