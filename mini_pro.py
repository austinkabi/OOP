'''  ASIMPLE PROJECT IN PYTHON'''
print("Select your option")
number=int(input("Option: "))
if number==1:
    print("Enter the First number to add ")
    num1=int(input())
    print("Enter the second number to add ")
    num2=int(input())
    sum=num1+num2
    print("The sum of {} and {} is {}".format(num1,num2,sum))
elif number==2:
    print("Enter the First number to subtract ")
    num1=int(input())
    print("Enter the second number to substract ")
    num2=int(input())
    sub=num1-num2
    print("The difference of {} and {} is {}".format(num1,num2,sub))
elif number==3:
    print("Enter the First number to multiply ")
    num1=int(input())
    print("Enter the second number to multiply ")
    num2=int(input())
    times=num1*num2
    print("The multiplication of {} and {} is {}".format(num1,num2,times))
elif number==4:
    print("Enter the First number to modulate ")
    num1=int(input())
    print("Enter the second number to modulate ")
    num2=int(input())
    mod=num1%num2
    print("The modulation of {} and {} is {}".format(num1,num2,mod))
    