# 백준 2422 - 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 분류 : 브루트포스

from itertools import combinations

N, M = map(int, input().split())

bad = [[False] * N for _ in range(N)]
for _ in range(M) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    bad[a][b] = True
    bad[b][a] = True

answer = 0
for combination in combinations(range(N), 3) :
    a = combination[0]
    b = combination[1]
    c = combination[2]

    if bad[a][b] or bad[b][c] or bad[c][a] :
        continue
    answer += 1

print(answer)