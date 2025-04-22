# 백준 13334 - 철로
# 분류 : 우선순위 큐

from queue import PriorityQueue

N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]
D = int(input())

X = []
for i in range(N) :
    if R[i][0] > R[i][1] : 
        R[i][0], R[i][1] = R[i][1], R[i][0]
    
    if R[i][1] - R[i][0] > D :
        continue

    X.append(R[i])

N = len(X)
X.sort()
pq = PriorityQueue()
for i in range(N) :
    pq.put(X[i][1])

answer = 0
for i in range(N) :
    # X[i][0] ~ X[i][0] + D
    while pq.qsize() != 0 :
        x = pq.get()
        if x > X[i][0] + D :
            pq.put(x)
            break

    answer = max(answer, N - i - pq.qsize())

print(answer)