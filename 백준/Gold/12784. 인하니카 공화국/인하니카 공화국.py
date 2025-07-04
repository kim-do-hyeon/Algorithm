# 백준 12784 - 인하니카 공화국
# 분류 : 다이나믹 프로그래밍

T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]

    for _ in range(M) :
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b, c))
        adj[b].append((a, c))
    
    visit = [False] * N
    D = [0] * N

    def dfs(u) :
        visit[u] = True

        is_leaf = True
        for v, w in adj[u] :
            if not visit[v] :
                dfs(v)
                D[u] += min(w, D[v])
                is_leaf = False
        
        if u != 0 and is_leaf :
            D[u] = 1e9
    
    dfs(0)
    print(D[0])