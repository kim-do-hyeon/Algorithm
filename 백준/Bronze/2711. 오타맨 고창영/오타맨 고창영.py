# 백준 2711 - 오타맨 고창영

T = int(input())
for _ in range(T) :
    A = input().split()
    N = int(A[0])
    S = list(A[1])
    del S[N - 1]

    print("".join(S))
