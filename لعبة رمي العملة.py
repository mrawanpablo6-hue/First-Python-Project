print("Welcome to The coin Gusseing Game!")
print("Choose a Method to toss the coin:")
my_random=("Using random.random()")
my_raindint=("Using random.raindint()")
print("1. Ussing random.random()")
print("2. Using random.raindint()")
coin=int(input("Enter your choice (1 or 2):"))
if coin==1:
    guss=input("Enter your guss (Heads Or Tails):")
    print(guss)
    if guss.lower()=="heads":
       print("cong!!, Your Win!!")
    elif guss.lower()=="tails":
        print("Sorry, Your lost!!")
        import random
        the_random=random.choice(["Heads","Tails"])
        print(f"the computer is coin toss result was: {the_random}")
    else:
        print(f"{[guss]} Not Avilab")
elif coin==2:
    guess=input("Enter your guss (Heads Or Tails):")
    print(guess)
    if guess.lower()=="tails":
        print("Cong !! your Win")
    elif guess.lower()=="heads":
        print("Sorry , Your Lost!!")
        import random
        is_random=random.choice(["Heads","Tails"])   
        print(f"The Computer Gussed : {is_random}")
    else:
        print(f"{[guess]} Not Avilable")
else:
    print(" invailed Choice number 1 or 2 ")

        
