# 백준 7785 - 회사에 있는 사람
# 분류 : 자료 구조

N = int(input())

people = {}

for i in range(N) :
    name, status = input().split()
    if name not in people and status == "enter" :
        people[name] = status
    else :
        del people[name]

people = list(people.keys())
people.sort(reverse=True)

for i in people :
    print(i)