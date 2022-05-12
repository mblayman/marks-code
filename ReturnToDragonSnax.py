print("You are in a dark room in a mysterious castle.")
print("In front of you are four doors. You must choose one.")
player_choice = input("Choose 1, 2, 3, or 4... ")
if player_choice == "1":
    print("You found hidden treasure. YOU'RE RICH!!!")
    print("GAME OVER, YOU WIN!")
elif player_choice == "2":
    print("You are hit by an ogre.")
    print("GAME OVER, YOU LOSE!")
elif player_choice == "3":
    print("You go into the room and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon to the exit.")
    dragon_choice = input("Choose 1 or 2... ")
    if dragon_choice == "1":
        print("The dragon wakes up and eats you. You are delicious.")
        print("GAME OVER, YOU LOSE!")
    elif dragon_choice == "2":
        print(
            "You sneak around the dragon and escape the castle, blinking in the sunshine."
        )
        print("GAME OVER! YOU WIN!")
    else:
        print("Sorry, you didn't enter 1 or 2!")

else:
    print("Run the game again to try again.")
