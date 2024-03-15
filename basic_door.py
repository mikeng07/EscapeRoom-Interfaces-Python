import door
import random

class BasicDoor(door.Door):
    """Represents a door that you push or pull"""

    def __init__(self):
        """Randomizes initial state of the door"""
        self._state = random.randint(0,1)
        self._input = 0 

     
    def examine_door(self):
        """Description of the door"""
        return "You encounter a basic door, you can either push or pull it to open"

     
    def menu_options(self):
        """Door menu"""
        return "1. Push\n2. Pull"

     
    def get_menu_max(self):
        """number of items in the door's menu"""
        return 2
        
     
    def attempt (self,option):
        """Use the input to determine whether user has unlocked the door. 
            Return what user attmpted."""
        if option == 1:
            # user push the door
            self._input = 1
            return "you push the door. "
        else:
            self._input = 0
            return "you pull the door. "


     
    def is_unlocked(self):
        """return true if the door was unlocked"""
        return self._state == self._input
    
     
    def clue(self):
        """Return hints if user was unsuccessful at their attempt"""
        return "Try the other option"

     
    def success(self):
        """return congratulatory message if user was successful"""
        return "Congratulations, you opened the door."