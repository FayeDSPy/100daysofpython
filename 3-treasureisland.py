print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction_1 = input("Do you want to move left or right? Please type 'R' for right or 'L' for left.\n").upper()

if direction_1 == "R":
    print("Fall into a hole.\nGame Over.")
else:
    direction_2 = input(
        "You come across a river. Do you want to swim or wait? Please type 'S' for swim and 'W' for wait.").upper()
    if direction_2 == "S":
        print("Attacked by trout.\nGame Over.")
    elif direction_2 == "W":
        print(
            "A strange old man finds you waiting. He offers to take you to his house. Once you're inside, he vanishes and 3 doors appear before you.")
        print("Do you want to go through the red door, the yellow door, or the blue door?")
        door = input("Please type 'R' for red, 'Y' for yellow, and 'B' for blue.").upper()

        if door == "R":
            print("Burned by fire.\nGame Over.")
        elif door == "Y":
            print("You found the treasure! You win!")
        elif door == "B":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("That's not a valid choice. Game Over.")
    else:
        print("That's not a valid choice. Game Over.")

print("Thank you for playing Treasure Island!")