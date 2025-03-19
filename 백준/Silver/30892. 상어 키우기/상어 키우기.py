# 백준 30892 - 상어 키우기
# 분류 : 그리디

from queue import PriorityQueue

N, K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
pq = PriorityQueue()

pos = 0
for _ in range(K) :
    while pos < N and A[pos] < T :
        pq.put(-A[pos])
        pos += 1
    
    if pq.qsize() == 0 :
        break

    T += -pq.get()

print(T)