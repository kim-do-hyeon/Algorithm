# 백준 11729 - 최대 힙

import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N) :
    x = int(input())
    if x == 0 :
        if len(heap) > 0 :
            print(-heapq.heappop(heap))
        else :
            print(0)
    else :
        heapq.heappush(heap, -x)