# write a python program to check if a given number is even or odd
# implement a simple calculator using conditional statements
# write a program to print fibonacci series using for loop

a = int(input("Enter first number: "))
b = int(input("Enter the second number:"))


print("The available options are 1. Addition , 2. Multiplication, 3. Division, 4. Subtraction, 5.exponential, 6.remainder")
inp = int(input("Enter your option to perform: "))
if inp == 1:
    print("Sum is ",a+b)
elif inp == 2:
    print("Product is",a*b)
elif inp == 3:
    print("Divide result is",a/b)
    print("Divide result(2) is ",b/a)
elif inp == 4:
    print("Difference is ", a-b)
elif inp == 5:
    print("1st number to the power 2nd number is", a**b)
    print("2nd number to the power 1st number is", b**a)

elif inp == 6:
    print("1st % 2nd is", a%b)
    print("2nd % your first is", b%a)

