class RockPaperScissor:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.hand = ""
    
    def choice(self, handout):
        if handout in self.choices:
            self.hand = handout
        else:
            print("Invalid choice! Please select rock, paper, or scissors.")
    
    def determine_winner(self, hero_choice, enemy_choice):
        if hero_choice == enemy_choice:
            return "It's a tie!"
        elif (hero_choice == 'rock' and enemy_choice == 'scissors') or \
             (hero_choice == 'scissors' and enemy_choice == 'paper') or \
             (hero_choice == 'paper' and enemy_choice == 'rock'):
            return "Win"
        else:
            return "Lose"
