# 백준 1356 - 유진수

N = list(input())

start = len(N)
result = False
for i in range(1, start) :
    A = N[:i]
    B = N[i:]

    temp_A, temp_B = 1, 1

    for x in A :
        temp_A *= int(x)
    for y in B :
        temp_B *= int(y)

    if temp_A == temp_B :
        result = True
        break

if result : 
    print("YES")
else :
    print("NO")