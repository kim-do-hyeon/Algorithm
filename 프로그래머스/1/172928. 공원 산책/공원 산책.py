def solution(park, routes):
    for i in range(len(park)) :
        for j in range(len(park[i])) :
            if park[i][j] == "S" :
                x, y = i, j
                break

    max_x = len(park)
    max_y = len(park[0])

    for i in routes :
        direction, block = i.split(" ")
        block = int(block)
        valid = True

        for j in range(1, block + 1) :
            if direction == "E" :
                new_x, new_y = x, y + j
            elif direction == "W" :
                new_x, new_y = x, y - j
            elif direction == "S" :
                new_x, new_y = x + j, y
            elif direction == "N" :
                new_x, new_y = x - j, y
            
            if not (0 <= new_x < max_x and 0 <= new_y < max_y) :
                valid = False
                break
            
            if park[new_x][new_y] == "X" :
                valid = False
                break
        
        if valid :
            if direction == "E" :
                y += block
            elif direction == "W" :
                y -= block
            elif direction == "S" :
                x += block
            elif direction == "N" :
                x -= block

    return [x, y]

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])) # [2, 1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])) # [0, 1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])) # [0, 0]