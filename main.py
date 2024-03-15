import basic_door
import locked_door
import deadbolt_door
import combo_door
import code_door
import check_input
import random 

def open_door(door):
    """Display information about the door and allows user to open the door"""
    print(door.examine_door())
    open = False
    while not open:
        print(door.menu_options())
        choice = check_input.get_int_range("Enter choice: ", 1, door.get_menu_max())
        print(door.attempt(choice))
        if door.is_unlocked():
            print(door.success())
            open = True 
        else:
            print(door.clue())

def main():
    print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...")

    for i in range(3):
        rand = random.randint(1,5)
        if rand == 1:
            door = basic_door.BasicDoor()
        if rand == 2:
            door = locked_door.LockedDoor()
        if rand == 3:
            door = deadbolt_door.DeadboltDoor()
        if rand == 4:
            door = combo_door.ComboDoor()
        if rand == 5:
            door = code_door.CodeDoor()

        open_door(door)
        print()

    print("Congratulations! You escaped... this time. ")

main()