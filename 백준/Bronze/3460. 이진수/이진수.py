# 백준 3460 - 이진수

T = int(input())
for _ in range(T) :
    N = int(input())
    DATA = list(reversed(str(bin(N))[2:]))
    for index, i in enumerate(DATA) :
        if i == '1' :
            print(index, end = " ")