# 백준 9657 - 돌게임 3
# 분류 : 다이나믹 프로그래밍

N = int(input())

D = [False] * 1001

D[1] = True
D[2] = False
D[3] = True
D[4] = True

for i in range(5, 1001) :
    D[i] = (not D[i - 1]) | (not D[i - 3]) | (not D[i - 4])

if D[N] :
    print("SK")
else :
    print("CY")