import os

with open("ASCII.txt","r") as file:
    art = file.read()
CORRECT_SPELL = True
GAME = True
IS_GAME_ON = True

os.system("cls")


print("Welcome to Treasure Island.\nYour mission is to find treasure.")


while IS_GAME_ON:
    print(art)
    dir1 = input("Left or Right?\n")
    if dir1.lower() == "left":
        swim_or_wait = input("Do you want to swim or wait?\n")
        if swim_or_wait.lower() == "wait":
            which_door = input("Which Door?Red or Blue or Yellow\n" )
            if which_door.lower() == "yellow":
                print("You won!")
            elif which_door.lower() != "blue" or which_door.lower() != "red":
                CORRECT_SPELL = False
            else:
                GAME = False
        elif swim_or_wait.lower() != "swim":
            CORRECT_SPELL = False
        else:
            GAME = False
    elif dir1.lower() != "right" :
        CORRECT_SPELL = False
    else:
        GAME = False

    if not CORRECT_SPELL:
        print("Enter Valid Input")
    elif not GAME:
        print("You Loose!")
        
    again_play = input('Want to play again? "Y" or "N"\n')
    if again_play.lower() != "y":
        IS_GAME_ON = False
    else:
        GAME = True
        IS_GAME_ON =True
        CORRECT_SPELL = True
        os.system("cls")


