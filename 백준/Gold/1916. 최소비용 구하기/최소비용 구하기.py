# 백준 1916 - 최소비용 구하기
# 분류 : 최단거리

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M) :
    u, v, cost = map(int, input().split())
    adj[u].append((v, cost))

start, end = map(int, input().split())

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue
        for next in adj[node] :
            cost = distance[node] + next[1]
            if cost < distance[next[0]] :
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    
dijkstra(start)

print(distance[end])
