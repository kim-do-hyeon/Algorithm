# [브론즈 2] 백준 2954 - 창영이의 일기장
data = input()
value = ['a', 'e', 'i', 'o', 'u']

number = 0
while number < len(data) :
    print(data[number], end='')
    if data[number] in value :
        number += 2
    number += 1