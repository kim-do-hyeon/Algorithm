# 백준 1021 - 회전하는 큐
# 분류 : 덱

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
dq = deque([i for i in range(1, N + 1)])

count = 0
for i in A :
    while True :
        if dq[0] == i :
            dq.popleft()
            break
        else :
            if dq.index(i) <= len(dq) // 2 :
                dq.rotate(-1)
                count += 1
            else :
                dq.rotate(1)
                count += 1
print(count)