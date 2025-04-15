# 백준 1038 - 감소하는 수
# 분류 : 브루트 포스

from itertools import combinations

N = int(input())

A = []
for i in range(1, 11) :
    for combination in combinations(list(range(10)), i) :
        gamso = 0
        for n in combination[::-1] :
            gamso *= 10
            gamso += n
        
        A.append(gamso)

A.sort()
if len(A) <= N :
    print(-1)
else :
    print(A[N])