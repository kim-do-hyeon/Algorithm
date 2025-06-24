# 백준 13023 - ABCDE
# DFS 없이 반복문으로 단순 경로(길이 4) 탐색

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

found = False

for a in range(N):
    for b in adj[a]:
        if b == a:
            continue
        for c in adj[b]:
            if c == a or c == b:
                continue
            for d in adj[c]:
                if d == a or d == b or d == c:
                    continue
                for e in adj[d]:
                    if e == a or e == b or e == c or e == d:
                        continue
                    found = True
                    break
                if found: break
            if found: break
        if found: break
    if found: break

print(1 if found else 0)