# 백준 2450 - 모양 정돈
# 분류 : 브루트포스

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A = [x - 1 for x in A]

answer = 1e9
count = [0] * 3
for x in A :
    count[x] += 1

for permutation in permutations(range(3), 3) :
    B = []
    for x in permutation :
        B += [x] * count[x]
    
    wrong = [[0] * 3 for _ in range(3)]
    for i in range(N) :
        if A[i] != B[i] :
            wrong[A[i]][B[i]] += 1

    num_changes = 0
    remain = 0

    for i in range(3) :
        for j in range(i + 1, 3) :
            # i -> j, j -> i, a, b min(a, b)
            tmp = min(wrong[i][j], wrong[j][i])
            num_changes += tmp

            wrong[i][j] -= tmp
            wrong[j][i] -= tmp
            remain = max(wrong[i][j], wrong[j][i])

    # i -> j, j -> k, k -> i : 2번, 같은 수,
    num_changes += 2 * remain
    answer = min(answer, num_changes)

print(answer)