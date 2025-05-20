# 백준 2744 - 대소문자 바꾸기

S = input()
for i in S :
    if i.isupper() :
        print(i.lower(), end = '')
    else :
        print(i.upper(), end = '')