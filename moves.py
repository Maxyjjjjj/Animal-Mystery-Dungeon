from enum import Enum, auto
import random
from main import *
from animals import *

class MoveCategory(Enum):
    PHYSICAL = auto()  # Based on strength/damage
    SPECIAL = auto()   # Based on intelligence
    STATUS = auto()    # Effects without direct damage, such as threatening sounds, sleep, etc.
    
class MoveEffect:
    def __init__(self, effect_type, chance, duration, magnitude):
        self.effect_type = effect_type  # Slow, poison, etc.
        self.chance = chance  # Probability of triggering
        self.duration = duration  # How many turns it lasts
        self.magnitude = magnitude  # How strong the effect is

class Move:
    def __init__(self, name, description, category, power, accuracy, pp, effect=None, restricted_to=None):
        self.name = name
        self.description = description
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.pp_used = 0
        self.effect = effect
        self.restricted_to = restricted_to

    def use(self, user, target):
        """
        Use the move on the target
        """
        if self.pp_used >= self.pp:
            return False
            
        # Check if the move hits
        if random.random() > self.accuracy/100:
            print(f"{user.name} missed!")
            return False
            
        self.pp_used += 1
        return True
    
    def apply_effect(self, target):
        if self.effect:
            self.effect.apply(target)

    def is_usable(self):
        return self.pp_used < self.pp

    def reset_pp(self):
        self.pp_used = 0

moves = {
    "tackle": Move("Tackle", "Hit a target", MoveCategory.PHYSICAL, 35, 95, 35),
    "scratch": Move("Scratch", "Scratch a target", MoveCategory.PHYSICAL, 40, 100, 35),
    "growl": Move("Growl", "Growl loudly", MoveCategory.STATUS, 0, 100, 40),
    "tail_whip": Move("Tail Whip", "Whip a target with your tail", MoveCategory.STATUS, 0, 100, 30),
    "pound": Move("Pound", "Hit a target with your knuckles", MoveCategory.PHYSICAL, 40, 100, 35, restricted_to=lambda animal: animal.has_arms),
    "bite": Move("Bite", "Bite a target", MoveCategory.PHYSICAL, 60, 100, 25),
    "pounce": Move("Pounce", "Pounce at a target", MoveCategory.PHYSICAL, 35, 95, 30),
    "leer": Move("Leer", "Leer at a target", MoveCategory.STATUS, 0, 100, 30),
    "snowball": Move("Snowball", "Throw a snowball at a target", MoveCategory.PHYSICAL, 20, 90, 30, restricted_to=lambda animal: animal.has_arms),
    "display": Move("Display", "Show off your fur, or feathers, whatever you have", MoveCategory.STATUS, 0, 100, 30),
    "roar": Move("Roar", "Roar at a target", MoveCategory.STATUS, 0, 100, 20),
    "howl": Move("Howl", "Howl to alert your teammates", MoveCategory.STATUS, 0, 100, 40),
    "claw_swipe": Move("Claw Swipe", "Swipe with your claws", MoveCategory.PHYSICAL, 40, 100, 35),
    "stomp": Move("Stomp", "Stomp on a target", MoveCategory.PHYSICAL, 65, 100, 20, restricted_to=lambda animal: animal.weight.value >= Rank.S.value)
}