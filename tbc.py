import random

class Character(object):
    def __init__(self, name = "Rogue",
                 hitPoints = 20,
                 hitChance = 70,
                 maxDamage = 20,
                 armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.name 
    
    @name.setter
    def name(self):
        self.name = "Rogue"
    
    @property
    def hitPoints(self):
        return self.hitPoints
    
    @hitPoints.setter
    def hitPoints(self):
        self.hitPoints = 20
    
    @property
    def hitChance(self):
        return self.hitChance
    
    @hitChance.setter
    def hitChance(self):
        self.hitChance = 70
    
    @property
    def maxDamage(self):
        return self.maxDamage
    
    @maxDamage.setter
    def maxDamage(self):
        self.maxDamage = 20
    
    @property
    def armor(self):
        return self.armor
    
    @armor.setter
    def armor(self):
        self.armor = 0
    
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
        return out
    
    def printStats(self):
        print(f""" {self.name}
        {self.hitPoints}
        {self.hitChance}
        {self.maxDamage}
        {self.armor} """)
    
    def hit(self, enemy):
        hitChance = random.randint(1, 100)
        if random.randint(1, 100) >= hitChance:
            hitDamage = random.randint(1, self.maxDamage)
            print(f"{self.name} hits {enemy.name} for {hitDamage} damage") 
            print(f" {enemy.name} hits {self.name} for {hitDamage} damage")
            print(f" {enemy.name}'s armor absorbs {enemy.aromor} damage")
            hitDamage -= enemy.armor 
            if hitDamage < 0:
                hitDamage = 0
        if enemy.armor > 0:
            enemy.hitPoints -= hitDamage
            print(f"{enemy.name}: {enemy.hitPoints}")
        else:
            hitDamage = 0
            print(f"{self.name} misses. {enemy.name} took no damage")
            
def fight(self, enemy):
    keepGoing = True
    while keepGoing:   
        if self.hitpoints > 0:
            self.fight(enemy)
        elif enemy.hitpoints > 0:
            enemy.fight(self)
        if self.hitpoints <= 0:
            print("You lose.")
        elif enemy.hitpoints <= 0:
            print("You have defeated {enemy.name}. You win")
            keepGoing = False
        
    