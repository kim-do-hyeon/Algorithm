# 백준 16466 - 콘서트
# 분류 : 정렬

N = int(input())
A = list(map(int, input().split()))

A.sort()
found = False
for i in range(N) :
    if A[i] != (i + 1) :
        print(i + 1)
        found = True
        break

if not found :
    print(N + 1)