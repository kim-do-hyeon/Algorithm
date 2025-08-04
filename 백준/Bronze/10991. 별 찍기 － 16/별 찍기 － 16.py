# 백준 10991 - 별 찍기 - 16
N = int(input())
for i in range(1, N + 1):
    print(" " * (N - i) + "* " * (i - 1) + "*")