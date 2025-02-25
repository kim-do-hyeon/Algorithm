# 백준 6064 - 카잉 달력
# 분류 : 브루트포스

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
result = []

for i in range(1, T + 1):
    M, N, x, y = map(int, data[i].split())

    k = x  # x에서 시작
    found = False

    while k <= M * N:
        if (k - y) % N == 0:
            result.append(str(k))
            found = True
            break
        k += M

    if not found:
        result.append("-1")

sys.stdout.write("\n".join(result) + "\n")
