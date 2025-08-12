# 백준 11365 - !밀비 급일

while True :
    S = input()
    if S == "END" :
        break
    S = list(S)
    S.reverse()
    print("".join(S))