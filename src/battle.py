from typing import Any
from src.pokemon_types import *
from src.logger import logger
import inquirer

class Battle:
    def __init__(self, trainer_1, trainer_2) -> None:
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
        self.pokemon_1 = trainer_1.active_pokeball.pokemon
        self.pokemon_2 = trainer_2.active_pokeball.pokemon
        self.turns = 0
        self.battle_log = []

    def restore_pokemon(self, pokemon):
        pokemon.hit_points = pokemon.full_hp

    def get_winner(self):
        if not self.pokemon_1.has_fainted() and not self.pokemon_2.has_fainted():
            return None
        winner = self.pokemon_1 if self.pokemon_2.has_fainted() else self.pokemon_2
        loser = self.pokemon_1 if self.pokemon_1.has_fainted() else self.pokemon_2
        text_output = f'{loser.name} has fainted, {winner.name} has won the battle!!'
        self.battle_log.append(text_output)
        logger.append(text_output)
        print(self.battle_log[-1])
        return winner
    
    def attack(self, p_1, p_2):
        text_output = p_1.use_move()
        print(text_output)
        self.battle_log.append(text_output)
        logger.append(text_output)
        p_1.get_multiplier(p_2)
        p_2.take_damage(p_1.effective_damage)
        text_output = f'{p_2.nickname or p_2.name} took {p_1.effective_damage} damage. {p_2.name} has {p_2.hit_points} HP.\n'
        self.battle_log.append(text_output)
        logger.append(text_output)
        self.turns += 1 
        print(text_output)

    def switch_pokemon(self, trainer, active_pokeball):
        pokemon_to_switch = None
        pokemon_exists = False
        print('')
        for pokeball in trainer.belt:
            print(pokeball.pokemon.name)
            logger.append(pokeball.pokemon.name)
        print('')
        choose_pokemon = lambda : input()
        chosen_pokemon = choose_pokemon()
        print(f'\nchosen_pokemon is {chosen_pokemon}')
        for pokeball in trainer.belt:
            if pokeball.pokemon.name.lower() == chosen_pokemon.lower():
                pokemon_exists = True
                print('Pokemon exists: ', pokemon_exists)
                pokemon_to_switch = pokeball

        if pokemon_exists == False:
            text_output = 'this pokemon does not exist!\nplease pick again:\n'
            print(text_output)
            logger.append(text_output)
            return self.switch_pokemon(trainer, active_pokeball)
        print(f"\n{active_pokeball.pokemon.name}, that's enough! have some rest!\n")
        print(f'{pokemon_to_switch.pokemon.name} is joining the battle\n')
        trainer.belt.append(active_pokeball)
        trainer.belt.remove(pokemon_to_switch)
        trainer.active_pokeball = pokemon_to_switch
        self.turns += 1 
            
    def take_turn(self, trainer1, trainer2):
        p_1 = trainer1.active_pokeball.pokemon
        p_2 = trainer2.active_pokeball.pokemon
        active_pokeball = trainer1.active_pokeball

        text_output = f"{trainer1.name}, enter 'attack' to use {p_1.move[0]} or 'switch' to switch {p_1.name} with another Pokemon from your party\n"
        print(text_output)
        logger.append(text_output)
        turn_action = input()                
        if turn_action.lower() == "attack":
            self.attack(p_1, p_2)
        elif turn_action.lower() == "switch":
            self.switch_pokemon(trainer1, active_pokeball)

    def __str__(self) -> str:
        return self.battle_log
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.take_turn(self.pokemon_1, self.pokemon_2, self.trainer_1, self.pokemon_1)
        return self.battle_log

# flareon = Fire_Pokemon("Flareon", None, 65, ["Fire Blast"], 20)
# eevee = Normal_Pokemon("Eevee", None, 55, ["Headbutt"], 18)
# battle1 = Battle(flareon, eevee)

# print(battle1())