# 백준 6603 - 로또
# 분류 : 조합

from itertools import combinations

T = []
while True :
    A = list(map(int, input().split()))
    if len(A) == 1 and A[0] == 0 :
        break
    else :
        T.append(A[1:])

for i in T :
    result = []
    for combination in combinations(i, 6) :
        result.append(sorted(combination))
    result.sort()
    for j in result :
        for k in j :
            print(k, end = " ")
        print()
    print()
        