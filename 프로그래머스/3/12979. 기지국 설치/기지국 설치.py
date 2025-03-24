import math

def solution(n, stations, w):
    answer = 0
    distance = []
    for i in range(1, len(stations)) :
        distance.append((stations[i] - w - 1) - (stations[i - 1] + w))
    
    distance.append(stations[0] - w - 1)
    distance.append(n - (stations[-1] + w))
    
    for i in distance : 
        if i <= 0 :
            continue
        else :
            answer += math.ceil(i / (2 * w + 1))

    return answer