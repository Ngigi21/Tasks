#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .try:
for i in range(0,10):
    try:
        number1=float(input("enter your number:"))
        number2=float(input("enter your number:"))
        total=number1+number2
        print(total)
        break
    except:
        print("you entered an invalid number")