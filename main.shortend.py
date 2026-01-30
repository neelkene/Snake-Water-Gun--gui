import random
''' 1 for snake 0 for gun -1 for water
'''
computer = random.choice([0 , -1 , 1 ]) 
yourstr = input("Enter your Choice :- ").strip().capitalize() 
your_dic =  {"Snake" : 1 , "Water" : -1, "Gun" : 0 } 
reverse_dic = { 1 : "Snake" , -1 : "Water" , 0 : "Gun" }
try:
    you = your_dic[yourstr]           
    print(f"You choose the {reverse_dic[you]} \n Computer choose {reverse_dic[computer]}")
    if ((computer - you == -1) and (computer - you == 2)):
        print ("You loose !")

    elif (computer == you):
        print("Your match is draw !!")
    else :
        print("You Won!!")
#     elif (computer == 1 and you == 0):
#         print("You Won !! ")
#     elif (computer == 1 and you == -1):
#         print("You lose !! ")
#     elif (computer == 0 and you == 1):         # we use loop to overcome witth this problem 
#         print("You lose !! ")
#     elif (computer == 0 and you == -1):
#         print("You Won !! ")
#     elif (computer == -1 and you == 1):
#         print("You Won !! ")
#     elif (computer == -1 and you == 0):
#         print("You lose !! ")
except KeyError:
    print("Invalid input. Please choose Snake, Water, or Gun.")
