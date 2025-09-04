# 백준 1225 - 이상한 곱셈

A, B = input().split()
A = list(A)
B = list(B)
result = 0 
for i in A :
    for j in B :
        result += int(i) * int(j)
print(result)