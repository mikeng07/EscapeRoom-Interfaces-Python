import door
import random

class CodeDoor(door.Door):
    """represents a locked door."""

    def __init__(self):
        """set the initial state of the door"""
        self._correct_code = ["X", "X", "X"]
        if random.randint(1,2) == 1:
            self._correct_code[0] = 'O'        
        if random.randint(1,2) == 1:
            self._correct_code[1] = 'O'        
        if random.randint(1,2) == 1:
            self._correct_code[2] = 'O'        
        self._input = ["O", "O", "O"]

    def examine_door(self):
        """Description of the door"""
        return "You encounter a coded door, you must enter the correct code to open the door.  There are 3 characters displayed, each one can be toggled to either an 'X' or an 'O'.  You can press the key under each character to toggle it."

     
    def menu_options(self):
        """Door menu"""
        return "1. Press key 1\n2. Press key 2\n3. Press key 3"

     
    def get_menu_max(self):
        """number of items in the door's menu"""    
        return 3
        
     
    def attempt (self,option):
        """Use the input to determine whether user has unlocked the door. 
            Return what user attmpted."""
        if option == 1:
            if self._input[0] == 'X':
                self._input[0] = 'O'
            else:
                self._input[0] = 'X'
            return "you toggle the first character.\n" + str(self._input)
        elif option == 2:
            if self._input[1] == 'X':
                self._input[1] = 'O'
            else:
                self._input[1] = 'X'
            return "you toggle the second character.\n" + str(self._input)
        elif option == 3:
            if self._input[2] == 'X':
                self._input[2] = 'O'
            else:
                self._input[2] = 'X'
            return "you toggle the third character.\n" + str(self._input)
     
    def is_unlocked(self):
        """return true if the door was unlocked"""
        return self._correct_code[0] == self._input[0] and self._correct_code[1] == self._input[1] and self._correct_code[2] == self._input[2]
    
     
    def clue(self):
        """Return hints if user was unsuccessful at their attempt"""
        if self._correct_code[0] == self._input[0]:
            return "the first character is correct."
        if self._correct_code[1] == self._input[1]:
            return "the second character is correct."
        if self._correct_code[2] == self._input[2]:
            return "the third character is correct."
        return "None of the characters seem to be correct."

     
    def success(self):
        """return congratulatory message if user was successful"""
        return "You entered the correct code and opened the door."