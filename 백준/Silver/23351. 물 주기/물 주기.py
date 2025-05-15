# 백준 23351 - 물 주기
# 분류 : 우선순위 큐

from queue import PriorityQueue
N, K, A, B = map(int, input().split())

N //= A
pq = PriorityQueue()
for _ in range(N) :
    pq.put(K)

count = 0
zero = 0
while True :
    x = pq.get()
    if x == zero :
        break

    x += B
    zero += 1

    pq.put(x)
    count += 1

print(count)