# 백준 2442 - 별 찍기 - 5

N = int(input())
for i in range(N, 0, -1) :
    for j in range(i, 1, -1) :
        print(" ", end = "")
    print("*" * (2 * (N - i) + 1))