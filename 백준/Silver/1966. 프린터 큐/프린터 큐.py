# 백준 1966 - 프린터 큐
# 분류 : 큐

from collections import deque

T = int(input())
for _ in range(T) :
    queue = deque()
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for index, important in enumerate(A) :
        queue.append((index, important))

    count = 0
    while queue :
        current = queue.popleft()
        if any(current[1] < other[1] for other in queue) :
            queue.append(current)
        else :
            count += 1
            if current[0] == M :
                print(count)
                break

