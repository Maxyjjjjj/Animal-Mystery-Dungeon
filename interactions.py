import pygame
from main import *
from animals import *
from obstacles import *

def eat_bamboo(animal, obstacle):
    
    if isinstance(animal, ("Giant Panda", "Red Panda")):
        if isinstance(obstacle, ("Bamboo", "Bamboo Shoots")):
            animal.health += 1
            obstacle.health -= 1
            if obstacle.health <= 0:
                obstacle.is_dead = True
    return False