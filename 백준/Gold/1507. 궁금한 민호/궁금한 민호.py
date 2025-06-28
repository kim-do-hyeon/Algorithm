N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
need = [[True] * N for _ in range(N)]

impossible = False
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or j == k:
                continue
            # 모순된 거리 정보
            if dist[i][k] + dist[k][j] < dist[i][j]:
                impossible = True
            # 간선이 없어도 되는 경우
            if dist[i][k] + dist[k][j] == dist[i][j]:
                need[i][j] = False

if impossible:
    print(-1)
else:
    answer = 0
    for i in range(N):
        for j in range(i + 1, N):
            if need[i][j]:
                answer += dist[i][j]
    print(answer)