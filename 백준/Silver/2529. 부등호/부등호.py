# 백준 2529 - 부등호
K = int(input())
oper = list(input().split())

def get_num(x, y, oper) :
    if oper == "<" :
        if x > y :
            return False
    else :
        if x < y :
            return False
    return True

def dfs(index, num) :
    if index == K + 1 :
        answer.append(num)
        return

    for i in range(10) :
        if not check[i] :
            if index == 0 or get_num(num[index - 1], str(i), oper[index - 1]) :
                check[i] = True
                dfs(index + 1, num + str(i))
                check[i] = False

check = [False] * 10
answer = []
dfs(0, '')

answer.sort()
print(answer[-1])
print(answer[0])