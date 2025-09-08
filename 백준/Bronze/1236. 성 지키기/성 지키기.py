# 백준 1236 - 성 지키기

N, M = map(int, input().split())
adj = [input() for _ in range(N)]

rows = (sum('X' not in row for row in adj))
cols = 0

for col in range(M) :
    guard = False
    for row in range(N) :
        if adj[row][col] == 'X' :
            guard = True
            break
    if not guard :
        cols += 1

print(max(rows, cols))