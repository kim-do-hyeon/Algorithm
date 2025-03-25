def solution(n, w, num):
    answer = []
    array = [[] for i in range((n // w) + 1)]
    
    row = 0
    current_w = 0
    for i in range(1, n + 1) :
        array[row].append(i)
        current_w += 1
        if current_w >= w :
            row += 1
            current_w = 0
            
    if len(array) > 1 and len(array[-1]) != len(array[-2]):
        for i in range(len(array[-2]) - len(array[-1])):
            array[-1].append("X")

    for i in range(len(array)) :
        if i % 2 == 1 :
            array[i].reverse()
    print(array)
    box_row = 0
    box_col = 0
    for i in range(len(array)) :
        for j in range(len(array[0])):
            if array[i][j] == num :
                box_row, box_col = i, j
                break
    print(box_row, box_col)
    for index, value in enumerate(array) :
        if index >= box_row :
            if array[index][box_col] != "X" :
                answer.append(array[index][box_col])

    return len(answer)