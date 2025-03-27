def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    
    data = set()
    
    while True :
        for i in range(m - 1) :
            for j in range(n - 1) :
                t = board[i][j]
                if t == [] :
                    continue
                if board[i + 1][j] == t and board[i][j + 1] == t and board[i + 1][j + 1] == t :
                    data.add((i, j))
                    data.add((i + 1, j))
                    data.add((i, j + 1))
                    data.add((i + 1, j + 1))
        if data :
            answer += len(data)
            for i, j in data :
                board[i][j] = []
            data = set()
        else :
            return answer
        
        while True :
            move = 0
            for i in range(m - 1) :
                for j in range(n) :
                    if board[i][j] and board[i + 1][j] == [] :
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        move = 1
            if move == 0 :
                break