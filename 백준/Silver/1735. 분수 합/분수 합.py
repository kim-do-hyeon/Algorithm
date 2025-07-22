# 백준 1735 - 분수 합
# 분류 : 수학

def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return a * b / gcd(a, b)


A, B = map(int, input().split())
C, D = map(int, input().split())

# A   C
# - * -
# B   D

max_bunmo = int(lcm(B, D))
X_bunja = A * (max_bunmo // B)
Y_bunja = C * (max_bunmo // D)
bunja = X_bunja + Y_bunja
is_gcd = gcd(X_bunja + Y_bunja, max_bunmo)
if is_gcd != 1 :
    print(int(bunja / is_gcd), int(max_bunmo / is_gcd))
else :
    print(bunja, max_bunmo)