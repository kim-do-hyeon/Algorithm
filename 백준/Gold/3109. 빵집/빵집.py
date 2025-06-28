# 백준 2109 - 빵집
# 분류 : DFS

R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]

def dfs(r, c) :
    visit[r][c] = True
    
    # 오른쪽 끝에 도달할 수 있으면 True else False
    if c == C - 1 :
        return True
    
    if r - 1 >= 0 and not visit[r - 1][c + 1] and B[r - 1][c + 1] == '.' :
        if dfs(r - 1, c + 1) :
            return True
    
    if not visit[r][c + 1] and B[r][c + 1] == '.' :
        if dfs(r, c + 1) :
            return True
        
    if r + 1 < R and not visit[r + 1][c + 1] and B[r + 1][c + 1] == '.' :
        if dfs(r + 1, c + 1) :
            return True
    
    return False

answer = 0
for i in range(R) :
    if dfs(i, 0) :
        answer += 1

print(answer)