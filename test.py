

# print("")


# version_selected = input('Select version (1 or 2): ')
# print('version ' + version_selected + " selected" ) 

# while version_selected != "1" or "2":
#     version_selected = input('Select version (1 or 2): ')







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
            print("Error: Invalid selection. Please enter 1 or 2.\n")

# Usage
selection = get_valid_input()
print(f"You selected: {selection}")