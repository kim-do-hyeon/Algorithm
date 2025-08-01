# 백준 9663 - N-Queen
# 분류 : 브루트포스, 백트래킹

N = int(input())

answer = 0
visited = [-1] * N

def check(row) :
    for r in range(row) :
        if visited[r] == visited[row] or row - r == abs(visited[row] - visited[r]) :
            return False
    return True

def dfs(row) :
    global answer

    if row == N :
        answer += 1
    else :
        for col in range(N) :
            visited[row] = col
            if check(row) : 
                dfs(row + 1)

dfs(0)
print(answer)