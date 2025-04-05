import numpy as np
import random

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