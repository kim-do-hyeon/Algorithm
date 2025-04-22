# 백준 10214 - Baseball
# 문제집 : Python 배우기 (1 ~ 50)

T = int(input())
for _ in range(T) :
    Y, K = 0, 0
    for i in range(9) :
        a, b = map(int, input().split())
        Y += a
        K += b
    if Y > K :
        print("Yonsei")
    elif K > Y :
        print("Korea")
    elif K == Y :
        print("Draw")