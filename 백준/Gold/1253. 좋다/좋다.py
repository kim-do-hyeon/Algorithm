# 백준 1253 - 좋다
# 분류 : 투포인터

N = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0
for i in range(N) :
    k = N - 1
    if k == i :
        k -= 1

    found = False
    for j in range(N) :
        if j == i :
            continue

        target = A[i] - A[j]

        while j < k and A[k] > target :
            k -= 1
            if k == i :
                k -= 1

        if j != k and A[k] == target :
            found = True
            break
    
    if found :
        count += 1

print(count)