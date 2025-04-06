import pygame
import random
import numpy as np
import sys
from enum import Enum, auto
from personality_quiz import PersonalityQuiz

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

class Dungeon:
    def __init__(self, width, height):
        """
        Initialize the dungeon grid
        0 = floor
        1 = wall
        """
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.generate_dungeon()
    
    def generate_dungeon(self):
        """
        Simple dungeon generation algorithm
        Creates walls around the edges and some random walls
        """
        # Create walls around the edges
        for x in range(self.width):
            self.grid[0][x] = 1
            self.grid[self.height-1][x] = 1
        
        for y in range(self.height):
            self.grid[y][0] = 1
            self.grid[y][self.width-1] = 1
        
        # Add some random walls
        for _ in range(self.width * self.height // 10):
            x = random.randint(1, self.width-2)
            y = random.randint(1, self.height-2)
            self.grid[y][x] = 1

class DungeonRoom:
    def __init__(self, room_type, width, height):
        self.room_type = room_type  # "normal", "treasure", "boss", etc.
        self.width = width
        self.height = height
        self.obstacles = []
        self.enemies = []
        self.items = []
        self.doors = []
        
    def add_obstacle(self, obstacle, x, y):
        obstacle.x = x
        obstacle.y = y
        self.obstacles.append(obstacle)
        
    def add_enemy(self, enemy, x, y):
        enemy.x = x
        enemy.y = y
        self.enemies.append(enemy)

class DungeonGenerator:
    def __init__(self, difficulty, theme):
        self.difficulty = difficulty
        self.theme = theme  # "forest", "cave", "underwater", etc.
        
    def generate_dungeon(self, num_rooms):
        rooms = []
        # Generate rooms based on difficulty and theme
        # Connect rooms with doors/passages
        return rooms

def generate_procedural_dungeon(width, height, complexity=0.75, density=0.5):
    """Generate a random dungeon with rooms and corridors"""
    # Initialize with walls
    grid = np.ones((height, width), dtype=int)
    
    # Make a grid with random walls
    for i in range(int(complexity * 5000)):
        x = random.randint(1, width-2)
        y = random.randint(1, height-2)
        grid[y][x] = 0
        
        # Connect with nearby open spaces
        for _ in range(int(density * 4)):
            nx, ny = x + random.randint(-1, 1), y + random.randint(-1, 1)
            if 0 < nx < width-1 and 0 < ny < height-1:
                grid[ny][nx] = 0
                
    return grid

class CombatSystem:
    def __init__(self):
        self.turn_order = []
    
    def calculate_damage(self, attacker, defender, move):
        """Calculate damage based on stats and move type"""
        base_damage = move.power
        attack_stat = attacker.damage.value
        defense_stat = defender.size.value
        
        damage = base_damage * attack_stat / defense_stat
        return max(1, int(damage))
    
    def execute_turn(self, animals):
        """Execute a single turn of combat for all animals"""
        # Sort by speed using the Rank enum value
        self.turn_order = sorted(animals, key=lambda x: x.speed.value, reverse=True)
        
        for animal in self.turn_order:
            if animal.is_player:
                # Player chooses action
                return "player_turn"
            else:
                # AI chooses action
                self.execute_ai_turn(animal)
    def execute_ai_turn(self, animal):
        # AI chooses action based on its AI behavior
        pass
    def execute_player_turn(self, player):
        # Player chooses action
        pass
    
class AnimalTeam:
    def __init__(self, leader):
        self.leader = leader  # Player's character
        self.members = [leader]
        self.max_size = 4
    
    def add_member(self, animal):
        if len(self.members) < self.max_size:
            self.members.append(animal)
            return True
        return False
    
    def remove_member(self, animal):
        if animal != self.leader and animal in self.members:
            self.members.remove(animal)
            return True
        return False

class ExperienceSystem:
    def __init__(self):
        self.level_thresholds = [0, 100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500]  # Example thresholds
    
    def gain_experience(self, animal, amount):
        """Add experience to an animal and handle level ups"""
        animal.experience += amount
        
        # Check for level up
        if animal.level < len(self.level_thresholds) - 1:
            if animal.experience >= self.level_thresholds[animal.level + 1]:
                self.level_up(animal)
    
    def level_up(self, animal):
        """Handle level up logic"""
        animal.level += 1
        
        # Increase stats
        animal.max_health += random.randint(3, 7)
        animal.attack += random.randint(1, 3)
        animal.defense += random.randint(1, 3)
        animal.speed += random.randint(1, 2)
        
        # Learn new moves
        self.check_new_moves(animal)

class Move:
    def __init__(self, name, type, power, accuracy, pp):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.pp_used = 0

    def use(self):
        """Reduce PP and return True if move is still usable"""
        self.pp_used += 1
        return self.pp_used < self.pp
    
    def reset_pp(self):
        """Reset PP used"""
        self.pp_used = 0
    
    def is_usable(self):
        """Check if move is still usable"""
        return self.pp_used < self.pp

class TerrainType(Enum):
    FLOOR = 0
    WALL = 1
    WATER = 2
    LAVA = 3
    MUD = 4
    ICE = 5
    GRASS = 6

class Terrain:
    def __init__(self, type, movement_cost, damage=0):
        self.type = type
        self.movement_cost = movement_cost
        self.damage = damage  # Damage per turn if standing on this terrain



class Diet(Enum):
    CARNIVORE = auto()
    HERBIVORE = auto()
    OMNIVORE = auto()
    SPECIALIST = auto()

class SpecialistType(Enum):
    MOLLUSKIVORE = auto()
    INSECTIVORE = auto()
    NECTARIVORE = auto()
    DETRITIVORE = auto()

class Rank(Enum):
    F = 1
    E = 2
    D = 3
    C = 4
    B = 5
    A = 6
    S = 7

class Size(Enum):
    XXS = 1
    XS = 2
    S = 3
    M = 4
    L = 5
    XL = 6
    XXL = 7

class Locomotion(Enum):
    TERRESTRIAL = auto()
    SEMIAQUATIC = auto()
    AQUATIC = auto()

class Animal:
    def __init__(self, name, species, diet, intelligence, size, 
                 has_wings, speed, damage, weight, has_arms, locomotion):
        """
        Initialize an animal with comprehensive stats
        """
        self.name = name
        self.species = species
        self.diet = diet
        self.intelligence = intelligence
        self.size = size
        self.has_wings = has_wings
        self.speed = speed
        self.damage = damage
        self.weight = weight
        self.has_arms = has_arms
        self.locomotion = locomotion

        # Position and health
        self.x = 0
        self.y = 0
        self.health = 100
        self.max_health = 100

        # Derive base stats from attributes
        self.calculate_derived_stats()

    def calculate_derived_stats(self):
        """
        Calculate additional stats based on animal's attributes
        """
        # Example stat calculation logic
        base_speed_multiplier = {
            Rank.F: 0.5, Rank.E: 0.7, Rank.D: 0.9, 
            Rank.C: 1.0, Rank.B: 1.2, Rank.A: 1.5, Rank.S: 2.0
        }
        
        # Speed bonus for wings
        wing_multiplier = 1.2 if self.has_wings else 1.0
        
        # Size impact on speed and health
        size_speed_factor = {
            Size.XXS: 1.3, Size.XS: 1.2, Size.S: 1.1, 
            Size.M: 1.0, Size.L: 0.9, Size.XL: 0.8, Size.XXL: 0.7
        }

        # Recalculate max health and speed based on attributes
        self.max_health = 100 * (self.size.value / Size.M.value)
        self.health = self.max_health
        
        self.base_speed = base_speed_multiplier[self.speed] * \
                          wing_multiplier * \
                          size_speed_factor[self.size]

    def move(self, dx, dy, dungeon):
        """
        Move the animal, checking for wall collisions
        Incorporate speed into movement
        """
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check if the new position is within the dungeon and not a wall
        if (0 <= new_x < dungeon.width and 
            0 <= new_y < dungeon.height and 
            dungeon.grid[new_y][new_x] == 0):
            self.x = new_x
            self.y = new_y
    
    def move_in_water(self, dx, dy, dungeon):
        """
        Move the animal in water, checking for water collisions
        Incorporate speed into movement
        """
        new_x = self.x + dx
        new_y = self.y + dy

        # Get water speed multiplier based on locomotion type
        water_multiplier = WaterMoveSpeed[self.locomotion].value

        # Check if animal can move in water based on locomotion
        confined_to_water = ConfinedToWater[self.locomotion].value

        # Check if the new position is within the dungeon and valid for movement
        if (0 <= new_x < dungeon.width and
            0 <= new_y < dungeon.height):
            
            # Get tile type
            tile = dungeon.grid[new_y][new_x]
            
            # If tile is water (0) and animal can move in water
            if tile == 0 and not confined_to_water:
                # Apply water movement speed modifier
                actual_dx = dx * water_multiplier * self.base_speed
                actual_dy = dy * water_multiplier * self.base_speed

                # Update position
                self.x += actual_dx
                self.y += actual_dy
                
                self.x = new_x
                self.y = new_y
def create_predefined_animals():
    from animals import animals
    return animals

class ObstacleMaterial(Enum):
    GRASS = 0.5
    WOOD = 1.0
    PLASTIC = 1.5
    STONE = 2.0
    METAL = 2.5
    CONCRETE = 3.0

class WaterMoveSpeed(Enum):
    """
    Water-specific speed multipliers for different locomotion types
    """
    # Water-specific multipliers
    TERRESTRIAL = 0.5  # Slower in water for terrestrial animals
    SEMIAQUATIC = 1.0  # Average speed in water for semiaquatic animals
    AQUATIC = 1.5      # Faster in water for aquatic animals

class ConfinedToWater(Enum):
    """
    Water-specific behavior for animals
    """
    # Water-specific behavior
    TERRESTRIAL = False  # Can move on land, yet is slower in water
    SEMIAQUATIC = False   # Can move in water and land with the same speed
    AQUATIC = True        # Can move in water only, not on land

class Obstacle:
    def __init__(self, name, width, height):
        """
        Initialize an obstacle with a bounding box
        """
        self.name = name
        self.width = width
        self.height = height
        self.material = ObstacleMaterial[name.upper()]
        self.hardness = self.material.value
        self.is_water = False

def create_obstacles():
    from obstacles import obstacles
    return obstacles

class WeatherSystem:
    def __init__(self):
        self.current_weather = "clear"
        self.weather_effects = {
            "clear": {},
            "rain": {"water_multiplier": 1.2, "visibility": 0.8},
            "fog": {"visibility": 0.5},
            "snow": {"movement_speed": 0.8}
        }
        
    def change_weather(self, new_weather):
        if new_weather in self.weather_effects:
            self.current_weather = new_weather
            
    def apply_effects(self, game_world):
        effects = self.weather_effects.get(self.current_weather, {})
        # Apply water multiplier
        if "water_multiplier" in effects:
            game_world.water_multiplier = effects["water_multiplier"]

        # Apply visibility
        if "visibility" in effects:
            game_world.visibility = effects["visibility"]
        # Apply movement speed
        if "movement_speed" in effects:
            game_world.movement_speed = effects["movement_speed"]
        

class Game:
    def __init__(self):
        """
        Initialize the game
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Animal Mystery Dungeon")
        
        self.clock = pygame.time.Clock()
        
        # Initialize personality quiz
        self.quiz = PersonalityQuiz()
        
        # Create dungeon
        self.dungeon = Dungeon(25, 20)
        
        # Create predefined animals
        self.animals = create_predefined_animals()
        
        # Create player based on personality quiz
        self.player = None
        self.start_personality_quiz()
        
        # Set player position
        player_start = self.find_empty_tile()
        self.player.x = player_start[0]
        self.player.y = player_start[1]
    
    def start_personality_quiz(self):
        """
        Run the personality quiz to determine player's animal
        """
        traits = {}
        for question in self.quiz.questions:
            # For now, randomly select answers for testing
            answer = random.choice(list(question["answers"].keys()))
            selected = question["answers"][answer]
            for trait, value in selected["traits"].items():
                traits[trait] = traits.get(trait, 0) + value
        
        # Find dominant trait
        dominant_trait = max(traits.items(), key=lambda x: x[1])[0]
        
        # Select random animal from matching animals for dominant trait
        if dominant_trait in self.quiz.trait_to_animal_mapping:
            animal_species = random.choice(self.quiz.trait_to_animal_mapping[dominant_trait])
            self.player = self.animals[animal_species]
    
    def find_empty_tile(self):
        """
        Find a random empty tile in the dungeon
        """
        while True:
            x = random.randint(0, self.dungeon.width-1)
            y = random.randint(0, self.dungeon.height-1)
            if self.dungeon.grid[y][x] == 0:
                return (x, y)
    
    def draw(self):
        """
        Draw the game state
        """
        self.screen.fill(WHITE)
        
        # Draw dungeon tiles
        for y in range(self.dungeon.height):
            for x in range(self.dungeon.width):
                rect = pygame.Rect(
                    x * TILE_SIZE, 
                    y * TILE_SIZE, 
                    TILE_SIZE, 
                    TILE_SIZE
                )
                if self.dungeon.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, GRAY, rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect, 1)
        
        # Draw player
        player_rect = pygame.Rect(
            self.player.x * TILE_SIZE, 
            self.player.y * TILE_SIZE, 
            TILE_SIZE, 
            TILE_SIZE
        )
        pygame.draw.rect(self.screen, BLACK, player_rect)
        
        pygame.display.flip()
    
    def handle_events(self):
        """
        Handle game events and input
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move(0, -1, self.dungeon)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 1, self.dungeon)
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1, 0, self.dungeon)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1, 0, self.dungeon)
        
        return True
    
    def run(self):
        """
        Main game loop
        """
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()