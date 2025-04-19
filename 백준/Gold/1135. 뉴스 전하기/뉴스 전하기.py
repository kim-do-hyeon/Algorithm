# 백준 1135 - 뉴스 전하기
# 분류 : 다이나믹 프로그래밍

N = int(input())
par = list(map(int, input().split()))

child = [[] for _ in range(N)]
for i in range(1, N) :
    child[par[i]].append(i)

D = [0] * N

def dfs(u) :
    # D[u] 의 값을 구하는게 최종 목표

    times = []
    for v in child[u] :
        dfs(v)
        times.append(D[v])
    
    times.sort(reverse=True)

    D[u] = 0
    for i in range(len(times)) :
        D[u] = max(D[u], i + 1 + times[i])

dfs(0)
print(D[0])