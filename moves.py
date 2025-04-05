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

class MoveEffectType(Enum):
    SLOW = auto()
    POISON = auto()
    FREEZE = auto()
    CONFUSE = auto()
    SLEEP = auto()
    BLIND = auto()
    STUN = auto()
    WHACKED = auto()
    DETECTED = auto()

class Move:
    def __init__(self, name, description, category, power, accuracy, pp, effect=None):
        self.name = name
        self.description = description
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.pp_used = 0
        self.effect = effect

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
    "pound": Move("Pound", "Hit a target with your knuckles", MoveCategory.PHYSICAL, 40, 100, 35),
    "bite": Move("Bite", "Bite a target", MoveCategory.PHYSICAL, 60, 100, 25),
    "pounce": Move("Pounce", "Pounce at a target", MoveCategory.PHYSICAL, 35, 95, 30),
    "leer": Move("Leer", "Leer at a target", MoveCategory.STATUS, 0, 100, 30),
    "snowball": Move("Snowball", "Throw a snowball at a target", MoveCategory.PHYSICAL, 20, 90, 30),
    "display": Move("Display", "Show off your fur, or feathers, whatever you have", MoveCategory.STATUS, 0, 100, 30),
    "roar": Move("Roar", "Roar at a target", MoveCategory.STATUS, 0, 100, 20),
    "howl": Move("Howl", "Howl to alert your teammates", MoveCategory.STATUS, 0, 100, 40),
    "claw_swipe": Move("Claw Swipe", "Swipe with your claws", MoveCategory.PHYSICAL, 40, 100, 35),
    "stomp": Move("Stomp", "Stomp on a target", MoveCategory.PHYSICAL, 65, 100, 20),
    "skydive": Move("Skydive", "Skydive to a target", MoveCategory.PHYSICAL, 80, 95, 15),
    "peck": Move("Peck", "Peck a target", MoveCategory.PHYSICAL, 35, 100, 35),
    "talon_strike": Move("Talon Strike", "Strike with your talons", MoveCategory.PHYSICAL, 70, 100, 20),
    "wing_attack": Move("Wing Attack", "Attack with your wings", MoveCategory.PHYSICAL, 60, 100, 35),
    "chomp": Move("Chomp", "Chomp on a target", MoveCategory.PHYSICAL, 80, 100, 15),
    "tear_down": Move("Tear Down", "Tear down a target", MoveCategory.PHYSICAL, 120, 100, 10),
    "flop_attack": Move("Flop Attack", "Flop at a target", MoveCategory.PHYSICAL, 65, 85, 20),
    "flop_around": Move("Flop Around", "Flop around", MoveCategory.STATUS, 0, 100, 20),
    "whirlwind": Move("Whirlwind", "Gust down a target", MoveCategory.PHYSICAL, 150, 100, 5),
    "hiss": Move("Hiss", "Hiss at a target", MoveCategory.STATUS, 0, 100, 40),
    "spit": Move("Spit", "Spit at a target", MoveCategory.PHYSICAL, 50, 100, 20),
    "nip": Move("Nip", "Nip a target", MoveCategory.PHYSICAL, 25, 100, 30),
    "claw_slash": Move("Claw Slash", "Slash with your claws", MoveCategory.PHYSICAL, 80, 100, 35),
    "tail_swipe": Move("Tail Swipe", "Swipe with your tail", MoveCategory.PHYSICAL, 40, 100, 35),
    "confuse_showoff": Move("Confuse Showoff", "Confuse a target", MoveCategory.SPECIAL, 10, 100, 20, MoveEffect(MoveEffectType.CONFUSE, 100, 2, 0.5)),
    "venomous_spit": Move("Venomous Spit", "Spit venom at a target", MoveCategory.PHYSICAL, 50, 100, 20, MoveEffect(MoveEffectType.POISON, 100, 2, 0.5)),
    "venomous_bite": Move("Venomous Bite", "Bite a target with venom", MoveCategory.PHYSICAL, 60, 100, 25, MoveEffect(MoveEffectType.POISON, 100, 2, 0.5)),
    "pierced_gaze": Move("Pierced Gaze", "Gaze at a target", MoveCategory.SPECIAL, 80, 100, 20, MoveEffect(MoveEffectType.STUN, 100, 2, 0.5)),
    "echolocation": Move("Echolocation", "Use echolocation to find a target", MoveCategory.SPECIAL, 0, 100, 20, MoveEffect(MoveEffectType.DETECTED, 100, 2, 0.5)),
}