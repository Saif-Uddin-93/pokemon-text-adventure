from src.pokemon import Pokemon

class Fire_Pokemon(Pokemon):
    def __init__(self, name, nickname, hit_points, move, damage):
        super().__init__(name, nickname, hit_points, move, damage, "Fire", "Grass", "Water")

class Normal_Pokemon(Pokemon):
    def __init__(self, name, nickname, hit_points, move, damage):
        super().__init__(name, nickname, hit_points, move, damage, "Normal", "None", "Fighting")

class Water_Pokemon(Pokemon):
    def __init__(self, name, nickname, hit_points, move, damage):
        super().__init__(name, nickname, hit_points, move, damage, "Water", "Fire", "Grass")

class Grass_Pokemon(Pokemon):
    def __init__(self, name, nickname, hit_points, move, damage):
        super().__init__(name, nickname, hit_points, move, damage, "Grass", "Water", "Fire")
