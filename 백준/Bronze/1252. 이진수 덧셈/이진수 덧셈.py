# 백준 1252 - 이진수 덧셈

N, M = input().split()
N = int("0b" + N, base = 0)
M = int("0b" + M, base = 0)
print(bin(N + M)[2:])