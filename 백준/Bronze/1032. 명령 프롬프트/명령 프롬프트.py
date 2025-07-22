# 백준 1032 - 명령 프롬프트
# 분류 : 구현

N = int(input())
S = [input() for _ in range(N)]

result = list(S[0])

for i in range(1, N) :
    for j in range(len(result)) :
        if result[j] != S[i][j] :
            result[j] = '?'

print("".join(result))