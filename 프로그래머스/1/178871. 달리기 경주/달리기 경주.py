'''
# 68.8 / 100.0
# players.index(i)가 O(N)이므로 시간초과 발생

def solution(players, callings):
    answer = []
    for i in callings :
        rank = players.index(i)
        user = players[rank]
        temp = players[rank - 1]
        players[rank - 1] = user
        players[rank] = temp

    return players
'''
def solution(players, callings):
    answer = {}
    for index, value in enumerate(players) :
        answer[value] = index
    for i in callings :
        index = answer[i]
        previous = index - 1
        previous_user = players[previous]

        players[previous], players[index] = players[index], players[previous]

        answer[i] = previous
        answer[previous_user] = index

    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])) #["mumu", "kai", "mine", "soe", "poe"]
# kai -> mumu soe kai poe mine
# kai -> mumu kai soe poe mine
# mine -> mumu kai soe mine poe 
# mine -> mumu kai mine soe poe