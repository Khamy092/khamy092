
'''
File: Crafter.py
Description: This class acts as a superclass for the Forge and Enchanter classes. It contains the the craft and diassemble methods that
are used in both the subclasses.
Author: Taqi Khaliqdad
StudentID: 110341761
EmailID: khamy092
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod

class Crafter(ABC):

    ''' 
    Crafter is a superclass for the Forge and Enchanter classes. It contains the craft and
    disassemble methods that are used in both the subclasses. This class is an abstract class and cannot be instantiated.'''

    def __init__(self) -> None:
        pass

    # abstract methods
    @abstractmethod
    def craft(self):
        pass
    
    @abstractmethod
    def disassemble(self):
        pass