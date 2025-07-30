# 백준 2552 - 별 찍기 - 12
N = int(input())
for i in range(2 * N - 1, 0, -1) :
    if i >= N :
        print(" " * (abs(N - i)), end = "")
        print("*" * (N - abs(N - i)))
    else :
        print(" " * abs(i - N), end = "")
        print("*" * (N - abs(N - i)))