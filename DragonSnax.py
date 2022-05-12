print("You are in a dark room in a mysterious castle.")
print("In front of you are three doors. You must choose one.")
player_choice = input("Choose 1, 2, or 3... ")
if player_choice == "1":
    print("You found hidden treasure. YOU'RE RICH!!!")
    print("GAME OVER, YOU WIN!")
elif player_choice == "2":
    print("You are hit by an ogre.")
    print("GAME OVER, YOU LOSE!")
elif player_choice == "3":
    print("You go into the room and find a sleeping dragon.")
    print("The dragon wakes up and eats you. You are delicious.")
    print("GAME OVER, YOU LOSE!")
else:
    print("Run the game again to try again.")
