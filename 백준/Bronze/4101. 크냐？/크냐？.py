# 백준 4101 - 크냐?
# 문제집 : Python 배우기

while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    if a > b :
        print("Yes")
    else :
        print("No")