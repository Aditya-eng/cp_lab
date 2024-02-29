count = 1
for num in range(1,100):
    if num>1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            count+=1
            print(num)
            if count >10:
                break