# 백준 2164 - 카드2
# 분류 : 자료구조

from collections import deque
N = int(input())
queue = deque()

if N == 1 :
    print(1)
else :
    for i in range(1, N + 1) :
        queue.append(i)

    temp = queue.popleft()
    while len(queue) > 1 :
        temp = queue.popleft()
        queue.append(temp)
        queue.popleft()

    print(queue[0])