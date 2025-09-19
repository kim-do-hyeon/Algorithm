# [브론즈 2] 백준 1871 - 좋은 자동차 번호판

N = int(input())
for _ in range(N) :
    S = input().split("-")
    A = list(S[0])
    B = int(S[1])
    A_value = 0
    curr = len(A)
    for index, value in enumerate(A) :
        A_value += ((ord(value) - 65) * (26 ** (curr - (index + 1))))
    
    if abs(A_value - B) <= 100 :
        print("nice")
    else :
        print("not nice")
        