# 백준 9375 - 패션왕 신빈
# 분류 : 조합

T = int(input())

for _ in range(T) :
    count = {}
    N = int(input())
    for _ in range(N) :
        _, t = input().split()

        if t not in count :
            count[t] = 0
        count[t] += 1
    
    answer = 1
    for k, v in count.items() :
        answer *= (v + 1)
    answer -= 1
    print(answer)
