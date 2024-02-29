def pal(n):
    x = n[::-1]
    if x==n:
        print("It is a palindrome")
    else:
        print("Not")

inp = input("enter: ")
pal(inp)
