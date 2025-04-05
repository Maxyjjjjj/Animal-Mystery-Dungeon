from main import *

obstacles = {
    "Tree": Obstacle(
        name="Tree",
        width=2,
        height=2,
        material=ObstacleMaterial.WOOD,
        is_water=False
    ),
    "Rock": Obstacle(
        name="Rock",
        width=1,
        height=1,
        material=ObstacleMaterial.STONE,
        is_water=False
    ),
    "Bush": Obstacle(
        name="Bush",
        width=1,
        height=1,
        material=ObstacleMaterial.GRASS,
        is_water=False
    ),
    "Stone Wall": Obstacle(
        name="Stone Wall",
        width=2,
        height=2,
        material=ObstacleMaterial.STONE,
        is_water=False
    ),
    "Wooden Fence": Obstacle(
        name="Wooden Wall",
        width=2,
        height=2,
        material=ObstacleMaterial.WOOD,
        is_water=False
    ),
    "Iron Fence": Obstacle(
        name="Iron Wall",
        width=2,
        height=2,
        material=ObstacleMaterial.METAL,
        is_water=False
    ),
    "Concrete Wall": Obstacle(
        name="Concrete Wall",
        width=2,
        height=2,
        material=ObstacleMaterial.CONCRETE,
        is_water=False
    ),
    "Net": Obstacle(
        name="Net",
        width=1,
        height=1,
        material=ObstacleMaterial.PLASTIC,
        is_water=False
    ),
    "Barbed Wire": Obstacle(
        name="Barbed Wire",
        width=1,
        height=1,
        material=ObstacleMaterial.METAL,
        is_water=False
    ),
    "Dead Tree": Obstacle(
        name="Dead Tree",
        width=2,
        height=2,
        material=ObstacleMaterial.WOOD,
        is_water=False
    ),
    "Cactus": Obstacle(
        name="Cactus",
        width=1,
        height=1,
        material=ObstacleMaterial.GRASS,
        is_water=False
    ),
    "Bamboo": Obstacle(
        name="Bamboo",
        width=1,
        height=1,
        material=ObstacleMaterial.GRASS,
        is_water=False
    ),
    "Bamboo Shoots": Obstacle(
        name="Bamboo Shoots",
        width=1,
        height=1,
        material=ObstacleMaterial.GRASS,
        is_water=False
    ),
    "Water": Obstacle(
        name="Water",
        width=1,
        height=1,
        material=ObstacleMaterial.WATER,
        is_water=True
    )
}