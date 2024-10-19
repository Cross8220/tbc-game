import tbc

def main():
    if __name__ == "__main__":
        rogue = tbc.Character
        rogue.name = "Rogue"
        rogue.hitPoints = 20
        rogue.hitChance = 70
        rogue.maxDamage = 20
        rogue.armor = 0
    
        knight = tbc.Character("Knight", 50, 30, 10, 10)
    
        rogue.printStats(rogue)
        knight.printStats(knight)
    
        tbc.fight(rogue, knight)  
    main()
        