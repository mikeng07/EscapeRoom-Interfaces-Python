import door
import random

class ComboDoor(door.Door):
    """represents a locked door."""

    def __init__(self):
        """set the initial state of the door"""
        

        self._correct_value = random.randint (1,10)
        self._input = 0 

    def examine_door(self):
        """Description of the door"""
        return "you encounter a door with a combination lock, you can spin the dial to a number 1-10."

     
    def menu_options(self):
        """Door menu"""
        return "Enter a number 1-10: "

     
    def get_menu_max(self):
        """number of items in the door's menu"""    
        return 10
        
     
    def attempt (self,option):
        """Use the input to determine whether user has unlocked the door. 
            Return what user attmpted."""
        self._input = option
        return "you turn the dial to... " + str(option)

     
    def is_unlocked(self):
        """return true if the door was unlocked"""
        return self._correct_value == self._input
    
     
    def clue(self):
        """Return hints if user was unsuccessful at their attempt"""
        if self._input < self._correct_value:
            return "try a higher value."
        else: 
            return "try a lower value."

     
    def success(self):
        """return congratulatory message if user was successful"""
        return "you round the correct value and opened the door. "