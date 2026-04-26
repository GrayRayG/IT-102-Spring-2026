'''
Create a conditional that takes an input and if its yes then return a reply
'''

#This is going to take an input from the user
answer = input("Is today a good day? (y/n) ").lower()


#it is an if statement checking if the string is equal to y and if so print yes it is
if answer == "y":
    print("Yes it is")
elif answer == "n":
    print("I'm sorry")
else:
    print("Please try again")