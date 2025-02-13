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
while True:
    print("Welcome to Rock-Paper-Scissors!\n""What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.")

    player_choice = int(input())
    if player_choice <= 0 or player_choice >=3:
        print("Invalid input. You lose. Please try again.")
        continue
    elif player_choice == 0:
        print("You played", rock)
    elif player_choice == 1:
        print("You played",paper)
    elif player_choice == 2:
        print("You played",scissors)

    comp_choice = random.choice([0, 1, 2])
    if comp_choice == 0:
        print("Computer played", rock)
    if comp_choice == 1:
        print("Computer played", paper)
    if comp_choice == 2:
       print("Computer played", scissors)

    if player_choice == comp_choice:
       print("Tie!")
    elif (player_choice == 0 and comp_choice == 1) or \
         (player_choice == 1 and comp_choice == 2) or \
         (player_choice == 2 and comp_choice == 0):
       print("You lose!")
    else:
        print("You win!\n")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break