#finding largest among three numbers using nested if

#taking inputs
firstNumber=int(input("enter the first number: "))
secondNumber=int(input("enter the second number"))
thirdNumber=int(input("enter the third number"))
# showing the numbers
print(f"first number = {firstNumber}")
print(f"second number = {secondNumber}")
print(f"third numbeer = {thirdNumber}")

#checking using nested if
if(firstNumber>secondNumber):
    if(firstNumber>thirdNumber):
        print(f"The largest number is : {firstNumber}")
    else:
        print(f"The largest number is : {thirdNumber}")
else:
    print(f"The largest number is : {secondNumber}")
