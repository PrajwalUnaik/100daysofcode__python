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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
direction = input(print("You're at a cross road ,How do you want to proceed 'left' or 'right' ? /n "))
if direction.lower() == "right":
    print("You have fallen into a hole, Game Over!")
else:
    lake_choice = input("You're at a lake. Type 'wait' for the boat or 'swim' to swim across: ")

    if lake_choice.lower() == "swim":
        print("You have been attacked by a trout, Game Over!")
    else:
        door_choice = input("You have arrived at an island unharmed. There are three doors. Type 'red', 'yellow', or 'blue' to enter the right door: ")

        if door_choice.lower() == "red":
            print("You have been burned by fire, Game Over!")
        elif door_choice.lower() == "blue":
            print("You have been eaten by a Dragon, Game Over!")
        else:
            print("You have arrived at the treasure, You Win!")