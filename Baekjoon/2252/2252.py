# 백준 2252 - 줄 세우기
# 분류 : 위상 정렬

'''
3명의 사람이 주어지면, 노드 그래프를 생성할 수 있다.
예제에서 1, 2, 3 이 주어지고, 1번은 3번보다 앞에 서야한다.
또한, 2번이 3번보다 앞에 서야한다.
그렇다면 1번에서 3번으로 가는 간선, 2번에서 3번으로 가는 간선
방향그래프를 얻게 된다, 즉 위상 정렬한 결과가 원하는 답이다.
'''

from collections import deque

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N)] # 인접리스트
need_to_learn = [0] * N

for i in range(M) :
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    need_to_learn[b - 1] += 1

# 위상 정렬
queue = deque([]) # 수강 가능한 목록이라 생각하기
for i in range(N) :
    if need_to_learn[i] == 0 :
        queue.append(i)

learn = []
while len(queue) != 0 :
    u = queue.popleft()
    learn.append(u)

    for v in adj[u] :
        need_to_learn[v] -= 1
        if need_to_learn[v] == 0 :
            queue.append(v)

for i in range(N) :
    print(learn[i] + 1, end = " ")