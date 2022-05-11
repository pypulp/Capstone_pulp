import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
                                                          
    _______
---'   ____)_____
          _______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_art=[rock,paper,scissors]
user_choice= int(input("What do you choose?\n0 for Rock,1 for Paper, 2 for Scissors\n"))
if (user_choice>=3) or (user_choice<0):
    print("Invalid Entry.You Lose")
else:
    print(f"You chose{game_art[user_choice]}")
    computer_choice = random.randint(0,2)
    print(f"Computer chose {game_art[computer_choice]}")
    if (user_choice==0) and (computer_choice==1):
        print("You lose")
    elif (user_choice==0) and (computer_choice==2):
        print("You win")
    elif (user_choice==1) and (computer_choice==0):
        print("You win")
    elif (user_choice==1) and (computer_choice==2):
        print("You Lose")
    elif (user_choice==2) and (computer_choice==0):
        print("You lose")
    elif (user_choice==2) and (computer_choice==1):
        print("You win")
    elif (user_choice==computer_choice):
        print("It's a draw")
    
