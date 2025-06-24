import random
class Character:
    def __init__(self, name, attack_power, max_defense, max_health, heal)  :
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power= attack_power
        self.heal = heal
        #self.max_defense = max_defense
        #self.armor=max_defense
    def attack(self, target):
        #damage = max(1, self.attack_power-target.armor)
        danages  = self.attack_power
        target.health -= danages
        if target.health <= 0:
            target.health = 0

        print(f"{self.name}  attacks {target.name} for {danages}  damage")

    def healup(self):
        if self.health + self.heal > self.max_health:
            self.health = self.max_health
            print(f"{self.name} heals to max health")
        else:
            self.health += self.heal
            print(f"{self.name}  heals up {self.heal} health")

    # def defenseup(self, amount):
    #     if self.armor + amount > self.max_defense:
    #         self.armor = self.max_defensebett
    #         print(f"{self.name} armors to max defense {self.max_defense}")
    #     else:
    #         self.armor += amount
    #         print(f"{self.name}  armors up {amount} ")
    def healthbar(self):
        healthbar = ("[")

        if self.health == self.max_health:

            for i in range(self.max_health):
                healthbar = healthbar + ("#")
        else:
            for i in range(self.max_health):
                if i < self.health:
                    healthbar = healthbar + ("#")
                else:
                    healthbar = healthbar + ("~")
        healthbar = healthbar + ("]")
        return f"{self.name} health: \n {healthbar} {self.health}/{self.max_health}"

actions = {1: lambda character, target: character.attack(target), 2: lambda character, target: character.defenseup(target)}

enemy_names = ["Goblin", "Orc", "Slime"]
templates = {"Goblin":{"health" :10, "attack":4, "defense": 3,"heal":2},
                   "Orc": {"health": 15, "attack": 2, "defense": 4, "heal":2},
                   "Slime": {"health": 8, "attack": 2, "defense": 2,"heal":2},
             "player": {"health": 10, "attack": 4, "defense": 3,"heal":2}
                   }
playername = input("Player name: ")
player_stats = templates["player"]
player = Character(playername, player_stats["attack"],1,player_stats["health"],player_stats["heal"])
enemy_name = random.choice(enemy_names)
enemy_stats = templates[enemy_name]
enemy = Character(enemy_name, enemy_stats["attack"],1,enemy_stats["health"],enemy_stats["heal"])
goes_first = random.choice([True, False])
while enemy.health > 0 and player.health > 0:
    print(player.healthbar())
    print(enemy.healthbar())
    if goes_first:
        print("your turn!")

        player_action = input("what do you want to do? 1 for attack 2 for heal ")
        while player_action != "1" and player_action != "2":
            player_action = input("what do you want to do? 1 for attack 2 for heal ")
        if player_action == "1":
            player.attack(enemy)
        elif player_action == "2":
            player.healup()

        print(player.healthbar())
        print(enemy.healthbar())

        if enemy.health > 0:
            print("enemy turn!")
            eneny_action = random.choice([1, 2])
            if eneny_action == 1:
                enemy.attack(player)

            elif eneny_action == 2:
                enemy.healup()
        else:
            break
    else:
        print("enemy turn!")
        eneny_action = random.choice([1, 2])
        if eneny_action == 1:
            enemy.attack(player)

        elif eneny_action == 2:
            enemy.healup()
        print(player.healthbar())
        print(enemy.healthbar())
        print("your turn!")



        if player.health > 0:
            player_action = input("what do you want to do? 1 for attack 2 for heal ")
            while player_action != "1" and player_action != "2":
                player_action = input("what do you want to do? 1 for attack 2 for heal ")
            if player_action == "1":
                player.attack(enemy)
            elif player_action == "2":
                player.healup()
                print(player.healthbar())
        else:
            break


    print(player.healthbar())
    print(enemy.healthbar())



print("game over!")
if player.health > 0:
    print("you won")
else :
    print("you lost")