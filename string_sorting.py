A1 = input("Enter: ")
A = list(A1)

#sorting
# for i in inp:

for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 

    A[i], A[min_idx] = A[min_idx], A[i]


# print(str(A))
str1 = ""
for i in A:
    str1+=i
print(str1)
    

#slicing
print(str1[2:4])