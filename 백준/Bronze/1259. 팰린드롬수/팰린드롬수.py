# 백준 1259 - 팰린드롬수

while True :
    N = input()
    if N == '0' :
        break
    
    if N[0] == "0" :
        print("no")
    else :
        mid = len(N) // 2
        if len(N) % 2 == 0 :
            if N[:mid] == N[mid:][::-1] :
                print("yes")
            else :
                print("no")
        else :
            if N[:mid] == N[mid + 1:][::-1] :
                print("yes")
            else :
                print("no")