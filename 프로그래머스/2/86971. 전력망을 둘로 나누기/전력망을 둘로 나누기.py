from collections import deque

def bfs(G, S, V) :
    queue = deque([S])
    V[S] = True
    count = 0
    while queue :
        v = queue.popleft()
        count += 1
        for i in G[v] :
            if not V[i] :
                queue.append(i)
                V[i] = True
    return count

def solution(n, wires):
    answer = n - 2
    for i in range(len(wires)) :
        tmps = wires.copy()
        G = [[] for i in range(n + 1)]
        V = [False] * (n + 1)
        tmps.pop(i)
        for wire in tmps :
            x, y = wire
            G[x].append(y)
            G[y].append(x)
        for index, graph in enumerate(G) :
            if graph != [] :
                S = index
                break
        counts = bfs(G, S, V)
        other = n - counts
        if abs(counts - other) < answer :
            answer = abs(counts - other)
    return answer