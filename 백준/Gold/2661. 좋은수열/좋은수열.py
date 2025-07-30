# 백준 2661 - 좋은수열
# 분류 : 백트래킹

N = int(input())

found = False

def is_good(seq) :
    length = len(seq)
    for i in range(1, length // 2 + 1) :
        if seq[-i:] == seq[-2 * i : -i] :
            return False
    return True

def dfs(seq) :
    global found
    if found : return
    if len(seq) == N :
        print(seq)
        found = True
        return 
    for digit in '123' :
        new_seq = seq + digit
        if is_good(new_seq) :
            dfs(new_seq)

dfs("")