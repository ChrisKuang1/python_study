import random
#对话式攻击小游戏
class Creature():
    def __init__(self, hp):
        self.hp = hp

    def attack(self):
        attack_value = random.randint(0, 50)
        return attack_value

    def be_attack(self, attack_value):
        self.hp = self.hp - attack_value

    def not_dead(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def get_hp(self):
        hp_str = None
        if self.hp <= 0:
            hp_str = 'dead'
        elif self.hp < 20:
            hp_str = '▄'
        elif self.hp < 40:
            hp_str = '▄ ▄'
        elif self.hp < 60:
            hp_str = '▄ ▄ ▄'
        elif self.hp < 80:
            hp_str = '▄ ▄ ▄ ▄'
        else:
            hp_str = '▄ ▄ ▄ ▄ ▄'

        return hp_str

player = Creature(100)
enermy1 = Creature(80)
enermy2 = Creature(100)

while player.not_dead() and (enermy1.not_dead() or enermy2.not_dead()):
    print('player\'s hp is {}, enermy1\'s hp is {}, enermy2\'s is {}'
        .format(player.get_hp(), enermy1.get_hp(), enermy2.get_hp()))

    user_input = input('Attack or Defence(A/D):')

    while user_input != 'A' and user_input != 'D':
        user_input = input("Invalid input, please try again(A/D):")

    if user_input == 'A':
        pav = player.attack()

        if enermy1.not_dead() and enermy2.not_dead():
            attack_type = input('What types of attack(S/A):')

            while attack_type != 'S' and attack_type != 'A':
                attack_type = input("Invalid input, please try again(S/A):")

            eav1 = enermy1.attack()
            eav2 = enermy2.attack()

            if attack_type == 'A':
                enermy1.be_attack(pav * 0.9)
                enermy2.be_attack(pav * 0.9)
            else:
                attack_target = input('Who do you want to attack(1/2):')

                while attack_target != '1' and attack_target != '2':
                    attack_target = input("Invalid input, please try again(1/2):")

                if attack_target == '1':
                    enermy1.be_attack(pav)
                else:
                    enermy2.be_attack(pav)

            player.be_attack(eav1 * 0.5)
            player.be_attack(eav2 * 0.6)
        else:
            if enermy1.not_dead():
                eav = enermy1.attack() * 0.4
                enermy1.be_attack(pav)
            else:
                eav = enermy2.attack() * 0.6
                enermy2.be_attack(pav)
            
            player.be_attack(eav)
    else:
        if enermy1.not_dead() and enermy2.not_dead():
            eav1 = enermy1.attack() * 0.1
            eav2 = enermy2.attack() * 0.1

            player.be_attack(eav1)
            player.be_attack(eav2)
        else:
            if enermy1.not_dead():
                eav = enermy1.attack() * 0.1
            else:
                eav = enermy2.attack() * 0.1
            
            player.be_attack(eav)

if player.not_dead():
    print('You win!')
else:
    print('Game over!')
