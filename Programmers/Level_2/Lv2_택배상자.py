def solution(order):
    num = 1
    sub = []
    index = 0

    for target in order:
        while num <= target:
            sub.append(num)
            num += 1
        
        if sub[-1] == target:
            sub.pop()
            index += 1
        else:
            break

    return index

print(solution([4, 3, 1, 2, 5]))  # Expected: 2
