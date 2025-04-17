# 백준 1976 - 여행 가자
# 분류 : BFS

from collections import deque

N = int(input())
M = int(input())

adj = [[] for _ in range(N)]
for i in range(N) :
    A = list(map(int, input().split()))

    for j in range(N) :
        if A[j] == 1 :
            adj[i].append(j)

T = list(map(int, input().split()))
for i in range(len(T)) :
    T[i] -= 1

visit = [-1] * N
queue = deque()

for i in range(N) :
    if visit[i] == -1 :
        queue.append(i)
        visit[i] = i

        while len(queue) != 0 :
            u = queue.popleft()

            for v in adj[u] :
                if visit[v] == -1 :
                    queue.append(v)
                    visit[v] = i

possible = True
for i in range(1, len(T)) :
    if visit[T[i - 1]] != visit[T[i]] :
        possible = False
        break

if possible :
    print("YES")
else :
    print("NO")