import time
import keyboard
import pynput
from KeyCodes import *
from colorama import Fore, Back, Style

running = False
start_time = 0
count_duration = 15.0 # 1 = 1 second
# phase_countdown = 15

# ask user what kind of version to run

# version_selected = input('Select version (1 or 2): ')

def auto_restart_game():
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

def move_up_and_accelerate():
    # start of up movment and acceleration
    time.sleep(5)
    MoveMouseUpContinuously(1, 0.001, 10)
    HoldKey(W)
    time.sleep(7)
    ReleaseKey(W)

def toggle_autopilot():
    HoldAndReleaseKey(Z, 10)


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

    # start of up movment and acceleration
    time.sleep(5)
    MoveMouseUpContinuously(1, 0.001, 10)
    HoldKey(W)
    time.sleep(7)
    ReleaseKey(W)


def MoveMouseUpContinuously(dy, delay, duration):
    """Move mouse up continuously using DirectInput relative movement"""
    end_time = time.time() + duration
    while time.time() < end_time:
        MouseMoveRelative(0, dy)  # negative dy = up, positive dy = down
        time.sleep(delay)

# def counter():

#     for count in range(phase_countdown, 0, -1):
#         print(count)
#         count -= 1
#         time.sleep(1)

def version_1():
    # global running
    # Countdown before starting
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)
        
    print("")
    print("Script is running in the background.")
    print("Press NUMPAD 5 to toggle")
    # print("Press NUMPAD 0 to releace keys from being held")
    print("Press Shift+Backspace to quit.")

    while True:
        # Toggle with Numpad 5
        if keyboard.is_pressed("num 5"):
            global running
            running = not running

            if running:
                print("Started holding W + E and moveing MOUSE to the right")
                HoldKey(W)
                HoldKey(E)
                # MouseMove(10,  0.01)
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

def version_2():
    # global running
    # Countdown before starting
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)

    print("")
    print("Script is running in the background.")
    print("Press NUMPAD 5 to toggle")
    print("Press NUMPAD 0 to releace keys from being held")
    print("Press Shift+Backspace to quit.")

    while True:
        # Toggle with num pad 5
        if keyboard.is_pressed("num 5"):
            global running
            running = not running


            if running:
                start_time = time.time()
                print("Started moving up and Accelerating")
                move_up_and_accelerate()
                print("Started autopilot")
                toggle_autopilot()
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
                # game_acctions()
                print("Started auto matic restart of game session")
                auto_restart_game()
                print("Started moving up and Accelerating")
                move_up_and_accelerate()
                print("Started autopilot")
                toggle_autopilot()
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


def get_valid_input():
    while True:
        print("")
        print("Select a command version")
        print("Version 1: only holds accteraion and yaw right")
        print("Version 2: holds accteraion and yaw right, flyes the plane to a high altitude to the center of the map and then triggers a restart after set time ")
        print("")
        user_input = input("Select version 1 or 2: ")
        
        if user_input == '1' or user_input == '2':
            return user_input
        else:
            print(Fore.RED + "Error: Invalid selection. Please enter 1 or 2.\n")
            print(Style.RESET_ALL)



def countdown_to_start():
    # Countdown before starting
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(1)


selection = get_valid_input()
print("")
print(f"You selected: {selection}")


# print("")
# print("Script is running in the background.")
# print("Press NUMPAD 5 to toggle")
# print("Press NUMPAD 0 to releace keys from being held")
# print("Press Shift+Backspace to quit.")
# print("")

if selection == "1":
    # countdown_to_start()
    version_1()
elif selection == "2":
    # countdown_to_start()
    version_2()
else:
    print("error")


# Makes sure keys are released before exiting the program
ReleaseKey(W)
ReleaseKey(E)
print("Exited the program")


