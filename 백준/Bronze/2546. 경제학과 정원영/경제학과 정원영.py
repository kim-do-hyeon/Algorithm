T = int(input())
 
for t in range(T):
    empty_line = input()
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Economics = list(map(int, input().split()))
    C_avg = sum(C) / N
    Economics_avg = sum(Economics) / M
    result = 0
    for c in C:
        if c < C_avg and c > Economics_avg:
            result += 1
    print(result)