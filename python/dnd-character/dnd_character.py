import random

class Character:
    def __init__(self):
        """ Initial abilities need to be calculated only once, not every time
            we access the ability attribute
        """
        self._initial_abilities = self.init_abilities()
        self.strength = self._initial_abilities['strength']
        self.dexterity = self._initial_abilities['dexterity']
        self.constitution = self._initial_abilities['constitution']
        self.intelligence = self._initial_abilities['intelligence']
        self.wisdom = self._initial_abilities['wisdom']
        self.charisma = self._initial_abilities['charisma']
        self._initial_hitpoints = self.init_hitpoints()
        self.hitpoints = self._initial_hitpoints


    def init_abilities(self):
        strength = self.get_ability_score()
        dexterity = self.get_ability_score()
        constitution = self.get_ability_score()
        intelligence = self.get_ability_score()
        wisdom = self.get_ability_score()
        charisma = self.get_ability_score()
        abilities = {'strength': strength, 'dexterity': dexterity, 'constitution': constitution,
                     'intelligence': intelligence, 'wisdom': wisdom, 'charisma': charisma,
                    }
        return abilities


    def get_ability_score(self):
        dice_result = self.roll_dice()
        score = sum(dice_result) - min(dice_result)
        return score


    def roll_dice(self):
        four_dice = [random.randrange(1,7) for i in range(4)]
        return four_dice


    def init_hitpoints(self):
        return 10 + modifier(self.constitution)


    def ability(self):
        """ Returns a random ability score
        """
        ability_map = {
            0: self.strength,
            1: self.dexterity,
            2: self.constitution,
            3: self.intelligence,
            4: self.wisdom,
            5: self.charisma
        }
        return (ability_map[random.randrange(0,6)])


def modifier(score):
    return (score - 10) // 2