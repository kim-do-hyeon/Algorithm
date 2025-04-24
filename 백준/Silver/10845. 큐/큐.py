# 백준 10845 - 큐
# 분류 : 자료구조

from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    S = input().split()
    cmd = S[0]

    if cmd == 'push':
        queue.append(S[1])
    elif cmd == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        print(0 if queue else 1)
    elif cmd == 'front':
        print(queue[0] if queue else -1)
    elif cmd == 'back':
        print(queue[-1] if queue else -1)
