# 백준 11098 - 첼시를 도와줘!
# 분류 : 구현

N = int(input())
for _ in range(N) :
    P = int(input())
    max_cost = 0
    max_name = ""
    for i in range(P) :
        information = input().split()
        cost = int(information[0])
        name = information[1]
        if cost > max_cost :
            max_cost = cost
            max_name = name
    
    print(max_name)

