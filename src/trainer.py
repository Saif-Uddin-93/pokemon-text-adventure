from src.pokeballs import Pokeballs

class Trainer:
    def __init__(self, name=None) -> None:
        print('\nEnter Trainer name: ')
        self.name = name or input()
        self.__belt_lmit = 6
        self.belt = []
        self.active_pokeball = None

    @property
    def belt_limit(self) ->int:
        return self.__belt_lmit
    
    def is_belt_full(self):
        return len(self.belt) == self.belt_limit
    
    def throw_pokeball(self, pokemon):
        if not self.is_belt_full():
            pokeball = Pokeballs()
            pokeball.catch(pokemon)
            self.belt.append(pokeball)
        else:
            print('Out of pokeballs!!\n')
        
