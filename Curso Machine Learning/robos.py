import random

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

class Robo(Ponto):
    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento proibido')
    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento proibido')
    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Movimento proibido')
    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento proibido')

class Recompensa_Dano(Ponto):
    def __init__(self, x, y, name):
        super(Recompensa_Dano, self).__init__(x, y)
        self.name = name
    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y, self.name)

def check_Recompensa(robot, rewards, lista_rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('O robô achou a recompensa: %s' % reward.name)
            lista_rewards.append(reward)
            ok = True
    return ok

def check_Dano(robot, damages, lista_damages):
    ok = False
    for damage in damages:
        if damage.x == robot.x and damage.y == robot.y:
            print('O robô sofreu um dano: %s' % damage.name)
            lista_damages.append(damage)
            ok = True
    return ok

r1 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Energon')
r2 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Energon')
r3 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Energon')
r4 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Weapon')
r5 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Weapon')
r6 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Weapon')
r7 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Extension')
r8 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Extension')
r9 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Extension')
rewards = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

d1 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Loss of energy')
d2 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Loss of energy')
d3 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Loss of energy')
d4 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'No weapon')
d5 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'No weapon')
d6 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'No weapon')
d7 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Damaged body part')
d8 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Damaged body part')
d9 = Recompensa_Dano(random.randint(0, 10), random.randint(0, 10), 'Damaged body part')
damages = [d1, d2, d3, d4, d5, d6, d7, d8, d9]

robo_1 = Robo(random.randint(0, 10), random.randint(0, 10))
list_rewards = []
list_damages = []
terminou = True

while terminou:
    movimento = input('Digite w, s, a ou d para os movimentos: ')
    if movimento == 'w':
        robo_1.move_up()
    elif movimento == 's':
        robo_1.move_down()
    elif movimento == 'd':
        robo_1.move_right()
    elif movimento == 'a':
        robo_1.move_left()
    else:
        print('Movimento Invalido!')
        continue
    print(robo_1)
    check_Recompensa(robo_1, rewards, list_rewards)
    check_Dano(robo_1, damages, list_damages)
    if len(list_rewards) == len(rewards):
        terminou = False
        print('\n\nYou Win!!!\n\n')
    elif len(list_damages) == len(damages):
        terminou = False
        print('\nGame Over!!!\n\n')

print()
print('Robo: ', robo_1)
print('Recompensas')
for r in list_rewards:
    print(r)
print('Danos')
for d in list_damages:
    print(d)
print()
