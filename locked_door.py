import door
import random

class LockedDoor(door.Door):
    """represents a locked door."""

    def __init__(self):
        """set the initial state of the door"""
        # 1 = under mat, 2 = in flower pot, 3 = in porch light

        self._key_location = random.randint (1,3)
        self._input = 0 

    def examine_door(self):
        """Description of the door"""
        return "you encounter a locked door, you should look around to find the key"

     
    def menu_options(self):
        """Door menu"""
        return "1. Look under doormat\n2. Look in the flower pot\n3. Look in the porch light"

     
    def get_menu_max(self):
        """number of items in the door's menu"""    
        return 3
        
     
    def attempt (self,option):
        """Use the input to determine whether user has unlocked the door. 
            Return what user attmpted."""
        self._input = option
        if option == 1:
            return "you look under the doormat."
        elif option == 2:
            return "you look under the flower pot."
        else:
            return "you look in the porch light."


     
    def is_unlocked(self):
        """return true if the door was unlocked"""
        return self._key_location == self._input
    
     
    def clue(self):
        """Return hints if user was unsuccessful at their attempt"""
        return "try looking somewhere else."

     
    def success(self):
        """return congratulatory message if user was successful"""
        return "you found the key and opened the door "