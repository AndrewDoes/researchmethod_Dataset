import random

player_name = ""
player_hp = 100
player_max_hp = 100
enemy_hp = 100
enemy_max_hp = 100
potions = 3
enemy_potions = 1
player_attack_min = 10
player_attack_max = 20
enemy_attack_min = 5
enemy_attack_max = 15
turn = 0

def startGame():
    global player_name
    print("Welcome to the Ultimate Battle Game!")
    player_name = input("Enter your name: ")
    print(f"Hello {player_name}, get ready to fight!")

def attack():
    global enemy_hp
    damage = random.randint(player_attack_min, player_attack_max)
    enemy_hp -= damage
    if enemy_hp < 0:
        enemy_hp = 0
    print(f"You attack the enemy for {damage} damage! Enemy HP: {enemy_hp}/{enemy_max_hp}")

def enemyAttack():
    global player_hp
    damage = random.randint(enemy_attack_min, enemy_attack_max)
    player_hp -= damage
    if player_hp < 0:
        player_hp = 0
    print(f"Enemy attacks you for {damage} damage! Your HP: {player_hp}/{player_max_hp}")

def usePotion():
    global player_hp, potions
    if potions > 0:
        heal = 20
        if player_hp + heal > player_max_hp:
            heal = player_max_hp - player_hp
        player_hp += heal
        potions -= 1
        print(f"You used a potion! Restored {heal} HP. Your HP: {player_hp}/{player_max_hp}. Potions left: {potions}")
    else:
        print("You have no potions left!")

def enemyUsePotion():
    global enemy_hp, enemy_potions
    if enemy_potions > 0 and enemy_hp < enemy_max_hp:
        heal = 15
        if enemy_hp + heal > enemy_max_hp:
            heal = enemy_max_hp - enemy_hp
        enemy_hp += heal
        enemy_potions -= 1
        print(f"Enemy used a potion! Enemy HP: {enemy_hp}/{enemy_max_hp}. Enemy potions left: {enemy_potions}")

def battle():
    global player_hp, enemy_hp
    while player_hp > 0 and enemy_hp > 0:
        print("\n1. Attack\n2. Use Potion\n3. Run")
        choice = input("Enter choice: ")
        if choice == "1":
            attack()
            if enemy_hp > 0:
                if enemy_hp < 30 and enemy_potions > 0:
                    enemyUsePotion()
                else:
                    enemyAttack()
        elif choice == "2":
            usePotion()
            enemyAttack()
        elif choice == "3":
            print("You ran away! Game over.")
            return
        else:
            print("Invalid choice.")

        if player_hp <= 0:
            print("You died! Game over.")
            return
        elif enemy_hp <= 0:
            print("You defeated the enemy! You win!")
            return

startGame()
battle()
