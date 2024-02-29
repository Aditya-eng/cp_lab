# count = 1
n=5
for i in range(5):
    for j in range(i):
        print(" ",end="")
    print("*"*(n-i))
