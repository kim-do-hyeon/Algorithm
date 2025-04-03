# 백준 1240 - 노드사이의 거리
# 분류 : 트리

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(N - 1) :
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1

    adj[u].append((v, w))
    adj[v].append((u, w))

visit = [False] * N
dist = [0] * N

def dfs(u) :
    visit[u] = True

    for v, w in adj[u] :
        if not visit[v] :
            dist[v] = dist[u] + w
            dfs(v)

for _ in range(M) :
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    visit = [False] * N
    dist = [0] * N

    dist[s] = 0
    dfs(s)

    print(dist[t])