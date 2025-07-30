# 백준 6666 - Help me With the Game

board = []
for i in range(17) :
    s = input()
    if s != "+---+---+---+---+---+---+---+---+" :
        s = s[1:-1].split("|")
        board.append(s)

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
priority = {'K' : 0, 'Q' : 1, 'R' : 2, 'B' : 3, 'N' : 4, "P" : 5}

white = []
balack = []
for row in range(8) :
    for col in range(8) :
        cell = board[row][col]
        piece = cell[1]
        if piece == '.' or piece == ':':
            continue
        col_letter = columns[col]
        row_number = 8 - row

        if piece.isupper() :
            kind = piece
            if kind == 'P' :
                name = f"{col_letter}{row_number}"
            else :
                name = f"{kind}{col_letter}{row_number}"
            white.append((priority[kind], row_number, col_letter, name))
        else :
            kind = piece.upper()
            if kind == 'P' :
                name = f"{col_letter}{row_number}"
            else :
                name = f"{kind}{col_letter}{row_number}"
            balack.append((priority[kind], -row_number, col_letter, name))

white.sort()
balack.sort()

print("White: " + ",".join(piece[3] for piece in white))
print("Black: " + ",".join(piece[3] for piece in balack))