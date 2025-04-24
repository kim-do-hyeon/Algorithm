# 백준 11508 - 2+1 세일
# 분류 : 그리디

N = int(input())
C = []
for i in range(N) :
    C.append(int(input()))

C.sort(reverse=True)
discount = 0
for i in range(0, N, 3) :
    if i + 2 < N :
        # i, i + 1, i + 2
        discount += C[i + 2]

print(sum(C) - discount)