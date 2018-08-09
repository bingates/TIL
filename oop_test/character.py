from abc import ABCMeta, abstractmethod

# 모든 자식 클래스가 상속 받을 추상 클래스
class Character():

    def __init__(self, name, hp, power):
        self.name=name
        self.hp=hp
        self.power=power

    #추상메서드->자식클래스재정의
    @abstractmethod
    def attack(self, other, attackkind):
        pass

    @abstractmethod
    def get_damage(self, power, attackkind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.hp)

# 둘다 정의 하지 않으면 자식클래스도 추상 클래스가 됨
class Player(Character):
    def __init__(self, name="player", hp=100, power=30, *skills):
        super().__init__(name, hp, power)
        self.skills=[]
        for skill in skills:
            self.skills.append(skill)

    def attack(self, enemy, attackkind):
        """
        만약 attackkind가 skills에 있다면 enemy 공격
        message passing 으로 구현
        """
        if attackkind in self.skills:
            enemy.get_damage(self.power, attackkind)

    def get_damage(self, power, attackkind):
        """
        attackkind가 skills 목록에 있으면 power//2
        아니면 그대로 hp-=power
        """
        if attackkind in self.skills:
            self.hp-=(power//2)
        else:
            self.hp-=power

"""
attack -> 만약 attackkind 가 self.attackkind 와 같으면 공격 아니면 공격 X
get_damage -> 만약 'ICE' 공격을 받았는데 내 self.attackkind='ICE' -> 오히려 체력이 늘어납니다.
            -> 그게 아니면 self.hp-=power
"""

class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attackkind=None

    def attack(self, other, attackkind):
        if attackkind == self.attackkind:
            other.get_damage(self.power, attackkind)
        
    def get_damage(self, power, attackkind):
        if attackkind==self.attackkind:
            self.hp+=power
        else:
            self.hp-=power
    
    #access function
    def get_attackkind(self):
        return self.attackkind

class IceMonster(Monster):
    def __init__(self, name="Ice Monster", hp=100, power=10):
        super().__init__(name, hp, power)
        self.attackkind='ICE'

class FireMonster(Monster):
    def __init__(self, name="Fire Monster", hp=100, power=20):
        super().__init__(name, hp, power)
        self.attackkind='FIRE'

if __name__=="__main__":
    
    player=Player("sword master", 100, 40, "ICE")
    print(player)

    monsters=[]
    monsters.append(IceMonster())
    monsters.append(FireMonster())

    for monster in monsters:
        print(monster)

    print('======== player attacks monsters ==========')

    for monster in monsters:
        player.attack(monster, "ICE")

    for monster in monsters:
        print(monster)

    print('======== monsters attacks player ==========')

    for monster in monsters:
        monster.attack(player, monster.get_attackkind())

    print(player)