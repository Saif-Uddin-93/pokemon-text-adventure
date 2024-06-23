from src.trainer import Trainer
from src.pokemon_types import *
from src.battle import Battle
from src.created_pokemon import *

def test_flareon_created_properly():
    assert flareon.type == "Fire"

def test_single_trainer_created_properly():
    ash = Trainer('Ash')
    assert ash.name == "Ash"

def test_ash_trying_to_catch_a_flareon():
    ash = Trainer()
    ash.throw_pokeball(flareon)
    assert len(ash.belt) == 1
    assert ash.belt[0].pokemon == flareon

def test_ash_trying_to_catch_a_flareon_and_eevee():
    ash = Trainer()
    ash.throw_pokeball(flareon)
    ash.throw_pokeball(eevee)
    assert len(ash.belt) == 2
    assert ash.belt[1].pokemon == eevee

def test_ash_catching_6_pkmn_returns_full_belt():
    ash = Trainer()
    ash.throw_pokeball(flareon)
    ash.throw_pokeball(eevee)
    ash.throw_pokeball(leafon)
    ash.throw_pokeball(vaporeon)
    ash.throw_pokeball(charmander)
    ash.throw_pokeball(squirtle)
    assert ash.is_belt_full() == True
    assert ash.belt[0].pokemon == flareon
    assert ash.belt[1].pokemon == eevee
    bool = False
    for pokeball in ash.belt:
        if flareon == pokeball.pokemon:
            bool = True
    assert bool == True

def test_does_battle_produce_winner():
    battle1 = Battle(flareon, eevee)

    battle1()

    assert battle1.get_winner() == flareon

def test_pokemon_going_second_wins_the_battle():
    battle1 = Battle(flareon, vaporeon)
    battle1()
    winner = battle1.get_winner()
    battle1.restore_pokemon(flareon)
    battle1.restore_pokemon(vaporeon)
    assert winner == vaporeon

def test_pokemon_sounds():
    assert eevee.sound == 'Eev... Eevee!'
    assert flareon.sound == 'Fla... Flareon!'
    assert vaporeon.sound == 'Vap... Vaporeon!'
    assert leafon.sound == 'Lea... Leafeon!'
    assert charmander.sound == 'Cha... Charmander!'
    assert squirtle.sound == 'Squ... Squirtle!'
    assert bublasaur.sound == 'Bul... Bulbasaur!'