
# Weapon Test Cases

from Weapon import *
from Materials import *
from Workshop import *

def test_calculateDamage():
    # test case 1
    weapon1 = Weapon("Weapon1", Wood(5), Wood(5))
    assert weapon1.calculateDamage() == 25.0

    # test case 2
    weapon2 = Weapon("Weapon2", Wood(10), Wood(10))
    assert weapon2.calculateDamage() == 100.0

    # test case 3
    weapon3 = Weapon("Weapon3", Wood(15), Wood(15))
    assert weapon3.calculateDamage() == 225.0


def test_attack():
    # test case 1
    weapon4 = Weapon("Weapon1", Wood(5), Wood(5))
    weapon4.calculateDamage()

    assert weapon4.attack() == "It deals 25 damage."