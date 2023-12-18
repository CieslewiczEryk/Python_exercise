A = [1,3,5,2,11,7]
L = 9 

n = 1
for index in range(len(A)-1):
    for ilosc in range(len(A)-1):  
        print(f"{A[index]} + {A[ilosc + n]}")
        result = A[index] + A[ilosc + n]
        n + 1 
        print(result)