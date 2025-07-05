# 백준 1629 - 곱셈
# 분류 : 다이나믹 프로그래밍

A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    x = power(a, b // 2, c)
    if b % 2 == 0:
        return (x * x) % c
    else:
        return (x * x * a) % c

print(power(A, B, C))