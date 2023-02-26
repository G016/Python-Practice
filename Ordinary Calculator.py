First = int(input("Enter Your First No. : "))
Operator = input("Enter Your Operator (+,-,*,/,%) : ")
Second = int(input("Enter Your Second no. : "))

if Operator == '+':
    print (First + Second)

elif Operator == '-':
    print (First - Second)

elif Operator == '*':
    print (First * Second)

elif Operator == '/':
    print (First / Second)

elif Operator == '%':
    print (First % Second)

else:
    print ("Invalid Operator")