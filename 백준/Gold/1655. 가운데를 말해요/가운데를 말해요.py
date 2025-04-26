# 백준 1655 - 가운데를 말해요
# 분류 : 우선순위 큐
# 문제집 : 단기간 성장 - 2번

import sys
import heapq

input = sys.stdin.readline

left = []
right = []

N = int(input())
for i in range(N) :
    X = int(input())
    heapq.heappush(left, -X)

    if right and -left[0] > right[0] :
        heapq.heappush(right, -heapq.heappop(left))
    
    if len(left) < len(right) :
        heapq.heappush(left, -heapq.heappop(right))
    elif len(left) > len(right) + 1 :
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])