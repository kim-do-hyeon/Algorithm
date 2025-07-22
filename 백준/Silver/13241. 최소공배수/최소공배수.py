# 백준 13241 - 최소공배수
# 분류 : 유클리드호제법

def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return a * b / gcd(a, b)

A, B = map(int, input().split())
print(int(lcm(A, B)))