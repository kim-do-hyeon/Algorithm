# 백준 11170 - 0의 개수
T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    A = list(map(str, [n for n in range(N, M + 1)]))
    result = 0
    for i in A :
        result += i.count("0")
    print(result)