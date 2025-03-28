# 백준 2530 - 인공지능 시계
# 분류 : 수학

A, B, C = map(int, input().split())
D = int(input())

for i in range(D) :
    C += 1
    if C == 60 :
        B += 1
        C = 0
    if B == 60 :
        A += 1
        B = 0
    if A == 24 :
        A = 0

print(A, B, C)