# 백준 1350 - 진짜 공간

N = int(input())
SIZE = list(map(int, input().split()))
CLUSTER = int(input())

result = 0
for i in SIZE :
    if i == 0 :
        continue

    if i > CLUSTER :
        if i % CLUSTER > 0 :
            result += i // CLUSTER + 1
        else :
            result += i // CLUSTER
    else :
        result += 1
print(result * CLUSTER)