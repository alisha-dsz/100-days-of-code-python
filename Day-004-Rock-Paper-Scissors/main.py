import random

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

game = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissors game!")
player_input=int(input("What would you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))

if player_input==0:
    print(rock)
elif player_input==1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
computer=random.randint(0,2)
print(game[computer])

if player_input==computer:
    print("You draw!")
else:
    if player_input==0 and computer==1:
        print("You lose!")
    elif player_input==0 and computer==2:
        print("You win!")
    elif player_input==1 and computer==0:
        print("You win!")
    elif player_input==1 and computer==2:
        print("You lose!")
    elif player_input==2 and computer==0:
        print("You lose!")
    else:
        print("You win!")
