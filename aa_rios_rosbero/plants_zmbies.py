class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        if zombie.health > 0:
            zombie.health -= self.damage
            print(self.name, "has attacked", zombie.name, "and", zombie.name, "now has", zombie.health, "health")
        else:
            print(zombie.name, "has died!!!!")

    def take_damage(self, amount):
        self.health -= amount
        print(self.name, "'s health is now", self.health)


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self, steps):
        self.distance -= steps
        print("The distance between the plants and zombie is:", self.distance)

    def attack(self, plant1, plant2):
        if plant1.health > 0:
            plant1.health -= self.damage
            print(self.name, "attacks", plant1.name, "for", self.damage, "damage!")
            print(plant1.name, "now has ", plant1.health, "health")
        elif plant2.health > 0:
            plant2.health -= self.damage
            print(self.name, "attacks", plant2.name, "for", self.damage, "damage!")
            print(plant2.name, "now has ", plant2.health, "health")
        else:
            print("All plants have died!")

    def take_damage(self, amount):
        self.health -= amount
        print(self.name, "'s health is now", self.health)


plant1 = Plant("Microwave", 49, 67)
plant2 = Plant("Refridgerator", 51, 76)
zombie1 = Zombie("Ava Harder", 600, 77, 50)

while True:
    if plant1.health > 0:
        plant1.attack(zombie1)
        zombie1.take_damage
    elif plant2.health > 0:
        plant2.attack(zombie1)
        zombie1.take_damage

    if zombie1.distance <=0:
        zombie1.attack(plant1, plant2)
        print(zombie1.name, "is here and they finna kill you !!!!!")
        plant1.take_damage
        plant2.take_damage

    elif zombie1.distance > 0:
        zombie1.move(30)
        
    
    if zombie1.health <= 0:
        print("----------------------------------------------")
        print("PLANTS WIN!!!!!!")
        break

    if plant1.health <= 0 and plant2.health <= 0:
        print("----------------------------------------------")
        print("ZOMBIES WIN!!!!")
        break