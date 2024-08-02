from Human import Warrior
from Thing import Thing, Weapon

Harry = Warrior(10)
John = Warrior(5)

sword = Weapon(3,2,100, 'sword', 5)

Harry.pick_up(sword)

Harry.give_damage(John)






