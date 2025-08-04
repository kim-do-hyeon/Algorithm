# 백준 2490 - 윷놀이

for _ in range(3) :
    X = list(map(int, input().split()))
    zero = X.count(0)
    one = X.count(1)
    if (zero == 1 and one == 3) :
        print("A")
    elif (zero == 2 and one == 2) :
        print("B")
    elif (zero == 3 and one == 1) :
        print("C")
    elif (zero == 4 and one == 0) :
        print("D")
    elif (zero == 0 and one == 4) :
        print("E")
