# 백준 1141 - 접두사
# 분류 : 문자열

N = int(input())
S = [input() for _ in range(N)]
S = list(set(S))

prefix = [False] * N

for i in range(len(S)) :
    for j in range(len(S)) :
        if i == j : 
            continue

        if len(S[i]) >= len(S[j]) :
            continue

        if S[i] == S[j][:len(S[i])] :
            prefix[i] = True
            break

count = 0
for i in range(len(S)) :
    if not prefix[i] :
        count += 1

print(count)