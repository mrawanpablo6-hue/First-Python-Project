import random
rock_ascart=("""
       ____
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)      
             """)
paper_ascart=("""
         _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) 
              """)
scissors_ascart=("""
                    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
                 """)
print("Welcome to the game of rock, paper, scissors!")
confirm=input("Press Enter to continue or type help for rules:\n")
if confirm.lower()=="help":
    print("""
          ******rules*****
            1. Rock beats scissors
            2. Scissors beats paper
            3. Paper beats rock
            4. If both players choose the same option, it's a tie.
          """)
user_choice=input("Enter your choice (rock, paper, or scissors):\n")
if  user_choice==["rock","paper","seissors"]:
    print("Error")
else:
    if user_choice.lower()=="rock":
        print(f"your choice \n{rock_ascart}")            
    elif user_choice.lower()=="paper":
        print(f"your choice \n{paper_ascart}")
    else:
        print(f"your choice \n{scissors_ascart} ")
# computer choice
computer_choice=random.choice(["rock","paper","scissors"])
if computer_choice=="rock":
    print(f"your computer choice \n{rock_ascart}")
elif computer_choice=="paper":
    print(f"your computer choice \n{paper_ascart}")
else:
    print(f"your coputer choice \n{scissors_ascart}") 
if user_choice==computer_choice:
    print("It is a tie!")
elif (
(user_choice=="rock" and computer_choice=="scissors")
or
(user_choice=="paper" and computer_choice=="rock")
or
(user_choice=="scissors" and computer_choice=="paper")):
    print(f"You win user choice {user_choice} beats {computer_choice}.")
else:
    print(f"your lost {computer_choice} beats {user_choice} ")
        