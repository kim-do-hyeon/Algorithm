# 백준 2381 - 최대 거리
# 분류 : 수학

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

max_plus = -1e9
min_plus = 1e9

for x, y in P :
    max_plus = max(max_plus, y + x)
    min_plus = min(min_plus, y + x)

max_minus = -1e9
min_minus = 1e9

for x, y in P :
    max_minus = max(max_minus, y - x)
    min_minus = min(min_minus, y - x)

print(max(max_plus - min_plus, max_minus - min_minus))