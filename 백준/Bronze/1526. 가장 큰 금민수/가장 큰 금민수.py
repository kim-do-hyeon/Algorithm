# 백준 1526 - 가장 큰 금민수
# 분류 : 브루트포스

from itertools import combinations

N = int(input())

A = []
for i in range(1, 7) :
    # [0, 1, 2, ..., i - 1]
    for j in range(i + 1) :
        for combination in combinations(list(range(i)), j) :
            kms = 0
            for k in range(i) :
                kms *= 10
                if k in combination :
                    kms += 7
                else :
                    kms += 4
            A.append(kms)

answer = -1
for a in A :
    if a <= N :
        answer = max(answer, a)

print(answer)
