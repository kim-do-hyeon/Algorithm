# 백준 4458 - 첫 글자를 대문자로

N = int(input())
for _ in range(N) :
    S = list(input())
    S[0] = S[0].upper()
    print("".join(S))