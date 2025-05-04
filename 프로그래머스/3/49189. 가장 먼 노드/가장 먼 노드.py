from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] for i in range(n)]
    
    for i in edge :
        u, v = i[0], i[1]
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    queue = deque()
    dist = [-1] * n
    queue.append(0)
    dist[0] = 0
    
    while queue :
        u = queue.popleft()
        for v in adj[u] :
            if dist[v] == -1 :
                dist[v] = dist[u] + 1
                queue.append(v)
    
    max_dist = max(dist)
    answer = dist.count(max_dist)

    return answer