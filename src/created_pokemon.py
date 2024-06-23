from src.pokemon_types import *

pokemon_list = []

# def create_pokemon(type, name, nickname, hp, moves, dmg):
#     new_pokemon = None
#     match type.lower():
#         case 'normal':
#             new_pokemon = Normal_Pokemon(name, nickname, hp, moves, dmg)
#         case 'fire':
#             new_pokemon =  Fire_Pokemon(name, nickname, hp, moves, dmg)
#         case 'water':
#             new_pokemon =  Water_Pokemon(name, nickname, hp, moves, dmg)
#         case 'grass':
#             new_pokemon =  Grass_Pokemon(name, nickname, hp, moves, dmg)
#     #pokemon_list.append(new_pokemon)
#     return new_pokemon

#eevee = create_pokemon('normal', "Eevee", None, 55, ["Headbutt"], 18)
eevee = Normal_Pokemon("Eevee", None, 55, ["Headbutt"], 18)
pokemon_list.append(eevee)

flareon = Fire_Pokemon("Flareon", None, 65, ["Fire Blast"], 20)
pokemon_list.append(flareon)

vaporeon = Water_Pokemon("Vaporeon", None, 70, ["Hydro Pump"], 19)
pokemon_list.append(vaporeon)

leafon = Grass_Pokemon("Leafeon", None, 65, ["Giga Drain"], 17)
pokemon_list.append(leafon)

charmander = Fire_Pokemon("Charmander", None, 44, ["Flamethrower"], 17)
pokemon_list.append(charmander)

squirtle = Water_Pokemon("Squirtle", None, 44, ["Surf"], 16)
pokemon_list.append(squirtle)

bublasaur = Grass_Pokemon("Bulbasaur", None, 45, ["Razor Leaf"], 16)
pokemon_list.append(bublasaur)