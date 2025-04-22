# 백준 5063 - TGN
# 문제집 : Python 배우기 (1 ~ 50)

T = int(input())
for i in range(T) :
    r, e, c = map(int, input().split())
    if e - c > r :
        print("advertise")
    elif e - c < r :
        print("do not advertise")
    elif e - c == r :
        print("does not matter")