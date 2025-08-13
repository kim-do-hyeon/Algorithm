# 백준 23971 - ZOAC 4
H, W, N, M = map(int, input().split())
row = (H + N) // (N + 1)
col = (W + M) // (M + 1)
print(row * col)