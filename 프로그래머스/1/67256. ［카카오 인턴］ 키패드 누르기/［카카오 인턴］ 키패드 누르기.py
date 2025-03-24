keypad = {
        1 : [0, 0],
        2 : [0, 1],
        3 : [0, 2],
        4 : [1, 0],
        5 : [1, 1],
        6 : [1, 2],
        7 : [2, 0],
        8 : [2, 1],
        9 : [2, 2],
        "*" : [3, 0],
        0 : [3, 1],
        "#" : [3, 2]
}
def calc_dist(x, y) :
    y1, x1 = x
    y2, x2 = y
    return abs(y2 - y1) + abs(x2 - x1)

def solution(numbers, hand):
    answer = ''
    left = keypad["*"]
    right = keypad["#"]
    
    for i in numbers :
        if i in [1, 4, 7] :
            left = keypad[i]
            answer += "L"
        elif i in [3, 6, 9] :
            right = keypad[i]
            answer += "R"
        else :
            if calc_dist(right, keypad[i]) < calc_dist(left, keypad[i]) :
                right = keypad[i]
                answer += "R"
            elif calc_dist(right, keypad[i]) > calc_dist(left, keypad[i]) :
                left = keypad[i]
                answer += "L"
            else :
                if hand == "right" :
                    right = keypad[i]
                    answer += "R"
                else :
                    left = keypad[i]
                    answer += "L"
    
    return answer