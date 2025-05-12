# 백준 1009 - 분산처리
# 분류 : 구현

T = int(input())
cycle = {
    0 : [10],
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1]
}
for i in range(T) :
    a, b = map(int, input().split())
    a %= 10
    c = cycle[a]
    index = (b - 1) % len(c)
    print(c[index])
