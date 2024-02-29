dict={}
for i in range(3):
    inp = input("Enter key: ")
    inp2 = input("Enter value: ")
    dict[i] = inp
    dict[inp] = inp2

print(dict)

#retreive

in1 = input("Enter key")
print(dict[in1])


