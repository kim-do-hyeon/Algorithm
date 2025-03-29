import heapq
from collections import defaultdict

def solution(N, road, K):
    G = defaultdict(list)
    for a, b, cost in road :
        G[a].append((b, cost))
        G[b].append((a, cost))
    
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    heap = [(0, 1)]
    while heap :
        curr_dist, curr_node = heapq.heappop(heap)
        
        if curr_dist > dist[curr_node] :
            continue
        
        for neighbor, weight in G[curr_node] :
            distance = curr_dist + weight
            if distance < dist[neighbor] :
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
        
    return sum(1 for d in dist if d <= K)