# 백준 10995 - 별 찍기 - 20
N = int(input())
for i in range(1, N + 1) :
    for j in range(1, N + 1) :
        print("*", end = " ")
    print()
    if i % 2 == 1 :
        print(" ", end = "")