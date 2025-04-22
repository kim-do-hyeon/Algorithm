# 백준 10103 - 주사위 게임
# 문제집 : Python 배우기 (1 ~ 50)

N = int(input())
A, B = 100, 100

for i in range(N) :
    N_a, N_b = map(int, input().split())
    if N_a > N_b :
        B -= N_a
    elif N_b > N_a :
        A -= N_b
print(A)
print(B)