from src.logger import logger
class Pokeballs:
    def __init__(self) -> None:
        self.pokemon = None
    
    def is_empty(self):
        return not (True and self.pokemon)
    
    def catch(self, pokemon):
        if self.is_empty():
            self.pokemon = pokemon
            print('Give a nickname to your Pokemon?: \n')
            pokemon.nickname = input() or None
        else:
            print("Pokeball already full")