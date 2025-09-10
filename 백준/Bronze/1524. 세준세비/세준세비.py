# 백준 1524 - 세준세비

T = int(input())
for _ in range(T) :
    input()
    N, M = map(int, input().split())
    sejuns = list(map(int, input().split()))
    sebis = list(map(int, input().split()))
    sejuns.sort(reverse = True)
    sebis.sort(reverse = True)
    
    while sejuns and sebis :
        if sejuns[-1] >= sebis[-1] :
            sebis.pop()
        else :
            sejuns.pop()
    
    if sejuns : 
        print("S")
    elif sebis :
        print("B")
    else :
        print("C")