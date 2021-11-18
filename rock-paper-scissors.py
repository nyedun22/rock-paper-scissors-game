import random

# visual elements for rock, paper, scissors printed to console when user and computer select an option
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# user selects to play rock, paper or scissors
player1 = str(input('Do you want to select Rock, Paper or Scissors?')).lower()
if player1 == 'rock':
    print(rock)
elif player1 == 'paper':
    print(scissors)
elif player1 == 'scissors':
    print(scissors)
else:
    print('Please select rock, paper or scissors')

# computer randomly selects an option to play against user
player2 = random.randint(0, 2)
if player2 == 0:
    print(rock)
elif player2 == 1:
    print(paper)
else:
    print(scissors)

# outcomes to determine whether user has won or lost the game - using if/else statements
if player1 == 'rock' and player2 == 1:
    print('You lose!')
elif player1 == 'paper' and player2 == 2:
    print('You lose!')
elif player1 == 'scissors' and player2 == 0:
    print('You lose!')
else:
    print('Congratulations, You win!')
