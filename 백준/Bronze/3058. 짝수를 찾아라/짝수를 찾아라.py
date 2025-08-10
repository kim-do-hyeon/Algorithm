# 백준 3058 - 짝수를 찾아라

T = int(input())
for _ in range(T) :
    A = list(map(int, input().split()))
    min_value = 1e9
    total_value = 0
    for i in A :
        if i % 2 == 0 :
            total_value += i
            min_value = min(min_value, i)
    print(total_value, min_value)