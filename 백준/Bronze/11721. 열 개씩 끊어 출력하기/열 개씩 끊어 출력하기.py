# 백준 11721 - 열 개씩 끊어 출력하기
S = input()
N = len(S)
start, end = 0, 10
while N > 0 :
    print(S[start:end])
    N -= 10
    start += 10
    end += 10