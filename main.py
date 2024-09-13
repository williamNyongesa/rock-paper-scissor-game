import random

choice_images = {"r":"🪨", "p":"🗞️", "s":"✂️"}
comp_choices = ("r","p","s")



while True:

    comp_choice = random.choice(comp_choices)
    user_choice = input("enter your choice: ")
    if user_choice not in comp_choices:
        print("enter a valid letter")
        continue
    if user_choice == comp_choice:
        print("tie")
        break
    elif user_choice == "p" and comp_choice == "r" or \
         user_choice == "r" and comp_choice == "s" or \
         user_choice == "s" and comp_choice == "p":
        print("You Win")
        break
    else:
        print("you lose")
        break
    print(f"you entered: {choice_images[user_choice]}")
    print(f"computer chose: {choice_images[comp_choice]}")