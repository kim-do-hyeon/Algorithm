# 백준 2526 - 싸이클
# 분류 : 구현

N, P = map(int, input().split())

n = N
order = {}
count = 0

while True :
    if n not in order :
        order[n] = count
        n = n * N % P
        count += 1
    else :
        print(count - order[n])
        break