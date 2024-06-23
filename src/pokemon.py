class Pokemon:
    def __init__(self, name, nickname, hit_points, move, damage, type, strength, weakness):
        self.name = name
        self.nickname = nickname
        self._name = self.nickname or self.name
        self.type = type
        self.hit_points = hit_points
        self.full_hp = hit_points
        self.move = move
        self.damage = damage
        self.effective_damage = damage
        self.strength = strength
        self.weakness = weakness
        self.sound = f'{self.name[:3]}... {self.name}!'

    def get_multiplier(self, pokemon):
        if pokemon.type == self.strength:
            self.effective_damage = self.damage * 1.5
        if pokemon.type == self.weakness:
            self.effective_damage = self.damage * 0.5

    def use_move(self):
        #print(f"{self.name} used {self.move[0]}\n")
        return f"{self.name} used {self.move[0]}\n"
    
    def take_damage(self, dmg):
        self.hit_points -= dmg

    def has_fainted(self):
        return self.hit_points <= 0


