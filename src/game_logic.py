from src.trainer import Trainer
from src.created_pokemon import pokemon_list
from src.battle import Battle
from src.logger import logger
from pprint import pprint
from copy import deepcopy

trainers_list = []
logger = []
current_player1 = None
current_player2 = None

def create_trainer():
    new_trainer = Trainer()
    return new_trainer

def choose_starter(trainer):
    text_output = f'Choose a starter Pokemon!\n{trainer.name} can choose from:\n'
    print(text_output)
    logger.append(text_output)
    for pokemon in pokemon_list:
        print(pokemon.name)
        logger.append(pokemon.name)
    print('')
    chosen_pokemon = input()
    pokemon_exists = False
    while not pokemon_exists:
        for pokemon in pokemon_list:
            if pokemon.name.lower() == chosen_pokemon.lower():
                pokemon_exists = True
                return deepcopy(pokemon)
        if not pokemon_exists:
            print('This pokemon does not exist!\nPlease pick again:\n')
            logger.append('This pokemon does not exist! Please pick again:')
            chosen_pokemon = input()

def start_battle_text():
    current_player1.active_pokeball = current_player1.belt.pop(0)
    current_player2.active_pokeball = current_player2.belt.pop(0)
    player1_pokemon_name = current_player1.active_pokeball.pokemon._name
    player2_pokemon_name = current_player2.active_pokeball.pokemon._name
    print(f"Battle started between {current_player1.name} and {current_player2.name}.\n{current_player1.name} sends out {player1_pokemon_name}.\n{current_player2.name} sends out {player2_pokemon_name}\n")
    logger.append(f"Battle started between {current_player1.name} and {current_player2.name}. {current_player1.name} sends out {player1_pokemon_name}. {current_player2.name} sends out {player2_pokemon_name}\n")

def game_loop():
    number_of_trainers = 2
    number_of_pokemon_each = 2
    for _ in range(number_of_trainers):
        trainers_list.append(create_trainer())
        logger.append('Enter Trainer name: ')
        logger.append(trainers_list[_].name)
    for trainer in trainers_list:
        for _ in range(number_of_pokemon_each):
            trainer.throw_pokeball(choose_starter(trainer))
    global current_player1
    global current_player2
    current_player1 = trainers_list[0]
    current_player2 = trainers_list[1]
    start_battle_text()
    battle = Battle(current_player1, current_player2)

    while not battle.get_winner():
        if battle.turns % 2 == 0:
            battle.take_turn(current_player1, current_player2)
        else:
            battle.take_turn(current_player2, current_player1)

game_loop()

# pprint(logger)
