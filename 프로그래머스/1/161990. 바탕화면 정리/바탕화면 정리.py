def solution(wallpaper):
    answer = [50, 50, 0, 0]
    x1, y1, x2, y2 = 0, 1, 2, 3
    for i, values in enumerate(wallpaper) :
        for j, value in enumerate(values) :
            if value == "#" :
                answer[x1] = min(answer[x1], i)
                answer[y1] = min(answer[y1], j)
                answer[x2] = max(answer[x2], i + 1)
                answer[y2] = max(answer[y2], j + 1)
    
    return answer

print(solution([".#...", "..#..", "...#."])) # [0, 1, 3, 4]