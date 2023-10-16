import random

Comp_No = random.randrange(1,61)
User_No = int(input("Enter your guess no. between 1 to 60 ---> "))

if Comp_No>User_No:
    print ("Computer No.-->",Comp_No)
    print ("Your guess no. is low")

elif Comp_No<User_No:
    print ("Computer No.-->",Comp_No)
    print ("Your guess no. is high")

else:
    print ("Computer No.-->",Comp_No)
    print ("Congratulation your guess no. is correct...")