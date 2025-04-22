# 백준 2476 - 주사위 게임
# 문제집 : Python 배우기

N = int(input())
max_money = 0
for i in range(N) :
    a, b, c = map(int, input().split())
    if a == b and b == c :
        money = 10000 + a * 1000
    elif a == b and b != c :
        money = 1000 + a * 100
    elif a == c and b != a :
        money = 1000 + a * 100
    elif b == c and b != a :
        money = 1000 + b * 100
    elif a != b and b != c :
        money = max([a, b, c]) * 100
    
    max_money = max(money, max_money)
print(max_money)