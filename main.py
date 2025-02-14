import random
import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword
from rock_paper_scissor import RockPaperScissor

# ------------ setup ------------
hero = Hero(name="Hero", health=100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow)

# ------------ game loop ------------
game = RockPaperScissor()

while hero.health > 0 and enemy.health > 0:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in game.choices:
        print("Invalid choice! Try again.")
        continue
    
    computer_choice = random.choice(game.choices)
    print(f"Enemy chose: {computer_choice}")
    
    attack_status = game.determine_winner(user_choice, computer_choice)
    print(attack_status)

    if attack_status == "Win":
        hero.attack(enemy)
    elif attack_status == "Lose":
        enemy.attack(hero)
    
        hero.health_bar.draw()
    enemy.health_bar.draw()

    if hero.health <= 0:
        print("Hero has been defeated!")
    elif enemy.health <= 0:
        print("Enemy has been defeated!")


