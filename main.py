
'''
1 for snake
-1 for water
0 for gun
'''

import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice ")

youDict = {"s": 1, "w": -1, "g":0}
reverseDict = {1:"Snake", -1: "water", 0:"Gun" }

you = youDict [youstr]

print(f"You choose {reverseDict [you]}\nComputer Choose {reverseDict[computer]}")

if (computer == you):
    print("draw!!!!!!!!!")

else:
    if(computer == -1 and you == 1):
      print("you win")
    
    elif (computer == -1 and you == 0):
       print ("You lose")


    elif (computer == 1 and you == -1):
       print("you lose")

    elif (computer == 1 and you == 0):
       print ("You win")
       
    elif (computer == 0 and you == -1):
       print("you lose")

    elif (computer == 0 and you == 1):
       print ("You win")
       
       print("somethingg went wrong!")   

