# 백준 1362 - 펫
import sys
input = sys.stdin.readline

def opt(O, W) :
    if W > O * 0.5 and W < 2 * O :
        return ":-)"
    elif W <= 0 :
        return "RIP"
    else :
        return ":-("
index = 1
while True :
    O, W = map(int, input().split())
    if O == 0 and W == 0 :
        break
    alive = (W > 0)
    while True :
        DATA = input().split()
        op = DATA[0]
        weight = int(DATA[1])
        if op == "#" and weight == 0 :
            if not alive:
                print(index, "RIP")
            else:
                print(index, opt(O, W))
            index += 1
            break
        if alive :
            if op == "E" :
                W -= weight
            elif op == "F" :
                W += weight
            
            if W <= 0 :
                alive = False
    

