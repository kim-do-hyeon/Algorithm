# 백준 3040 - 백설 공주와 일좁 난쟁이
# 분류 : 브루트포스

from itertools import combinations

A = [int(input()) for _ in range(9)]

for combination in combinations(A, 7) :
    if sum(combination) == 100 :
        for i in combination :
            print(i)
        break