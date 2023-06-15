
# Test the Workshop class


from Workshop import *
from Enchanter import *
from Forge import *

# create a workshop object
workshop = Workshop(Enchanter(), Forge("Sword", "Iron", "Fire"))

def test_addWeapon():
    '''
    This method tests the addWeapon method in the Workshop class.
    '''
    # create a weapon object
    weapon = "Sword"
    # add the weapon to the workshop
    workshop.addWeapon(weapon)
    # check if the weapon was added to the workshop
    assert weapon in workshop._weapons


