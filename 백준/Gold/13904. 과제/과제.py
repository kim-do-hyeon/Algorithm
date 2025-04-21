# 백준 13904 - 과제
# 분류 - 우선순위 큐

from queue import PriorityQueue

N = int(input())

due = [[] for _ in range(1001)]

for i in range(N) :
    d, w = map(int, input().split())
    due[d].append(w)

pq = PriorityQueue()
answer = 0
for i in range(1000, 0, -1) :
    for w in due[i] :
        pq.put(-w)
    
    if pq.qsize() > 0 :
        answer += -pq.get()

print(answer)