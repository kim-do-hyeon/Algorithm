# 백준 9085 - 더하기

T = int(input())
for _ in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))