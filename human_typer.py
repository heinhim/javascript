import random
class Player:
    def __init__(self):
        self.hp=20
        self.gold=0
        self.name="Hero"

class Enemy:
    def __init__(self):
        self.hp=random.randint(5,15)
        self.damage=random.randint(1,5)

def encounter(player):
    enemy=Enemy()
    print("An enemy appeared!")
    while enemy.hp>0 and player.hp>0:
        print(f"Player HP:{player.hp} Enemy HP:{enemy.hp}")
        choice=input("Attack or Run? ").lower()
        if choice=="attack":
            dmg=random.randint(2,6)
            enemy.hp-=dmg
            print(f"You dealt {dmg} damage!")
            if enemy.hp>0:
                player.hp-=enemy.damage
                print(f"Enemy hits you for {enemy.damage}!")
        elif choice=="run":
            if random.random()<0.5:
                print("You escaped!")
                return
            else:
                print("You failed to run!")
                player.hp-=enemy.damage
        else:
            print("Invalid choice.")
    if player.hp<=0:
        print("You died!")
    else:
        reward=random.randint(1,10)
        player.gold+=reward
        print(f"Enemy defeated! You got {reward} gold.")

def find_treasure(player):
    gold=random.randint(5,15)
    player.gold+=gold
    print(f"You found a treasure chest with {gold} gold!")

def trap(player):
    dmg=random.randint(1,5)
    player.hp-=dmg
    print(f"You stepped on a trap and lost {dmg} HP!")

def random_event(player):
    events=[encounter,find_treasure,trap,lambda p:print("Nothing happened.")]
    event=random.choice(events)
    event(player)

def game_loop():
    player=Player()
    print("Welcome to the Dungeon!")
    while True:
        print(f"\nHP:{player.hp} Gold:{player.gold}")
        action=input("Move forward? (y/n) ").lower()
        if action=="y":
            random_event(player)
            if player.hp<=0:
                print("Game Over.")
                break
        elif action=="n":
            print("You leave the dungeon.")
            break
        else:
            print("Invalid input.")

    print("\nFinal Stats:")
    print(f"HP:{player.hp}")
    print(f"Gold:{player.gold}")

if __name__=="__main__":
    game_loop()