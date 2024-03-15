import door
import random

class DeadboltDoor(door.Door):
    """represents a locked door with 2 deadbolts."""

    def __init__(self):
        """set the initial state of the door"""
        # 0 = locked, 1 = unlocked
        self._bolt1 = random.randint(0,1)
        self._bolt2 = random.randint(0,1) 

    def examine_door(self):
        """Description of the door"""
        return "you encounter a boulde deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them where they're locked or unlocked"

     
    def menu_options(self):
        """Door menu"""
        return "1. Toggle Bolt1\n2. Toggle Bolt 2"

     
    def get_menu_max(self):
        """number of items in the door's menu"""    
        return 2
        
     
    def attempt (self,option):
        """Use the input to determine whether user has unlocked the door. 
            Return what user attmpted."""
        if option == 1:
            if self._bolt1 == 1:
                self._bolt1 = 0
            else:
                self._bolt1 = 1
            return "you toggle the first bolt."
        else:
            if self._bolt2 == 1:
                self._bolt2 = 0
            else:
                self._bolt2 =1 
            return "you toggle the second bolt."


     
    def is_unlocked(self):
        """return true if the door was unlocked"""
        return self._bolt1 == 1 and self._bolt2 == 1
    
     
    def clue(self):
        """Return hints if user was unsuccessful at their attempt"""
        if self._bolt1 == 1 or self._bolt2 == 1:
            return "you jiggle the door... it seems like one of the bolts is unlocked"
        else:
            return "you jiggle the door... it's completely locked. "

     
    def success(self):
        """return congratulatory message if user was successful"""
        return "you unlocked both deadbolts and opened the door"