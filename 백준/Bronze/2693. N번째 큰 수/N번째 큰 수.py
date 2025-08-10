# 백준 2693 - N번째 큰 수

T = int(input())
for _ in range(T) :
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(A[2])