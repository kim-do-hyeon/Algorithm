# 백준 31823 - 악질 검거
# 분류 : 구현

N, M = map(int, input().split())

answer = []
name = []
for i in range(N) :
    S = input().split()
    name.append(S[-1])
    S = S[:-1]

    max_count = 0
    count = 0
    for j in range(M) :
        if S[j] == "." :
            count += 1
        if S[j] == "*" :
            count = 0
        
        max_count = max(max_count, count)
    answer.append(max_count)

print(len(set(answer)))
for i in range(N) :
    print(answer[i], name[i])