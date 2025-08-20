# 백준 11286 - 절대값 힙
import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N) :
    X = int(input())
    if X == 0 :
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    else :
        heapq.heappush(heap, (abs(X), X))