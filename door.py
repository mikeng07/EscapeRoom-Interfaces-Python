import abc
class Door(abc.ABC):
    """represents a door"""

    @abc.abstractmethod
    def examine_door(self):
        """Description of the door"""
        pass

    @abc.abstractmethod
    def menu_options(self):
        """Door menu"""
        pass

    @abc.abstractmethod
    def get_menu_max(self):
        """number of items in the door's menu"""
        pass
        
    @abc.abstractmethod
    def attempt (self,option):
        """Use the input to determine whether user has unlocked the door. 
            Return what user attmpted."""
        pass

    @abc.abstractmethod
    def is_unlocked(self):
        """return true if the door was unlocked"""
        pass
    
    @abc.abstractmethod
    def clue(self):
        """Return hints if user was unsuccessful at their attempt"""
        pass

    @abc.abstractmethod
    def success(self):
        """return congratulatory message if user was successful"""
        pass