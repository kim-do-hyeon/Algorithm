# 백준 2921 - 도미노

N = int(input())
total = 0

for i in range(N + 1):
    for j in range(i, N + 1):
        total += i + j

print(total)