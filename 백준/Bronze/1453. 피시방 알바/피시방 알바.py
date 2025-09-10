# 백준 1453 - 피시방 알바

check = [False] * 100
N = int(input())
A = list(map(int, input().split()))

result = 0
for i in A :
    if check[i - 1] == False :
        check[i - 1] = True
    else :
        result += 1

print(result)