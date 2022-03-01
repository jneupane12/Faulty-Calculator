firstNumber = int(input("Enter a first number"))
secondNumber = int(input("enter a second number"))
addition = firstNumber+secondNumber
subtraction = firstNumber-secondNumber
multiplication = firstNumber*secondNumber
division = firstNumber/secondNumber
choice = input("Enter \n 1 for addition \n 2  for subtraction \n 3  for division \n 4 for multiplication\t")

if choice=='1':
    if firstNumber==56 and secondNumber==9:
        faultyanswer =77
        print("Addition of",firstNumber, "and",secondNumber,"is",faultyanswer)
    else:
        print("Addition of ",firstNumber,"and", secondNumber,"is",addition)


elif choice=='2':
    print("Subtraction of",firstNumber,"and",secondNumber,"is",subtraction)


elif choice=='3':
    if firstNumber==56 and secondNumber==6:
        faultyanswer = 4
    else:
        print("Division of",firstNumber,"with",secondNumber,"is",division)
elif choice=='4':
    if firstNumber==45 and secondNumber==3:
        faultyanswer=555
        print("Multiplication of",firstNumber,"and",secondNumber,"is",faultyanswer)
    else:
        print("Multiplication of",firstNumber,"and",secondNumber,"is",multiplication)

else:
    print("Wrong selection, Try again")









