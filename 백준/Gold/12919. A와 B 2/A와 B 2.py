# 백준 12919 - A와 B 2
# 분류 : 문자열

S = input()
T = input()

def dfs(t) :
    if len(t) == len(S) :
        return t == S
    
    if t[-1] == "A" :
        if dfs(t[:-1]) :
            return True
    
    if t[0] == 'B' :
        if dfs(t[1:][::-1]) :
            return True

    return False

if dfs(T) :
    print(1)
else :
    print(0)