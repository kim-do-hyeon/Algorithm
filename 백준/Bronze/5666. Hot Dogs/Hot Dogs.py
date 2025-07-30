# 백준 5666 - Hot Dogs
while True :
    try :
        a, b = map(int, input().split())
        print("%.2f" % round(a / b, 2))
    except :
        break