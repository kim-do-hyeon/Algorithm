# 백준 3085 - 사탕 게임
# 분류 : 코딩 테스트 준비 - 기초 ) 브루트 포스

N = int(input())
board = [list(input()) for _ in range(N)]

def check(board) :
    max_count = 1
    for i in range(N) :
        count = 1
        for j in range(1, N) :
            if board[i][j] == board[i][j - 1] :
                count += 1
                max_count = max(max_count, count)
            else :
                count = 1
        count = 1
        for j in range(1, N) :
            if board[j][i] == board[j - 1][i] :
                count += 1
                max_count = max(max_count, count)
            else :
                count = 1
    return max_count

answer = 0
for i in range(N) :
    for j in range(N) :
        if j + 1 < N :
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < N :
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)