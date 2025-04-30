# 백준 16198 - 에너지 모으기
# 분류 : 브루트포스, 재귀

N = int(input())
A = list(map(int, input().split()))

def dfs(a, w) :
    if len(a) == 2 :
        return w
    
    ret = 0
    for i in range(1, len(a) - 1) :
        na = a[ : i] + a[i + 1 :]
        tmp = dfs(na, w + a[i - 1] * a[i + 1])
        if ret < tmp :
            ret = tmp
    
    return ret

print(dfs(A, 0))