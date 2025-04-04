# 백준 11945 - 뜨거운 붕어빵
# 분류 : 구현

N, M = map(int, input().split())
B = [input() for _ in range(N)]

for i in range(N) :
    print(B[i][::-1])