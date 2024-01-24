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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You are at a crossroads. To the left is a dark forest, to the right is a beautiful beach.")
direction = input("Where would you like to go? Type 'left' or 'right' ").lower()

if direction =="left":
    print("You arrive at an ocean-sized lake. The weather is nice and you can see an island in the distance. You can swim that distance, however, the waves look slightly concerning...")
    action = input("Are you staying savely ashore or do you dare to take a swim? Type 'stay' or 'swim' ").lower()
    if action == "stay":
        print("A meteor hits you out of nowhere. You die on the spot. Game over.")
    elif action == "swim":
        print('''You ready yourself and step into the water only to realise it is not even knee deep. You strut over to the island and see a small house with three doors. One is red, one is yellow and one is blue.''')
        door = input("Which door do you choose? Type 'red', 'yellow' or 'blue' ").lower()
        if door == "red":
            print("As you touch the handle of the red door, a terrible monster bursts through it ending your journey immediately. You family will miss you...")
        elif door == "blue":
            print("As you touch the handle of the blue door, you notice the handle is wet. You open the door and a wall of water hits you and flushes you away. You see your life flash before your eyes as you drown. Game over")
        elif door == "yellow":
            print("You open the yellow door and bright light engulfes you. You ascend to whatever your version of an afterlife is. You win!")
        else:
            print("You are too indecisive. You noticed earlier a meteor hitting the beach. The tsunami it caused has reached you and washes you against the red door. As you try and scramble to open it, the water pressure crushes you into a pulp. As the wave subsides a monster bursts through the red door and feast on what remains of you. Game over")
    else:
        print("You clearly can't decide what to do (Are the options too complex?). You stay on the beach and are struck by a meteor. You die on the spot. Game over.")
elif direction == "right":
     print("You enter the dark forest and are attacked by a pack of wolves. Game over.")
else:
     print("The directions are too complex for you. You stay on the spot and die of dehydration. Game over.")