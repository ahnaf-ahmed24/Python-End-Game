import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
yourString = input("Enter Your Choice : ")
yourDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = yourDict[yourString]

# By now we have 2 number (variables), you and Computer 
 
print(f"You Chose{reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Lose!")
    else:
        print("You Win!")