# 백준 1333 - 부재중 전화
# 분류 : 구현

N, L, D = map(int, input().split())

check = [False] * 5000

index = 0
for _ in range(N) :
    for _ in range(L) :
        check[index] = True
        index += 1
    for _ in range(5) :
        index += 1

for i in range(0, 5000, D) :
    if not check[i] :
        print(i)
        break