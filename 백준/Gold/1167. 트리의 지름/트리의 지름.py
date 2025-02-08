# 백준 1167 - 트리의 지름
# 분류 : 트리, DFS

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V = int(input())

Graph = [[] for _ in range(V + 1)]

for i in range(V) :
    data = list(map(int, input().split()))
    node = data[0]
    index = 1
    while data[index] != -1 :
        Graph[node].append((data[index], data[index + 1]))
        index += 2

def dfs(node, dist) :
    global max_dist, far
    if dist > max_dist :
        max_dist = dist
        far = node
    for n, w in Graph[node] :
        if not visited[n] :
            visited[n] = True
            dfs(n, dist + w)

visited = [False] * (V + 1)
max_dist = 0
far = 0
visited[1] = True
dfs(1, 0)

visited = [False] * (V + 1)
max_dist = 0
visited[far] = True
dfs(far, 0)

print(max_dist)